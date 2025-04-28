# Abstract Document Outline

## 1. Document Purpose
The goal of this document is to capture all the essential properties, functionalities, constraints, and architectural decisions for the Password Manager project. This abstract serves as the foundational reference for the development and maintenance of the application, ensuring that all stakeholders have a unified understanding of the system’s design, behavior, and security posture.

The document will cover:

- **Functional Requirements:** Detailed descriptions of user-facing features, interactions, and expected behavior of the application.
- **Non-Functional Requirements:** Performance, security, scalability, and reliability goals that the system must meet.
- **Architecture Decisions:** High-level design, technology stack, and key trade-offs made during the project planning phase.
- **Data Models and API Specifications:** The structure of stored data, API endpoints, and interactions.
- **Security and Privacy:** Encryption strategies, user authentication methods, and overall security model.

By clearly defining these aspects, this document serves as the backbone of the project's development lifecycle, guiding decisions and ensuring alignment between all teams involved.

### Role in development
This document drives development by:
1. **Defining Clear Requirements:** It outlines the expected functionalities and behaviors of the application, serving as the source of truth for feature implementation.
2. **Guiding Design and Architecture:** By specifying architecture decisions and technology choices, it ensures that the development follows a unified structure, reducing ambiguity and improving collaboration.
3. **Ensuring Security Compliance:** It sets forth the security measures that must be implemented and adhered to, ensuring that all development efforts comply with best practices and regulatory standards.
4. **Maintaining Traceability:** As development progresses, this document will provide a clear reference for ensuring that the system is being built as planned. It will be updated to reflect significant changes, keeping all stakeholders aligned.
5. **Providing Testing and Validation Criteria:** The specifications described in this document will serve as a foundation for testing the system, including performance, security, and functional testing. Testers and developers can use it to verify that the implementation meets all requirements.

## 2. Application Overview
### 2.1. Vision and Scope
The vision of this project is, for me as a student, to develop a secure, scalable, and user-friendly password manager that demonstrates professional software engineering practices and showcases advanced technical skills in real-world application development.

**What I will do**:
- Implement a fully functional password manager with a front-end and back-end.
- Ensure strong security features and secure password storage.
- Follow (in my best capabilites) industry-standard practices for code quality, version control, and documentation.
- Design an intuitive user interface and a robust API for seamless interaction between front-end and back-end.
- Document all decisions, code, and architectures thoroughly to maintain clarity and traceability.

**What I will not do**:
- Implement mobile applications or multi-platform support (focus will be on web).
- Use third-party authentication providers (e.g., Google/Facebook login); the focus will be on custom authentication mechanisms.
- Add non-essential features (e.g., advanced settings, integrations with other tools) that do not align with core functionality.
- Use low-level or outdated technologies that are not in line with modern best practices (e.g., jQuery, legacy authentication mechanisms).
- Implement full-blown enterprise-grade security features (e.g., intrusion detection systems, complex cryptographic key management), though strong encryption and basic security best practices will be adhered to.
### 2.2. High-Level Features
**Core user stories**:
- **Register Account:**
  As a user, I want to create a secure account with a strong master password so that I can access my personal vault.

- **Authenticate and Login:**
  As a user, I want to securely log into my account using my master password so that I can access my stored credentials.

- **Store Credentials:**
  As a user, I want to securely store website usernames and passwords so that I can retrieve them when needed.

- **Retrieve Credentials:**
  As a user, I want to view my saved credentials securely so that I can log into my accounts quickly.

- **Update Credentials:**
  As a user, I want to update stored usernames, passwords, or notes so that my credential information remains current.

- **Delete Credentials:**
  As a user, I want to delete credentials I no longer need so that I can keep my vault organized and secure.

- **Search Credentials:**
  As a user, I want to search through my stored credentials so that I can find specific entries easily.

- **Organize Credentials into Vaults/Folders:**
  As a user, I want to categorize my credentials into folders or vaults so that I can manage them more efficiently.

- **Share Vault or Credentials (optional future scope):**
  As a user, I want to securely share specific credentials or entire vaults with another trusted user.

- **Change Master Password:**
  As a user, I want to change my master password periodically to maintain account security.

- **Recover Master Password:**
  As a user, I want a secure recovery mechanism for my master password so that I can regain access if I forget it.

- **Logout / Session Management:**
  As a user, I want to be able to log out and automatically terminate sessions after inactivity for enhanced security.

- **Multi-Factor Authentication (MFA) Setup (optional future scope):**
  As a user, I want to enable MFA so that my account access is protected by an additional layer of security.

## 3. Functional Requirements
## 3.1 User Management

### 3.1.1 Register

**Objective:**
Allow new users to create a secure account by choosing a strong master password and providing minimal required information.

**Functional Behavior:**
- Users provide:
  - Email address (required, unique).
  - Master password (required, minimum complexity enforced).
- Email address must be verified through a confirmation link before the account is activated.
- Password is never stored in plaintext; only a derived and salted hash is stored.
- Initial encryption keys are derived from the master password using a secure KDF (e.g., Argon2id).
- Terms of service and privacy policy acknowledgment checkbox mandatory.

**Security Requirements:**
- Password strength validation client-side and server-side.
- Server applies rate limiting on registration attempts.
- Confirmation tokens are cryptographically random and expire after a short period (e.g., 24 hours).
- Email addresses are normalized and validated against known disposable email providers.

**API Design:**
- **POST /api/auth/register**
- Request body contains email and hashed/encrypted password payload.
- Server responds with 201 Created and sends a verification email.

### 3.1.2 Login

**Objective:**
Authenticate users securely and establish a trusted session.

**Functional Behavior:**
- User submits email and master password.
- Server authenticates using stored password hash comparison.
- On success, server issues a secure, short-lived access token (e.g., JWT or session cookie).
- Option to enable Multi-Factor Authentication (MFA) in future versions.

**Security Requirements:**
- Passwords compared using constant-time algorithms to prevent timing attacks.
- Brute-force protection: account lockout or exponential backoff after several failed attempts.
- Sessions expire after inactivity (short TTL for access tokens).
- Refresh token mechanism (optional) for seamless session renewal.

**API Design:**
- **POST /api/auth/login**
- Returns authentication token(s) upon success.

### 3.1.3 Password Reset Flow

**Objective:**
Enable users to reset their password securely if forgotten, without compromising stored encrypted data.

**Functional Behavior:**
- Users request a password reset by entering their email.
- Server generates a one-time, time-limited reset token and sends it via email.
- Clicking the link allows the user to input a new master password.
- Important: Changing the master password must either re-encrypt vault data or warn the user that previous data will be unrecoverable if client-side encryption cannot be reversed (zero-knowledge constraint).

**Security Requirements:**
- Reset tokens are cryptographically random and expire within minutes or hours.
- No sensitive data is leaked in reset emails.
- Ensure email ownership through confirmation before allowing password change.

**API Design:**
- **POST /api/auth/forgot-password** — Request password reset link.
- **POST /api/auth/reset-password** — Reset password using valid token.

**Edge Handling:**
- Token reuse is forbidden.
- Invalid or expired token responses must not disclose account existence to avoid user enumeration attacks.

### 3.1.4 Roles and Permissions

**Objective:**
Implement a simple role-based access control (RBAC) system to define user and administrative capabilities.

**Roles:**
- **User:**
  - Full access to personal vaults.
  - No access to other users' data or system-wide operations.
- **Admin:**
  - Ability to manage users (view, deactivate, reset accounts).
  - Monitor system health and logs.
  - Does not have access to user vault contents (maintains zero-knowledge principle).

**Permissions Enforcement:**
- Backend enforces permissions on every sensitive route.
- Admin-only routes protected through middleware or guards.

**Security Requirements:**
- Clear separation of user vs. admin operations at API and database levels.
- Admin privilege escalation is forbidden without proper verification processes.
- Regular review of user permissions to prevent privilege creep.

