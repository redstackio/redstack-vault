---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - persistent-xss
  - phabricator
  - javascript-bypass
  - self-xss
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/Browser-Network-Inspector]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Navigate-to-Phabricator-Settings]]'
  - '[[procedures/Capture-Phabricator-Settings-POST-Request]]'
  - '[[procedures/Inject-Malicious-Editor-Parameter-via-Curl]]'
  - '[[procedures/Trigger-Persistent-XSS-in-Repository-Edit-Link]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.210Z'
description: >-
  A multi-stage attack exploiting a persistent XSS vulnerability in
  Phabricator's editor link setting by bypassing the javascript: scheme
  validation with a newline character, leading to JavaScript execution upon
  clicking the Edit link in a repository.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Persistent XSS in Phabricator Editor Link via JavaScript Scheme Bypass

Multi-stage attack chain demonstrating a complete attack workflow exploiting a persistent XSS in Phabricator's editor link setting.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Settings] --> B[Capture Request]
    B --> C[Inject Payload]
    C --> D[Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/Browser-Network-Inspector]]

### Target Environment

- Phabricator web application
- Required services/ports: HTTP/HTTPS on standard web ports (80/443)
- Network access requirements: Valid user session in Phabricator

### Initial Access Requirements

- Authenticated user account in Phabricator
- Network position: Direct access to the Phabricator instance
- Prior access needed: Logged-in session

## Detailed Attack Procedures

### Step 1: Access Settings Page
procedure: [[procedures/Navigate-to-Phabricator-Settings]]

**Objective**: Gain access to the display settings panel to prepare for payload injection.

**Instructions**: Open the Phabricator application in a browser and navigate directly to the settings endpoint.

**Expected Output**: The settings panel loads, displaying user preferences including the editor link option.

**Success Indicators**:
- Settings page accessible without errors
- User is authenticated and can view editor settings

### Step 2: Capture Save Request
procedure: [[procedures/Capture-Phabricator-Settings-POST-Request]]

**Objective**: Monitor and capture the legitimate POST request used to save settings, which will be modified for the exploit.

**Instructions**: With the network panel open, interact with the save functionality to capture the request details for replication.

**Expected Output**: Captured POST request to /settings/panel/display/ with form data including the editor parameter.

**Success Indicators**:
- Network panel shows the POST request details
- Request can be copied as a curl command

### Step 3: Inject Malicious Payload
procedure: [[procedures/Inject-Malicious-Editor-Parameter-via-Curl]]

**Objective**: Bypass browser sanitization by using curl to submit a modified POST request with the XSS payload in the editor parameter.

**Instructions**: Modify the captured request to include the encoded payload and execute it via [[commands/inject-phabricator-xss-payload]].

```bash
curl 'https://phabricator.example.com/api/config.set' --data-raw 'editor=javascript%0A%3Aalert(1)&__csrf__=token' -H 'Cookie: session=abc123'
```

**Expected Output**: HTTP 200 response indicating successful save of the editor setting.

**Success Indicators**:
- No errors in curl output
- Settings updated in Phabricator (verifiable by checking user preferences)

### Step 4: Trigger the XSS
procedure: [[procedures/Trigger-Persistent-XSS-in-Repository-Edit-Link]]

**Objective**: Execute the injected JavaScript by interacting with the vulnerable Edit link in a repository.

**Instructions**: Navigate to any repository and click the Edit link, which now uses the malicious editor URL.

**Expected Output**: JavaScript alert(1) pops up, confirming XSS execution.

**Success Indicators**:
- Alert dialog appears
- Arbitrary JavaScript executes in the browser context

## Attack Chain Summary

### Key Achievements

1. Bypassed Phabricator's javascript: scheme validation using a newline character.
2. Achieved persistent self-XSS stored in user settings.
3. Demonstrated potential for account takeover when combined with CSRF.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
