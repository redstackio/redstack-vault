---
id: ac-reflected-xss-glassdoor-job-path
tags:
  - xss
  - reflected-xss
  - web-vulnerability
  - javascript-execution
  - cookie-theft
type: attack_chain
tools:
  - '[[tools/Chrome-Browser]]'
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Navigate-to-Glassdoor-Job-Search-Page]]'
  - '[[procedures/Identify-URL-Path-Reflection-Point]]'
  - '[[procedures/Attempt-XSS-Payload-with-Length-Limitation]]'
  - '[[procedures/Bypass-URL-Path-Length-Limitation]]'
  - '[[procedures/Inject-and-Execute-Malicious-XSS-Payload]]'
  - '[[procedures/Bypass-Post-Fix-XSS-in-Title-and-Meta-Tags]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:12.985Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the Glassdoor
  job search URL path, bypassing length restrictions to execute JavaScript for
  cookie theft and redirection.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Reflected XSS in Glassdoor Job Search URL Path Leading to Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the Glassdoor.co.in job search functionality, allowing arbitrary JavaScript execution in the victim's browser for data theft and phishing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Target Page] --> B[Identify Reflection]
    B --> C[Attempt Payload]
    C --> D[Bypass Length Limit]
    D --> E[Inject and Execute XSS]
    E --> F[Post-Fix Bypass]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
    style F fill:#e67e22
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Chrome-Browser]]
- [[tools/Firefox-Browser]]

### Target Environment

- Web platform
- Access to Glassdoor.co.in job search pages
- No specific ports or services required beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to craft and share malicious URLs (e.g., via phishing emails or social engineering)
- Victim must click the link in their browser
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Navigate to Vulnerable Job Search Page
procedure: [[procedures/Navigate-to-Glassdoor-Job-Search-Page]]

**Objective**: Access the base job search URL to establish the attack surface.

**Instructions**: Open a web browser and navigate to the Glassdoor job search page for a specific query, such as Pratt & Whitney jobs.

**Expected Output**: The page loads displaying job listings with the URL path including the search term.

**Success Indicators**:
- Page loads without errors
- URL matches https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true

### Step 2: Identify Reflection Point in URL Path
procedure: [[procedures/Identify-URL-Path-Reflection-Point]]

**Objective**: Locate where user input in the URL path is unsanitized and reflected back into the HTML.

**Instructions**: Inspect the page source or use browser developer tools to observe how the /Job/[INPUT] segment is mirrored in the HTML content without escaping.

**Expected Output**: Confirmation that input like 'pratt-whitney-jobs' appears directly in the page HTML.

**Success Indicators**:
- Input reflected without HTML encoding
- Special characters like < or " would break HTML if injected

### Step 3: Attempt to Input XSS Payload but Note Length Limitation
procedure: [[procedures/Attempt-XSS-Payload-with-Length-Limitation]]

**Objective**: Test a basic XSS payload in the path to verify vulnerability, identifying any restrictions.

**Instructions**: Modify the URL path to include a URL-encoded XSS payload such as '%22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3e' after /Job/.

**Expected Output**: Payload fails to execute due to character length restriction in the path.

**Success Indicators**:
- Page loads but no alert pops up
- Error or truncation observed in reflection

### Step 4: Bypass Length Limitation
procedure: [[procedures/Bypass-URL-Path-Length-Limitation]]

**Objective**: Increase allowable input length to accommodate the full payload.

**Instructions**: Edit the numeric value after the comma in the SRCH_KE parameter (e.g., change ,13 to ,50) to allow longer paths.

**Expected Output**: The URL now accepts longer inputs without truncation.

**Success Indicators**:
- Longer strings in path are processed
- No length-based errors

### Step 5: Construct and Access the Malicious URL
procedure: [[procedures/Inject-and-Execute-Malicious-XSS-Payload]]

**Objective**: Deliver the full payload to trigger JavaScript execution in the victim's browser.

**Instructions**: Construct the full malicious URL with the bypassed length and encoded payload, then open it in the browser.

**Expected Output**: An alert box pops up with '1', confirming XSS execution.

**Success Indicators**:
- JavaScript alert executes
- Potential for further payloads to steal cookies or redirect

## Attack Chain Summary

### Key Achievements

1. Successful identification and exploitation of reflected XSS in URL path
2. Bypassing client-side or server-side length restrictions
3. Demonstration of post-fix bypass in HTML head elements for persistent execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