**API Design Examples:**
- **GET /api/admin/users** — Admin only.
- **PATCH /api/admin/user/:id/deactivate** — Admin only.
- **GET /api/vault** — User authenticated access.

### 3.1.5 General Security Measures Across User Management
- All personal information is encrypted in-transit (HTTPS) and sensitive identifiers are tokenized or anonymized where possible.
- Server logs redact sensitive fields to prevent leakage of credentials or personal data.
- Input validation and sanitization on all forms and endpoints.
- Detailed audit logging for registration, login, and password reset events.
## 3.2 Vault Operations

### 3.2.1 Create Vault Entry

**Objective:**
Allow authenticated users to securely create and store a new vault entry containing login credentials or secure notes.

**Functional Behavior:**
- Users provide:
  - Title (required).
  - Username (optional).
  - Password (optional).
  - URL (optional).
  - Notes (optional).
  - Tags or Folder association (optional).
- Client-side encryption applied before transmission.
- Newly created entries are linked to the authenticated user account.

**Security Requirements:**
- All sensitive fields encrypted client-side using a key derived from the master password.
- HTTPS enforced for all communication.
- Server only stores encrypted payloads; no plaintext.

**API Design:**
- **POST /api/vault/entries**
- Authenticated endpoint.
- Returns 201 Created upon success.

### 3.2.2 Read Vault Entries

**Objective:**
Allow authenticated users to securely retrieve their stored vault entries.

**Functional Behavior:**
- Users can retrieve:
  - All vault entries.
  - Entries filtered by folder, tag, or keyword search.
- Entries are decrypted client-side only after retrieval.
- Support pagination for large vaults.

**Security Requirements:**
- Server responds with encrypted entries only.
- Sensitive metadata minimized in server responses.

**API Design:**
- **GET /api/vault/entries** — List all entries.
- **GET /api/vault/entries?folder=folder_id** — Filter by folder.
- **GET /api/vault/entries?tag=tag_name** — Filter by tag.

### 3.2.3 Update Vault Entry

**Objective:**
Allow authenticated users to securely update fields of an existing vault entry.

**Functional Behavior:**
- Users can update:
  - Title
  - Username
  - Password
  - URL
  - Notes
  - Associated folder or tags
- Updated data encrypted client-side before sending.
- Old record replaced atomically with new encrypted record.

**Security Requirements:**
- Access control ensures only the owner can update their entries.
- Conflict handling if two clients attempt to update simultaneously (optimistic locking or timestamps).

**API Design:**
- **PATCH /api/vault/entries/:entry_id**
- Authenticated endpoint.

### 3.2.4 Delete Vault Entry

**Objective:**
Allow authenticated users to permanently delete a vault entry.

**Functional Behavior:**
- Users confirm deletion.
- Record is hard-deleted or soft-deleted based on implementation choice (prefer soft-deletion for auditability).

**Security Requirements:**
- Verify ownership before deletion.
- Encrypted audit log entry created if necessary (e.g., "user X deleted entry Y at time Z").

**API Design:**
- **DELETE /api/vault/entries/:entry_id**
- Authenticated endpoint.

### 3.2.5 Folder Organization

**Objective:**
Enable users to group entries into folders for better management.

**Functional Behavior:**
- Users create folders with:
  - Folder name (required, unique per user).
- Entries can be assigned to folders at creation or updated later.
- Users can rename or delete folders.
- Deleting a folder should either delete contained entries (with confirmation) or unassign them.

**Security Requirements:**
- Folder names encrypted if required to maintain zero-knowledge principles.
- Folder structure retrieved securely without leaking user metadata.

**API Design:**
- **POST /api/vault/folders** — Create folder.
- **PATCH /api/vault/folders/:folder_id** — Rename folder.
- **DELETE /api/vault/folders/:folder_id** — Delete folder.

### 3.2.6 Tag Organization

**Objective:**
Allow users to assign multiple tags to vault entries for flexible classification.

**Functional Behavior:**
- Tags are arbitrary text labels users attach to entries.
- Entries can have multiple tags.
- Users can create, edit, and delete tags.
- Tags support search and filtering of entries.

**Security Requirements:**
- Tags associated only with entries owned by the user.
- Optionally encrypt tag names if high confidentiality required.

**API Design:**
- **POST /api/vault/tags** — Create tag.
- **PATCH /api/vault/tags/:tag_id** — Rename tag.
- **DELETE /api/vault/tags/:tag_id** — Delete tag.

### 3.2.7 General Security Measures Across Vault Operations

- Ownership verification enforced server-side before any read/update/delete operations.
- Minimal metadata exposure in API responses (e.g., timestamps, encrypted titles).
- No plaintext vault data handled server-side at any point.
- Consistent logging of vault operations without recording sensitive field contents.
## 3.3 Encryption/Decryption

### 3.3.1 Client-Side AES-256-GCM Usage

**Objective:**
Ensure that all sensitive user data is encrypted on the client before transmission and storage, providing confidentiality even in case of server breach.

**Functional Behavior:**
- Data encryption occurs within the user's device (browser or app).
- AES-256-GCM algorithm is used:
  - 256-bit key length.
  - Galois/Counter Mode (GCM) for authenticated encryption.
  - Produces both ciphertext and an authentication tag.
- Each encrypted object (vault entry, folder name, etc.) includes:
  - Randomly generated 96-bit (12 bytes) nonce/IV (Initialization Vector).
  - Ciphertext.
  - Authentication tag.
- Nonce is unique per encryption operation and stored alongside ciphertext.

**Implementation Details:**
- Use cryptographic libraries with strong guarantees and vetted security (e.g., WebCrypto API, libsodium.js).
- Secure random generator (e.g., crypto.getRandomValues()) for IV generation.
- Combine IV + ciphertext + tag for transmission and storage.

**Security Requirements:**
- Never reuse IVs with the same key.
- Perform integrity verification during decryption by validating GCM authentication tag.
- Discard corrupted entries if integrity validation fails.

### 3.3.2 Key Derivation via Argon2

**Objective:**
Derive strong encryption keys from the user's master password in a way that resists brute-force and side-channel attacks.

**Functional Behavior:**
- Argon2id used as the Key Derivation Function (KDF):
  - Combines Argon2i's resistance to side-channel attacks with Argon2d's brute-force hardness.
- Parameters (recommended starting point, tuned per device capabilities):
  - Memory cost: 64 MB to 256 MB.
  - Iterations: 3 to 5 passes.
  - Parallelism: 1 to 4 threads.
- Salt:
  - Secure random 128-bit salt generated per user during registration.
  - Stored separately and retrieved at login.
- Derived Key Usage:
  - Encryption key for AES-GCM.
  - Optionally: a separate key for HMACs (if needed for additional message authentication).

**Implementation Details:**
- Key derivation happens entirely client-side.
- Master password never leaves the client device.
- Argon2 library must be hardened against timing attacks and side-channel leaks.

**Security Requirements:**
- Salts must be unique and random per user.
- Re-keying required if KDF parameters are upgraded later (prompt user to rederive key).

### 3.3.3 Zero-Knowledge Guarantee

**Objective:**
Architect the system to ensure that the server is incapable of reading any user vault contents, even with full access to stored data.

**Principles:**
- All sensitive user content is encrypted on the client.
- The server only sees and stores ciphertexts, IVs, authentication tags, and public metadata (e.g., registration timestamps).
- Passwords, derived keys, and decrypted content are never transmitted or stored server-side.
- Admins have zero ability to decrypt user vaults.

**Security Design Features:**
- Authentication tokens (e.g., JWTs) do not grant decryption ability, only access control.
- Loss of the master password results in irreversible data loss (unless explicit backup/recovery mechanisms are implemented client-side).
- Password reset flows must clearly warn users that resetting the master password without decrypting old vault data will render previous entries inaccessible.

**Constraints:**
- Certain minimal metadata (e.g., entry creation timestamps, folder structures if not encrypted) may remain exposed unless full database encryption is applied.
- Future features (e.g., vault sharing) must be designed carefully to preserve zero-knowledge by encrypting shared content separately.

