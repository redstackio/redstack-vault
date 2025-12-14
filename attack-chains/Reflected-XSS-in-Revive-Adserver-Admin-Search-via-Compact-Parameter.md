---
id: ac-reflected-xss-revive-adserver-552
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - session-hijacking
  - revive-adserver
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-XSS-Vulnerability-in-Revive-Adserver]]'
  - '[[procedures/Craft-XSS-Payload-for-Compact-Parameter]]'
  - '[[procedures/Deliver-Reflected-XSS-Payload-via-Malicious-URL]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:38.886Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in Revive
  Adserver 5.5.2 by injecting JavaScript via the unsanitized 'compact' parameter
  in the admin search interface, leading to session cookie theft and
  unauthorized actions.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in Revive Adserver Admin Search via Compact Parameter

Multi-stage attack chain demonstrating a complete reflected XSS workflow in Revive Adserver 5.5.2, targeting the admin search functionality to inject and execute arbitrary JavaScript in an administrator's browser context.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerability] --> B[Craft Payload]
    B --> C[Deliver and Execute]
    C --> D[Exfiltrate Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for testing (e.g., Firefox Developer Tools)
- Optional: [[tools/Burp-Suite]] for URL manipulation

### Target Environment

- Revive Adserver 5.5.2 running on PHP web server
- Access to source code or live instance for inspection
- Administrative interface accessible

### Initial Access Requirements

- No prior credentials needed for identification and crafting
- Social engineering to trick admin into visiting malicious URL
- Network access to the target web application

## Detailed Attack Procedures

### Step 1: Identify the Vulnerable Endpoint
procedure: [[procedures/Identify-XSS-Vulnerability-in-Revive-Adserver]]

**Objective**: Locate the reflected XSS vulnerability by reviewing the source code of the admin search functionality, focusing on the 'compact' parameter handling.

**Instructions**: Access the Revive Adserver source files, specifically examine www/admin/admin-search.php and lib/templates/admin/layout/search.html. Note that the 'compact' parameter is registered globally using phpAds_registerGlobalUnslashed without sanitization and directly inserted into an HTML input field as <input type='hidden' name='compact' value='{$compact}'>. This allows attribute breakout and script injection.

**Expected Output**: Confirmation of unsanitized parameter usage in the template.

**Success Indicators**:
- Identification of direct HTML embedding without escaping
- Understanding of parameter flow from PHP to template

### Step 2: Craft Malicious Payload
procedure: [[procedures/Craft-XSS-Payload-for-Compact-Parameter]]

**Objective**: Develop a JavaScript payload that breaks out of the HTML attribute context to execute arbitrary code, such as alerting document cookies.

**Instructions**: Design a payload like compact=1'><script>alert(document.cookie)</script> to close the input tag prematurely and inject a script tag. Test the payload in a local or staging environment by appending it to the parameter in a search URL.

**Expected Output**: Payload that triggers JavaScript execution when reflected in the page.

**Success Indicators**:
- Payload successfully breaks out of the value attribute
- Script executes in the browser console without errors

### Step 3: Deliver the Malicious URL
procedure: [[procedures/Deliver-Reflected-XSS-Payload-via-Malicious-URL]]

**Objective**: Construct and deliver a full malicious URL to an administrator, resulting in XSS execution upon visit.

**Instructions**: Build the exploit URL: http://target-ip/www/admin/admin-search.php?affiliate=1&banner=1&campaign=1&client=1&compact=1'><script>alert(document.cookie)</script>&keyword=1&zone=1. Use social engineering (e.g., phishing email) to lure the admin to click the link. Upon visit, the payload reflects and executes in the browser.

**Expected Output**: JavaScript alert displaying session cookies or other malicious action.

**Success Indicators**:
- Victim's browser executes the injected script
- Cookies or session data are accessible to the attacker

## Attack Chain Summary

### Key Achievements

1. Successful identification of unsanitized input in admin interface
2. Crafting and testing of effective XSS payload
3. Delivery leading to JavaScript execution and potential session theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
