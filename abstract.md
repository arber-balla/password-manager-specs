
## Table of Contents

- [Abstract](#abstract)
- [Abstract Document Outline](#abstract-document-outline)
- [1. Stakeholders & Responsibilities](#1-stakeholders-responsibilities)
  - [1.1. Student Developer (Project Owner)](#11-student-developer-project-owner)
  - [1.2. Frontend Engineer (Role Simulated)](#12-frontend-engineer-role-simulated)
  - [1.3. Backend Engineer (Role Simulated)](#13-backend-engineer-role-simulated)
  - [1.4. DevOps Engineer (Role Simulated)](#14-devops-engineer-role-simulated)
  - [1.5. Security Reviewer (Role Simulated)](#15-security-reviewer-role-simulated)
  - [1.6. UI/UX Designer (Role Simulated)](#16-uiux-designer-role-simulated)
  - [1.7. Stakeholder Proxy (e.g., Peer Reviewers, Mentors)](#17-stakeholder-proxy-eg-peer-reviewers-mentors)
- [2. Document Purpose](#2-document-purpose)
  - [2.1 Role in development](#21-role-in-development)
- [3. Application Overview](#3-application-overview)
  - [3.1. Vision and Scope](#31-vision-and-scope)
  - [3.2. High-Level Features](#32-highlevel-features)
- [4. Project Plan](#4-project-plan)
  - [4.1. Milestones & Timeline](#41-milestones-timeline)
  - [4.2. Resources & Budget](#42-resources-budget)
  - [4.3. Assumptions](#43-assumptions)
  - [4.4. Constraints](#44-constraints)
- [5 Functional Requirements](#5-functional-requirements)
- [5.1 User Management](#51-user-management)
  - [5.1.1 Register](#511-register)
  - [5.1.2 Login](#512-login)
  - [5.1.3 Password Reset Flow](#513-password-reset-flow)
  - [5.1.4 Roles and Permissions](#514-roles-and-permissions)
  - [5.1.5 General Security Measures Across User Management](#515-general-security-measures-across-user-management)
- [5.2 Vault Operations](#52-vault-operations)
  - [5.2.1 Create Vault Entry](#521-create-vault-entry)
  - [5.2.2 Read Vault Entries](#522-read-vault-entries)
  - [5.2.3 Update Vault Entry](#523-update-vault-entry)
  - [5.2.4 Delete Vault Entry](#524-delete-vault-entry)
  - [5.2.5 Folder Organization](#525-folder-organization)
  - [5.2.6 Tag Organization](#526-tag-organization)
  - [5.2.7 General Security Measures Across Vault Operations](#527-general-security-measures-across-vault-operations)
- [5.3 Encryption/Decryption](#53-encryptiondecryption)
  - [5.3.1 Client-Side AES-256-GCM Usage](#531-clientside-aes256gcm-usage)
  - [5.3.2 Key Derivation via Argon2](#532-key-derivation-via-argon2)
  - [5.3.3 Zero-Knowledge Guarantee](#533-zeroknowledge-guarantee)
- [5.5 Audit & Logging](#55-audit-logging)
  - [5.5.1 Purpose](#551-purpose)
  - [5.5.2 Scope of Logged Events](#552-scope-of-logged-events)
  - [5.5.3 Logged Metadata for Each Event](#553-logged-metadata-for-each-event)
  - [5.5.4 Storage and Retention](#554-storage-and-retention)
  - [5.5.5 Access Control and Privacy](#555-access-control-and-privacy)
  - [5.5.6 Compliance and Best Practices](#556-compliance-and-best-practices)
- [6. Non-Functional Requirements (In the future!)](#6-nonfunctional-requirements-in-the-future)
- [6.1 Security](#61-security)
  - [6.1.1 OWASP Top 10 Mitigations](#611-owasp-top-10-mitigations)
  - [6.1.2 Data-at-Rest Encryption](#612-dataatrest-encryption)
  - [6.1.3 Data-in-Transit Encryption](#613-dataintransit-encryption)
  - [6.1.4 Additional Security Layers](#614-additional-security-layers)
- [6.2 Performance](#62-performance)
  - [6.2.1 Target Latency for Vault Read/Write](#621-target-latency-for-vault-readwrite)
  - [6.2.2 Concurrency Requirements](#622-concurrency-requirements)
  - [6.2.3 Performance Monitoring](#623-performance-monitoring)
- [6.3 Scalability](#63-scalability)
  - [6.3.1 Horizontal Scaling Strategy](#631-horizontal-scaling-strategy)
- [6.4 Availability & Reliability](#64-availability-reliability)
  - [6.4.1 SLA Targets](#641-sla-targets)
  - [6.4.2 Backup and Disaster Recovery](#642-backup-and-disaster-recovery)
- [6.5 Maintainability](#65-maintainability)
  - [6.5.1 Code Standards](#651-code-standards)
  - [6.5.2 Documentation](#652-documentation)
  - [6.5.3 Automated Checks](#653-automated-checks)
  - [6.5.4 Version Control & Branching Strategy](#654-version-control-branching-strategy)
- [7. Risk Assessment](#7-risk-assessment)
- [8. System Architecture](#8-system-architecture)
  - [8.1. Technology Stack & Rationale](#81-technology-stack-rationale)
  - [8.1.1 Front-End](#811-frontend)
  - [8.1.2 Back-End](#812-backend)
  - [8.1.3 Database & ORM](#813-database-orm)
  - [8.1.4 Cryptography](#814-cryptography)
  - [8.1.5 Infrastructure & DevOps](#815-infrastructure-devops)
  - [8.1.6 CI/CD & Testing](#816-cicd-testing)
  - [8.1.7 Monitoring & Logging](#817-monitoring-logging)
- [8.2 Component Diagram](#82-component-diagram)
  - [1. **Front-End (Client-Side Application)**](#1-frontend-clientside-application)
  - [2. **API Layer (Back-End)**](#2-api-layer-backend)
  - [3. **Database**](#3-database)
  - [4. **Key-Management System (KMS)**](#4-keymanagement-system-kms)
  - [5. **Hardware Security Module (HSM) / Vault**](#5-hardware-security-module-hsm-vault)
  - [Component Interaction:](#component-interaction)
- [8.3 Data Flow](#83-data-flow)
  - [1. **Login**](#1-login)
  - [2. **Key Derivation**](#2-key-derivation)
  - [3. **Vault Fetch**](#3-vault-fetch)
  - [4. **Decryption**](#4-decryption)
  - [Summary of the Data Flow:](#summary-of-the-data-flow)
- [8.4 Deployment Topology](#84-deployment-topology)
  - [1. **Docker**](#1-docker)
  - [2. **Amazon ECS (Elastic Container Service)**](#2-amazon-ecs-elastic-container-service)
  - [3. **Kubernetes**](#3-kubernetes)
  - [4. **Environments**](#4-environments)
  - [5. **CI/CD Pipeline**](#5-cicd-pipeline)
  - [Summary of Deployment Topology:](#summary-of-deployment-topology)
- [9. Data Model](#9-data-model)
  - [9.1 Entities](#91-entities)
    - [**User**](#user)
    - [**VaultEntry**](#vaultentry)
    - [**SharedVault**](#sharedvault)
    - [**AuditLog**](#auditlog)
    - [**Session**](#session)
  - [Summary](#summary)
  - [9.2 Attributes & Constraints](#92-attributes-constraints)
    - [**User Entity**](#user-entity)
    - [**VaultEntry Entity**](#vaultentry-entity)
    - [**SharedVault Entity**](#sharedvault-entity)
    - [**AuditLog Entity**](#auditlog-entity)
    - [**Session Entity**](#session-entity)
  - [2. **Encryption Columns**](#2-encryption-columns)
  - [3. **Row-Level Security (RLS) Policies**](#3-rowlevel-security-rls-policies)
  - [Summary](#summary)
  - [9.3 Relationships](#93-relationships)
    - [**1. One-to-Many Relationship: User → VaultEntry**](#1-onetomany-relationship-user-vaultentry)
    - [**2. Many-to-Many Relationship: Vault → User (SharedVault)**](#2-manytomany-relationship-vault-user-sharedvault)
    - [**3. One-to-Many Relationship: User → AuditLog**](#3-onetomany-relationship-user-auditlog)
    - [**4. One-to-Many Relationship: User → Session**](#4-onetomany-relationship-user-session)
    - [**Entity-Relationship (ER) Diagram Overview**](#entityrelationship-er-diagram-overview)
  - [Summary of Relationships](#summary-of-relationships)
- [10. API Specification](#10-api-specification)
  - [10.1. Endpoint Catalog](#101-endpoint-catalog)
  - [10.2. Rate Limiting & Throttling](#102-rate-limiting-throttling)
  - [10.3. Versioning Strategy](#103-versioning-strategy)
- [11. User Interface Specification](#11-user-interface-specification)
  - [11.1. Design Philosophy](#111-design-philosophy)
  - [11.2. Core Screens](#112-core-screens)
  - [11.3. Page Wireframes](#113-page-wireframes)
    - [Login Page](#login-page)
    - [Dashboard Page](#dashboard-page)
    - [Vault Detail Page](#vault-detail-page)
    - [Settings Page](#settings-page)
  - [11.4. Component Catalogue](#114-component-catalogue)
    - [Input Components](#input-components)
    - [Modal Components](#modal-components)
    - [Data Display Components](#data-display-components)
    - [Feedback Components](#feedback-components)
    - [Layout Components](#layout-components)
  - [11.5. Accessibility Requirements](#115-accessibility-requirements)
    - [Perceivable](#perceivable)
    - [Operable](#operable)
    - [Understandable](#understandable)
    - [Robust](#robust)
- [12. Security Model](#12-security-model)
  - [12.1. Threat Model](#121-threat-model)
    - [STRIDE Categories](#stride-categories)
    - [Attacker Capabilities](#attacker-capabilities)
  - [12.2. Key Management](#122-key-management)
    - [12.2.1. Master Key Handling](#1221-master-key-handling)
    - [12.2.2. Hardware Security Module (HSM) Integration](#1222-hardware-security-module-hsm-integration)
    - [12.2.3. Key Rotation Policy](#1223-key-rotation-policy)
    - [12.2.4. Backup & Disaster Recovery](#1224-backup-disaster-recovery)
  - [12.3. MFA & Recovery](#123-mfa-recovery)
    - [12.3.1. TOTP Enrollment](#1231-totp-enrollment)
    - [12.3.2. Backup Codes](#1232-backup-codes)
    - [12.3.3. Account Recovery Flow](#1233-account-recovery-flow)
- [13. Regulatory & Compliance](#13-regulatory-compliance)
  - [13.1 GDPR Compliance](#131-gdpr-compliance)
  - [13.2 Data Residency & Sovereignty](#132-data-residency-sovereignty)
  - [13.3 Legal Considerations](#133-legal-considerations)
- [14. Infrastructure & Deployment](#14-infrastructure-deployment)
  - [14.1. Environments](#141-environments)
    - [14.1.1. Development Environment](#1411-development-environment)
    - [14.1.2. Staging Environment](#1412-staging-environment)
    - [14.1.3. Production Environment](#1413-production-environment)
    - [14.1.4. Differences Between Environments](#1414-differences-between-environments)
  - [14.2. IaC & Configuration](#142-iac-configuration)
    - [14.2.1. Terraform Modules](#1421-terraform-modules)
      - [Examples of Terraform Modules:](#examples-of-terraform-modules)
    - [14.2.2. Parameter Store & Secrets Management](#1422-parameter-store-secrets-management)
      - [Examples of Parameters and Secrets Stored:](#examples-of-parameters-and-secrets-stored)
      - [Integration with Terraform:](#integration-with-terraform)
  - [14.2.3](#1423)
  - [14.3. CI/CD Pipelines](#143-cicd-pipelines)
    - [14.3.1. CI/CD Flow](#1431-cicd-flow)
    - [14.3.2. CI/CD Tools and Technologies](#1432-cicd-tools-and-technologies)
    - [14.3.3. Deployment Strategies](#1433-deployment-strategies)
    - [14.3.4. Approval & Manual Interventions](#1434-approval-manual-interventions)
    - [14.3.5. Notifications and Alerts](#1435-notifications-and-alerts)
    - [14.3.6. Pipeline Example](#1436-pipeline-example)
- [15. Testing Strategy](#15-testing-strategy)
  - [15.1. Unit Tests](#151-unit-tests)
    - [15.1.1. Coverage Targets](#1511-coverage-targets)
    - [15.1.2. Key Modules](#1512-key-modules)
  - [15.2. Integration Tests](#152-integration-tests)
    - [15.2.1. End-to-End Flows](#1521-endtoend-flows)
    - [15.2.2. Encryption Sanity](#1522-encryption-sanity)
  - [15.3. Security Tests](#153-security-tests)
    - [15.3.1. Static Analysis](#1531-static-analysis)
    - [15.3.2. Penetration Testing](#1532-penetration-testing)
    - [15.3.3. Dependency Scans](#1533-dependency-scans)
  - [15.4. Testing Tools and Frameworks](#154-testing-tools-and-frameworks)
  - [15.5. Reporting & Metrics](#155-reporting-metrics)
  - [15.6. Performance Testing (Optional but recommended)](#156-performance-testing-optional-but-recommended)
- [16. Glossary](#16-glossary)
- [17. References](#17-references)
  - [Standards & Specifications](#standards-specifications)
  - [Cryptography & Security Libraries](#cryptography-security-libraries)
  - [Backend Dependencies](#backend-dependencies)
  - [Frontend Dependencies](#frontend-dependencies)
  - [Infrastructure & DevOps Tools](#infrastructure-devops-tools)
  - [Testing Tools](#testing-tools)
  - [Internal Best Practices (to be documented)](#internal-best-practices-to-be-documented)

# Abstract

This project stems from a student’s need to demonstrate modern software engineering capabilities through a real-world application. Its objective is to design and implement a full-stack password manager with end-to-end encryption, a zero-knowledge architecture, and professional development workflows. The methodology combines a React/TypeScript front end with a NestJS/Node.js API, client-side AES-256-GCM encryption, Argon2id key derivation, PostgreSQL with RLS, Terraform-based infrastructure as code, and automated CI/CD pipelines. Emphasis is placed on modular code structure, automated testing (unit, integration, security), and DevOps best practices (containerization, orchestration, monitoring). Expected outcomes include a fully functional, secure vault for creating, reading, updating, and deleting encrypted credentials; a documented API; infrastructure configurations; and comprehensive test coverage. The significance lies in showcasing the student’s ability to apply industry-standard tools and processes, to learn advanced technologies (e.g., HSM integration, IaC, performance tuning) during development, and to deliver a portfolio-worthy artifact that meets real-world requirements for security, scalability, and maintainability.

## 1. Stakeholders & Responsibilities

This section outlines the key roles involved in the development, deployment, and maintenance of the Password Manager application, along with their associated responsibilities. While currently fulfilled by a single student-developer, these roles are defined to reflect real-world software engineering practices and may be assumed by distinct individuals or teams in a production setting.

### 1.1. Student Developer (Project Owner)
- Define project scope, requirements, and boundaries.
- Design and implement all backend and frontend components.
- Ensure adherence to coding standards, security practices, and performance goals.
- Manage Git version control, branching, and documentation.
- Configure CI/CD pipelines and deploy environments (dev/staging/prod).
- Write unit, integration, and security tests.
- Conduct research and learn missing technologies during implementation.

### 1.2. Frontend Engineer (Role Simulated)
- Build and maintain all UI components using React and TypeScript.
- Ensure accessibility compliance (WCAG AA).
- Integrate with backend APIs and handle client-side cryptographic logic.
- Perform cross-browser and mobile responsiveness testing.

### 1.3. Backend Engineer (Role Simulated)
- Implement RESTful APIs using NestJS and Express.
- Apply business logic, input validation, RBAC, and rate limiting.
- Handle key derivation, encryption, and secure session management.
- Ensure database schema integrity and enforce RLS policies.

### 1.4. DevOps Engineer (Role Simulated)
- Define Infrastructure as Code (Terraform).
- Provision and manage cloud environments.
- Set up monitoring, alerting, and logging systems.
- Automate deployments via CI/CD workflows with approval gates.

### 1.5. Security Reviewer (Role Simulated)
- Perform threat modeling (STRIDE) and code audits.
- Evaluate encryption protocols, key handling, and MFA mechanisms.
- Run static analysis and dependency scans.
- Document mitigation of OWASP Top 10 vulnerabilities.

### 1.6. UI/UX Designer (Role Simulated)
- Create wireframes and mockups for core views (login, dashboard, vault).
- Define interaction patterns, modals, and form behaviors.
- Ensure UI consistency and user-centric design.

### 1.7. Stakeholder Proxy (e.g., Peer Reviewers, Mentors)
- Provide feedback on functionality, usability, and code quality.
- Review documentation and offer suggestions for improvements.
- Validate adherence to professional standards.

> **Note:** All these roles are currently centralized under the student-developer persona for educational and demonstrative purposes.



## 2. Document Purpose

The goal of this document is to capture all the essential properties, functionalities, constraints, and architectural decisions for the Password Manager project. This abstract serves as the foundational reference for the development and maintenance of the application, ensuring that all stakeholders have a unified understanding of the system’s design, behavior, and security posture.

The document will cover:

- **Functional Requirements:** Detailed descriptions of user-facing features, interactions, and expected behavior of the application.
- **Non-Functional Requirements:** Performance, security, scalability, and reliability goals that the system must meet.
- **Architecture Decisions:** High-level design, technology stack, and key trade-offs made during the project planning phase.
- **Data Models and API Specifications:** The structure of stored data, API endpoints, and interactions.
- **Security and Privacy:** Encryption strategies, user authentication methods, and overall security model.

By clearly defining these aspects, this document serves as the backbone of the project's development lifecycle, guiding decisions and ensuring alignment between all teams involved.

### 2.1 Role in development

This document drives development by:

1. **Defining Clear Requirements:** It outlines the expected functionalities and behaviors of the application, serving as the source of truth for feature implementation.
2. **Guiding Design and Architecture:** By specifying architecture decisions and technology choices, it ensures that the development follows a unified structure, reducing ambiguity and improving collaboration.
3. **Ensuring Security Compliance:** It sets forth the security measures that must be implemented and adhered to, ensuring that all development efforts comply with best practices and regulatory standards.
4. **Maintaining Traceability:** As development progresses, this document will provide a clear reference for ensuring that the system is being built as planned. It will be updated to reflect significant changes, keeping all stakeholders aligned.
5. **Providing Testing and Validation Criteria:** The specifications described in this document will serve as a foundation for testing the system, including performance, security, and functional testing. Testers and developers can use it to verify that the implementation meets all requirements.

## 3. Application Overview

### 3.1. Vision and Scope

The vision of this project is, for me as a student, to develop a secure, scalable, and user-friendly password manager that demonstrates professional software engineering practices and showcases advanced technical skills in real-world application development.

**What I will do**:

- Implement a fully functional password manager with a front-end and back-end.
- Ensure strong security features and secure password storage.
- Follow (in my best capabilities) industry-standard practices for code quality, version control, and documentation.
- Design an intuitive user interface and a robust API for seamless interaction between front-end and back-end.
- Document all decisions, code, and architectures thoroughly to maintain clarity and traceability.

**What I will not do**:

- Implement mobile applications or multi-platform support (focus will be on web).
- Use third-party authentication providers (e.g., Google/Facebook login); the focus will be on custom authentication mechanisms.
- Add non-essential features (e.g., advanced settings, integrations with other tools) that do not align with core functionality.
- Use low-level or outdated technologies that are not in line with modern best practices (e.g., jQuery, legacy authentication mechanisms).
- Implement full-blown enterprise-grade security features (e.g., intrusion detection systems, complex cryptographic key management), though strong encryption and basic security best practices will be adhered to.

### 3.2. High-Level Features

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



## 4. Project Plan

This section outlines the structured roadmap for building the Password Manager application. It includes key milestones, a tentative timeline, resource allocations, cost estimations, critical assumptions, and known constraints. The plan is designed to simulate industry-grade project delivery within a student-driven, resource-constrained environment.

### 4.1. Milestones & Timeline

| Phase                        | Deliverables                                    | Target Duration |
|------------------------------|-------------------------------------------------|-----------------|
| Requirements Specification   | Finalized abstract, user stories, data model    | Week 1          |
| System Architecture          | Component diagrams, data flow, deployment topo  | Week 3          |
| Frontend Skeleton            | React setup, routing, page scaffolding          | Week 5          |
| Backend API Foundation       | Auth flows, RESTful API, DB schema (PostgreSQL) | Week 7          |
| Core Vault Functionality     | Vault CRUD, encryption, Argon2 key derivation   | Week 9          |
| Sharing & Permissions        | RBAC, shared vault logic                        | Week 11         |
| Testing Suite Implementation | Unit, integration, security tests               | Week 13         |
| CI/CD & Deployment           | Docker, GitHub Actions, test deployment         | Week 15         |
| UI Finalization & Styling    | Responsive components, accessibility adherence  | Week 17         |
| Security Hardening           | STRIDE, MFA, rate limiting, audit logs          | Week 19         |
| Documentation Finalization   | README, specs, glossaries, diagrams             | Week 21         |
| Final Review & Polishing     | Bug fixes, test coverage review                 | Week 23         |

> Total Estimated Time: ~23 weeks (assuming part-time commitment)

### 4.2. Resources & Budget

| Resource            | Description                                 | Estimated Cost         |
|---------------------|---------------------------------------------|------------------------|
| Development Machine | Personal laptop, no extra cost              | €0                     |
| IDE/Tools           | WebStorm (student license), Postman, Docker | €0 (student licenses)  |
| Hosting/Deployment  | GitHub (free tier), optional Vercel/Render  | €0–€10/month if scaled |
| Domain (Optional)   | Project-specific domain for demo            | €10–€20/year           |
| Time Commitment     | ~10–12 hrs/week for 12 weeks                | ~120–140 total hrs     |

> Budget total: ~€0–€30 (if hosting externally). Core assumption: infrastructure is optional for MVP demonstration.

### 4.3. Assumptions

- The student (developer) can allocate consistent weekly time.
- No team collaboration is required—solo project.
- PostgreSQL, Node.js, and React are already installed or installable.
- Open-source libraries are available and permissible for non-commercial use.
- Dev and staging environments are simulated locally using Docker.

### 4.4. Constraints

- Limited real-user testing; simulated users and test scripts used instead.
- No production-grade HSM or cloud security modules—simulated via secure storage logic.
- Project scope may be adjusted mid-course if new requirements arise or time constraints demand it.
- Full accessibility, performance, and scalability objectives will be prioritized only after MVP.

---

## 5 Functional Requirements

## 5.1 User Management

### 5.1.1 Register

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

### 5.1.2 Login

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

### 5.1.3 Password Reset Flow

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

### 5.1.4 Roles and Permissions

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

### 5.1.5 General Security Measures Across User Management

- All personal information is encrypted in-transit (HTTPS) and sensitive identifiers are tokenized or anonymized where possible.
- Server logs redact sensitive fields to prevent leakage of credentials or personal data.
- Input validation and sanitization on all forms and endpoints.
- Detailed audit logging for registration, login, and password reset events.

## 5.2 Vault Operations

### 5.2.1 Create Vault Entry

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

### 5.2.2 Read Vault Entries

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

### 5.2.3 Update Vault Entry

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

### 5.2.4 Delete Vault Entry

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

### 5.2.5 Folder Organization

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

### 5.2.6 Tag Organization

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

### 5.2.7 General Security Measures Across Vault Operations

- Ownership verification enforced server-side before any read/update/delete operations.
- Minimal metadata exposure in API responses (e.g., timestamps, encrypted titles).
- No plaintext vault data handled server-side at any point.
- Consistent logging of vault operations without recording sensitive field contents.

## 5.3 Encryption/Decryption

### 5.3.1 Client-Side AES-256-GCM Usage

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

### 5.3.2 Key Derivation via Argon2

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

### 5.3.3 Zero-Knowledge Guarantee

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

## 5.5 Audit & Logging

### 5.5.1 Purpose

Establish a verifiable and tamper-resistant trail of critical user and system actions for security audits, intrusion detection, incident response, and user accountability without violating the application's zero-knowledge guarantees.

---

### 5.5.2 Scope of Logged Events

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

### 5.5.3 Logged Metadata for Each Event

- **Event Type:** Identifier (e.g., LOGIN_SUCCESS, ENTRY_CREATE, ENTRY_UPDATE).
- **Timestamp:** UTC timestamp with milliseconds precision (ISO 8601 format).
- **User ID:** Internal user identifier (never username or email directly in the log).
- **IP Address:** Source IP of the request.
- **User Agent:** Device/browser information (optional for further forensic value).
- **Resource ID:** (only if applicable) Encrypted entry or folder ID involved.
- **Status Code:** Success or failure indicator (plus error reason if applicable).

_Note:_ Never log any sensitive plaintext vault data, user passwords, or encryption keys.

---

### 5.5.4 Storage and Retention

- Logs stored in append-only systems where deletion or alteration requires explicit privileged actions.
- Secure separation of logs from operational databases (e.g., separate write-only logging service).
- Encrypt logs at rest if they contain user-identifiable metadata (e.g., IPs).
- Minimum retention: 90 days. Extendable up to 1–2 years depending on regulatory requirements or organizational policies.

---

### 5.5.5 Access Control and Privacy

- Only designated system administrators have access to view or export logs.
- Audit access to logs themselves must also be logged.
- Regular review of logs to detect anomalous behaviors (e.g., brute-force login attempts, mass vault deletion).

---

### 5.5.6 Compliance and Best Practices

- Follow security and privacy frameworks (e.g., OWASP ASVS Audit Logging controls).
- If exporting logs externally (e.g., for SIEM analysis), maintain encryption and access control.
- Redact sensitive fields even within internal analytic environments if necessary.
- Implement log integrity protections (e.g., digital signatures or hash chaining) to detect tampering.

## 6. Non-Functional Requirements (In the future!)

Some of the more advanced features outlined in this document, such as horizontal scaling, advanced disaster recovery mechanisms, and enhanced auditing/logging capabilities, will be integrated into the application once the foundational aspects of the system are fully developed and stable. These improvements will be implemented in future phases as the application evolves, ensuring a scalable, secure, and high-performance system. The initial focus will be on building a robust core, with advanced optimizations and features added progressively as the user base and system complexity grow.

## 6.1 Security

### 6.1.1 OWASP Top 10 Mitigations

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

### 6.1.2 Data-at-Rest Encryption

**Server-Side:**

- Even though vault contents are encrypted client-side, server will encrypt stored blobs again using volume/database encryption (e.g., AES-256 at database layer).
- Database credentials stored securely, outside codebase (environment variables, vault services).
- Backup storage encrypted to the same standards as primary data.

**Client-Side:**

- All vault data encrypted on the device before transmission.
- Persistent storage (localStorage, IndexedDB) uses encrypted forms only if offline access is implemented.

---

### 6.1.3 Data-in-Transit Encryption

- Enforce HTTPS with TLS 1.3 only.
- HSTS (HTTP Strict Transport Security) enabled with a long max-age and preload.
- TLS certificates from trusted Certificate Authorities (CA).
- Redirect all HTTP traffic to HTTPS automatically.
- WebSocket connections (if used) secured via WSS.

---

### 6.1.4 Additional Security Layers

- Content Security Policy (CSP) to prevent XSS attacks.
- X-Frame-Options set to DENY to prevent clickjacking.
- Rate-limiting on authentication endpoints to deter brute-force attacks.
- CAPTCHA integration after multiple failed login attempts (optional for higher security).

## 6.2 Performance

### 6.2.1 Target Latency for Vault Read/Write

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

### 6.2.2 Concurrency Requirements

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

### 6.2.3 Performance Monitoring

- Implement real-time application performance monitoring (APM) tools (e.g., New Relic, Datadog) during staging and production.
- Collect telemetry on:
  - API endpoint response times.
  - Vault synchronization durations.
  - Encryption/decryption processing times.
- Use this data to continuously optimize system bottlenecks before major releases.

## 6.3 Scalability

### 6.3.1 Horizontal Scaling Strategy

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

## 6.4 Availability & Reliability

### 6.4.1 SLA Targets

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

### 6.4.2 Backup and Disaster Recovery

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

## 6.5 Maintainability

### 6.5.1 Code Standards

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

### 6.5.2 Documentation

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

### 6.5.3 Automated Checks

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

### 6.5.4 Version Control & Branching Strategy

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

## 7. Risk Assessment

This section outlines potential risks that may affect the successful completion of the Password Manager project. Each risk is evaluated based on its likelihood of occurrence, potential impact, and associated mitigation strategy. This exercise is critical to planning for contingencies and ensuring delivery under constraints.

| Risk ID | Risk Description                                 | Likelihood | Impact | Mitigation Strategy                                                               |
|---------|--------------------------------------------------|------------|--------|-----------------------------------------------------------------------------------|
| R1      | Underestimating technical complexity             | High       | High   | Limit MVP scope initially, research before implementation, iterate in small steps |
| R2      | Incomplete knowledge of cryptographic primitives | Medium     | High   | Study standards (e.g., AES-GCM, Argon2), verify with community-accepted libraries |
| R3      | Time constraints due to academic workload        | High       | Medium | Plan weekly time blocks, keep progress modular, avoid scope creep                 |
| R4      | Toolchain misconfiguration (Docker, CI/CD)       | Medium     | Medium | Follow official documentation, isolate environments, seek mentor/help if blocked  |
| R5      | Data loss due to lack of backups                 | Low        | High   | Implement backup scripts locally, use GitHub versioning for source code           |
| R6      | Insecure implementation of authentication        | Medium     | High   | Follow OWASP guidelines, avoid writing crypto manually, rely on proven libraries  |
| R7      | Performance degradation under simulated load     | Low        | Medium | Use indexes, optimize queries, test with dummy data                               |
| R8      | Dependency vulnerabilities                       | Medium     | High   | Use `npm audit`, `dependabot`, limit dependency count                             |
| R9      | Lack of accessibility compliance                 | Medium     | Low    | Use WCAG checklists, integrate contrast/language tools during UI testing          |
| R10     | Inability to demonstrate scalability features    | Low        | Medium | Document design choices, simulate horizontal scaling scenarios with diagrams      |

---

## 8. System Architecture

In the System Architecture section, we will outline the high-level structure of the application, describing how different components interact to deliver the functionality of the password manager. This will include the organization of the front-end and back-end layers, database design, and the communication between services. We will cover the choice of technologies, the role of each component, and how they work together to ensure performance, security, and scalability. Key architectural patterns such as client-server model, microservices (if applicable), and security considerations (e.g., encryption, authentication) will also be addressed. This section will provide a clear, modular view of the application’s design and how it supports both the current requirements and future growth.

### 8.1. Technology Stack & Rationale

### 8.1.1 Front-End

- **React + TypeScript**
  - **Justification:** Component-based architecture, strong ecosystem, type safety for maintainability.
  - **Trade-Off:** Initial setup complexity, larger bundle sizes; offset by code reuse and predictability.

- **Next.js**
  - **Justification:** Built-in routing, SSR/SSG for performance and SEO, API routes for simple back-end stubs.
  - **Trade-Off:** Steeper learning curve and framework constraints; chosen over Vite for production-ready features.

- **Tailwind CSS**
  - **Justification:** Utility-first CSS enables rapid styling, consistent design tokens, minimal custom CSS.
  - **Trade-Off:** Verbose class names in markup; reduced by component abstraction.

### 8.1.2 Back-End

- **NestJS + Node.js + TypeScript**
  - **Justification:** Modular, opinionated framework with dependency injection, decorators, built-in testing support.
  - **Trade-Off:** Boilerplate overhead versus raw Express simplicity; preferred for maintainable large codebases.

- **Express.js Middleware (helmet, cors, rate-limiter-flexible)**
  - **Justification:** Essential security headers, CORS policy enforcement, request throttling.
  - **Trade-Off:** Adds layers of abstraction; required for OWASP compliance.

### 8.1.3 Database & ORM

- **PostgreSQL**
  - **Justification:** ACID compliance, advanced features (RLS, JSONB), strong community support.
  - **Trade-Off:** Operational complexity compared to NoSQL; chosen for transactional integrity.

- **Prisma ORM**
  - **Justification:** Type-safe database client, auto-generated migrations, developer productivity.
  - **Trade-Off:** Runtime overhead, abstraction layer; offset by fewer runtime errors and faster schema evolution.

### 8.1.4 Cryptography

- **AES-256-GCM (WebCrypto API / libsodium.js)**
  - **Justification:** Authenticated encryption, high performance in browsers and Node.
  - **Trade-Off:** Requires careful nonce management; standardized implementation reduces risk.

- **Argon2id**
  - **Justification:** Best resistance to GPU attacks and side-channel leaks for key derivation.
  - **Trade-Off:** Slower derivation time; acceptable on login with configurable parameters.

### 8.1.5 Infrastructure & DevOps

- **Docker**
  - **Justification:** Environment consistency, simplified local development, container portability.
  - **Trade-Off:** Resource overhead on developer machines; mitigated with slim base images.

- **Terraform**
  - **Justification:** Declarative IaC, version control of infrastructure, multi-cloud support.
  - **Trade-Off:** Steep learning curve; chosen for reproducibility and auditability.

- **AWS ECS / Kubernetes**
  - **Justification:** Managed container orchestration with auto-scaling and high availability.
  - **Trade-Off:** ECS reduces complexity but is AWS-specific; Kubernetes is flexible but more operational overhead.

### 8.1.6 CI/CD & Testing

- **GitHub Actions**
  - **Justification:** Integrated with repository, simple to configure for build/test/deploy workflows.
  - **Trade-Off:** Limited concurrency on free tier; acceptable for student project scope.

- **Jest + Supertest**
  - **Justification:** Comprehensive unit and API integration testing, snapshot capabilities.
  - **Trade-Off:** Test execution time overhead; managed with parallelization.

- **OWASP ZAP / Snyk**
  - **Justification:** Automated security scanning for dynamic and dependency vulnerabilities.
  - **Trade-Off:** Occasional false positives; integrated into CI for ongoing risk detection.

### 8.1.7 Monitoring & Logging

- **Prometheus + Grafana**
  - **Justification:** Open-source metrics collection and visualization for performance monitoring.
  - **Trade-Off:** Requires additional services; critical for SLA adherence.

- **ELK Stack (Elasticsearch, Logstash, Kibana)**
  - **Justification:** Centralized log aggregation and analysis for audit and incident response.
  - **Trade-Off:** Infrastructure overhead; used in staging/production only.


## 8.2 Component Diagram

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

## 8.3 Data Flow

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

## 8.4 Deployment Topology

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

## 9. Data Model

The **Data Model** defines the structure and relationships between the various entities within the password manager application. The data model will ensure the secure and efficient storage and retrieval of sensitive information, including user accounts, vault entries, encryption keys, and audit logs. This section details the database schema, entity relationships, and key design decisions.

### 9.1 Entities

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

### 9.2 Attributes & Constraints

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

### 9.3 Relationships

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

| Entity      | Attributes                                                                                          | Relationships                                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| User        | id (PK), email, hashed_password, salt, created_at, updated_at                                       | One-to-Many → VaultEntry<br>One-to-Many → AuditLog<br>One-to-Many → Session<br>Many-to-Many → Vault (via SharedVault) |
| VaultEntry  | id (PK), user_id (FK), title, username, password (encrypted), notes, folder, created_at, updated_at | Many-to-One → User                                                                                                    |
| SharedVault | id (PK), vault_id (FK), user_id (FK), permissions, created_at, updated_at                           | Many-to-One → User<br>Many-to-One → Vault                                                                             |
| AuditLog    | id (PK), user_id (FK), action, timestamp, ip_address, details                                       | Many-to-One → User                                                                                                    |
| Session     | id (PK), user_id (FK), token, created_at, expires_at, last_activity_at                              | Many-to-One → User                                                                                                    |

---

### Summary of Relationships

- **User ↔ VaultEntry**: A one-to-many relationship where a user can have many vault entries.
- **User ↔ Vault (via SharedVault)**: A many-to-many relationship where a vault can be shared with many users, and a user can have access to many vaults.
- **User ↔ AuditLog**: A one-to-many relationship where a user can generate multiple audit logs for various actions.
- **User ↔ Session**: A one-to-many relationship where a user can have multiple active sessions.

These relationships allow us to structure the data in a way that supports the application’s core functionalities such as vault management, auditing, and session handling while maintaining integrity and security across the system.

## 10. API Specification

Defines a versioned, RESTful JSON API secured by Bearer tokens and scoped by RBAC. All endpoints reside under `/api/v1`.
**Conventions:**

- All requests and responses use `application/json`.
- Standard HTTP status codes: `2xx` success, `4xx` client error, `5xx` server error.
- Errors return `{ code: string, message: string, details?: any }`.
- Rate limiting applied to authentication and write endpoints.
- CORS configured to allow only trusted origins.
- Endpoints enforce RLS and RBAC guards.

### 10.1. Endpoint Catalog

| Method | Path                      | Auth Required | Request Schema                              | Response Schema             | Common Errors                           |
|--------|---------------------------|---------------|---------------------------------------------|-----------------------------|-----------------------------------------|
| POST   | /auth/register            | No            | email, password                             | success message             | 400 (validation), 409 (conflict)        |
| POST   | /auth/login               | No            | email, password                             | access_token, refresh_token | 400 (invalid), 401 (unauthorized)       |
| POST   | /auth/forgot-password     | No            | email                                       | success message             | 400 (validation), 404 (not found)       |
| POST   | /auth/reset-password      | No            | token, new_password                         | success message             | 400 (validation), 401 (invalid token)   |
| GET    | /vault/entries            | Yes           | none                                        | list of VaultEntries        | 401 (unauthenticated)                   |
| POST   | /vault/entries            | Yes           | title, username, password, notes, folder_id | created VaultEntry          | 400 (validation), 401 (unauthenticated) |
| PATCH  | /vault/entries/{entryId}  | Yes           | partial VaultEntry fields                   | updated VaultEntry          | 400 (validation), 404 (not found)       |
| DELETE | /vault/entries/{entryId}  | Yes           | none                                        | success message             | 404 (not found), 401 (unauthorized)     |
| GET    | /vault/folders            | Yes           | none                                        | list of Folders             | 401 (unauthenticated)                   |
| POST   | /vault/folders            | Yes           | name                                        | created Folder              | 400 (validation)                        |
| PATCH  | /vault/folders/{folderId} | Yes           | name                                        | updated Folder              | 404 (not found)                         |
| DELETE | /vault/folders/{folderId} | Yes           | none                                        | success message             | 404 (not found)                         |
| GET    | /vault/tags               | Yes           | none                                        | list of Tags                | 401 (unauthenticated)                   |
| POST   | /vault/tags               | Yes           | name                                        | created Tag                 | 400 (validation)                        |
| PATCH  | /vault/tags/{tagId}       | Yes           | name                                        | updated Tag                 | 404 (not found)                         |
| DELETE | /vault/tags/{tagId}       | Yes           | none                                        | success message             | 404 (not found)                         |
| POST   | /vault/share              | Yes           | vault_entry_id, recipient_email             | share record                | 400 (validation), 404 (not found)       |
| GET    | /vault/shared             | Yes           | none                                        | list of shared entries      | 401 (unauthenticated)                   |
| PATCH  | /vault/share/{shareId}    | Yes           | updated permissions                         | updated share               | 404 (not found)                         |
| DELETE | /vault/share/{shareId}    | Yes           | none                                        | success message             | 404 (not found)                         |
| GET    | /audit/logs               | Admin only    | filters (optional)                          | list of AuditLogs           | 403 (forbidden)                         |
| GET    | /admin/users              | Admin only    | filters (optional)                          | list of Users               | 403 (forbidden)                         |
| PATCH  | /admin/users/{userId}     | Admin only    | partial user updates                        | updated User                | 404 (not found)                         |
| DELETE | /admin/users/{userId}     | Admin only    | none                                        | success message             | 404 (not found)                         |

### 10.2. Rate Limiting & Throttling

Rate limiting ensures fair use, prevents abuse, and mitigates brute-force attacks. Rules are applied per authenticated user or per IP address for unauthenticated requests.

| Endpoint Group                                | Limit Rule                       | Notes                                             |
|-----------------------------------------------|----------------------------------|---------------------------------------------------|
| POST /auth/register                           | 5 requests per hour per IP       | Prevent mass account creation                     |
| POST /auth/login                              | 10 requests per minute per IP    | Mitigate brute-force login attempts               |
| POST /auth/forgot-password                    | 3 requests per hour per IP       | Control password reset abuse                      |
| POST /auth/reset-password                     | 5 requests per hour per IP       | Control reset abuse after token issuance          |
| Vault Operations (GET/POST/PATCH/DELETE)      | 60 requests per minute per user  | Allow fluid vault management while limiting abuse |
| Folder/Tag Management (GET/POST/PATCH/DELETE) | 30 requests per minute per user  | Lightweight control over metadata ops             |
| Sharing Endpoints (POST/PATCH/DELETE)         | 20 requests per minute per user  | Prevent spam-sharing attacks                      |
| GET /vault/shared                             | 60 requests per minute per user  | Standard read operation allowance                 |
| Audit/Admin Endpoints (GET/PATCH/DELETE)      | 15 requests per minute per admin | Admin operations are heavy and sensitive          |

**Enforcement Details:**

- Exceeding limits returns HTTP `429 Too Many Requests`.
- Rate limits reset using rolling windows.
- Critical endpoints (login, register, reset) are more restrictive.

### 10.3. Versioning Strategy

All API endpoints are namespaced under `/api/v1` to ensure stability and controlled evolution over time.

| Aspect               | Policy                                                                           |
|----------------------|----------------------------------------------------------------------------------|
| Namespace            | `/api/v1/...` for all current endpoints                                          |
| Breaking Changes     | Introduced only in a new major version (`v2`, `v3`, etc.)                        |
| Minor Enhancements   | Non-breaking changes (e.g., new optional fields) allowed in `v1`                 |
| Deprecation Notice   | Deprecated fields/endpoints marked clearly in response metadata                  |
| Deprecation Timeline | Minimum 6 months notice before removing deprecated functionality                 |
| Client Compatibility | Old clients remain functional during deprecation window                          |
| Communication        | Major changes and deprecations announced via changelog and documentation updates |

**Guiding Principle:**
Maintain backward compatibility within a major version. Only additive, non-breaking changes allowed until a full new version is warranted.

## 11. User Interface Specification

This section defines the expected structure, behavior, and constraints of the user interface (UI) for the Password Manager web application.

### 11.1. Design Philosophy

- Clean, minimalistic, professional design focused on usability.
- Responsive across desktop, tablet, and mobile devices.
- Accessibility compliant (WCAG 2.1 AA standards).
- Emphasize security through UI (clear session/logout indicators, sensitive operation confirmations).

### 11.2. Core Screens

| Screen                  | Description                                                            | Key Actions                             |
|-------------------------|------------------------------------------------------------------------|-----------------------------------------|
| Landing Page            | Public homepage with app overview and login/register options           | Login, Register navigation              |
| Registration            | Form to create an account, validate input, strong password suggestions | Submit registration form                |
| Login                   | Authentication page with "Remember Me" and "Forgot Password" options   | Submit credentials, redirect on success |
| Dashboard               | Main landing after login; overview of vault entries, folders, tags     | Navigate to entries, create new, search |
| Vault Entry View/Edit   | Detailed view to read, edit, or delete a vault entry                   | Update fields, save, delete             |
| Folder/Tag Management   | Manage organization structures for entries                             | Add, edit, delete folders and tags      |
| Sharing Management      | View/manage shared entries and access controls                         | Invite users, revoke access             |
| Settings/Profile        | Update personal info, change master password, manage session tokens    | Save changes, logout from all devices   |
| Audit Log (Admin)       | View system activity (login, CRUD, sharing events) with filters        | Search logs, filter by user or action   |
| User Management (Admin) | Manage user accounts, reset credentials, assign roles                  |

### 11.3. Page Wireframes

Wireframes define the skeletal layout of core pages. These act as blueprints for implementation, focusing on structure, placement, and function over visual styling.

---

#### Login Page

- **Header**: App logo centered at the top.
- **Form**:
  - Email input
  - Password input (masked, toggle visibility)
  - "Remember Me" checkbox
  - "Forgot Password?" link
- **Actions**:
  - Primary button: "Log In"
  - Secondary text link: "Don't have an account? Register"

_Notes_: Minimal distractions, focus solely on authentication. Submit triggers client-side validation before API request.

---

#### Dashboard Page

- **Top Navigation Bar**:

  - App logo (left)
  - Search bar (center)
  - Profile menu with avatar (right)

- **Side Navigation Menu**:

  - Home
  - Vault Entries
  - Folders
  - Tags
  - Shared Vaults
  - Audit Logs (admin only)
  - Settings

- **Main Content Area**:
  - Quick stats (number of entries, folders, tags)
  - Recent activity (logins, recent edits)
  - Button: "Add New Vault Entry"

_Notes_: Dashboard acts as control center. Information density balanced to avoid overwhelming the user.

---

#### Vault Detail Page

- **Breadcrumb Navigation**: Home > Vault > Entry Name
- **Entry Metadata Display**:

  - Title
  - Username
  - URL (clickable)
  - Notes
  - Creation/Last modified timestamps
  - Folder/Tags assignment

- **Actions**:

  - Edit Entry (opens form view)
  - Delete Entry (confirmation modal)
  - Share Entry (opens share modal)

- **Security Features**:
  - Toggle to reveal/hide passwords securely
  - Copy-to-clipboard button for fields

_Notes_: Entry data must be presented clearly, minimizing clicks for essential actions while safeguarding sensitive content.

---

#### Settings Page

- **Sections**:

  - **Profile Info**:
    - View and update name, email.
    - Change master password (mandatory re-authentication).
  - **Security Settings**:
    - Enable/disable 2FA (future enhancement).
    - View active sessions and log out individually or all at once.
  - **Application Preferences**:
    - Toggle light/dark theme.
    - Set auto-logout timeout duration.

- **Actions**:
  - Save Changes (primary button)
  - Cancel Changes (secondary button)

_Notes_: Settings structured into collapsible panels for a clean experience. Sensitive changes require password confirmation.

---

**General Wireframe Principles**:

- All pages responsive and mobile-friendly.
- Primary actions emphasized using distinctive button styling.
- Error states, empty states, and loading skeletons included from the beginning.

---

### 11.4. Component Catalogue

Defines all atomic and composite components to ensure UI consistency, reusability, and maintainability.

---

#### Input Components

- **TextInput**

  - Props: `label`, `placeholder`, `type`, `value`, `onChange`, `error`
  - Supports types: text, email, password
  - Integrated validation feedback (e.g., red border on error)

- **Checkbox**

  - Props: `label`, `checked`, `onChange`
  - Used for options like "Remember Me" and setting toggles

- **DropdownSelect**

  - Props: `label`, `options`, `selected`, `onChange`
  - Used for folder selection, tagging entries, settings choices

- **TextArea**
  - Props: `label`, `placeholder`, `value`, `onChange`, `rows`
  - Used for notes or long text fields inside vault entries

---

#### Modal Components

- **Modal**

  - Props: `title`, `isOpen`, `onClose`, `children`
  - Overlay with darkened background
  - Supports multiple sizes (small, medium, large)
  - Accessible (focus trap, esc-to-close, aria roles)

- **ConfirmModal**

  - Specialized modal for confirmation flows (e.g., delete entry)
  - Props: `title`, `message`, `onConfirm`, `onCancel`

- **ShareModal**
  - Custom modal allowing selection of users to share vault entries with
  - Includes email autocomplete, permission levels

---

#### Data Display Components

- **DataTable**

  - Props: `columns`, `data`, `pagination`, `onRowClick`
  - Responsive design with sorting, filtering, pagination
  - Used for vault entries, shared vaults, audit logs

- **Card**

  - Props: `title`, `description`, `icon`, `onClick`
  - Used for dashboard quick stats, empty states

- **Badge**

  - Props: `text`, `color`
  - Used to display tag labels or statuses

- **Breadcrumbs**
  - Props: `paths`
  - Used for navigation context inside Vault detail views

---

#### Feedback Components

- **ToastNotification**

  - Props: `type`, `message`, `duration`
  - Used for success, error, warning feedback

- **Loader**

  - Props: `size`
  - Spinner or skeleton loading indicators for async content

- **EmptyState**
  - Props: `title`, `description`, `actionLabel`, `onAction`
  - Displayed when no entries, no search results, etc.

---

#### Layout Components

- **Sidebar**

  - Dynamic generation based on user role (user, admin)

- **TopNav**

  - Includes logo, search bar, profile dropdown

- **PageContainer**
  - Standardized padding and width constraints for all pages

---

**Component Guidelines**:

- Designed mobile-first, fully responsive
- Styled using a design system (e.g., TailwindCSS or custom tokens)
- Accessibility first: semantic HTML, keyboard navigability, screen reader support
- All components unit-tested individually

---

### 11.5. Accessibility Requirements

The application will adhere strictly to WCAG 2.1 AA guidelines to ensure accessibility for all users, including those with disabilities.

---

#### Perceivable

- **Text Alternatives**: All non-text content (icons, images, buttons) will include descriptive `alt` text or `aria-labels`.
- **Adaptable Content**: Support for screen reader navigation and content resizing up to 200% without loss of functionality.
- **Distinguishable**:
  - Minimum contrast ratio of 4.5:1 for normal text, 3:1 for large text.
  - No reliance on color alone to convey information (e.g., errors use color + icons/text).
  - Provide clear focus indicators on interactive elements.

---

#### Operable

- **Keyboard Accessible**:
  - Full application navigation and actions via keyboard alone.
  - Logical tab order maintained across all pages.
  - Visible focus states for inputs, links, buttons, and controls.
- **Enough Time**:
  - No time-limited interactions without user consent (e.g., token expiration prompts will allow extensions).
- **Seizures and Physical Reactions**:
  - No flashing content or animations triggering more than three times per second.
- **Navigable**:
  - Use of landmarks (`<main>`, `<nav>`, `<header>`, `<footer>`) for semantic structure.
  - Breadcrumb navigation on internal pages.
  - Skip-to-content links for assistive tech users.

---

#### Understandable

- **Readable Text**:
  - Plain, clear language usage across the UI.
  - Language of each page is programmatically identified (`<html lang="en">`).
- **Predictable Behavior**:
  - Consistent navigation, component layouts, and interaction patterns across the entire app.
- **Input Assistance**:
  - Inline form validation errors announced to assistive technologies.
  - Clear labels and instructions for all form inputs.

---

#### Robust

- **Assistive Technology Support**:
  - Full compatibility with screen readers (e.g., NVDA, VoiceOver).
  - Use of ARIA roles and attributes where necessary.
- **Valid HTML/CSS**:
  - All markup will pass W3C validation to ensure interoperability across platforms and devices.

---

**Accessibility Testing Tools and Practices**:

- Automated scanners (axe, Lighthouse).
- Manual keyboard-only testing.
- Screen reader verification (NVDA, VoiceOver).
- Regular audits pre-release and on major UI changes.

---

## 12. Security Model

This section outlines the security foundations of the Password Manager, ensuring protection against common threats and guaranteeing confidentiality, integrity, and availability of user data.

### 12.1. Threat Model

This section defines the assumed threat landscape for the Password Manager, following Microsoft's STRIDE methodology to systematically identify and mitigate risks.

---

#### STRIDE Categories

| Threat Category             | Description                                | Example Mitigations                                                    |
|:----------------------------|:-------------------------------------------|:-----------------------------------------------------------------------|
| **Spoofing**                | Impersonating another user or system.      | Strong authentication (MFA), password policies, session management.    |
| **Tampering**               | Unauthorized modification of data.         | End-to-end encryption, data integrity checks (GCM tags), RLS policies. |
| **Repudiation**             | Denying actions without accountability.    | Immutable audit logs with tamper-evident storage.                      |
| **Information Disclosure**  | Exposing confidential information.         | Client-side encryption, TLS 1.3, strict API access controls.           |
| **Denial of Service (DoS)** | Degrading or blocking system availability. | Rate limiting, scalable deployments, WAF/DDoS protections.             |
| **Elevation of Privilege**  | Gaining unauthorized higher permissions.   | Strict RBAC, scope-restricted tokens, rigorous access controls.        |

---

#### Attacker Capabilities

- **External Attackers**:

  - Network-level attackers (attempting MITM, eavesdropping).
  - Credential stuffing with leaked credentials.
  - Phishing attempts targeting user credentials.

- **Insider Threats**:

  - Malicious administrators or compromised support staff attempting unauthorized data access.

- **Compromised Clients**:

  - Malware or browser extensions extracting master passwords or vault data.
  - Users losing device control without proper session revocation.

- **Server-Side Threats**:

  - API abuse (e.g., exploiting weak endpoint validation).
  - Attempting privilege escalation through flawed RLS or RBAC misconfigurations.

- **Environmental Risks**:
  - Misconfigured cloud services exposing storage buckets or logs.
  - Outdated server software leading to known exploit vulnerabilities.

---

All design decisions explicitly assume that:

- The backend may become partially compromised but cannot decrypt vault data without user master secrets.
- The frontend code can be viewed by attackers, requiring zero-trust assumptions.
- Secrets such as master passwords never leave the client device unencrypted.

---

### 12.2. Key Management

Effective key management is central to the security and confidentiality of user data in the Password Manager. This section details how keys are generated, stored, rotated, and protected throughout the system.

---

#### 12.2.1. Master Key Handling

- **Master Key Generation**:

  - The master key is derived from the user's master password using the Argon2id Key Derivation Function (KDF).
  - The process incorporates a strong salt to prevent precomputed attacks and uses high iterations to slow down brute-force attempts.

- **Master Key Storage**:

  - The master key itself is **never stored** on the server. Only the **hash** of the master key (using bcrypt or Argon2) is stored in the database.
  - Vault data is encrypted using the derived key on the client side before it is sent to the server, ensuring no unencrypted data is stored or transmitted.

- **Key Usage**:
  - The derived key is used exclusively for encryption/decryption of the user's vault entries.
  - The key never leaves the client’s environment. This guarantees a **zero-knowledge** architecture, where the server can never access the user's data.

---

#### 12.2.2. Hardware Security Module (HSM) Integration

- **HSM for Key Storage**:

  - **External Hardware Security Modules (HSMs)** may be used to store critical encryption keys (e.g., for encrypting database backups, securing internal API keys, or further protecting master key derivation).
  - The HSM would never store user vault keys or any user-specific data, but it would be used for securing internal service credentials, encryption keys, and application-level secrets.

- **Key Management Integration**:
  - An HSM is integrated with the backend API layer to secure keys related to server-side operations (e.g., encryption of user data storage, signing tokens).
  - Each key is only accessible within the HSM and is never exposed in plaintext in memory, ensuring the integrity of the encryption process.

---

#### 12.2.3. Key Rotation Policy

- **Periodic Key Rotation**:

  - Master keys are rotated periodically by the user through a **re-encryption process** triggered by a password change. The system will prompt users to update their master password if deemed necessary (e.g., after a security breach).
  - This key rotation is enforced client-side, ensuring the user’s vault remains securely encrypted with a fresh master key.

- **Key Rotation for Stored Vault Entries**:

  - The user’s vault entries are re-encrypted with the new key every time the master password is updated.
  - All previous vault data encrypted with the old key will be re-encrypted using the newly derived master key, and the old key will be discarded immediately after.

- **Secure Key Expiration**:

  - Keys are set with an expiration date, and once expired, the system will trigger a secure rotation of keys, accompanied by the re-encryption of data stored with the old keys.

- **Key Revocation**:

  - In cases where a key is suspected to have been compromised, it can be revoked immediately by the system. Vault data encrypted with the compromised key will be made inaccessible until re-encrypted with a new key derived from the updated master password.

- **Logging Key Rotation Events**:
  - All key rotations and related operations (including key revocation, re-encryption, and password updates) are logged and accessible only to authorized personnel, ensuring complete audit trails for compliance and security purposes.

---

#### 12.2.4. Backup & Disaster Recovery

- **Key Backups**:

  - For disaster recovery, keys used for encryption (especially the master keys) can be backed up in a **secure offline manner**. This may involve backup to a secure, encrypted cloud storage solution, or physical storage in a certified secure facility, ensuring only authorized administrators can access the keys if needed.

- **Key Destruction**:

  - Upon user account deletion or deactivation, all associated encryption keys will be permanently destroyed both from the server and backup locations, ensuring no residual access to sensitive data.

- **Redundancy**:
  - Key management systems, especially those related to HSMs and key vaults, are designed with high availability to avoid single points of failure and ensure system uptime in case of key service failure.

### 12.3. MFA & Recovery

Multi-factor authentication (MFA) is a critical security layer to protect user accounts from unauthorized access. This section outlines the implementation of MFA, including TOTP (Time-based One-Time Password) enrollment, backup codes, and the account recovery flow.

---

#### 12.3.1. TOTP Enrollment

- **TOTP Setup**:

  - Users can enable **TOTP-based MFA** through their account settings by scanning a QR code with an authenticator app (e.g., Google Authenticator, Authy, etc.).
  - The backend generates a secret key, which is shared with the user's authenticator app via a QR code. The secret key is never exposed to the server in plaintext.
  - The user is prompted to enter a one-time code generated by their authenticator app to verify successful enrollment. This ensures that the user has control of the MFA device.

- **TOTP Secret Storage**:

  - The TOTP secret key is securely stored on the server in a hashed format using a cryptographic hashing algorithm (e.g., SHA-256) to prevent direct access to the secret.
  - The hashed TOTP secret is used to verify the codes generated by the user's authenticator app.

- **TOTP Validation**:

  - Each time the user logs in, they are prompted to enter the code generated by their authenticator app in addition to their master password.
  - The system checks the code against the stored hash to authenticate the user.

- **TOTP Backup**:
  - Upon successful enrollment, the user is provided with a set of **backup codes**. These codes can be used to access the account in case the user loses access to their MFA device (e.g., phone lost or reset).
  - Backup codes are one-time use and must be regenerated after each use. Users are encouraged to store backup codes securely (e.g., printed and stored offline).

---

#### 12.3.2. Backup Codes

- **Generation & Storage**:

  - Backup codes are randomly generated during the MFA setup process. A set of backup codes (typically 5-10) is issued and shown to the user, who is instructed to save them in a secure location.
  - Backup codes are stored in the database in an encrypted form to prevent unauthorized access.

- **Usage & Expiry**:

  - Each backup code can be used once. After it is used, it is automatically marked as expired and cannot be reused.
  - The system logs the usage of each backup code and notifies the user when backup codes are about to expire or when they have been fully used.
  - Users are encouraged to generate new backup codes if they have exhausted their original set.

- **Regeneration**:
  - If the user loses access to their MFA device and backup codes, they can regenerate a new set of backup codes by going through the account recovery process.

---

#### 12.3.3. Account Recovery Flow

- **Recovery Initiation**:

  - In the event that the user cannot access their MFA device or backup codes, the account recovery process can be initiated via the "Forgot MFA" or "Can't access MFA?" link on the login page.
  - The user is prompted to verify their identity using a secondary email or security questions (if enabled).

- **Identity Verification**:

  - To verify the user’s identity, the system may require the user to provide personal information (e.g., email, phone number) or answer pre-set security questions.
  - In some cases, a **recovery code** or a **security verification email** is sent to a trusted secondary email address to confirm the identity.

- **Disabling MFA Temporarily**:

  - Once the user's identity is verified, MFA is temporarily disabled for their account. The user is then notified that they can access the account without MFA.
  - The user is strongly encouraged to re-enable MFA immediately after recovering access.

- **New MFA Enrollment**:

  - After MFA is disabled, the user can set up a new MFA method (e.g., TOTP enrollment) and regenerate new backup codes for continued protection.
  - The system ensures that all backup codes are invalidated during the recovery process and generates a new set of backup codes for the user.

- **Logging & Auditing**:

  - All recovery attempts are logged for security purposes, with relevant details such as timestamps, recovery methods used, and IP addresses.
  - Suspicious recovery attempts (e.g., multiple failed attempts, unusual IP addresses) trigger alerts to system administrators and may require additional verification steps.

- **Rate Limiting on Recovery Attempts**:
  - To prevent brute-force attacks on the account recovery process, the system applies **rate limiting** on recovery requests. Multiple failed attempts trigger account lockout or CAPTCHA challenges to ensure that recovery requests are legitimate.

---

This comprehensive MFA and recovery system ensures that user accounts are protected even if the primary authentication method is compromised, providing secure fallback options while maintaining strict controls over the recovery process.

## 13. Regulatory & Compliance

### 13.1 GDPR Compliance
- Data Protection by Design and Default: encryption of personal data at rest and in transit, minimal data collection.
- Lawful Basis for Processing: explicit user consent obtained at registration; audit trail of consent.
- Data Subject Rights: mechanisms for access, rectification, erasure (“right to be forgotten”), restriction of processing, and data portability.
- Data Breach Notification: internal detection and reporting process; notify supervisory authority within 72 hours; inform affected users without undue delay.
- Record of Processing Activities (RoPA): document processing purposes, categories, retention periods, and security measures.

### 13.2 Data Residency & Sovereignty
- Regional Hosting Constraints: deploy primary data stores in EU data centers to comply with EU data residency requirements.
- Cross-Border Data Transfers: if replication outside EU, implement Standard Contractual Clauses or Binding Corporate Rules.
- Backup Storage Location: ensure backups remain within approved jurisdictions; apply same encryption and access controls.
- Data Segregation: logical separation of data per region; environment-specific configurations enforce residency rules.

### 13.3 Legal Considerations
- Privacy Policy & Terms of Service: clear documentation of data collection, processing, user rights, liability disclaimers, jurisdiction.
- Cookie & Tracking Compliance: limit use of cookies to essential functionality; obtain consent for analytics or non-essential cookies.
- Third-Party License Compliance: audit all dependencies (MIT, Apache 2.0, BSD licenses); maintain SPDX license list in repository.
- Export Controls & Cryptography Regulations: verify compliance with local laws governing the use and export of encryption technology.
- Data Retention & Deletion Policy: define retention periods (e.g., logs 90 days, encrypted vault data until account deletion); automate secure deletion upon request.
- Accessibility & Non-Discrimination: adhere to accessibility laws (e.g., EU Web Accessibility Directive) to avoid legal liability.


## 14. Infrastructure & Deployment

This section outlines the infrastructure and deployment strategies that will be used to host, scale, and maintain the password manager application. It provides details on the chosen technologies, environments, and processes for deploying the application securely and efficiently.

### 14.1. Environments

The password manager application will be deployed across three primary environments: **Development**, **Staging**, and **Production**. Each environment serves a distinct purpose in the development lifecycle, ensuring that the application is built, tested, and deployed in an organized and efficient manner. Below is an overview of each environment, including key differences and configurations:

---

#### 14.1.1. Development Environment

The **Development** environment is used by the development team for building, testing, and debugging new features. It allows for rapid iteration and testing with minimal restrictions. The environment will be set up to simulate the production environment, but with reduced security and performance optimizations to facilitate easy debugging and quick updates.

- **Purpose**: Testing new features, debugging, and development of core functionality.
- **Key Characteristics**:
  - Runs on local machines or developer-specific cloud instances.
  - Quick deployment and frequent code pushes.
  - Access to logging, debugging tools, and real-time monitoring for developers.
  - Lower security constraints for faster iteration.
  - Database is a separate instance, not containing production data.
  - Manual data population may be required for feature testing.
- **Deployment**: Uses Docker Compose or Kubernetes for local or dedicated cloud-based environments.

---

#### 14.1.2. Staging Environment

The **Staging** environment is used for integration testing and to validate new features before they are deployed to production. This environment closely mimics the production setup, using the same cloud infrastructure, configuration, and database structure (with anonymized data). The staging environment provides a final validation step to ensure the application is ready for release.

- **Purpose**: Full integration testing, load testing, and pre-production validation.
- **Key Characteristics**:
  - Mirrors production in terms of infrastructure, database, and services.
  - Anonymized production data may be used for testing.
  - More stringent security controls compared to development (e.g., HTTPS, rate limiting).
  - Continuous integration (CI) processes automate deployment to staging after each commit.
  - Ensures that features work as expected in a production-like environment.
- **Deployment**: Deployed using automated CI/CD pipelines, with configuration tailored to the staging environment (e.g., separate database, storage, etc.).

---

#### 14.1.3. Production Environment

The **Production** environment is the live environment where the application serves real users. It is designed for high availability, reliability, and security. This environment handles live user traffic and stores real data, making it the most critical and closely monitored environment.

- **Purpose**: Serving real user traffic, storing production data, and providing the final service.
- **Key Characteristics**:
  - Designed for scalability, reliability, and high availability (e.g., multi-AZ or multi-region deployment).
  - Production data (encrypted) is stored here.
  - Full security controls are in place, including network segmentation, firewalls, and encryption.
  - Traffic routing is optimized for load balancing and failover.
  - Continuous monitoring and alerting systems in place for uptime, performance, and security.
- **Deployment**: Deployed using CI/CD pipelines with strict validation and approval before pushing to production. Rollback strategies are in place in case of deployment failures.

---

#### 14.1.4. Differences Between Environments

| Feature                  | Development           | Staging                                  | Production                                         |
|--------------------------|-----------------------|------------------------------------------|----------------------------------------------------|
| **Purpose**              | Development & Testing | Full integration testing                 | Live user traffic & data                           |
| **Data**                 | Mock/anonymized data  | Anonymized production data               | Real user data (encrypted)                         |
| **Security**             | Low security controls | High security controls                   | Full security (SSL, encryption, RBAC)              |
| **Performance**          | Low optimization      | Medium optimization                      | Fully optimized for performance                    |
| **Deployment Frequency** | Frequent code pushes  | After successful tests                   | After final review, stable releases                |
| **Monitoring**           | Logging and debugging | Integration monitoring                   | Continuous uptime, error alerts, and health checks |
| **Scale**                | Low scale (local/VM)  | Medium scale (scaled to production size) | High scale (auto-scaling, load balancing)          |

---

The **Development** and **Staging** environments enable the development team to test and ensure that features are functional and secure before they reach the **Production** environment. Each environment is optimized to suit its specific purpose, ensuring that issues are identified and addressed early in the development process, reducing the risk of problems in the production environment.

---

### 14.2. IaC & Configuration

Infrastructure as Code (IaC) is a key practice in modern software development and deployment, enabling the management and provisioning of infrastructure using machine-readable configuration files. For this password manager application, **Terraform** will be used to define and provision the infrastructure across various environments (Development, Staging, and Production). This approach ensures consistency, repeatability, and scalability, allowing the infrastructure to be easily maintained and version-controlled.

---

#### 14.2.1. Terraform Modules

**Terraform Modules** will be used to organize infrastructure resources into reusable components, improving both maintainability and scalability. Modules are self-contained, reusable pieces of infrastructure that define specific aspects of the environment, such as virtual machines, networking, and storage. These modules will be written in HashiCorp Configuration Language (HCL) and stored in the version-controlled repository.

- **Purpose**: To define reusable infrastructure components for creating, updating, and managing cloud resources (e.g., VMs, storage, networking).
- **Benefits**:
  - **Reusability**: Define once and reuse across multiple environments.
  - **Modularity**: Isolate individual components (e.g., database, networking, security) for better separation of concerns.
  - **Versioning**: Track changes and roll back to previous infrastructure configurations.

##### Examples of Terraform Modules:

1. **Networking Module**:

   - Defines VPCs, subnets, security groups, and other networking resources.
   - Ensures secure and consistent network configurations across environments.

2. **Compute Module**:

   - Defines EC2 instances, auto-scaling groups, or Kubernetes clusters for deployment.
   - Configures instance types, availability zones, and scaling policies.

3. **Database Module**:

   - Manages cloud database services (e.g., AWS RDS, Google Cloud SQL).
   - Configures database clusters, backup policies, and scaling options.

4. **Secrets Management Module**:
   - Integrates with secret management systems (e.g., AWS Secrets Manager, Azure Key Vault).
   - Ensures secure storage and access to sensitive data (e.g., database credentials).

---

#### 14.2.2. Parameter Store & Secrets Management

The **Parameter Store** (or Secrets Manager) will be used for managing configuration values and sensitive data such as API keys, database credentials, and environment-specific variables. Parameter Store provides a secure, centralized place to store and manage configuration settings, which can be easily referenced by applications and infrastructure components at runtime.

- **Purpose**: To securely store configuration values and secrets, ensuring that sensitive data is not hardcoded in source code or configuration files.
- **Tools**: For AWS, **AWS Systems Manager Parameter Store** will be used; for GCP, **Google Secret Manager** will be utilized; for Azure, **Azure Key Vault** will be the choice.
- **Encryption**: All parameters and secrets will be encrypted using strong encryption keys (e.g., AWS KMS, Google Cloud KMS).

##### Examples of Parameters and Secrets Stored:

- **Environment Variables**: E.g., database connection strings, API keys.
- **Sensitive Configuration**: E.g., admin credentials, encryption keys.
- **Database Credentials**: E.g., RDS login information or Redis authentication tokens.

##### Integration with Terraform:

Terraform can also manage the deployment of these parameters and secrets using the appropriate provider's integration. For example:

- **AWS Secrets Manager Example**:

```hcl
  resource "aws_secretsmanager_secret" "db_password" {
    name = "db_password"
  }

  resource "aws_secretsmanager_secret_version" "db_password_version" {
    secret_id     = aws_secretsmanager_secret.db_password.id
    secret_string = "your-db-password-here"
  }
```

- **AWS SSM Parameter Store Example**:

```hcl
  resource "aws_ssm_parameter" "db_host" {
  name  = "/app/db/host"
  type  = "SecureString"
  value = "db.example.com"
  key_id = "alias/aws/ssm"
  }

```
By using Terraform to manage parameters and secrets, configurations become versioned and can be applied in a consistent manner across all environments.

---

### 14.2.3

In addition to using IaC for infrastructure provisioning, configuration management tools can be used to manage application settings, dependencies, and environment-specific configurations. Tools like Ansible, Chef, or Puppet can be integrated to configure virtual machines or Kubernetes clusters after infrastructure deployment.
- Environment-specific configurations: Each environment (Development, Staging, Production) may have specific configurations that need to be handled, such as database credentials or API keys.
- Version-controlled configuration files: All configuration files should be stored in version-controlled repositories to track changes and ensure consistency across environments.

---
By utilizing Terraform modules and parameter stores for managing infrastructure and configuration, this approach ensures that the application can scale easily, maintain consistency across environments, and minimize errors due to misconfigured infrastructure or sensitive data mishandling. With infrastructure versioned alongside application code, the deployment process becomes fully automated, improving both reliability and agility.

### 14.3. CI/CD Pipelines

Continuous Integration and Continuous Deployment (CI/CD) are vital practices in modern software development, enabling the automation of build, testing, and deployment processes. By implementing CI/CD pipelines, the password manager application can ensure faster development cycles, higher-quality code, and automated deployment across various environments.

---

#### 14.3.1. CI/CD Flow

The CI/CD pipeline for the password manager application will consist of the following stages:

1. **Build**:
   - Triggered automatically on code push or merge to the repository.
   - The build step compiles the application, installs dependencies, and ensures that all components are properly integrated.
   - For frontend components, this step will include bundling JavaScript and CSS. For backend, it includes compiling code and preparing artifacts for deployment.

2. **Test**:
   - Automated unit and integration tests will run to verify that the application's functionality works as expected.
   - For backend, tests will be executed to ensure API functionality, security, and database interactions are correct. For frontend, tests will validate UI components and interactions.
   - Security and vulnerability scans will also be part of the test stage to ensure compliance with best practices and security standards.
   - Tools like **Jest**, **Mocha**, **Cypress**, or **Selenium** can be used for automated testing, while **SonarQube** or **OWASP Dependency-Check** can be utilized for static code analysis and security vulnerability scanning.

3. **Deploy**:
   - On successful test completion, the deployment pipeline is triggered.
   - For **Development Environment**: Automatically deploy the latest version to a dev server or cloud service for further manual or automated testing.
   - For **Staging Environment**: A staging environment will mimic production as closely as possible. Deployments here will go through acceptance tests and validation before production.
   - For **Production Environment**: Production deployments will have stricter controls with approval gates in place.
   - **Approval Gates**: Human approval may be required before deploying to staging or production environments, ensuring that any changes are reviewed before they are pushed live.

---

#### 14.3.2. CI/CD Tools and Technologies

- **CI/CD Platform**: The choice of CI/CD platform can include Jenkins, GitHub Actions, GitLab CI, CircleCI, or Bitbucket Pipelines. These platforms allow for automated execution of the pipeline and offer integrations with version control systems (e.g., GitHub, GitLab).

  - **GitHub Actions Example**:
    - Configure workflows that automatically trigger build and test pipelines on each pull request or commit.
    - Utilize jobs and steps for each part of the pipeline, such as installing dependencies, running tests, and deploying.

  - **GitLab CI Example**:
    - Define a `.gitlab-ci.yml` file with stages like `build`, `test`, `deploy`.
    - Include scripts to deploy to Kubernetes clusters or cloud infrastructure.

- **Containerization**:
  - **Docker** will be used to package the application into containers to ensure consistency between development, staging, and production environments.
  - CI pipelines will build Docker images for both frontend and backend, ensuring the latest application code is packaged with all necessary dependencies.

- **Cloud Providers**:
  - **AWS** (via services like ECS, EKS, or Lambda), **Google Cloud**, or **Azure** will be used for hosting and deploying the application.
  - The pipelines will integrate with the chosen cloud provider's services, such as deploying to ECS (Elastic Container Service) or Kubernetes for orchestration.

---

#### 14.3.3. Deployment Strategies

- **Blue/Green Deployment**: This strategy will be used to ensure zero downtime during production deployments. One version of the app (Blue) will be live, while the new version (Green) is deployed in parallel. Once validated, traffic is switched from Blue to Green.

- **Canary Releases**: A gradual deployment approach where new versions of the application are rolled out to a small percentage of users first. This helps identify potential issues without impacting the entire user base.

- **Rolling Deployments**: For environments with high traffic, rolling deployments will be implemented to ensure that updates are applied incrementally, minimizing disruption.

---

#### 14.3.4. Approval & Manual Interventions

For certain steps in the CI/CD pipeline (especially for production deployments), **manual approval** gates can be added. These gates ensure that a senior developer or administrator reviews the changes before they are pushed to production. This minimizes the risk of errors and enhances the quality assurance process.

- **Staging Approval**: After successful deployment to staging, an approval gate can ensure that the staging environment passes all acceptance tests before promoting the build to production.

- **Production Approval**: The final production deployment step can require an approval from a designated stakeholder, ensuring that the release is thoroughly reviewed and validated before being deployed to users.

---

#### 14.3.5. Notifications and Alerts

To keep the development and operations teams informed, the CI/CD pipeline will send notifications for the following events:

- **Build Failures**: Alerts will be sent to the development team when a build fails, specifying which step failed (e.g., compilation, tests, security scans).

- **Test Failures**: Notifications will be triggered when unit, integration, or security tests fail, providing details on which tests did not pass.

- **Deployment Success/Failure**: After deployments to staging or production, notifications will inform teams of success or failure, providing logs and other pertinent details.

- **Manual Approval Pending**: If manual intervention is required (e.g., approval for staging or production deployments), an alert will notify the designated approvers.

---

#### 14.3.6. Pipeline Example

Here’s an example pipeline flow in **GitLab CI** using `.gitlab-ci.yml`:

```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t password-manager-app .
    - docker push myregistry/password-manager-app

test:
  stage: test
  script:
    - docker run myregistry/password-manager-app npm run test
    - docker run myregistry/password-manager-app npm run lint

deploy_staging:
  stage: deploy
  script:
    - kubectl apply -f k8s/staging.yaml
  environment: staging
  when: manual
  only:
    - main

deploy_production:
  stage: deploy
  script:
    - kubectl apply -f k8s/production.yaml
  environment: production
  when: manual
  only:
    - main
```

## 15. Testing Strategy

A comprehensive testing strategy will be employed to ensure the quality, reliability, and security of the password manager application. This includes unit testing, integration testing, and security testing to cover both the functional and non-functional aspects of the application.

---

### 15.1. Unit Tests

**Unit tests** are essential for verifying the individual components of the application in isolation, ensuring that each part of the system behaves as expected.

#### 15.1.1. Coverage Targets

- **Goal**: Aim for a minimum of 80% code coverage across key modules to ensure that the core functionality is thoroughly tested.
- **Priority Areas**:
  - **Authentication**: Register, login, password reset, and user management logic.
  - **Vault Management**: Create, read, update, and delete (CRUD) operations for vault entries.
  - **Encryption**: Functions related to encryption and decryption using AES-256-GCM and key derivation with Argon2.
  - **Session Management**: Functions managing user sessions and token handling.
  - **Validation**: Ensure proper validation of inputs (e.g., password strength, username format).

#### 15.1.2. Key Modules

- **Auth Module**: Tests for successful registration, login, password reset, and failed authentication attempts.
- **Vault Module**: Tests for creating, updating, reading, and deleting vault entries.
- **Encryption Module**: Ensure that encryption and decryption methods are working as intended.
- **User Management Module**: Tests for user creation, role assignment, and permission enforcement.
- **Error Handling**: Verify that errors are correctly thrown and handled (e.g., invalid inputs, unauthorized access).

---

### 15.2. Integration Tests

**Integration tests** verify the interactions between different components of the application, ensuring that they work together as expected.

#### 15.2.1. End-to-End Flows

- **Authentication Flow**: Test the complete flow of registering a new user, logging in, and retrieving authentication tokens. This will also test user session creation and expiration.
- **Vault CRUD Flow**: Simulate creating, updating, and deleting vault entries. Ensure that data is properly stored and retrieved from the database, and that the encryption/decryption process works end-to-end.
- **Sharing Flow**: Test the ability to share vault entries with other users, including permission checks and ensuring that the shared data is properly encrypted and accessible only by the intended users.
- **Role-Based Access Control (RBAC)**: Verify that different user roles (e.g., admin, regular user) have the appropriate access to different resources (e.g., vault entries, user management).

#### 15.2.2. Encryption Sanity

- **Test Encryption/Decryption**: Ensure that encryption and decryption work across different modules. Test encrypted data storage and ensure that it can only be decrypted by the rightful user.
- **Cross-Platform Encryption**: Verify that encryption and decryption processes function consistently across different environments (e.g., local, staging, production).

---

### 15.3. Security Tests

Security testing will be a critical part of the testing strategy to ensure that the application is robust against common threats and vulnerabilities.

#### 15.3.1. Static Analysis

- **Tools**: Use static analysis tools such as **SonarQube** or **ESLint** to check for common security flaws like SQL injection, XSS vulnerabilities, and insecure data handling in code.
- **Code Review**: Regular code reviews should be conducted, with an emphasis on identifying potential security issues like hardcoded credentials, improper error handling, or insecure API calls.

#### 15.3.2. Penetration Testing

- **Scope**: Conduct penetration testing to simulate attacks such as SQL injection, XSS, CSRF, and brute-force login attempts.
- **Tools**: Use automated penetration testing tools like **OWASP ZAP**, **Burp Suite**, or **Nikto** to identify common vulnerabilities in the application.
- **Manual Testing**: Manual security testing will be performed to simulate real-world attack vectors that automated tools may miss, such as session hijacking or privilege escalation.

#### 15.3.3. Dependency Scans

- **Security Dependencies**: Use tools like **OWASP Dependency-Check** or **Snyk** to scan project dependencies for known security vulnerabilities.
- **Patch Management**: Ensure that any vulnerabilities found in dependencies are addressed promptly by updating or replacing insecure libraries.

---

### 15.4. Testing Tools and Frameworks

- **Unit Testing**: Use frameworks like **Jest**, **Mocha**, or **Jasmine** for JavaScript/Node.js unit testing. For backend testing, **CUnit** or **Google Test** could be used in C.
- **Integration Testing**: Use **Supertest** for API testing to simulate HTTP requests and responses for the REST API. Additionally, **Postman** or **Insomnia** can be used for manual API testing during development.
- **Security Testing**: Use **OWASP ZAP**, **Burp Suite**, **Snyk**, and **Nikto** for automated penetration tests, vulnerability scanning, and dependency checks.
- **CI/CD Integration**: Integrate all testing into the CI/CD pipeline using tools like **Jenkins**, **GitHub Actions**, or **GitLab CI** to ensure that tests run automatically during each build and deployment.

---

### 15.5. Reporting & Metrics

- **Test Reports**: Generate detailed test reports after each test run. This includes pass/fail status, error logs, and performance metrics.
- **Test Coverage Metrics**: Use code coverage tools such as **Istanbul** or **Jest Coverage** to report on test coverage, ensuring that key areas of the application are adequately tested.
- **Security Testing Reports**: Detailed reports from static analysis, penetration tests, and dependency scans should be generated, highlighting any vulnerabilities found and their severity.

---

### 15.6. Performance Testing (Optional but recommended)

- **Load Testing**: Simulate heavy usage with tools like **Apache JMeter** or **Locust** to test the system's behavior under load and identify potential bottlenecks.
- **Stress Testing**: Push the system to its limits to evaluate how it performs under extreme conditions and ensure graceful degradation of service.

By ensuring comprehensive testing across these levels, the password manager application will not only meet functional requirements but also provide a secure, reliable, and high-performance solution.


## 16. Glossary

Defines every acronym, technical term, and domain-specific concept referenced in this document to prevent misinterpretations and ensure operational precision.

| Term                        | Definition                                                                                                                                                                          |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACID                        | Atomicity, Consistency, Isolation, Durability: set of properties guaranteeing reliable transaction processing in relational databases.                                              |
| Agile                       | Iterative software development methodology emphasizing adaptive planning, continuous feedback, and flexible responses to change (e.g., Scrum, Kanban).                              |
| Argon2id                    | Memory-hard key derivation function combining Argon2i and Argon2d modes; resists both side-channel and brute-force attacks for deriving cryptographic keys from passwords.          |
| API                         | Application Programming Interface: defined set of rules and protocols enabling communication between software components, often via HTTP/HTTPS in RESTful or GraphQL systems.       |
| API Gateway                 | Service that routes client requests to backend services, enforcing security, rate limiting, and protocol translation.                                                               |
| AWS ECS                     | Amazon Elastic Container Service: managed container orchestration service for running Docker containers at scale on AWS, supporting EC2 and Fargate launch types.                   |
| Bcrypt                      | Password hashing algorithm based on the Blowfish cipher; includes adaptive work factor to increase computational cost over time.                                                    |
| Cache                       | Temporary storage layer (in-memory or distributed) that speeds up data retrieval by storing frequently accessed data (e.g., Redis, Memcached).                                      |
| CDN                         | Content Delivery Network: distributed network of servers caching and delivering static assets to users from geographically proximate locations to reduce latency.                   |
| CI                          | Continuous Integration: practice of frequently merging developer changes into a shared repository, accompanied by automated tests and builds.                                       |
| CI/CD                       | Continuous Integration / Continuous Deployment (or Delivery): automated workflows that build, test, and deploy applications to various environments upon code changes.              |
| CMK                         | Customer Master Key: primary encryption key stored and managed by a KMS or HSM, used to encrypt data encryption keys.                                                               |
| CORS                        | Cross-Origin Resource Sharing: browser mechanism controlled via HTTP headers to allow or restrict resource requests from different origins.                                         |
| CRUD                        | Create, Read, Update, Delete: basic operations for persistent storage, mapped to HTTP methods POST, GET, PUT/PATCH, and DELETE.                                                     |
| CSRF                        | Cross-Site Request Forgery: web vulnerability where unauthorized commands are transmitted from a user trusted by the application.                                                   |
| CSP                         | Content Security Policy: HTTP header-based security standard that restricts resource loading sources to mitigate XSS and data injection attacks.                                    |
| DevOps                      | Collaboration practice combining software development and IT operations to automate and streamline build, test, and deployment pipelines.                                           |
| DevSecOps                   | Integration of security practices into the DevOps lifecycle, emphasizing automated security testing (SAST, DAST) and compliance checks in CI/CD.                                    |
| DNS                         | Domain Name System: hierarchical naming system translating human-readable domain names to IP addresses.                                                                             |
| Docker                      | Containerization platform packaging applications and dependencies into portable images for consistent deployment across environments.                                               |
| DDoS                        | Distributed Denial of Service: attack that overwhelms a service with traffic from multiple sources, aiming to disrupt availability.                                                 |
| E2EE                        | End-to-End Encryption: encryption model where only communicating endpoints can decrypt messages, preventing intermediaries (including servers) from accessing plaintext.            |
| EC2                         | Amazon Elastic Compute Cloud: scalable virtual server instances in AWS for running applications.                                                                                    |
| ELK                         | Elasticsearch, Logstash, Kibana: stack for log ingestion, storage, and visualization.                                                                                               |
| Encryption Key              | Secret value derived or generated for cryptographic operations, used to encrypt and decrypt data; includes data encryption keys (DEK) and key encryption keys (KEK).                |
| Eventual Consistency        | Consistency model where updates propagate asynchronously across replicas, leading to temporary discrepancies that converge over time.                                               |
| GCM                         | Galois/Counter Mode: block cipher mode providing authenticated encryption, producing ciphertext and authentication tag.                                                             |
| GraphQL                     | Query language and runtime for APIs, enabling clients to request exactly the data they need in a single request.                                                                    |
| HMAC                        | Hash-Based Message Authentication Code: mechanism that uses a secret key and hash function to verify message integrity and authenticity.                                            |
| HSM                         | Hardware Security Module: dedicated hardware device or cloud service for secure generation, storage, and usage of cryptographic keys without exposing them to the host environment. |
| HTTPS                       | HTTP over TLS/SSL: protocol securing HTTP requests and responses to prevent eavesdropping and tampering.                                                                            |
| HTTP/2                      | Updated version of HTTP providing multiplexed streams, header compression (HPACK), and server push to improve performance.                                                          |
| IaC                         | Infrastructure as Code: practice of managing infrastructure provisioning and configuration through declarative code definitions (e.g., Terraform).                                  |
| IAM                         | Identity and Access Management: framework for defining and enforcing user identities and permissions in cloud services or applications.                                             |
| IV                          | Initialization Vector: nonce value used in encryption to ensure unique ciphertexts and prevent reuse of keystreams.                                                                 |
| Jacoco                      | Java code coverage library that instruments code to collect execution metrics for reporting.                                                                                        |
| Jest                        | JavaScript testing framework for unit, integration, and snapshot tests in Node.js and front-end applications.                                                                       |
| JSON                        | JavaScript Object Notation: lightweight, text-based data interchange format widely used for APIs and configuration.                                                                 |
| JWT                         | JSON Web Token: compact, URL-safe token format encoding claims negotiated between parties, signed to verify authenticity.                                                           |
| KDF                         | Key Derivation Function: algorithm for generating cryptographic keys from a secret input (e.g., password), parameterized by memory, time, and parallelism costs.                    |
| Kubernetes                  | Open-source container orchestration platform automating deployment, scaling, and management of containerized applications across clusters.                                          |
| LRU Cache                   | Least Recently Used cache eviction strategy that discards the least recently accessed items when the cache reaches capacity.                                                        |
| Load Balancer               | Network device or service distributing incoming traffic across multiple servers to optimize resource use and availability.                                                          |
| Microservices               | Architectural style organizing an application as a collection of loosely coupled, independently deployable services.                                                                |
| MFA                         | Multi-Factor Authentication: security process requiring multiple independent credentials (e.g., password, token, biometric) for verification.                                       |
| MVC                         | Model-View-Controller: software design pattern separating application logic (model), UI (view), and input handling (controller).                                                    |
| MVVM                        | Model-View-ViewModel: design pattern where the ViewModel exposes data and operations to the view, facilitating two-way data binding.                                                |
| Next.js                     | React framework for server-side rendering, static site generation, and API routes, enhancing performance and SEO.                                                                   |
| NoSQL                       | Non-relational database models (e.g., document, key-value, graph) designed for flexible schemas and horizontal scalability.                                                         |
| OAuth2                      | Authorization framework enabling third-party applications to obtain limited access to user resources without exposing credentials.                                                  |
| OpenID Connect              | Authentication layer built on OAuth2 providing identity verification via JSON Web Tokens.                                                                                           |
| ORM                         | Object-Relational Mapping: technique that converts data between incompatible systems (object-oriented languages and relational databases) using an abstraction layer.               |
| OWASP                       | Open Web Application Security Project: nonprofit organization publishing guidelines and best practices for securing web applications.                                               |
| Postman                     | API development tool for building, testing, and documenting HTTP requests and workflows.                                                                                            |
| PostgreSQL                  | Open-source, ACID-compliant relational database supporting advanced features such as JSONB, RLS, and full-text search.                                                              |
| Prometheus                  | Open-source metrics collection and alerting toolkit designed for monitoring distributed systems.                                                                                    |
| Prisma ORM                  | Type-safe database client and migration tool for Node.js and TypeScript, generating schema-driven query interfaces.                                                                 |
| RabbitMQ                    | Open-source message broker implementing AMQP for asynchronous communication between services.                                                                                       |
| RBAC                        | Role-Based Access Control: authorization model where permissions are assigned to roles and roles are assigned to users.                                                             |
| RLS                         | Row-Level Security: database feature enforcing access policies on individual rows based on session context or user identity.                                                        |
| REST                        | Representational State Transfer: architectural style for stateless, resource-oriented HTTP APIs using standard methods and URIs.                                                    |
| RTO / RPO                   | Recovery Time Objective: maximum tolerable downtime; Recovery Point Objective: maximum tolerable data loss, defined in disaster recovery planning.                                  |
| SAML                        | Security Assertion Markup Language: XML-based framework for exchanging authentication and authorization data between parties.                                                       |
| SaaS                        | Software as a Service: cloud delivery model providing hosted software over the internet on a subscription basis.                                                                    |
| SAST                        | Static Application Security Testing: analysis of application source code for security vulnerabilities without executing programs.                                                   |
| SCSS                        | Sassy CSS: CSS preprocessor extending CSS with variables, nesting, and mixins.                                                                                                      |
| Scrum                       | Agile framework using fixed-length iterations (sprints), defined roles, and ceremonies to deliver incremental product enhancements.                                                 |
| SCSI                        | Small Computer System Interface: set of standards for connecting and transferring data between computers and peripheral devices.                                                    |
| SDS                         | Software-Defined Storage: storage architecture decoupling hardware from software, enabling centralized control and automated provisioning.                                          |
| SFTP                        | Secure File Transfer Protocol: network protocol providing file access, transfer, and management over a secure SSH connection.                                                       |
| SHA-256                     | Secure Hash Algorithm 256-bit: cryptographic hash function producing fixed-size digest, used in data integrity and digital signatures.                                              |
| SNI                         | Server Name Indication: TLS extension allowing multiple domains to share the same IP and certificate, enabling virtual hosting.                                                     |
| SNI                         | Server Name Indication: TLS extension to select appropriate certificate based on hostname during handshake.                                                                         |
| SRI                         | Subresource Integrity: browser security feature enabling verification that fetched resources (e.g., scripts, styles) have not been tampered with by checking hash digests.          |
| SSR                         | Server-Side Rendering: technique of rendering web application markup on the server before sending to client, improving performance and SEO.                                         |
| SSOT                        | Single Source of Truth: principle that data is stored in one authoritative location to ensure consistency.                                                                          |
| SSO                         | Single Sign-On: authentication scheme allowing users to access multiple applications with one set of credentials.                                                                   |
| SSL/TLS                     | Secure Sockets Layer / Transport Layer Security: cryptographic protocols securing data-in-transit with encryption, integrity, and authentication.                                   |
| Static Analysis             | Examination of code without execution to detect vulnerabilities, code quality issues, and style violations.                                                                         |
| Terraform                   | Declarative Infrastructure as Code tool for provisioning cloud and on-premise resources through version-controlled configurations.                                                  |
| Throughput                  | Measure of the rate at which requests or transactions are processed by a system per unit time.                                                                                      |
| TTL                         | Time-To-Live: duration or number of hops after which data (e.g., DNS record, cache entry, token) expires or is discarded.                                                           |
| TOTP                        | Time-Based One-Time Password: algorithm generating short-lived numeric codes for MFA based on shared secret and current time.                                                       |
| UI/UX                       | User Interface / User Experience: disciplines focusing on interface design and overall experience to ensure usability and satisfaction.                                             |
| Vault                       | Encrypted storage container for user credentials, secure notes, or other sensitive data in a password manager.                                                                      |
| Veracode                    | Cloud-based platform for static and dynamic application security testing and remediation guidance.                                                                                  |
| WAF                         | Web Application Firewall: security layer inspecting and filtering HTTP traffic to block malicious requests and attacks.                                                             |
| WebSocket                   | Full-duplex communication protocol over a single TCP connection, enabling real-time data exchange between client and server.                                                        |
| WebCrypto API               | Native browser API providing cryptographic primitives (e.g., hashing, encryption) for secure operations within web applications.                                                    |
| Webpack                     | Module bundler for JavaScript applications, managing dependencies and asset transformations for production deployment.                                                              |
| YAML                        | YAML Ain't Markup Language: human-readable data serialization format often used for configuration files.                                                                            |
| Zero-Knowledge Architecture | System design ensuring servers store only ciphertext; encryption and decryption occur exclusively on the client, preserving user privacy and confidentiality.                       |

---

## 17. References

This section consolidates all external and internal references critical for the design, development, security, and maintenance of the Password Manager application. It includes standards, specifications, libraries, tools, and internal best practices.

---

### Standards & Specifications

- [OWASP Top Ten Web Application Security Risks](https://owasp.org/www-project-top-ten/)
- [NIST SP 800-63B Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [NIST SP 800-38D: Galois/Counter Mode (GCM)](https://csrc.nist.gov/publications/detail/sp/800-38d/final)
- [RFC 7519: JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)
- [RFC 5869: HKDF – Key Derivation Function Based on HMAC](https://datatracker.ietf.org/doc/html/rfc5869)
- [RFC 6238: TOTP – Time-Based One-Time Password Algorithm](https://datatracker.ietf.org/doc/html/rfc6238)
- [RFC 5280: X.509 Certificate and CRL Profile](https://datatracker.ietf.org/doc/html/rfc5280)
- [WCAG 2.1 AA Accessibility Guidelines](https://www.w3.org/TR/WCAG21/)
- [ISO/IEC 27001 Information Security Management](https://www.iso.org/isoiec-27001-information-security.html)

---

### Cryptography & Security Libraries

- [libsodium](https://libsodium.gitbook.io/doc/) — Modern cryptographic library.
- [argon2-cffi](https://argon2-cffi.readthedocs.io/en/stable/) — Password hashing with Argon2.
- [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken) — JWT creation and verification.
- [bcrypt.js](https://github.com/dcodeIO/bcrypt.js) — Password hashing for Node.js (authentication fallback).
- [crypto-js](https://github.com/brix/crypto-js) — AES encryption for browser-side encryption/decryption.

---

### Backend Dependencies

- [Node.js](https://nodejs.org/en) — JavaScript runtime environment.
- [Express.js](https://expressjs.com/) — Web framework for Node.js.
- [Prisma ORM](https://www.prisma.io/) — Type-safe database client.
- [PostgreSQL](https://www.postgresql.org/) — Relational database.
- [Zod](https://zod.dev/) — Schema validation for API inputs and outputs.
- [helmet](https://github.com/helmetjs/helmet) — HTTP headers security middleware.
- [cors](https://github.com/expressjs/cors) — CORS configuration middleware.
- [rate-limiter-flexible](https://github.com/animir/node-rate-limiter-flexible) — Rate limiting and throttling library.
- [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken) — Authentication tokens.

---

### Frontend Dependencies

- [React.js](https://react.dev/) — Frontend library.
- [Next.js](https://nextjs.org/) — React framework for server-side rendering and static generation.
- [TailwindCSS](https://tailwindcss.com/) — Utility-first CSS framework.
- [react-hook-form](https://react-hook-form.com/) — Forms and validation management.
- [axios](https://axios-http.com/) — HTTP client for API communication.
- [react-query](https://tanstack.com/query/latest) — Server state management.
- [zxcvbn](https://github.com/dropbox/zxcvbn) — Password strength estimation.

---

### Infrastructure & DevOps Tools

- [Docker](https://www.docker.com/) — Containerization platform.
- [Docker Compose](https://docs.docker.com/compose/) — Multi-container orchestration.
- [Terraform](https://developer.hashicorp.com/terraform) — Infrastructure as Code (IaC).
- [AWS ECS/EKS](https://aws.amazon.com/ecs/) — Deployment platforms.
- [AWS RDS PostgreSQL](https://aws.amazon.com/rds/postgresql/) — Managed PostgreSQL database.
- [AWS KMS](https://aws.amazon.com/kms/) — Key Management Service for encryption keys.
- [Vault by HashiCorp](https://www.vaultproject.io/) — Secrets management (optional future integration).
- [GitHub Actions](https://github.com/features/actions) — CI/CD pipeline automation.

---

### Testing Tools

- [Jest](https://jestjs.io/) — Unit and integration testing framework.
- [Supertest](https://github.com/ladjs/supertest) — HTTP assertions for API testing.
- [OWASP ZAP](https://www.zaproxy.org/) — Dynamic Application Security Testing (DAST).
- [Snyk](https://snyk.io/) — Dependency and container vulnerability scanner.
- [ESLint](https://eslint.org/) — Code linting.
- [Prettier](https://prettier.io/) — Code formatting.

---

### Internal Best Practices (to be documented)

- Secure Development Lifecycle (SDLC) guidelines.
- Internal password complexity and rotation policies.
- Role-based access control (RBAC) model documentation.
- Incident response plan.
- Data retention and audit log storage policies.


