---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - xss
  - dom-xss
  - javascript
  - duckduckgo
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-DOM-XSS-in-DuckDuckGo-relsexp-Parameter]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.424Z'
description: >-
  A single-stage attack exploiting a DOM-based XSS vulnerability in the
  DuckDuckGo search page's 'relsexp' parameter to execute arbitrary JavaScript
  in the browser context.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS via relsexp Parameter on DuckDuckGo Search

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Malicious URL] --> B[JavaScript Execution]
    B --> C[Data Exfiltration or Session Hijacking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Target Platform: Web
- Required Services: DuckDuckGo search engine
- Network Access: Internet connectivity to access duckduckgo.com

### Initial Access Requirements

- No credentials required
- Victim must visit the malicious URL
- No prior access needed

## Detailed Attack Procedures

### Step 1: Craft and Access Malicious URL
procedure: [[procedures/Exploit-DOM-XSS-in-DuckDuckGo-relsexp-Parameter]]

**Objective**: Inject malicious JavaScript via the 'relsexp' parameter to execute code in the duckduckgo.com domain context.

**Instructions**: Construct the proof-of-concept URL and open it in a browser to trigger the DOM XSS. The URL manipulates the 'relsexp' parameter to inject an HTML img tag with an onerror handler.

Use a browser to navigate to the following URL:

```url
https://duckduckgo.com/?q=a&relsexp="><img src=/ onerror=alert(document.domain)>&ia=web
```

This URL injects the payload into the DOM, causing the onerror event to fire and execute alert(document.domain).

**Expected Output**: A browser alert box displaying "duckduckgo.com", confirming JavaScript execution.

**Success Indicators**:
- Alert popup appears showing the document domain
- No errors in browser console related to the injection
- JavaScript executes in the context of duckduckgo.com

## Attack Chain Summary

### Key Achievements

1. Successful injection of arbitrary JavaScript via DOM manipulation
2. Demonstration of potential for session hijacking or cookie theft
3. Exploitation of client-side parameter handling flaw

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2024-01-01T00:00:00Z*
