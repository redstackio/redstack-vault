---
tags:
  - xss
  - reflected-xss
  - null-byte
  - javascript
  - client-side
type: attack_chain
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-with-Null-Byte-Truncation]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.579Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the Gratipay
  npm package handler by using a null byte to truncate the package name for
  lookup while reflecting the full malicious payload in the HTML output.
skill_level: intermediate
impact_level: high
id: ab7aab54-2f4e-48d0-abf5-9c2b84c805eb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reflected XSS in Gratipay NPM Package Handler via Null Byte Truncation

Multi-stage attack chain demonstrating a complete reflected XSS workflow on gratipay.com, where a null byte (%00) in the URL path truncates the package name for server-side lookup but allows the full unsanitized payload to be reflected in the HTML, leading to arbitrary JavaScript execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Craft Malicious URL] --> B[Execution: Trigger XSS Payload]
    B --> C[Impact: Steal Cookies or Execute JS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]

### Target Environment

- Web platform
- Gratipay.com service handling npm package paths (/on/npm/{package_name})
- No specific ports required (HTTPS on 443)
- Network access to gratipay.com

### Initial Access Requirements

- No credentials needed
- Direct internet access to the target site
- Victim must click the malicious URL (phishing or social engineering implied)

## Detailed Attack Procedures

### Step 1: Access the Malicious URL to Trigger the Reflected XSS
procedure: [[procedures/Exploit-Reflected-XSS-with-Null-Byte-Truncation]]

**Objective**: Craft and navigate to a URL that uses a null byte to bypass package name validation, causing the server to reflect an XSS payload in the HTML.

**Instructions**: Open [[tools/Firefox]] and navigate to the malicious URL: https://gratipay.com/on/npm/cx%00A<svg onload=alert(1)>. The null byte (%00) truncates the package name to 'cx' for the server-side lookup (fetching the valid npm package), but the full string including the payload is inserted into the HTML template without sanitization using the |safe filter in Aspen.

**Expected Output**: The page loads with the package details for 'cx', but the reflected payload executes, showing an alert box with '1'.

**Success Indicators**:
- Alert(1) pops up in the browser
- Page title or content shows the truncated package but full payload in the DOM

### Step 2: Observe the Payload Reflection and Execution
procedure: [[procedures/Exploit-Reflected-XSS-with-Null-Byte-Truncation]]

**Objective**: Verify that the unsanitized package name is reflected in an HTML element, leading to script execution.

**Instructions**: Inspect the page source in [[tools/Firefox]] developer tools after loading the URL from Step 1. Look for the <a> tag containing the full malicious string, e.g., <a href="https://www.npmjs.com/package/cx[%00]A<svg onload=alert(1)>">cx[%00]A<svg onload=alert(1)></a>. The SVG onload attribute triggers the JavaScript execution.

**Expected Output**: DOM inspection reveals the unescaped payload; alert executes immediately upon load.

**Success Indicators**:
- SVG element present in the page with onload handler
- JavaScript console shows no errors, but alert fires

### Step 3: Test Cookie Theft Payload
procedure: [[procedures/Exploit-Reflected-XSS-with-Null-Byte-Truncation]]

**Objective**: Demonstrate the impact by modifying the payload to exfiltrate sensitive data like cookies.

**Instructions**: In [[tools/Firefox]], navigate to https://gratipay.com/on/npm/cx%00A<svg onload=alert(document.cookie)>. This replaces the test alert with one that displays the victim's cookies, simulating theft via an external endpoint (e.g., replace alert with an img src to attacker server).

**Expected Output**: Alert box displays the document.cookie value, revealing session tokens or other client-side data.

**Success Indicators**:
- Cookies are revealed in the alert
- Potential for data exfiltration if payload sends to attacker-controlled server

## Attack Chain Summary

### Key Achievements

1. Bypassed input sanitization using null byte truncation for package lookup
2. Achieved arbitrary JavaScript execution in the victim's browser context
3. Demonstrated cookie theft, enabling session hijacking or further client-side attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2024-10-01T00:00:00Z*
