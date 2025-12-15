---
tags:
  - idor
  - web
  - api
  - access-control
  - data-exfiltration
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Capture-Legitimate-Veris-Venue-Request]]'
  - '[[procedures/Modify-Venue-ID-for-IDOR-Exploitation]]'
  - '[[procedures/Send-Modified-Request-and-Exfil-Data]]'
step_count: 3
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.381Z'
description: >-
  A multi-step attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the Veris application's API to unauthorizedly retrieve
  sensitive venue data from any organization by manipulating the venue_id
  parameter.
skill_level: intermediate
impact_level: high
id: ad301a07-a5ca-41a3-9ea6-8a558c8db837
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Veris Application to Access Any Organization's Venue Data Remotely

Multi-stage attack chain demonstrating a complete IDOR exploitation workflow in the Veris application, allowing remote attackers to access sensitive venue information of arbitrary organizations without authentication or authorization.

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
    A[Capture Legitimate Request] --> B[Modify venue_id Parameter]
    B --> C[Send Modified Request and Exfil Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application (Veris API)
- Required services/ports: HTTP/HTTPS on standard ports (80/443)
- Network access requirements: Direct internet access to the Veris API endpoint

### Initial Access Requirements

- Credential requirements: Valid user account in Veris for initial legitimate request
- Network position: External attacker position
- Prior access needed: Ability to authenticate and make API calls to own venue data

## Detailed Attack Procedures

### Step 1: Capture Legitimate Request
procedure: [[procedures/Capture-Legitimate-Veris-Venue-Request]]

**Objective**: Intercept a legitimate HTTP request to the Veris venue data endpoint using the attacker's own venue_id to understand the request structure.

**Instructions**: Configure a proxy tool like Burp Suite to intercept traffic from the Veris web application. Log in with valid credentials and navigate to retrieve your organization's venue data, capturing the API request.

**Expected Output**: A captured HTTP GET or POST request to the venue endpoint, e.g., `GET /api/venues/{own_venue_id}` with headers including authentication tokens.

**Success Indicators**:
- Request intercepted successfully showing own venue_id
- Response contains legitimate venue data for verification

### Step 2: Modify venue_id Parameter
procedure: [[procedures/Modify-Venue-ID-for-IDOR-Exploitation]]

**Objective**: Alter the venue_id in the captured request to reference another organization's venue, exploiting the lack of authorization checks.

**Instructions**: In the proxy tool, edit the request by replacing the venue_id with an arbitrary ID (e.g., obtained from enumeration or guessing sequential IDs). Ensure the request retains original authentication but targets unauthorized data.

**Expected Output**: Modified request ready for forwarding, e.g., `GET /api/venues/{target_venue_id}`.

**Success Indicators**:
- Parameter successfully changed without breaking request syntax
- No immediate server-side validation errors on modification

### Step 3: Send Modified Request and Exfil Data
procedure: [[procedures/Send-Modified-Request-and-Exfil-Data]]

**Objective**: Forward the tampered request to the API and retrieve the unauthorized venue data, confirming the IDOR.

**Instructions**: Drop the modified request through the proxy or use a tool like curl to send it directly. Analyze the response for the targeted organization's venue details.

**Expected Output**: HTTP response containing full venue data (e.g., JSON with sensitive fields like addresses, configurations) for the targeted organization.

**Success Indicators**:
- Response status 200 OK with unauthorized data
- Data leakage confirmed by comparing to known legitimate response

## Attack Chain Summary

### Key Achievements

1. Successful interception of legitimate API request
2. Bypassing access controls via parameter manipulation
3. Remote exfiltration of sensitive organizational data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
