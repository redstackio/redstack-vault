---
id: ac-reflected-xss-emailbody-dod-info-leak
tags:
  - xss
  - reflected-xss
  - information-disclosure
  - web
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Account-Without-Verification]]'
  - '[[procedures/Log-In-to-Authenticated-Area]]'
  - '[[procedures/Inject-Reflected-XSS-Payload]]'
  - '[[procedures/Trigger-XSS-and-Verify-Execution]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:16:37.502Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the emailbody
  GET parameter on a DoD subdomain's admin preview page, combined with
  information disclosure from the open registration page, enabling JavaScript
  execution and reconnaissance on organizations and managers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Gather Victim Host Information]]'
---
# Reflected XSS in Emailbody Parameter with Registration Information Disclosure

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in a U.S. Department of Defense subdomain, allowing arbitrary JavaScript execution, combined with information disclosure from an unrestricted registration page that leaks details on 162 organizations and 144,366 managers.

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
    A[Initial Access via Registration] --> B[Authentication]
    B --> C[Payload Injection]
    C --> D[Execution and Exfiltration]
    E[Information Disclosure] --> A

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome with developer tools)

### Target Environment

- Web application on .NET platform (inferred from .aspx pages)
- No specific ports required; standard HTTPS access

### Initial Access Requirements

- No prior credentials needed; registration is open without email confirmation or restrictions on disposable emails
- Network access to the target DoD subdomain (e.g., https://█████)

## Detailed Attack Procedures

### Step 1: Register Account Without Verification
procedure: [[procedures/Register-Account-Without-Verification]]

**Objective**: Gain initial access by creating an account on the open registration page, which also exposes sensitive organizational data.

**Instructions**: Navigate to the target subdomain and access the registration page. Fill in basic details using a disposable email if desired, then submit to create the account. While on the page, review the publicly listed information on organizations and managers for reconnaissance.

**Expected Output**: Successful account creation with redirect to login or dashboard; visible list of 162 organizations and 144,366 managers.

**Success Indicators**:
- Account registered without email confirmation
- Sensitive organization and manager data leaked and noted

### Step 2: Log In to Authenticated Area
procedure: [[procedures/Log-In-to-Authenticated-Area]]

**Objective**: Authenticate to access protected pages like the admin notifications preview.

**Instructions**: Use the newly created credentials to log in via the login form on the subdomain.

**Expected Output**: Successful login redirecting to the authenticated dashboard or admin sections.

**Success Indicators**:
- Access granted to authenticated endpoints
- No additional verification prompts

### Step 3: Inject Reflected XSS Payload
procedure: [[procedures/Inject-Reflected-XSS-Payload]]

**Objective**: Modify the URL to include a crafted, encoded XSS payload in the emailbody parameter to bypass sanitization and WAF.

**Instructions**: From an authenticated session, navigate to the target preview page and append the URL-encoded payload to the emailbody parameter. The payload starts as '0xd3adc0de<ScRiPt>alert('XSS Success!')</sCripT>', HTML-encoded to '&lt;ScRiPt&gt;alert('XSS Success!')&lt;/sCripT&gt;', and then URL-encoded.

**Expected Output**: Modified URL loads the page with the injected parameter.

**Success Indicators**:
- URL successfully modified without errors
- Payload reflected in the page source (inspect via browser dev tools)

### Step 4: Trigger XSS and Verify Execution
procedure: [[procedures/Trigger-XSS-and-Verify-Execution]]

**Objective**: Execute the JavaScript payload to confirm XSS and demonstrate potential for cookie theft or phishing.

**Instructions**: Load the modified URL in the browser. The reflected payload should trigger an alert box.

**Expected Output**: Alert box pops up displaying 'XSS Success!'.

**Success Indicators**:
- JavaScript alert executes
- Potential for further payloads to steal cookies or perform attacks

## Attack Chain Summary

### Key Achievements

1. Bypassed open registration to gain authenticated access without verification.
2. Exploited unsanitized emailbody parameter for reflected XSS, enabling JavaScript execution.
3. Disclosed sensitive reconnaissance data on DoD organizations and managers.
4. Demonstrated high-impact browser-based attacks like session hijacking.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Gather Victim Host Information]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]
- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
