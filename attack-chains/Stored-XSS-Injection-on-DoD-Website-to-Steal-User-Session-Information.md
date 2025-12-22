---
tags:
  - xss
  - stored-xss
  - web-injection
  - session-hijacking
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Malicious-Script-via-Stored-XSS]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.202Z'
description: >-
  A multi-stage demonstration of exploiting a stored XSS vulnerability on a U.S.
  Department of Defense website to inject malicious scripts, leading to session
  hijacking and content manipulation for affected users.
skill_level: intermediate
impact_level: high
id: d100005c-58ce-486a-85be-3a93e9b73fc9
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS Injection on DoD Website to Steal User Session Information

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored cross-site scripting vulnerability on a U.S. Department of Defense website.

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
    A[Discovery and Injection] --> B[Script Execution and Exfiltration]
    B --> C[Session Theft or Content Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for payload crafting
- Proxy tool like Burp Suite for intercepting requests (optional)

### Target Environment

- Web application on a public-facing DoD website
- HTTP/HTTPS access to the vulnerable endpoint
- No specific ports beyond standard web (80/443)

### Initial Access Requirements

- Public access to the website (no authentication needed for injection in this stored XSS case)
- Ability to submit input via URL parameters or forms
- Network position: External attacker

## Detailed Attack Procedures

### Step 1: Discovery and Injection
procedure: [[procedures/Inject-Malicious-Script-via-Stored-XSS]]

**Objective**: Identify the vulnerable input field or parameter and inject a malicious JavaScript payload that gets stored on the server, executing when other users view the page.

**Instructions**: Begin by exploring the DoD website for input fields like comments, search bars, or profile updates that accept user input without proper sanitization. Craft a URL with a payload such as `javascript:alert(document.cookie)` embedded in a parameter, e.g., `https://dod-website.example.gov/page?input=<script>alert(document.cookie)</script>`. Submit this to store the script. Use browser console or a simple curl request to test:

```bash
curl -X GET "https://dod-website.example.gov/page?input=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E" -v
```

Then, visit the affected page as another user to trigger execution. Monitor for the alert popping up with session cookies.

**Expected Output**: The malicious script executes, displaying an alert with cookie data or sending it to an attacker-controlled server.

**Success Indicators**:
- Payload is stored and reflected without escaping when viewing the page
- JavaScript executes, revealing session information like cookies or tokens
- No server-side errors blocking the injection

## Attack Chain Summary

### Key Achievements

1. Successful injection of persistent malicious script into a high-security DoD website
2. Demonstration of session information theft for authenticated users
3. Potential for content modification or phishing attacks on subsequent visitors

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
