# System overview

## 1. Major system components

### 1.1. User authentication

- Each user logs with a master password, which is never stored in plaintext. The password is processed with a strong key derivation function (e.g. PBKDF2-SHA256 or Argon2) and a unique salt.
- The sever stores only salted hashes. This ensures credential verification is secure and aligns with OWASP best practices for password storage.
- Two-factor or multi-factor authentication (MFA) is supported as an additional setting; enabling MFA (e.g. TOTP, hardware token) “adds another layer of security” to guard the master password.
- Administrative or emergency recovery options (such as recovery codes) are also managed in this component.

### 1.2. Password Vault

- The vault is the encrypted store of all user credentials.
- All encryption and decryption is performed client-side.
- In our design, a key derived from the master password is used to generate a symmetric encryption key.
- The vault data is encrypted on the user’s device before any upload, and only the encrypted blob is stored on the server.
- When the user opens the vault, the client downloads the encrypted data and decrypts it locally with the key. This “zero-knowledge” architecture means the server has no knowledge of plaintext passwords or the master key ￼ ￼.

### 1.3. Password Management (Add/Edit/Delete)

- This component handles creating, updating, and removing individual credential entries.
- When adding or editing a password, the client encrypts the new or modified entry with the vault key before sending it to the server.
- On deletion, the client tells the server to remove the specified encrypted entry.
- All operations are logged: the client or server records an audit event for each Create, Update, or Delete action on vault items. For example, audit logs include events like “Created item” or “Permanently Deleted item,” each tagged with a timestamp, user, and identifier. These logs ensure users can review their own vault activity, and administrators can monitor aggregate activity.

### 1.4. User Settings (Preferences, MFA)

- Users can manage personal settings such as account preferences, UI themes, and security options. In particular, MFA setup (e.g. linking a TOTP authenticator) is handled here.
- Enabling MFA requires verifying the user’s identity (typically by entering the master password or a one-time code) and storing the MFA secret securely on the server.
- Disabling MFA likewise requires re-authentication.
- All changes to security settings are logged as critical events.
- By design, the system follows best practices: for instance, authoritative sources note that enabling MFA is a “crucial component” of password management security.
- Other settings (e.g. email, language, auto-lock timeout) are stored in the user’s profile and updated through secure API calls.

### 1.5. Sharing/Access Management (in future updates)

- Though each user initially has a single vault, the system allows controlled sharing of specific entries or folders.
- When a user shares a password with another user or group, the client re-encrypts that entry using a shared key or the recipient’s public key. This way, only the intended recipient can decrypt the shared data.
- The server may keep track of share permissions or encrypted copies, but never holds any unencrypted password.
- Administrators can grant or revoke access rights, and all sharing actions (sharing or revoking an entry) are audited.

### 1.6. Audit Logs (for Security Monitoring)

- The system maintains comprehensive audit logs of all critical activities.
- Users see their own vault audit logs, which include CRUD actions on items in their vault, with timestamps and details. Our implementation logs each vault operation so users can review their history.
- Administrative or system-level events (user account creation/deletion, password policy changes, system errors, etc.) are logged in a separate admin audit log.
- Access to logs is role-restricted: only administrators can view system or sensitive logs.
- All logs are timestamped and retained per policy to support security monitoring and compliance.

## 2. Core Data Flow

### 2.1. Login (Authentication) Flow

1. The user navigates to the login page and submits username/email and master password.
2. The client app applies a KDF with a salt to the password (salting with the username/email) and sends the resulting hash over HTTPS to the server.
3. The server looks up the user's stored salt and hash, then compares hashes. If credentials match, the server issues a JWT token, If not, login fails.
4. On success, the server logs a "Login" event with timestamp and client details. The user is now authenticated and can proceed.

### 2.2. Vault Access Flow

1. After login, the user, requests to view or unlock their vault (visiting the vault page).
2. The client retrieves the encrypted vault data from the server via an API call. This is just ciphertext - the server never sees the plaintext.
3. The client derives the vault encryption key from the master password (using the same KDF process) ad decrypts the vault locally.
4. Decrypted entries are loaded into the UI for the user. All decryption happens in memory and the client; no plaintext is sent over the network.
5. The client logs a "Vault Access" event in the user's audit log. If decryption fails, an error is shown and no data is loaded.

### 2.3. Password management flow

#### 2.3.1. Add new Entry

1. The user fills in and new credentials.
2. The client encrypts the new entry with the vault key and sends the encrypted blob to the server to store.
3. The server saves it under the user's vault and returns success.
4. Both client and server record a "Create item" audit event.

#### 2.3.2. Edit Entry

1. The user selects an existing entry to edit.
2. The client decrypts it locally.
3. The user edits fields.
4. Client re-encrypts the updated data and sens it to the server.
5. The server overwrites the stored ciphertext.
6. An "Edit item" event is logged (with item id) for auditing.

#### 2.3.3. Delete Entry

1. The user deletes an entry (ask confirm from user).
2. The client sends a delete command to the server. 
3. The server removes the encrypted entry from storage. 
4. A “Delete item” audit event is logged (e.g. “Permanently Deleted item”).

> **Note:** All these operations require that the user is authenticated and authorized; the master password (or session token) is used to prove the operation is allowed. The client re-encrypts data immediately whenever it’s changed, ensuring plaintext never leaves the browser or app. For each operation, the server may also log a generic access event with timestamp and user ID 

### 2.4. Sharing/Access Flow (in future updates)

1. The user chooses to share a password or folder with another user or group. The client fetches the relevant entries form the vault (decrypted in memory).
2. The client generates a sharing payload: it encrypts the entry with a key that only the recipient(s) can use (e.g. derived from the recipient’s public key or a shared secret). This ensures true end-to-end encryption for the shared data.
3. The client sends the encrypted share package and metadata (e.g. recipient IDs) to the server. The server stores the share record or forwards it to recipients. The server never sees the share contents unencrypted.
4. The recipient’s client receives the encrypted share (either via notification or when they next sync). The client decrypts it using the recipient’s key and adds it to their vault. An audit event like “Received shared item” is logged for both parties. Administrators can view high-level share events in the admin logs, but actual password contents remain hidden.

### 2.5. User Settings Adjustment Flow
1. The authenticated user navigates to Settings. For each change (e.g. changing master password, enabling MFA, updating preferences), the client requires re-authentication (re-entering current password or a code) to proceed.
2. Changing Master Password: The user provides old and new passwords. The client verifies the old password by trying to decrypt a vault item or confirming via a server call. The client then re-derives a new encryption key from the new password, re-encrypts the vault data with it, and sends the updated hashes and any re-encrypted keys to the server. The server updates the stored salted hash and any stored vault key. A “Changed account password” event is logged.
3. Enabling/Disabling MFA: When the user enables MFA, the client generates or retrieves a TOTP secret, displays a QR code, and the user confirms with a TOTP code. The secret (in encrypted form) is sent to the server and stored. Disabling MFA similarly requires confirming identity. Each action logs an event (“Enabled two-step login” or “Disabled two-step login”).
4. Other Preferences: Updates to profile info (email, language) or UI settings are sent to the server and saved in the user profile. These non-sensitive changes are also logged.

> **Note**: Throughout, the system enforces authorization: only the rightful user (or an admin, in case of account recovery) can change settings. Sensitive changes are logged for auditing (e.g. “Changed account password”, “Enabled two-step login”)