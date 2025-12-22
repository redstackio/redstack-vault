---
tags:
  - xss
  - stored-xss
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Stored-XSS-in-Company-Logo-Location]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:07.791Z'
description: >-
  A stored cross-site scripting attack exploiting the lack of encoding in the
  custom company logo location field of the ContactNow application, allowing
  malicious JavaScript execution when the logo is rendered for viewing users.
skill_level: intermediate
impact_level: high
id: 51465fce-75e7-45fc-8d51-4c9a56ded4e6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Stored XSS via Custom Company Logo Location in ContactNow

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in the ContactNow application's custom company logo feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access to Settings] --> B[Injection and Storage]
    B --> C[Execution on Render]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with Developer Tools)
- Optional: Proxy tool like Burp Suite for interception

### Target Environment

- Web platform
- ContactNow application with administrative access to company settings
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid user credentials with permission to edit company logo settings
- Direct network access to the ContactNow web interface
- No prior access beyond authentication needed

## Detailed Attack Procedures

### Step 1: Exploit Stored XSS
procedure: [[procedures/Exploit-Stored-XSS-in-Company-Logo-Location]]

**Objective**: Inject a malicious script into the custom company logo location field, store it server-side, and achieve JavaScript execution when other users view the logo.

**Instructions**: Authenticate to the ContactNow application and navigate to the company settings page for custom logo configuration. In the logo location field, inject a payload such as `javascript:alert('XSS')` or a more advanced script like `<img src=x onerror=alert(document.cookie)>`. Submit the form to store the payload. Then, log out and view the dashboard or any page where the logo is rendered to trigger execution.

**Expected Output**: A JavaScript alert or console log confirming execution, potentially stealing cookies or session data if the payload is crafted for data exfiltration.

**Success Indicators**:
- Payload is accepted and saved without validation errors
- Malicious script executes in the browser context of viewing users
- No immediate server-side sanitization blocks the injection

## Attack Chain Summary

### Key Achievements

1. Successful storage of malicious payload in the logo location field
2. Execution of JavaScript in the context of authenticated users viewing the application
3. Potential for session hijacking or data theft depending on payload sophistication

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
