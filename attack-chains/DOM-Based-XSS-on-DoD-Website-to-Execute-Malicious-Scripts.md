---
id: ac-dom-xss-dod-191416
tags:
  - xss
  - dom-based-xss
  - web-vulnerability
  - script-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-URL-for-DOM-Based-XSS]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.240Z'
description: >-
  A single-stage attack exploiting a DOM-based XSS vulnerability on a U.S.
  Department of Defense website by crafting a malicious URL to inject and
  execute JavaScript in the victim's browser, potentially leading to cookie
  theft or content manipulation.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM-Based XSS on DoD Website to Execute Malicious Scripts

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
    A[Initial Access via Malicious URL] --> B[Script Execution in Browser]
    B --> C[Data Exfiltration or Content Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox) for testing
- URL encoding tool (built-in browser dev tools or online encoder)

### Target Environment

- Target Platform: Web application (DoD public-facing website)
- Required Services/Ports: HTTP/HTTPS on port 80/443
- Network Access Requirements: Public internet access to the target URL

### Initial Access Requirements

- No credentials required (public-facing site)
- Victim must click or visit the crafted URL
- Prior access: None, but social engineering may be needed to lure victim

## Detailed Attack Procedures

### Step 1: Craft and Deliver Malicious URL
procedure: [[procedures/Craft-Malicious-URL-for-DOM-Based-XSS]]

**Objective**: Exploit insufficient input validation of URL parameters to inject JavaScript into the DOM, leading to arbitrary script execution in the victim's browser.

**Instructions**: Identify a vulnerable endpoint on the DoD website where URL parameters (e.g., fragments or query strings) are directly reflected into the DOM without sanitization. Craft a URL with a payload like a JavaScript alert or data exfiltration script. For demonstration, use a simple alert payload encoded to bypass basic filters.

First, construct the base vulnerable URL (inferred from typical DOM-XSS patterns, e.g., http://dod-website.example.com/search#). Append the payload to the hash or parameter:

```bash
# Example using browser console or manual URL construction (no CLI tool needed)
# Vulnerable URL: http://dod-website.example.com/page?param=
# Payload: <script>alert(document.cookie)</script>
# Full URL: http://dod-website.example.com/page?param=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E
```

Encode the payload using URL encoding to ensure it passes through. Test in a browser by navigating to the crafted URL.

**Expected Output**: Upon loading, the browser executes the script, displaying an alert with cookies or modifying the page content.

**Success Indicators**:
- JavaScript alert pops up or console logs execute
- Browser cookies are accessed or page DOM is altered
- No server-side errors; execution happens client-side

## Attack Chain Summary

### Key Achievements

1. Successful injection of malicious JavaScript via URL manipulation
2. Demonstration of potential cookie theft or session hijacking
3. Highlighted lack of DOM sanitization in web application

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
