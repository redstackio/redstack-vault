---
tags:
  - cors
  - information-disclosure
  - pii
  - api
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-CORS-Misconfiguration]]'
  - '[[procedures/Retrieve-Excessive-Personal-Data-via-API]]'
  - '[[procedures/Craft-Malicious-Webpage-for-PII-Exfiltration]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:18.041Z'
description: >-
  A multi-stage attack exploiting CORS misconfiguration on the StudyRoom API to
  bypass SOP and disclose excessive personal information via a malicious
  webpage.
skill_level: intermediate
impact_level: high
id: 77449cb9-6cc3-4c45-b5a2-c66bb97e3467
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# CORS Misconfiguration Leading to PII Disclosure on StudyRoom API

Multi-stage attack chain demonstrating a complete attack workflow exploiting CORS misconfiguration on the StudyRoom API server to enable unauthorized cross-origin requests and steal user PII.

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
    A[Identify CORS Misconfiguration] --> B[Exploit Profile API for Data Retrieval]
    B --> C[Craft Malicious Webpage for Exfiltration]
    C --> D[PII Theft via Victim Visit]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools
- Text Editor for HTML/JS

### Target Environment

- Web platform
- StudyRoom API at https://studyroom.line.me
- No specific ports required (HTTPS/443)
- Internet access to the API

### Initial Access Requirements

- No credentials needed for discovery
- Victim must be authenticated to the API (e.g., via cookies)
- Attacker needs a domain to host malicious page

## Detailed Attack Procedures

### Step 1: Identify CORS Misconfiguration
procedure: [[procedures/Identify-CORS-Misconfiguration]]

**Objective**: Detect the CORS policy weakness allowing unauthorized cross-origin requests to the API.

**Instructions**: Use browser dev tools or curl to test requests from a different origin to the API endpoint.

**Expected Output**: Successful response from API without origin restrictions.

**Success Indicators**:
- API responds to cross-origin requests with custom Origin header
- No Access-Control-Allow-Origin restriction

### Step 2: Exploit Profile API for Data Retrieval
procedure: [[procedures/Retrieve-Excessive-Personal-Data-via-API]]

**Objective**: Access and confirm the API returns excessive PII without proper controls.

**Instructions**: Send a request to the profile endpoint using the victim's session (e.g., via dev tools or scripted request).

**Expected Output**: JSON response containing user details like name, email, etc.

**Success Indicators**:
- Retrieval of PII fields beyond necessary (e.g., full profile data)
- Data accessible cross-origin

### Step 3: Craft Malicious Webpage for Exfiltration
procedure: [[procedures/Craft-Malicious-Webpage-for-PII-Exfiltration]]

**Objective**: Create a phishing-like page that tricks victims into loading it, triggering unauthorized API calls to steal PII.

**Instructions**: Host an HTML page with JavaScript that makes fetch requests to the profile API and sends data to attacker's server.

**Expected Output**: Victim's PII exfiltrated to attacker's endpoint upon page load.

**Success Indicators**:
- Malicious page loads without errors
- PII data received on attacker's server

## Attack Chain Summary

### Key Achievements

1. Bypassed SOP via CORS misconfiguration
2. Accessed excessive PII from profile API
3. Enabled drive-by PII theft through malicious webpage

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
