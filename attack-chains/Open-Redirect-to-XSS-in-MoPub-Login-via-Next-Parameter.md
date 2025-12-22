---
tags:
  - open-redirect
  - xss
  - web-vuln
  - mopub
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-poc]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-Open-Redirect-in-MoPub-Login]]'
  - '[[procedures/Execute-XSS-via-JavaScript-URI]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  Exploits an open redirect vulnerability in the MoPub login page to redirect
  users to arbitrary URLs or execute XSS via javascript: URIs
skill_level: beginner
impact_level: high
id: 64996661-bcb4-4404-bc5f-e4b61a3cf7be
created_at: '2025-12-13T23:56:20.518Z'
updated_at: '2025-12-13T23:56:20.518Z'
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
# Open Redirect to XSS in MoPub Login via Next Parameter

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability in the MoPub login page, allowing redirection to arbitrary URLs or execution of JavaScript for phishing, cookie jacking, or session compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Login URL] --> B[Modify Next Parameter]
    B --> C[Perform Login]
    C --> D[Observe Redirect or XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (browser-based)

### Target Environment

- Web platform
- MoPub services
- Accessible via browser

### Initial Access Requirements

- Valid MoPub login credentials
- Browser access to https://app.mopub.com/login

## Detailed Attack Procedures

### Step 1: Access the Login URL with Sample Next Parameter
procedure: [[procedures/Exploit-Open-Redirect-in-MoPub-Login]]

**Objective**: Initiate access to the vulnerable login page with a baseline next parameter.

**Instructions**: Navigate to the base URL in a browser:

```bash
https://app.mopub.com/login?next=https://google.com
```

**Expected Output**: The login page loads normally.

**Success Indicators**:
- Login page is displayed
- Next parameter is present in the URL

### Step 2: Modify the Next Parameter to Desired Redirect URL
procedure: [[procedures/Exploit-Open-Redirect-in-MoPub-Login]]

**Objective**: Alter the next parameter to point to an arbitrary or malicious URL.

**Instructions**: Change the next parameter value, for example:

```bash
https://app.mopub.com/login?next=https://attacker.com
```

Or for XSS, use [[commands/javascript-alert-poc]]:

```bash
https://app.mopub.com/login?next=javascript:alert("proof of concept")
```

**Expected Output**: URL is modified without errors.

**Success Indicators**:
- Parameter accepts arbitrary values
- No immediate validation errors

### Step 3: Visit the Modified URL and Perform Login
procedure: [[procedures/Exploit-Open-Redirect-in-MoPub-Login]]

**Objective**: Authenticate to trigger the redirect.

**Instructions**: Load the modified URL in the browser and log in with valid credentials.

**Expected Output**: Successful login followed by redirect.

**Success Indicators**:
- Login succeeds
- Redirect occurs post-authentication

### Step 4: Observe the Redirection or XSS Execution
procedure: [[procedures/Execute-XSS-via-JavaScript-URI]]

**Objective**: Confirm the exploit by observing the redirect or JavaScript execution.

**Instructions**: After login, note the redirection to the specified URL or execution of JavaScript if using a javascript: URI, such as [[commands/javascript-alert-poc]].

**Expected Output**: User is redirected to the arbitrary URL, or a JavaScript alert box appears showing 'proof of concept'.

**Success Indicators**:
- Successful redirect to external site
- JavaScript execution in the MoPub domain context

## Attack Chain Summary

### Key Achievements

1. Demonstrated open redirect for phishing attacks
2. Executed XSS via javascript: URI for potential session hijacking
3. Highlighted lack of parameter validation leading to user data compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