**Security Requirements:**
- Full cryptographic audits for encryption libraries and methods used.
- Strong segregation of encrypted user data and authentication/identity management components.
- Periodic revalidation of zero-knowledge properties during system upgrades or changes.
## 3.5 Audit & Logging

### 3.5.1 Purpose

Establish a verifiable and tamper-resistant trail of critical user and system actions for security audits, intrusion detection, incident response, and user accountability without violating the application's zero-knowledge guarantees.

---

### 3.5.2 Scope of Logged Events

**Login Events:**
- Successful login.
- Failed login attempts (invalid password, invalid credentials).
- Two-factor authentication challenges and results (if implemented).

**CRUD Operations on Vault Entries:**
- Creation of a new vault entry.
- Reading (fetching) a vault entry (logged only as an access event without revealing which entry was accessed).
- Updating an existing vault entry.
- Deleting a vault entry.

**Sharing Actions:**
- Initiating vault sharing with another user.
- Accepting or rejecting a shared vault entry.
- Revoking access to shared entries.

**Administrative Actions (if admin role exists):**
- User account deactivation or deletion.
- Password reset request handling.
- Role changes or escalations.

---

### 3.5.3 Logged Metadata for Each Event

- **Event Type:** Identifier (e.g., LOGIN_SUCCESS, ENTRY_CREATE, ENTRY_UPDATE).
- **Timestamp:** UTC timestamp with milliseconds precision (ISO 8601 format).
- **User ID:** Internal user identifier (never username or email directly in the log).
- **IP Address:** Source IP of the request.
- **User Agent:** Device/browser information (optional for further forensic value).
- **Resource ID:** (only if applicable) Encrypted entry or folder ID involved.
- **Status Code:** Success or failure indicator (plus error reason if applicable).

*Note:* Never log any sensitive plaintext vault data, user passwords, or encryption keys.

---

### 3.5.4 Storage and Retention

- Logs stored in append-only systems where deletion or alteration requires explicit privileged actions.
- Secure separation of logs from operational databases (e.g., separate write-only logging service).
- Encrypt logs at rest if they contain user-identifiable metadata (e.g., IPs).
- Minimum retention: 90 days. Extendable up to 1–2 years depending on regulatory requirements or organizational policies.

---

### 3.5.5 Access Control and Privacy

- Only designated system administrators have access to view or export logs.
- Audit access to logs themselves must also be logged.
- Regular review of logs to detect anomalous behaviors (e.g., brute-force login attempts, mass vault deletion).

---

### 3.5.6 Compliance and Best Practices

- Follow security and privacy frameworks (e.g., OWASP ASVS Audit Logging controls).
- If exporting logs externally (e.g., for SIEM analysis), maintain encryption and access control.
- Redact sensitive fields even within internal analytic environments if necessary.
- Implement log integrity protections (e.g., digital signatures or hash chaining) to detect tampering.

## 4. Non-Functional Requirements (In the future!)

Some of the more advanced features outlined in this document, such as horizontal scaling, advanced disaster recovery mechanisms, and enhanced auditing/logging capabilities, will be integrated into the application once the foundational aspects of the system are fully developed and stable. These improvements will be implemented in future phases as the application evolves, ensuring a scalable, secure, and high-performance system. The initial focus will be on building a robust core, with advanced optimizations and features added progressively as the user base and system complexity grow.

## 4.1 Security

### 4.1.1 OWASP Top 10 Mitigations

**A01 - Broken Access Control**
- Enforce strict server-side authorization for every request.
- Role-based access control (RBAC) system (user, admin).
- Deny by default: every resource access must be explicitly granted.

**A02 - Cryptographic Failures**
- Encrypt all sensitive data client-side before transmission.
- Use industry-standard cryptography (AES-256-GCM, Argon2id) with vetted libraries.
- Implement strong random key material and IV generation.

**A03 - Injection**
- Sanitize all user inputs (vault entry names, notes) even if encrypted.
- Use parameterized queries on the server to prevent SQL injection.
- Escape outputs correctly in the front-end.

**A04 - Insecure Design**
- Explicit zero-knowledge architecture: server cannot decrypt user vaults.
- Threat modeling documented and reviewed per major release.

**A05 - Security Misconfiguration**
- Minimal server permissions; deny unused services and ports.
- Secure HTTP headers (CSP, HSTS, X-Content-Type-Options, etc.).
- Default to secure settings; no debug modes in production.

**A06 - Vulnerable and Outdated Components**
- Regular dependency audits with tools (e.g., npm audit, Snyk).
- Patch management process for back-end and front-end libraries.

**A07 - Identification and Authentication Failures**
- Secure password handling:
  - Argon2id for password hashing.
  - MFA (optional but recommended) at login.
- Short-lived JWTs with refresh tokens.
- Session expiration and revocation capabilities.

**A08 - Software and Data Integrity Failures**
- Front-end bundle integrity verification (e.g., Subresource Integrity, SRI).
- Digital signatures on updates if distributed outside standard web platform.

**A09 - Security Logging and Monitoring Failures**
- Comprehensive audit logging (login, CRUD actions, sharing) as per 3.5.
- Anomaly detection integration (future scope).

**A10 - Server-Side Request Forgery (SSRF)**
- No server-side retrieval of external URLs without strict whitelisting (future-proofing).

---

### 4.1.2 Data-at-Rest Encryption

**Server-Side:**
- Even though vault contents are encrypted client-side, server will encrypt stored blobs again using volume/database encryption (e.g., AES-256 at database layer).
- Database credentials stored securely, outside codebase (environment variables, vault services).
- Backup storage encrypted to the same standards as primary data.

**Client-Side:**
- All vault data encrypted on the device before transmission.
- Persistent storage (localStorage, IndexedDB) uses encrypted forms only if offline access is implemented.

---

### 4.1.3 Data-in-Transit Encryption

- Enforce HTTPS with TLS 1.3 only.
- HSTS (HTTP Strict Transport Security) enabled with a long max-age and preload.
- TLS certificates from trusted Certificate Authorities (CA).
- Redirect all HTTP traffic to HTTPS automatically.
- WebSocket connections (if used) secured via WSS.

---

### 4.1.4 Additional Security Layers

- Content Security Policy (CSP) to prevent XSS attacks.
- X-Frame-Options set to DENY to prevent clickjacking.
- Rate-limiting on authentication endpoints to deter brute-force attacks.
- CAPTCHA integration after multiple failed login attempts (optional for higher security).
## 4.2 Performance

### 4.2.1 Target Latency for Vault Read/Write

**Read Operations:**
- Decrypting and rendering a vault entry after user action (e.g., opening the vault dashboard) must occur in under **200ms** for 95th percentile of cases.
- Full vault synchronization (pulling all metadata and required encrypted objects) must complete in under **2 seconds** for vaults with up to **1000 entries**.

**Write Operations:**
- Creating, updating, or deleting a vault entry must achieve confirmation (including server acknowledgment) in under **300ms** in normal network conditions.
- Vault sync state after write must be consistent and available within **500ms** maximum.

**Encryption Overhead:**
- Client-side encryption/decryption operations must not introduce perceivable lag:
  - Single entry encrypt/decrypt under **50ms** on a typical user device (mid-range smartphone or laptop).
  - Argon2id password-derived key generation at login acceptable within **1–2 seconds**.

**Network Conditions Assumed:**
- Latency benchmarks based on typical broadband or 4G+ network conditions (~50–100ms RTT).
- Application must degrade gracefully on higher-latency networks (e.g., visual loading indicators, background sync).

---

### 4.2.2 Concurrency Requirements

**User Concurrency:**
- Back-end API must be able to handle a minimum of **1000 concurrent authenticated sessions** without significant degradation in response time.
- Horizontal scaling architecture (stateless back-end services where possible) to allow future scaling to **10,000+ concurrent users**.

