---
tags:
  - information-disclosure
  - idor
  - enumeration
  - privacy-breach
type: attack_chain
tools:
  - '[[tools/Burp-Suite-Repeater]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Manage-Users-Endpoint]]'
  - '[[procedures/Bruteforce-User-IDs-with-Burp-Repeater]]'
  - '[[procedures/Extract-Emails-from-Responses]]'
step_count: 3
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:12.704Z'
description: >-
  A multi-step attack exploiting an information disclosure vulnerability in the
  Manage Users endpoint of staging.seatme.us, allowing unauthorized enumeration
  and harvesting of user emails by sequentially guessing user_ids without
  authentication checks.
skill_level: intermediate
impact_level: high
id: e657051b-ba64-471c-83fb-ddb31ff59488
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# User Email Enumeration via Unauthenticated User ID Guessing in Manage Users Feature

Multi-stage attack chain demonstrating a complete workflow for exploiting an information disclosure vulnerability to enumerate user emails from a web application.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Endpoint] --> B[Guess User IDs]
    B --> C[Harvest Emails]
    C --> D[Privacy Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite-Repeater]]

### Target Environment

- Web application (staging.seatme.us)
- No specific ports required beyond standard HTTP/HTTPS (80/443)
- Public network access to the staging environment

### Initial Access Requirements

- No credentials needed due to lack of authentication
- Direct HTTP access to the Manage Users endpoint
- No prior access; assumes public-facing application

## Detailed Attack Procedures

### Step 1: Access Manage Users Endpoint
procedure: [[procedures/Access-Manage-Users-Endpoint]]

**Objective**: Navigate to and identify the Manage Users feature endpoint to prepare for parameter manipulation.

**Instructions**: Open a browser or proxy tool like Burp Suite and navigate to the staging.seatme.us domain. Locate the 'Manage users' section, which handles user queries via an HTTP endpoint (likely a GET or POST request to a path like /manage-users or similar). Intercept the initial request using Burp Proxy to understand the baseline structure.

**Expected Output**: Successful access to the endpoint without errors, revealing the request format including the user_id parameter.

**Success Indicators**:
- Endpoint responds with a 200 OK status for valid requests
- Request structure captured, showing user_id as a query or body parameter

### Step 2: Bruteforce User IDs with Burp Repeater
procedure: [[procedures/Bruteforce-User-IDs-with-Burp-Repeater]]

**Objective**: Systematically test sequential user_id values to identify valid accounts without authentication barriers.

**Instructions**: In Burp Repeater, load the intercepted request from Step 1. Modify the user_id parameter to sequential integers, such as 1, 514755, 514775, 514764. Send each request individually and note the response differences. Repeat for a range of IDs to simulate bruteforcing.

**Expected Output**: Responses for valid user_ids include user details; invalid ones return errors or empty data.

**Success Indicators**:
- Multiple valid user_ids identified through differing response patterns
- No rate limiting or authentication prompts encountered

### Step 3: Extract Emails from Responses
procedure: [[procedures/Extract-Emails-from-Responses]]

**Objective**: Collect and harvest email addresses exposed in the HTTP responses for valid user_ids.

**Instructions**: Review the JSON or HTML responses in Burp Repeater for each valid user_id. Manually extract email fields (e.g., from a 'user' object in the response body). Log emails to a file or spreadsheet for further analysis, continuing enumeration until a sufficient dataset is gathered.

**Expected Output**: A list of harvested user emails, demonstrating the scale of disclosure (potentially thousands if IDs are sequential).

**Success Indicators**:
- Emails visible in plaintext within responses
- Successful compilation of a email list without additional access controls

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access user details by ID
2. Enumerated valid user accounts through sequential guessing
3. Harvested sensitive email data, enabling privacy violations like spam or phishing targeting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
