---
tags:
  - ssrf
  - gitlab
  - internal-access
  - web
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
  - '[[procedures/Access-GitLab-Project-Import-Feature]]'
  - '[[procedures/Specify-Malicious-Localhost-URL-for-SSRF]]'
  - '[[procedures/Exploit-SSRF-to-Interact-with-Internal-Services]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.618Z'
description: >-
  Multi-stage attack exploiting SSRF in GitLab's project import feature to
  access unauthenticated internal services via localhost URLs.
skill_level: intermediate
impact_level: high
id: 35e14075-170b-42c5-93db-f5ffcbd237be
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in GitLab Project Import via Repo by URL to Access Internal Services

Multi-stage attack chain demonstrating exploitation of Server-Side Request Forgery (SSRF) in GitLab's project import feature to target internal services without authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Import Feature] --> B[Specify Malicious URL]
    B --> C[Interact with Internal Services]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-send-import-request]]

### Target Environment

- GitLab instance (self-hosted or SaaS)
- Required services/ports: Git repositories on ports 22, 80, 443; internal local services on localhost
- Network access requirements: Access to GitLab web interface

### Initial Access Requirements

- Valid user account on GitLab (no admin privileges needed)
- Network position: External or authenticated access to GitLab UI/API
- Prior access needed: Ability to create projects

## Detailed Attack Procedures

### Step 1: Access GitLab Project Import Feature
procedure: [[procedures/Access-GitLab-Project-Import-Feature]]

**Objective**: Navigate to the project import functionality in GitLab to prepare for URL-based repository import.

**Instructions**: Log in to the GitLab instance and initiate a new project creation, selecting the 'Repo by URL' import option. This exposes the URL input field vulnerable to SSRF.

**Expected Output**: Import form with URL parameter field visible.

**Success Indicators**:
- Import interface loaded successfully
- URL input field available for manipulation

### Step 2: Specify Malicious Localhost URL for SSRF
procedure: [[procedures/Specify-Malicious-Localhost-URL-for-SSRF]]

**Objective**: Submit a localhost or internal IP URL to trigger the server-side request to local services.

**Instructions**: In the 'Repo by URL' field, enter a URL like `http://localhost:8080` targeting an internal service. Submit the import request using the UI or API.

For API simulation, use [[commands/curl-send-import-request]]:

```bash
curl -X POST 'https://gitlab.example.com/api/v4/projects/import?namespace_id=1' \
  -H 'Private-Token: your_token' \
  -d 'url=http://localhost:8080/internal-endpoint'
```

**Expected Output**: GitLab processes the request, making an internal fetch to the specified localhost URL.

**Success Indicators**:
- Import request accepted without URL validation error
- Server logs (if accessible) show internal request attempt

### Step 3: Exploit SSRF to Interact with Internal Services
procedure: [[procedures/Exploit-SSRF-to-Interact-with-Internal-Services]]

**Objective**: Use the SSRF to read data or perform actions on unauthenticated internal services exposed on localhost.

**Instructions**: Target services like metadata endpoints (e.g., `http://localhost:1690/debug/vars` for GitLab internals) or other local apps. Monitor for responses in import logs or error messages that disclose internal data.

Repeat with variations like `http://127.0.0.1:port` or internal IPs to probe multiple services.

**Expected Output**: Disclosure of internal service data, such as configuration or sensitive info, via import feedback or errors.

**Success Indicators**:
- Internal service response leaked in GitLab output
- Unauthorized access confirmed (e.g., data exfiltration)

## Attack Chain Summary

### Key Achievements

1. Bypassed URL validation to force internal requests
2. Accessed unauthenticated local services without credentials
3. Enabled potential information disclosure or further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