**Per-User Operations:**
- Support multiple concurrent sessions per user (e.g., logged in simultaneously on desktop and mobile).
- Vault sync mechanism must resolve conflicts safely:
  - Last-write-wins strategy for simple overwrites.
  - Future implementation scope: full operational transformation (OT) or conflict-free replicated data types (CRDTs) for real-time collaboration features.

**Server Load Management:**
- Use connection pooling and async I/O on the back-end to maximize throughput (e.g., Node.js event loop efficiency, Postgres connection pooling).
- Rate limit non-critical API calls to prevent abuse or accidental overload.

**Resource Constraints:**
- Vault data structures optimized for low memory and CPU usage on client devices.
- Server queries and storage access designed to avoid N+1 problems and unnecessary full scans.

---

### 4.2.3 Performance Monitoring

- Implement real-time application performance monitoring (APM) tools (e.g., New Relic, Datadog) during staging and production.
- Collect telemetry on:
  - API endpoint response times.
  - Vault synchronization durations.
  - Encryption/decryption processing times.
- Use this data to continuously optimize system bottlenecks before major releases.
## 4.3 Scalability

### 4.3.1 Horizontal Scaling Strategy

**Application Layer:**
- Design back-end services to be stateless, allowing replication across multiple instances.
- Deploy application servers behind a load balancer (e.g., AWS ELB, NGINX) to distribute incoming API requests evenly.
- Auto-scaling groups configured to dynamically adjust the number of application instances based on CPU, memory usage, or request throughput thresholds.

**Database Layer:**
- Use a relational database (e.g., PostgreSQL) with vertical scaling initially (scale-up).
- Plan for read replicas to distribute read-heavy traffic (eventually consistent reads acceptable for non-critical operations like dashboard vault listings).
- Connection pooling middleware (e.g., PgBouncer) to optimize database concurrency under load.
- Future scope: investigate sharding strategies (by user ID range) when the primary database approaches performance limits.

**Object Storage:**
- Store encrypted vault blobs (if separated from database records) in scalable object storage (e.g., AWS S3, Azure Blob Storage) with redundant, distributed architecture.
- Implement Content Delivery Network (CDN) caching layers if vault metadata or assets become sufficiently large or frequently accessed.

**Caching Layer:**
- Introduce an in-memory cache (e.g., Redis, Memcached) for:
  - Session/token management.
  - Frequently accessed non-sensitive metadata (e.g., folder structures, sharing relationships).
- Cache invalidation policies must ensure consistency after CRUD operations.

**Front-End Delivery:**
- Front-end built assets hosted on a global CDN for low-latency delivery worldwide.
- Versioned front-end deployments to ensure cache busting and smooth rollouts.

**Scaling for Background Jobs:**
- Use distributed queue systems (e.g., RabbitMQ, Redis Streams) for non-immediate processing tasks:
  - Audit log writing.
  - Notification sending.
  - Sharing acceptance processing.

- Scale worker pools independently from API servers according to job queue backlog.

**Monitoring and Auto-healing:**
- Health checks configured at the load balancer level.
- Automatic replacement of unhealthy instances without human intervention.
- Alerting systems in place to detect load anomalies and trigger scaling events before saturation.

**Data Partitioning Considerations (Future Scope):**
- If single-database writes become a bottleneck, partition user vaults logically (e.g., by user ID modulo N across database clusters).
- Maintain a global index service to map user IDs to the correct partition.

---
## 4.4 Availability & Reliability

### 4.4.1 SLA Targets

**Service Availability:**
- Target service uptime of **99.9%** annually (excluding scheduled maintenance).
  - This equates to no more than **8.77 hours** of downtime per year or approximately **43 minutes** of downtime per month.

**API Response Time:**
- **99% of all API requests** should respond in **under 200ms** for read operations and **under 300ms** for write operations.
- Critical operations (e.g., login, vault access) should have response times under **100ms** for **95% of users**.

**Database Availability:**
- Aim for **99.99%** database availability, with replication and failover mechanisms ensuring minimal downtime in case of failure.

**Disaster Recovery & Failover:**
- All critical services (e.g., web servers, database servers) should have failover capabilities configured to automatically route traffic to healthy instances or regions without user interruption.

---

### 4.4.2 Backup and Disaster Recovery

**Backup Strategy:**
- **Database Backups:**
  - Perform **daily full backups** of all production databases.
  - **Hourly incremental backups** of critical vault data (to minimize data loss in case of failure).
  - Backups stored offsite in a geographically redundant region (e.g., AWS S3 with versioning enabled or a secondary data center).

- **Application Backups:**
  - Regularly backup application configuration and critical settings (e.g., user roles, permissions).
  - Store backups encrypted at rest with robust key management practices.

- **Backup Retention:**
  - Retain daily backups for **30 days**.
  - Retain weekly backups for **90 days**.
  - Retain monthly backups for **1 year**.

- **Backup Integrity:**
  - Periodically test backup restoration procedures to ensure data can be restored quickly and correctly.
  - Log each backup process for verification and auditing purposes.

---

**Disaster Recovery Plan:**
- **RTO (Recovery Time Objective):** Target **2 hours** to fully restore service in the event of a critical failure or disaster.
- **RPO (Recovery Point Objective):** Ensure that the maximum data loss is **less than 1 hour** by having backups taken at least every hour.

**High-Availability (HA) Architecture:**
- Deploy applications across **multiple availability zones** or data centers to ensure service continuity during zone failures.
- Set up **automatic failover** between active and passive instances in case of primary system failure (e.g., for databases, load balancers).
- Use **geo-redundant** deployments for critical systems (e.g., database replicas, application services) to provide failover across regions.

**Incident Response:**
- Establish an incident response team for fast identification and mitigation of service failures.
- Incident reports and resolution timelines must be documented for internal review.
- Users should be notified about outages with clear explanations and expected timelines for resolution.

---

## 4.5 Maintainability

### 4.5.1 Code Standards

