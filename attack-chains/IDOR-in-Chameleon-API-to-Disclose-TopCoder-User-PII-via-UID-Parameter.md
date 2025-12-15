---
tags:
  - idor
  - pii-disclosure
  - api-vulnerability
  - topcoder
  - chameleon
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-TopCoder-Account-and-Access-Forums]]'
  - '[[procedures/Intercept-Watch-Thread-Request]]'
  - '[[procedures/Extract-Target-User-ID]]'
  - '[[procedures/Modify-Request-with-Target-UID]]'
  - '[[procedures/Send-Modified-Request-to-Exploit-IDOR]]'
step_count: 5
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.013Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the Chameleon API endpoint used by TopCoder forums, allowing
  unauthorized access to private user profiles and PII disclosure.
skill_level: intermediate
impact_level: high
id: 18fda5b6-5e6f-4449-9b04-06618759362c
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Chameleon API to Disclose TopCoder User PII via UID Parameter

Multi-stage attack chain demonstrating a complete workflow to exploit an IDOR vulnerability in the https://fast.trychameleon.com/observe/v2/profiles/ endpoint, leading to the unauthorized disclosure of private PII for TopCoder users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Create Account] --> B[Recon: Intercept Request]
    B --> C[Discovery: Extract UID]
    C --> D[Execution: Modify Request]
    D --> E[Collection: Send and Retrieve PII]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (TopCoder forums at apps.topcoder.com/forums)
- No specific ports or services required beyond standard HTTPS (443)
- Internet access to TopCoder and Chameleon API

### Initial Access Requirements

- No prior credentials needed; create a new TopCoder account
- Browser with developer tools
- Proxy tool like Burp Suite for request interception

## Detailed Attack Procedures

### Step 1: Create TopCoder Account and Access Forums
procedure: [[procedures/Create-TopCoder-Account-and-Access-Forums]]

**Objective**: Gain legitimate access to TopCoder forums to trigger API requests.

**Instructions**: Register a new user account on topcoder.com and log in to the forums.

**Expected Output**: Successful login and access to forum threads.

**Success Indicators**:
- Account creation confirmation
- Forum dashboard visible

### Step 2: Intercept Watch Thread Request
procedure: [[procedures/Intercept-Watch-Thread-Request]]

**Objective**: Capture the legitimate API request triggered by forum interactions.

**Instructions**: Navigate to a forum thread and use Burp Suite to intercept the 'Watch Thread' POST request to the Chameleon API.

**Expected Output**: Intercepted request in Burp Proxy.

**Success Indicators**:
- Request body visible with 'uid' parameter
- Forwarded to Repeater module

### Step 3: Extract Target User ID
procedure: [[procedures/Extract-Target-User-ID]]

**Objective**: Identify the userID of a target user from public profile.

**Instructions**: Visit the target user's TopCoder profile and use browser dev tools to search for 'userID' in the page source.

**Expected Output**: Numeric userID value (e.g., 40991562).

**Success Indicators**:
- userID found in HTML source
- Valid integer ID copied

### Step 4: Modify Request with Target UID
procedure: [[procedures/Modify-Request-with-Target-UID]]

**Objective**: Alter the intercepted request to reference the target user's profile.

**Instructions**: In Burp Repeater, replace the 'uid' value in the request body with the extracted userID and add a random path segment.

**Expected Output**: Modified POST request ready for submission.

**Success Indicators**:
- 'uid' updated to target ID
- Request path includes random string (e.g., /profiles/dawda)

### Step 5: Send Modified Request to Exploit IDOR
procedure: [[procedures/Send-Modified-Request-to-Exploit-IDOR]]

**Objective**: Submit the tampered request to retrieve private PII.

**Instructions**: Execute the modified POST request using [[commands/post-request-to-chameleon-api-with-modified-uid]] in Burp Repeater.

```http
POST /observe/v2/profiles/dawda HTTP/1.1
Host: fast.trychameleon.com
Content-Type: text/plain

{"id":"5ff4c6eca2227c001d72c4b8","uid":"40991562","username":"nochnoidozorh1","browser_x":1366,"browser_n":"chrome","browser_k":"desktop","browser_tz":3,"now":"2021-01-09T09:56:10.892Z","_method":"PATCH","_mode":"user","_account_id":"59aedc1ce5680b0004301f6d"}
```

**Expected Output**: JSON response with profile data including email, names, and roles.

**Success Indicators**:
- Response contains private PII (e.g., email: nochnoidozorh1@gmail.com)
- No authorization error (200 OK status)

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to any TopCoder user's private profile via IDOR
2. Disclosure of sensitive PII such as email addresses and full names
3. Demonstration of missing authorization checks in the Chameleon API

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
