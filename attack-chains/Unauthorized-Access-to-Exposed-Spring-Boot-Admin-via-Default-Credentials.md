---
tags:
  - default-credentials
  - information-disclosure
  - spring-boot
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Exposed-Spring-Boot-Admin-Instance]]'
  - '[[procedures/Access-Spring-Boot-Admin-with-Default-Credentials]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.651Z'
description: >-
  Attack chain exploiting an exposed Spring Boot Admin instance using default
  credentials to gain unauthorized access and disclose sensitive information.
skill_level: intermediate
impact_level: high
id: 1e94961f-5870-4186-b973-1eba4ba43c70
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Access to Exposed Spring Boot Admin via Default Credentials

Multi-stage attack chain demonstrating a complete attack workflow targeting an exposed Spring Boot Admin interface with default credentials, leading to information disclosure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Exposed Instance] --> B[Initial Access: Login with Default Credentials]
    B --> C[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[curl]]

### Target Environment

- Publicly accessible web server running Spring Boot Admin
- Exposed endpoint on default port (e.g., 8080)
- No authentication hardening

### Initial Access Requirements

- Internet access to scan or directly access the target URL
- Knowledge of common Spring Boot Admin default credentials (e.g., admin/admin)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Discover Exposed Spring Boot Admin Instance
procedure: [[procedures/Discover-Exposed-Spring-Boot-Admin-Instance]]

**Objective**: Identify a publicly accessible Spring Boot Admin server without access controls through reconnaissance or scanning.

**Instructions**: Perform reconnaissance on the target's public-facing services to locate the Spring Boot Admin endpoint, typically accessible at http://target:8080/applications or similar. Use manual browsing or scanning tools to check for exposed admin interfaces.

**Expected Output**: Confirmation of the Spring Boot Admin login page or interface without restrictions.

**Success Indicators**:
- Exposed endpoint responds with Spring Boot Admin UI
- No immediate authentication prompt or weak controls observed

### Step 2: Access with Default Credentials
procedure: [[procedures/Access-Spring-Boot-Admin-with-Default-Credentials]]

**Objective**: Gain unauthorized entry to the admin interface using common default credentials, enabling access to sensitive data.

**Instructions**: Navigate to the login page of the discovered Spring Boot Admin instance and attempt login with default credentials such as username 'admin' and password 'admin'. If successful, explore the interface for metrics, logs, and configurations.

**Expected Output**: Successful login redirecting to the admin dashboard, displaying application details.

**Success Indicators**:
- Login succeeds without custom credentials
- Access to logs, health checks, and configuration data granted

## Attack Chain Summary

### Key Achievements

1. Identified exposed Spring Boot Admin without protections
2. Bypassed authentication using default credentials
3. Disclosed sensitive application information including logs and configs

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