**Consistency:**
- Adhere to established coding standards for all languages and frameworks used (e.g., JavaScript, TypeScript, Node.js, etc.).
- Utilize industry best practices for clean, modular, and scalable code:
  - Use **SOLID** principles for object-oriented design.
  - Follow **DRY (Don't Repeat Yourself)** and **KISS (Keep It Simple, Stupid)** principles.

**Code Style:**
- Use consistent naming conventions across all files, variables, and functions:
  - **camelCase** for variables, functions, and method names.
  - **PascalCase** for classes and components.
  - **UPPER_CASE** for constants and environment variables.

- Enforce formatting consistency using linters and auto-formatters (e.g., **Prettier**, **ESLint** for JavaScript/TypeScript).
  - Configurations should be set up for both front-end and back-end development to ensure code quality is maintained across the project.

**Modular Code:**
- Split functionality into clear, well-defined modules. This allows for easier testing, maintenance, and updates.
- Apply proper separation of concerns (e.g., separate services, utilities, models, and controllers).

**Error Handling:**
- Implement consistent and clear error handling throughout the application:
  - Use **try-catch** blocks where appropriate in asynchronous code.
  - Implement proper error messages with meaningful error codes.
  - Log errors centrally using a logging system like **Winston** (for Node.js).

---

### 4.5.2 Documentation

**Code Documentation:**
- Every public function, method, and class must be documented with meaningful comments describing:
  - The function's purpose.
  - Expected inputs and outputs (parameters and return types).
  - Side effects, if any.

- Use **JSDoc** or similar tools to generate API documentation from comments. This should be automated as part of the build process.
  - Example:
    ```javascript
    /**
     * Encrypts the vault entry data with AES-256-GCM.
     * @param {string} data - The plain text data to be encrypted.
     * @param {string} password - The password used for encryption.
     * @returns {string} - The encrypted data in base64 format.
     */
    function encryptVaultEntry(data, password) {
      // Implementation
    }
    ```

**Project Documentation:**
- Provide detailed documentation for the project setup, deployment, and architecture:
  - Include information on setting up the development environment, building the project, and running tests.
  - High-level overviews of system components, their interactions, and the underlying architecture.

- Store **README.md** files in each module or service directory to provide specific instructions for those components.

**User Documentation:**
- A user manual should be created to guide end-users on how to use the password manager, explaining features like vault creation, password generation, and sharing.

---

### 4.5.3 Automated Checks

**Linting and Formatting:**
- Integrate **ESLint** and **Prettier** into the build pipeline to enforce code quality standards.
  - Linting should cover both JavaScript/TypeScript code and configuration files (e.g., JSON, YAML).
  - Prettier should automatically format code to ensure consistency across the project.

**Unit Testing:**
- Set up automated unit testing using a framework like **Jest** or **Mocha** (for JavaScript/TypeScript) or **Cucumber** for behavior-driven development.
  - Aim for a minimum of **80% test coverage** across all critical modules.
  - Ensure that tests are easily run using commands like `npm run test`.

**Integration Testing:**
- Integration tests should be in place to verify that different parts of the system work together as expected:
  - **API testing** to ensure that routes, authentication, and database interactions are working.
  - Use tools like **Supertest** or **Postman** for automated API testing.

**Continuous Integration (CI):**
- Implement a CI pipeline with a platform like **GitHub Actions**, **Travis CI**, or **CircleCI** to automate:
  - Code linting and formatting checks.
  - Unit and integration testing on every pull request.
  - Deployment pipeline for staging and production.

**Continuous Deployment (CD):**
- Automate deployment processes with a **CD pipeline** that deploys code to staging and production environments:
  - Implement automatic deployments upon merging code into main branches.
  - Ensure successful build and tests before deployment to production.

**Code Coverage Reports:**
- Use coverage tools like **Istanbul** (via Jest) or **nyc** to generate code coverage reports.
  - Coverage reports should be generated automatically and accessible for review after each test run.

**Static Analysis Tools:**
- Use static analysis tools (e.g., **SonarQube**, **CodeClimate**) to analyze code quality and identify areas for improvement, like unused code, potential bugs, or security vulnerabilities.

---

### 4.5.4 Version Control & Branching Strategy

**Git Flow:**
- Use **Git Flow** or a similar branching strategy:
  - **Main branch** holds production-ready code.
  - **Develop branch** is for ongoing development and integration.
  - **Feature branches** for new features, bug fixes, and experiments.
  - **Release branches** for preparing and stabilizing production releases.

**Commit Messages:**
- Follow a standardized format for commit messages (e.g., **Conventional Commits**):
  - `feat:` for new features.
  - `fix:` for bug fixes.
  - `docs:` for documentation changes.
  - `style:` for code style changes (no logic changes).
  - `refactor:` for refactoring code.
  - `test:` for adding or updating tests.

**Pull Requests (PRs):**
- All code changes must go through a PR process where:
  - Code is reviewed by at least one other team member.
  - The PR description clearly explains the purpose of the changes.
  - The code is thoroughly tested, with proper test coverage.

**Release Notes:**
- Keep a **CHANGELOG.md** to track new features, fixes, and breaking changes across releases.

---

## 5. System Architecture

In the System Architecture section, we will outline the high-level structure of the application, describing how different components interact to deliver the functionality of the password manager. This will include the organization of the front-end and back-end layers, database design, and the communication between services. We will cover the choice of technologies, the role of each component, and how they work together to ensure performance, security, and scalability. Key architectural patterns such as client-server model, microservices (if applicable), and security considerations (e.g., encryption, authentication) will also be addressed. This section will provide a clear, modular view of the application’s design and how it supports both the current requirements and future growth.

## 5.1 Component Diagram

The **Component Diagram** provides an overview of the application's main components and their interactions. Below is a description of each major component within the architecture:

### 1. **Front-End (Client-Side Application)**
The front-end application is responsible for the user interface and the overall user experience. It is typically built using **React** or **Vue.js** and communicates with the back-end API to send and receive data. The front-end ensures secure handling of user inputs, such as login credentials and vault data, and presents them in a user-friendly manner.

- **Key Responsibilities**:
  - User registration, login, and authentication.
  - Vault management: Create, read, update, delete entries.
  - Interaction with encrypted data (e.g., display passwords without exposing them in plain text).

---

### 2. **API Layer (Back-End)**
The back-end API layer handles client requests and processes them in line with business logic. It ensures that all operations, such as authentication, CRUD operations on the vault, and user management, are secure, efficient, and accurate.

- **Key Responsibilities**:
  - Expose RESTful API endpoints for user authentication and vault management.
  - Interface with the database to store and retrieve user data and encrypted vault entries.
  - Handle encryption and decryption of sensitive data on the server-side.

---

### 3. **Database**
The database stores user data, vault entries, and metadata. A relational database such as **PostgreSQL** is used to store structured data, ensuring data integrity and consistency. Data such as user credentials, vault metadata (e.g., folder names, tags), and sharing information are stored here.

- **Key Responsibilities**:
  - Store user authentication information (e.g., hashed passwords, user profiles).
  - Store metadata related to vault entries, such as tags, labels, and folder structures.
  - Ensure fast and reliable access to encrypted vault entries and metadata.

---

### 4. **Key-Management System (KMS)**
The KMS is responsible for securely managing the encryption keys used to protect sensitive user data. In the application, encryption keys are critical for maintaining data confidentiality. A KMS may be implemented either as a custom solution or with a third-party service (e.g., AWS KMS, Azure Key Vault).

- **Key Responsibilities**:
  - Generate, store, and rotate encryption keys.
  - Protect user data by ensuring that encryption keys are never stored in plaintext.
  - Integrate with the encryption/decryption logic to ensure keys are securely handled.

---

### 5. **Hardware Security Module (HSM) / Vault**
A **Hardware Security Module (HSM)** or **Vault** is a physical or cloud-based service that securely stores encryption keys. HSMs provide additional protection by ensuring that keys are never exposed to unauthorized access. If integrated, an HSM would add an extra layer of security for managing sensitive encryption operations and key storage.

- **Key Responsibilities**:
  - Store encryption keys securely.
  - Perform cryptographic operations (e.g., key generation, encryption, decryption) without exposing sensitive data.
  - Provide tamper-proof hardware to ensure that keys cannot be compromised or extracted.

---

### Component Interaction:
- The **Front-End** communicates with the **API Layer** over HTTPS, using authentication tokens (e.g., JWT) to ensure secure communication.
- The **API Layer** handles business logic, authenticating users and performing operations on data, like adding, editing, or deleting vault entries.
- The **API Layer** interacts with the **Database** to store user data and encrypted vault entries.
- The **API Layer** also interfaces with the **Key-Management System (KMS)** for encryption and decryption of sensitive data.
- If an **HSM** or **Vault** is used, the KMS will delegate key management and cryptographic operations to it, ensuring that encryption keys are never exposed in plain text during the process.

This modular architecture ensures that sensitive data remains secure at all stages, while allowing for easy maintenance, scalability, and future enhancements.

---

## 5.2 Data Flow

The **Data Flow** section outlines the sequence of operations performed by the application when a user interacts with it. This section focuses on the key operations related to user authentication and secure vault data handling, from login through to vault entry decryption. Below is a step-by-step breakdown of the typical data flow in the system.

### 1. **Login**
- The user enters their credentials (username/email and password) on the front-end login page.
- The front-end sends an HTTP POST request to the back-end API with the user’s credentials over a secure HTTPS connection.
- The API verifies the credentials by checking the user’s stored, hashed password in the database.
- Upon successful authentication, the API generates a **JWT (JSON Web Token)** or a session token, which is sent back to the front-end. This token will be used for subsequent authorized requests.
- **Important**: The password is never stored in plain text on the server; it is hashed using a strong hashing algorithm (e.g., **bcrypt** or **Argon2**).

---

### 2. **Key Derivation**
- After successful login, the front-end sends a request to the back-end to access the user’s vault.
- The back-end retrieves the user’s **salt** from the database (associated with their account) and uses it along with the user’s password to perform **key derivation**.
  - **Key Derivation Function (KDF)**: **Argon2** is used to securely derive a key from the user’s password and salt. This ensures that even if two users have the same password, the resulting keys will be unique due to the use of different salts.
  - The derived key is used to decrypt the **master encryption key** for the vault stored securely in the KMS (Key-Management System) or HSM.

---

### 3. **Vault Fetch**
- Once the key is derived, the back-end uses it to decrypt the **master key** and then fetch the encrypted vault entries from the database.
- The vault entries are encrypted with **AES-256-GCM** encryption. The back-end fetches the corresponding encrypted data from the database and prepares it for decryption.
- The back-end sends the encrypted vault entries to the front-end in response to the request. The data remains encrypted during transmission.

---

### 4. **Decryption**
- The front-end receives the encrypted vault data from the back-end and begins the decryption process.
- The **master key**, which was derived using Argon2 and fetched from the back-end, is used to decrypt the vault entries. This decryption happens client-side to ensure that the application never exposes sensitive data in plaintext to the server.
  - **AES-256-GCM** is used for the decryption process to ensure that the vault data remains protected.
- Once the vault entries are decrypted, the front-end displays them securely in the user interface.
- The front-end is responsible for securely managing the decrypted data, ensuring that it is never stored in local storage or exposed unnecessarily.

---

### Summary of the Data Flow:
1. **Login**: User submits credentials → API verifies credentials → JWT/session token returned.
2. **Key Derivation**: User password + salt → Argon2 KDF → Derived key used for decrypting master key.
3. **Vault Fetch**: API fetches encrypted vault data from the database → Sends encrypted data to front-end.
4. **Decryption**: Front-end decrypts vault entries using master key → Decrypted data displayed to the user.

This secure, client-side decryption flow ensures that the application remains zero-knowledge, meaning even the back-end never has access to the user’s sensitive vault data in plaintext. Only the client, with the correct password-derived key, can decrypt and access the vault content.

---

## 5.3 Deployment Topology

The **Deployment Topology** outlines the infrastructure setup and deployment strategy for the password manager application. This section details how the application will be deployed in different environments (e.g., development, staging, production) using containerization and orchestration tools like **Docker**, **Amazon ECS (Elastic Container Service)**, and **Kubernetes**.

### 1. **Docker**
- **Docker** is used for containerizing the application components, ensuring consistency across different environments and simplifying the deployment process.
- Each major component of the application (front-end, back-end, database, key-management system) will be containerized into separate Docker images.
  - **Front-End**: A container running the front-end React/Vue application.
  - **Back-End**: A container running the Node.js/Express or other back-end server.
  - **Database**: A container running a relational database (e.g., PostgreSQL or MySQL).
  - **Key Management**: A container for the key-management system, such as HashiCorp Vault, or an integrated KMS service.

- **Docker Compose**: During development, **Docker Compose** can be used to spin up all containers locally for testing and integration purposes. The Docker Compose file will define the services, networks, and volumes required for the development environment.

---

### 2. **Amazon ECS (Elastic Container Service)**
- In production, the application will be deployed using **Amazon ECS**, which automates the deployment, scaling, and management of Docker containers on AWS.
- **ECS Cluster**: The ECS cluster will consist of multiple EC2 instances (or Fargate tasks, if using serverless) where the application containers will be deployed.
  - **Tasks**: Each component of the application (front-end, back-end, database) will run in its own ECS task.
  - **Task Definitions**: Task definitions define the containers’ configurations, including the Docker image, environment variables, resource allocation (CPU, memory), and networking settings.

- **Load Balancer**: An **Application Load Balancer (ALB)** can be used to distribute traffic to the appropriate ECS tasks based on routing rules (e.g., forward traffic to the front-end container or the back-end API container based on URL paths).

- **Auto-Scaling**: ECS can be configured to automatically scale the application’s services based on load. For example, the back-end service can be scaled up to handle a high volume of API requests during peak usage times.

---

### 3. **Kubernetes**
- As the application grows, **Kubernetes** can be used for container orchestration across multiple cloud environments or on-premise clusters.
- **Kubernetes Cluster**: The application components (front-end, back-end, database, etc.) will be deployed as **Pods** in a **Kubernetes Cluster**.
  - Each component will be managed by its own **Deployment**, ensuring that replicas are maintained for high availability.
  - **Services** will be defined to expose each component (e.g., front-end service, back-end API service) and enable communication between them.

- **Kubernetes Horizontal Pod Autoscaling (HPA)**: HPA will be used to scale the number of replicas for components such as the back-end or database based on CPU or memory usage. This helps ensure optimal performance and availability during varying levels of traffic.

- **Ingress Controller**: An **Ingress Controller** will manage external access to the services running in the Kubernetes cluster. It will route requests to the appropriate services, using an **Ingress resource** to manage traffic routing and SSL termination.

---

### 4. **Environments**
- The deployment topology will support multiple environments, each tailored to different stages of the development lifecycle (e.g., development, staging, production).

  - **Development Environment**:
    - Locally using Docker Compose for fast iteration and testing.
    - Containerized services are orchestrated manually or via Docker Compose.

  - **Staging Environment**:
    - Hosted on ECS or Kubernetes, reflecting the production environment closely.
    - Used for testing in a production-like setup, including continuous integration/continuous deployment (CI/CD) pipelines.

  - **Production Environment**:
    - Fully managed ECS or Kubernetes clusters for high availability, scalability, and fault tolerance.
    - Load balancers, auto-scaling, and monitoring tools in place to ensure optimal performance.

---

### 5. **CI/CD Pipeline**
- The deployment process will be automated with a **CI/CD pipeline** that handles:
  - **Code Integration**: Code from the repository is automatically built, tested, and packaged into Docker containers.
  - **Continuous Delivery**: Once tested, the Docker images are pushed to a container registry (e.g., Docker Hub, Amazon ECR).
  - **Deployment**: The containerized application is deployed to ECS, Kubernetes, or other environments automatically.
  - **Rollback Mechanism**: If any issues arise during deployment, the pipeline allows for easy rollback to the previous stable version.

---

### Summary of Deployment Topology:
1. **Docker**: Containerizes all components for local and production environments.
2. **Amazon ECS**: Orchestrates containers on EC2 instances or using serverless Fargate for scalable, managed deployments.
3. **Kubernetes**: Used for advanced orchestration with auto-scaling and high availability, for future scaling needs.
4. **CI/CD Pipeline**: Automated testing and deployment processes to ensure consistent and reliable releases across all environments.

By using Docker, ECS, and Kubernetes, the application can be efficiently managed and scaled while maintaining high availability and fault tolerance in different environments.

---

## 6. Data Model
The **Data Model** defines the structure and relationships between the various entities within the password manager application. The data model will ensure the secure and efficient storage and retrieval of sensitive information, including user accounts, vault entries, encryption keys, and audit logs. This section details the database schema, entity relationships, and key design decisions.

### 6.1 Entities

The following entities are the core components of the password manager system. Each entity is designed to represent a specific aspect of the application and its interaction with the user and the underlying database. Below is a detailed breakdown of each entity and its key attributes.

---

#### **User**
- **Purpose**: Represents a person who uses the password manager application.
- **Attributes**:
  - **id**: Unique identifier for each user (auto-incremented).
  - **email**: The user’s email address, used for login.
  - **hashed_password**: The securely hashed password of the user (using a secure hashing algorithm like bcrypt or Argon2).
  - **salt**: The salt used in the password hashing process to ensure uniqueness and prevent rainbow table attacks.
  - **created_at**: Timestamp for when the user account was created.
  - **updated_at**: Timestamp for when the user account was last updated.

- **Relationships**:
  - A **User** can have multiple **Vaults** (one-to-many).
  - A **User** can have multiple **AuditLogs** (one-to-many).
  - A **User** can have multiple **Sessions** (one-to-many).

---

#### **VaultEntry**
- **Purpose**: Represents an individual piece of stored data in the vault, such as a password, secure note, or URL.
- **Attributes**:
  - **id**: Unique identifier for each vault entry.
  - **vault_id**: Foreign key referencing the vault the entry belongs to.
  - **title**: The title or name of the entry (e.g., "Gmail Password").
  - **username**: The username associated with the entry.
  - **password**: The encrypted password associated with the entry.
  - **url**: A URL associated with the entry (e.g., the website URL).
  - **notes**: Additional notes or details about the entry.
  - **tags**: An array of tags used to categorize the vault entry (e.g., “work”, “banking”).
  - **created_at**: Timestamp for when the entry was created.
  - **updated_at**: Timestamp for when the entry was last updated.

- **Relationships**:
  - A **VaultEntry** belongs to a **Vault** (many-to-one).
  - A **VaultEntry** can have multiple **Tags** (many-to-many), which are used for categorization.

---

#### **SharedVault**
- **Purpose**: Represents a vault that can be shared with other users, allowing collaboration on specific vault entries.
- **Attributes**:
  - **id**: Unique identifier for each shared vault.
  - **vault_id**: Foreign key referencing the vault that is being shared.
  - **shared_with_user_id**: Foreign key referencing the user who the vault is shared with.
  - **permissions**: Defines the permissions for the shared vault, such as read-only or read/write access.
  - **created_at**: Timestamp for when the shared vault was created.
  - **updated_at**: Timestamp for when the shared vault was last updated.

- **Relationships**:
  - A **SharedVault** is associated with a single **Vault** (many-to-one).
  - A **SharedVault** can be shared with multiple **Users** (many-to-many).
  - A **User** can have multiple **SharedVaults** (one-to-many).

---

#### **AuditLog**
- **Purpose**: Tracks significant actions or events within the system, such as user logins, CRUD operations, and sharing actions.
- **Attributes**:
  - **id**: Unique identifier for each log entry.
  - **user_id**: Foreign key referencing the user who performed the action.
  - **action**: A description of the action that was logged (e.g., "create vault entry", "login").
  - **timestamp**: Timestamp when the action occurred.
  - **ip_address**: The IP address from which the action was performed.
  - **details**: Any additional details related to the action (e.g., specific vault or entry affected).

- **Relationships**:
  - An **AuditLog** is associated with a **User** (many-to-one).

---

#### **Session**
- **Purpose**: Represents an active session for a user, typically established after login and used to authorize access to the password manager’s vault.
- **Attributes**:
  - **id**: Unique identifier for each session.
  - **user_id**: Foreign key referencing the user who owns the session.
  - **token**: A secure, uniquely generated token for authenticating requests.
  - **created_at**: Timestamp for when the session was created.
  - **expires_at**: Timestamp for when the session will expire, indicating session timeout.
  - **last_activity_at**: Timestamp for the last user activity associated with the session.

- **Relationships**:
  - A **Session** is associated with a single **User** (many-to-one).

---

### Summary

The **Entities** section defines the core building blocks of the system, representing various aspects of the password manager application. Each entity has a set of attributes that enable secure and efficient management of user data, vault entries, and actions. Relationships between entities ensure that the data can be accessed, modified, and organized in a logical and secure manner. This design facilitates scalability, security, and maintainability across the entire application.

---

### 6.2 Attributes & Constraints

This section defines the attributes and constraints associated with each entity in the data model. It covers column types, encryption strategies, and Row-Level Security (RLS) policies that ensure the security and integrity of the data.

---

#### **User Entity**

- **id**:
  - Type: `SERIAL`
  - Constraint: `PRIMARY KEY`
  - Description: Auto-incremented identifier for each user.

- **email**:
  - Type: `VARCHAR(255)`
  - Constraint: `UNIQUE NOT NULL`
  - Description: The user's email address, which is unique for each user and is used for login.

- **hashed_password**:
  - Type: `VARCHAR(255)`
  - Constraint: `NOT NULL`
  - Description: The securely hashed password of the user. This column stores the result of the password hashing function (e.g., bcrypt, Argon2).

- **salt**:
  - Type: `VARCHAR(255)`
  - Constraint: `NOT NULL`
  - Description: The salt used during the password hashing process, ensuring the uniqueness of hashed passwords for the same input.

- **created_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp when the user account was created.

- **updated_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp when the user account was last updated.

---

#### **VaultEntry Entity**

- **id**:
  - Type: `SERIAL`
  - Constraint: `PRIMARY KEY`
  - Description: Unique identifier for each vault entry.

- **vault_id**:
  - Type: `INTEGER`
  - Constraint: `REFERENCES vaults(id) ON DELETE CASCADE`
  - Description: Foreign key to the vault that contains the entry. Ensures cascading delete if the vault is deleted.

- **title**:
  - Type: `VARCHAR(255)`
  - Constraint: `NOT NULL`
  - Description: The title or name of the entry (e.g., "Gmail Password").

- **username**:
  - Type: `VARCHAR(255)`
  - Constraint: `NULL`
  - Description: The username associated with the entry.

- **password**:
  - Type: `TEXT`
  - Constraint: `NOT NULL`
  - Encryption: This column will store encrypted password data using **AES-256-GCM**.
  - Description: The encrypted password associated with the entry.

- **url**:
  - Type: `VARCHAR(255)`
  - Constraint: `NULL`
  - Description: The URL associated with the entry (e.g., the website URL).

- **notes**:
  - Type: `TEXT`
  - Constraint: `NULL`
  - Description: Additional notes related to the entry.

- **tags**:
  - Type: `TEXT[]`
  - Constraint: `NULL`
  - Description: An array of tags used to categorize the vault entry (e.g., "work", "banking").

- **created_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp when the entry was created.

- **updated_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp when the entry was last updated.

---

#### **SharedVault Entity**

- **id**:
  - Type: `SERIAL`
  - Constraint: `PRIMARY KEY`
  - Description: Unique identifier for each shared vault.

- **vault_id**:
  - Type: `INTEGER`
  - Constraint: `REFERENCES vaults(id) ON DELETE CASCADE`
  - Description: Foreign key to the vault being shared.

- **shared_with_user_id**:
  - Type: `INTEGER`
  - Constraint: `REFERENCES users(id) ON DELETE CASCADE`
  - Description: Foreign key to the user with whom the vault is shared.

- **permissions**:
  - Type: `VARCHAR(255)`
  - Constraint: `NOT NULL`
  - Description: Defines the permissions granted for the shared vault (e.g., read-only, read/write).

- **created_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp when the shared vault was created.

- **updated_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp when the shared vault was last updated.

---

#### **AuditLog Entity**

- **id**:
  - Type: `SERIAL`
  - Constraint: `PRIMARY KEY`
  - Description: Unique identifier for each log entry.

- **user_id**:
  - Type: `INTEGER`
  - Constraint: `REFERENCES users(id) ON DELETE CASCADE`
  - Description: Foreign key to the user who performed the action.

- **action**:
  - Type: `VARCHAR(255)`
  - Constraint: `NOT NULL`
  - Description: Describes the action logged (e.g., "create vault entry", "login").

- **timestamp**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp of when the action occurred.

- **ip_address**:
  - Type: `VARCHAR(50)`
  - Constraint: `NULL`
  - Description: IP address from which the action was performed.

- **details**:
  - Type: `TEXT`
  - Constraint: `NULL`
  - Description: Any additional details related to the action (e.g., specific vault or entry affected).

---

#### **Session Entity**

- **id**:
  - Type: `SERIAL`
  - Constraint: `PRIMARY KEY`
  - Description: Unique identifier for each session.

- **user_id**:
  - Type: `INTEGER`
  - Constraint: `REFERENCES users(id) ON DELETE CASCADE`
  - Description: Foreign key referencing the user associated with the session.

- **token**:
  - Type: `VARCHAR(255)`
  - Constraint: `NOT NULL`
  - Description: A secure, randomly generated token used for authentication.

- **created_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp when the session was created.

- **expires_at**:
  - Type: `TIMESTAMP`
  - Constraint: `NOT NULL`
  - Description: Timestamp when the session will expire.

- **last_activity_at**:
  - Type: `TIMESTAMP`
  - Constraint: `DEFAULT CURRENT_TIMESTAMP`
  - Description: Timestamp for the last user activity in the session.

---

### 2. **Encryption Columns**

Certain sensitive columns will be encrypted using **AES-256-GCM** to ensure data privacy. Specifically:
- **VaultEntry.password**: This column stores passwords and other sensitive data, and will be encrypted before storage. The encryption key will be derived from the user's master password using a secure key derivation function (e.g., Argon2).
- **VaultEntry.notes**: If storing particularly sensitive information in notes, this can be encrypted with a separate key or the same key used for passwords.

The encryption and decryption of these fields will be handled at the application level, ensuring that data is never stored in plaintext.

---

### 3. **Row-Level Security (RLS) Policies**

Row-Level Security (RLS) is used to ensure that users can only access the vaults and entries that belong to them or that they have been explicitly shared with. The following RLS policies will be enforced:

- **Users can only access their own vaults**:
  - Policy: Only allow access to vaults where the `user_id` matches the session's user ID.

- **Users can only access their own vault entries**:
  - Policy: Only allow access to vault entries where the `vault_id` belongs to the user's vault.

- **Shared vaults**:
  - Policy: Allow access to shared vaults based on the `shared_with_user_id` field.

- **Audit logs are restricted**:
  - Policy: Audit logs will be accessible only by administrators or the users who performed the action, ensuring that each user can only view their own actions and not those of others.

---

### Summary

The **Attributes & Constraints** section defines the data types, encryption requirements, and security constraints for the various entities in the system. By implementing proper column types, encryption for sensitive data, and strict Row-Level Security policies, we ensure that the application is both secure and efficient while maintaining user privacy. These constraints form the foundation for secure data access and storage, and play a crucial role in the overall system's integrity and confidentiality.

---

### 6.3 Relationships

This section defines the relationships between the various entities in the system, emphasizing the structure of data and how entities are interconnected. The relationships are important for ensuring the integrity of the system and for enabling proper data access. Below is the description of the relationships and the corresponding Entity-Relationship (ER) diagram.

---

#### **1. One-to-Many Relationship: User → VaultEntry**

- **Description**: A user can have multiple vault entries, but each vault entry is associated with exactly one user. This relationship ensures that a user's vault entries are tied to their account and can be managed accordingly.

- **Entities Involved**:
  - **User** → **VaultEntry**

- **Relationship**:
  - A **User** can create many **VaultEntry** records (one-to-many).
  - A **VaultEntry** belongs to one **User** (many-to-one).

- **Foreign Key**:
  - The `user_id` in the **VaultEntry** table references the `id` field in the **User** table.

---

#### **2. Many-to-Many Relationship: Vault → User (SharedVault)**

- **Description**: A vault can be shared with multiple users, and a user can have access to multiple vaults. This relationship is implemented through the **SharedVault** entity, which manages the many-to-many relationship between users and shared vaults.

- **Entities Involved**:
  - **User** ↔ **Vault** (via **SharedVault**)

- **Relationship**:
  - A **Vault** can be shared with many **Users** (many-to-many).
  - A **User** can have access to many **Vaults** (many-to-many).

- **Through Entity**:
  - The **SharedVault** entity manages this many-to-many relationship. It stores the `user_id`, `vault_id`, and the `permissions` granted to the user for that specific vault.

- **Foreign Keys**:
  - The `user_id` in the **SharedVault** table references the `id` field in the **User** table.
  - The `vault_id` in the **SharedVault** table references the `id` field in the **Vault** table.

---

#### **3. One-to-Many Relationship: User → AuditLog**

- **Description**: Each action performed by a user (such as logging in, creating an entry, etc.) is logged in the **AuditLog** table. A user can have multiple log entries, but each log entry is associated with exactly one user.

- **Entities Involved**:
  - **User** → **AuditLog**

- **Relationship**:
  - A **User** can generate many **AuditLog** entries (one-to-many).
  - An **AuditLog** belongs to one **User** (many-to-one).

- **Foreign Key**:
  - The `user_id` in the **AuditLog** table references the `id` field in the **User** table.

---

#### **4. One-to-Many Relationship: User → Session**

- **Description**: A user can have multiple active sessions (e.g., from different devices or browsers), but each session is associated with exactly one user.

- **Entities Involved**:
  - **User** → **Session**

- **Relationship**:
  - A **User** can have many **Session** records (one-to-many).
  - A **Session** is associated with one **User** (many-to-one).

- **Foreign Key**:
  - The `user_id` in the **Session** table references the `id` field in the **User** table.

---

#### **Entity-Relationship (ER) Diagram Overview**

Below is the textual representation of the Entity-Relationship (ER) diagram for the described relationships:

| Entity         | Attributes                                             | Relationships                                                    |
|----------------|---------------------------------------------------------|-------------------------------------------------------------------|
| User           | id (PK), email, hashed_password, salt, created_at, updated_at | One-to-Many → VaultEntry<br>One-to-Many → AuditLog<br>One-to-Many → Session<br>Many-to-Many → Vault (via SharedVault) |
| VaultEntry     | id (PK), user_id (FK), title, username, password (encrypted), notes, folder, created_at, updated_at | Many-to-One → User                                               |
| SharedVault    | id (PK), vault_id (FK), user_id (FK), permissions, created_at, updated_at | Many-to-One → User<br>Many-to-One → Vault                        |
| AuditLog       | id (PK), user_id (FK), action, timestamp, ip_address, details | Many-to-One → User                                               |
| Session        | id (PK), user_id (FK), token, created_at, expires_at, last_activity_at | Many-to-One → User                                               |

---

### Summary of Relationships

- **User ↔ VaultEntry**: A one-to-many relationship where a user can have many vault entries.
- **User ↔ Vault (via SharedVault)**: A many-to-many relationship where a vault can be shared with many users, and a user can have access to many vaults.
- **User ↔ AuditLog**: A one-to-many relationship where a user can generate multiple audit logs for various actions.
- **User ↔ Session**: A one-to-many relationship where a user can have multiple active sessions.

These relationships allow us to structure the data in a way that supports the application’s core functionalities such as vault management, auditing, and session handling while maintaining integrity and security across the system.



## 7. API Specification
### 7.1. Endpoint Catalog
- Table: Method, Path, Auth, Request schema, Response schema, Errors.
### 7.2. Rate Limiting & Throttling
- Rules per endpoint.
### 7.3. Versioning Strategy
- “v1” prefix, deprecation policy.

## 8. User Interface Specification
### 8.1. Page Wireframes
- Login, Dashboard, VaultDetail, Settings.
### 8.2. Component Catalogue
- Reusable UI elements: Input, Modal, DataTable.
### 8.3. Accessibility Requirements
- WCAG AA compliance checklist.

## 9. Security Model
### 9.1. Threat Model
- STRIDE categories, attacker capabilities.
### 9.2. Key Management
- Master key handling, HSM integration, rotation policy.
### 9.3. MFA & Recovery
- TOTP enrollment, backup codes, recovery flow.

## 10. Infrastructure & Deployment
### 10.1. Environments
- Dev, staging, production – differences.
### 10.2. IaC & Configuration
- Terraform modules, parameter store.
### 10.3. CI/CD Pipelines
- Build → test → deploy steps, approval gates.

## 11. Testing Strategy
### 11.1. Unit Tests
- Coverage targets, key modules.
### 11.2. Integration Tests
- End-to-end flows, encryption sanity.
### 11.3. Security Tests
- Static analysis, penetration tests, dependency scans.

## 12. Glossary
- Define acronyms and domain terms (AES-GCM, RLS, HSM).

## 13. References
- Links to standards, RFCs, crypto libraries, internal policies.

---

**Instructions to Build This File:**
1. Create a Markdown file `abstract.md`.
2. Copy the outline above into it.
3. Under each heading, draft detailed prose and bullet points covering the specified content.
4. Cross-reference sections where needed (e.g., link Functional to Security Model).
5. Review for completeness before development.
6. Freeze version 1.0; update as changes occur.```
