---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - reddit
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-URL-for-Reflected-XSS-in-Reddit-Verification]]'
  - '[[procedures/Trigger-XSS-Payload-via-Email-Verification-Button]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:29.893Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in Reddit's
  email verification URL path, allowing injection and execution of arbitrary
  JavaScript to steal cookies, deliver malware, or perform social engineering.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reflected XSS in Reddit Email Verification Endpoint for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting unsanitized URL path reflection in Reddit's email verification process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious URL] --> B[Visit URL and Click Verify]
    B --> C[JavaScript Execution]
    C --> D[Impact: Cookie Theft or Malware]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Target Platform: Web application (Reddit.com)
- Required services/ports: HTTPS (port 443)
- Network access requirements: Internet access to reddit.com

### Initial Access Requirements

- No credentials required; social engineering to trick victim into visiting the URL
- Network position: External attacker
- Prior access needed: None, but victim must have received or been sent the malicious verification link

## Detailed Attack Procedures

### Step 1: Craft Malicious URL
procedure: [[procedures/Craft-Malicious-URL-for-Reflected-XSS-in-Reddit-Verification]]

**Objective**: Construct a URL with an injected JavaScript payload in the verification token path to bypass sanitization and enable reflection on the interstitial page.

**Instructions**: Manually construct the URL by appending a payload to the /verification/ endpoint. For example, use a payload like 'asd', alert(document.location), ' to inject JavaScript that executes on page reflection.

The full URL would be: https://www.reddit.com/verification/asd',%20alert(document.location),%20'

**Expected Output**: A valid-looking Reddit verification link containing the XSS payload in the path.

**Success Indicators**:
- URL is formed without syntax errors
- Payload is URL-encoded properly (e.g., spaces as %20, quotes escaped)

### Step 2: Trigger XSS Payload
procedure: [[procedures/Trigger-XSS-Payload-via-Email-Verification-Button]]

**Objective**: Visit the crafted URL in a browser and interact with the verification page to cause the unsanitized token to be reflected, executing the JavaScript payload.

**Instructions**: Open the malicious URL in a web browser. The page will load the email verification interstitial, reflecting the path token without sanitization. Click the 'Verify Email' button to trigger the payload execution, such as alerting the document location or stealing cookies.

**Expected Output**: JavaScript alert box or console execution confirming payload run; potential cookie theft via network requests.

**Success Indicators**:
- Payload executes (e.g., alert pops up)
- No errors in browser console; page modifies as per payload (e.g., redirects or data exfiltration)

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript via URL path without server-side validation
2. Arbitrary code execution in victim's browser context
3. Potential for session hijacking, malware delivery, or phishing via page manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T12:00:00Z*
