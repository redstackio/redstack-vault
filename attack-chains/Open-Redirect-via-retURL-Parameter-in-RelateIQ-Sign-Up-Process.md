---
id: ac-open-redirect-relateiq-returl
tags:
  - open-redirect
  - phishing
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Tamper-Data]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-via-retURL-Parameter]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.300Z'
description: >-
  A multi-step attack exploiting an open redirect vulnerability in the RelateIQ
  sign-up process by manipulating the 'retURL' parameter to redirect users to
  malicious sites, enabling phishing attacks.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect via retURL Parameter in RelateIQ Sign-Up Process

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability in the RelateIQ sign-up form, allowing redirection to arbitrary external URLs for phishing or social engineering.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Sign-Up] --> B[Fill and Submit Form]
    B --> C[Intercept and Modify retURL]
    C --> D[Observe Redirect to Malicious Site]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Tamper-Data]]

### Target Environment

- Web platform
- Access to RelateIQ sign-up page at https://www.relateiq.com/sign-up
- No specific services or ports required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Public internet access
- No credentials needed for sign-up process
- Browser with extension support for request interception

## Detailed Attack Procedures

### Step 1: Navigate to the Sign-Up Page
procedure: [[procedures/Exploit-Open-Redirect-via-retURL-Parameter]]

**Objective**: Access the vulnerable sign-up endpoint to initiate the registration flow.

**Instructions**: Open a web browser and navigate to the RelateIQ sign-up page.

**Expected Output**: The sign-up form loads, displaying fields for registration.

**Success Indicators**:
- Sign-up page is accessible
- Form fields are visible and interactive

### Step 2: Fill the Form and Click the Signup Free Button
procedure: [[procedures/Exploit-Open-Redirect-via-retURL-Parameter]]

**Objective**: Prepare the form submission to trigger the vulnerable redirect parameter.

**Instructions**: Complete the required registration fields (e.g., email, name) and click the "Sign up free" button to submit the form.

**Expected Output**: The form submission request is initiated, ready for interception.

**Success Indicators**:
- Form is filled without errors
- Submission button triggers the POST request

### Step 3: Intercept the Request and Modify the 'retURL' Parameter
procedure: [[procedures/Exploit-Open-Redirect-via-retURL-Parameter]]

**Objective**: Alter the 'retURL' parameter in the HTTP request to point to an external malicious URL.

**Instructions**: Use [[tools/Tamper-Data]] to intercept the form submission request. Locate the 'retURL' parameter and modify its value to an arbitrary external URL, such as `https://google.com` for testing or a phishing site like `https://evil.com/phish`.

**Expected Output**: The modified request shows the updated 'retURL' value in the tool's interface.

**Success Indicators**:
- Request is successfully intercepted
- 'retURL' parameter is edited without validation errors

### Step 4: Observe the Redirect to the Evil Website
procedure: [[procedures/Exploit-Open-Redirect-via-retURL-Parameter]]

**Objective**: Confirm the vulnerability by verifying the redirect to the specified external site.

**Instructions**: Resume the request in Tamper Data to submit the modified form. Monitor the browser for the redirect behavior.

**Expected Output**: The application processes the request and redirects the browser to the modified 'retURL' destination.

**Success Indicators**:
- Browser navigates to the external URL (e.g., google.com)
- No server-side validation blocks the redirect

## Attack Chain Summary

### Key Achievements

1. Successful interception and modification of the sign-up request
2. Bypass of redirect validation to external domains
3. Demonstration of potential for phishing by redirecting to malicious sites

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
