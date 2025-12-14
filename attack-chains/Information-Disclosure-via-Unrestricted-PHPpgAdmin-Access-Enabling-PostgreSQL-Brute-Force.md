---
tags:
  - information-disclosure
  - phppgadmin
  - postgresql
  - brute-force
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/hydra]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - PostgreSQL
submitted: true
complexity: medium
procedures:
  - '[[procedures/Discover-Exposed-PHPpgAdmin-Interface]]'
  - '[[procedures/Brute-Force-PHPpgAdmin-for-Database-Access]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Password Spraying]]'
description: >-
  Multi-stage attack exploiting unrestricted access to the PHPpgAdmin web
  interface, leading to discovery, brute-force, and unauthorized PostgreSQL
  database management.
skill_level: intermediate
impact_level: high
id: e733abd2-7a6b-452f-9f5b-a6eed1dfac68
created_at: '2025-12-14T17:24:55.760Z'
updated_at: '2025-12-14T17:24:55.760Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Password Spraying]]'
---
# Information Disclosure via Unrestricted PHPpgAdmin Access Enabling PostgreSQL Brute-Force

Multi-stage attack chain demonstrating discovery and exploitation of an exposed PHPpgAdmin interface, allowing unauthorized users to brute-force access and perform database operations on PostgreSQL without authentication controls.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Interface] --> B[Brute-Force Access]
    B --> C[Database Operations]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/hydra]]

### Target Environment

- Web platform with PHP-based services
- PostgreSQL database server
- Exposed PHPpgAdmin on default port 80/443

### Initial Access Requirements

- Network access to the target web server
- No prior credentials needed due to lack of access controls
- Basic reconnaissance tools for scanning

## Detailed Attack Procedures

### Step 1: Discovery of Exposed Interface
procedure: [[procedures/Discover-Exposed-PHPpgAdmin-Interface]]

**Objective**: Identify the unrestricted PHPpgAdmin web interface to confirm information disclosure vulnerability.

**Instructions**: Use [[commands/curl-access-phppgadmin]] to probe for the presence of the PHPpgAdmin login page without authentication barriers:

```bash
curl -s http://target-ip/phppgadmin/ | grep -i "phpPgAdmin"
```

If the interface responds with identifiable banners or login forms, it indicates unrestricted access.

**Expected Output**: HTML response containing PHPpgAdmin elements, such as login form or version info, confirming exposure.

**Success Indicators**:
- Presence of PHPpgAdmin login page in response
- No immediate authentication prompt blocking access

### Step 2: Brute-Force Access for Database Management
procedure: [[procedures/Brute-Force-PHPpgAdmin-for-Database-Access]]

**Objective**: Exploit the lack of rate limiting or access controls to brute-force credentials and gain unauthorized database operations.

**Instructions**: Launch a brute-force attack using [[commands/hydra-bruteforce-phppgadmin]] against the login endpoint:

```bash
hydra -l admin -P /path/to/passwords.txt target-ip http-post-form "/phppgadmin/login.php:user=^USER^&pass=^PASS^:Invalid" -t 4
```

Upon successful login, access database queries directly via the interface or follow-up requests.

**Expected Output**: Successful login response redirecting to the database management dashboard.

**Success Indicators**:
- Valid credentials cracked
- Access to PostgreSQL server lists and query execution

## Attack Chain Summary

### Key Achievements

1. Discovered exposed PHPpgAdmin interface without access restrictions
2. Brute-forced credentials to bypass authentication
3. Gained unauthorized control over PostgreSQL database operations, enabling data disclosure and manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Password Spraying]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01*
