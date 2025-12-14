---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - reflected-xss
  - web-vulnerability
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Reflected-XSS-Vulnerability]]'
  - '[[procedures/Demonstrate-Reflected-XSS-with-Malicious-Payload]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.958Z'
description: >-
  A reflected cross-site scripting attack exploiting unsanitized URL parameters
  on a U.S. Department of Defense website to inject and execute malicious
  JavaScript.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS on U.S. Department of Defense Website

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery] --> B[Demonstration]
    B --> C[Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for inspection
- URL crafting tools (e.g., manual editing or Burp Suite)

### Target Environment

- Web platform
- Publicly accessible Department of Defense website
- No specific ports or services beyond standard HTTP/HTTPS

### Initial Access Requirements

- Internet access to the target website
- No credentials required for public-facing endpoint
- Ability to craft and share malicious URLs

## Detailed Attack Procedures

### Step 1: Discovery
procedure: [[procedures/Discover-Reflected-XSS-Vulnerability]]

**Objective**: Identify points in the web application where user input from URL parameters is reflected back without sanitization, enabling XSS injection.

**Instructions**: Inspect the website's URL parameters using browser developer tools. Look for search fields, error messages, or dynamic content that echoes input directly into the HTML. Test with benign payloads like `<script>alert('test')</script>` appended to parameters to check for reflection without encoding.

**Expected Output**: Confirmation of reflected input in the page source without HTML entity encoding.

**Success Indicators**:
- Input from URL appears unescaped in the DOM
- Basic script tag executes an alert

### Step 2: Demonstration
procedure: [[procedures/Demonstrate-Reflected-XSS-with-Malicious-Payload]]

**Objective**: Craft and deliver a malicious URL that executes arbitrary JavaScript in the victim's browser, simulating real-world impact like cookie theft.

**Instructions**: Construct a URL with a payload such as `javascript:alert(document.cookie)` or more advanced scripts for data exfiltration. Share the URL via phishing or direct link. Observe execution when the victim accesses it.

**Expected Output**: Malicious script runs, displaying or sending sensitive data like cookies.

**Success Indicators**:
- Script executes in the browser context
- Access to browser storage or modifications to page content

## Attack Chain Summary

### Key Achievements

1. Identified a reflected XSS entry point on a high-security government website.
2. Demonstrated payload execution leading to potential session hijacking.
3. Highlighted risks of unsanitized user input in web applications.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
