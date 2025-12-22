---
tags:
  - xss
  - dom-xss
  - javascript-injection
  - rockstar-games
  - gtaonline
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
  - '[[procedures/Exploit-DOM-based-XSS-in-ReturnUrl-Parameter]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.156Z'
description: >-
  A single-stage attack exploiting a DOM-based XSS vulnerability in the logout
  function of Rockstar Games' GTAOnline site, specifically in non-English
  locales like /br/, to inject and execute arbitrary JavaScript in the victim's
  browser.
skill_level: intermediate
impact_level: high
id: 87e71833-f469-443f-9cf6-a6b7790b7032
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS via ReturnUrl Parameter in Rockstar GTAOnline Logout Function

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Initial Access via Malicious Link] --> B[JavaScript Execution]
    B --> C[Session Hijacking or Data Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools (e.g., Chrome DevTools)
- URL encoder (built-in or online tool)

### Target Environment

- Web platform
- Rockstar Games GTAOnline site, non-English versions (e.g., /br/)
- No specific ports or services required beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to send phishing links to victims or trick them into clicking a crafted URL
- No prior credentials needed; exploits public-facing logout endpoint
- Victim must be authenticated or navigating the site for full impact

## Detailed Attack Procedures

### Step 1: Exploit DOM-based XSS
procedure: [[procedures/Exploit-DOM-based-XSS-in-ReturnUrl-Parameter]]

**Objective**: Inject malicious JavaScript via the ReturnUrl parameter in the logout function to execute arbitrary code in the victim's browser, enabling session hijacking, data theft, or phishing.

**Instructions**: Craft a malicious URL targeting the vulnerable logout endpoint. For the Brazilian (/br/) version, use a payload like javascript:alert(document.cookie) encoded in the ReturnUrl parameter. Deliver via phishing or social engineering to lure the victim into clicking it while on the site.

Example crafted URL:

```url
https://www.rockstargames.com/br/logout?ReturnUrl=javascript:alert%28document.cookie%29
```

Test in browser: Open the URL in a browser while logged into the site. The DOM manipulation in the logout function will parse the ReturnUrl and execute the script.

**Expected Output**: Alert box displaying session cookies or other client-side data, confirming execution.

**Success Indicators**:
- JavaScript alert or console log triggers
- Access to victim cookies or local storage
- Potential for further actions like keylogging or form manipulation
