---
tags:
  - xss
  - dom-xss
  - javascript
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-DOM-XSS-via-atb-Parameter]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.335Z'
description: >-
  A single-stage attack exploiting a DOM-based XSS vulnerability on DuckDuckGo's
  50x.html error page by injecting malicious JavaScript via the 'atb' query
  parameter, leading to arbitrary code execution in the victim's browser.
skill_level: beginner
impact_level: high
id: ae660cad-e15e-46f7-a931-39859e5fcbf6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS on DuckDuckGo 50x.html Error Page

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
    A[Access Malicious URL] --> B[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to DuckDuckGo domain (https://duckduckgo.com)
- No specific services/ports required beyond HTTP/HTTPS

### Initial Access Requirements

- No credentials needed
- Direct network access to the internet
- No prior access required

## Detailed Attack Procedures

### Step 1: Craft and Access Malicious URL
procedure: [[procedures/Exploit-DOM-XSS-via-atb-Parameter]]

**Objective**: Inject malicious JavaScript payload into the 'atb' query parameter on the 50x.html error page to execute arbitrary code in the browser context.

**Instructions**: Construct the proof-of-concept (PoC) URL with the payload that breaks out of an HTML attribute and triggers JavaScript execution via an onerror handler on an img tag. The payload exploits the unsanitized insertion of location.search into innerHTML in lib/l110.js.

Visit the following URL in a web browser:

```url
https://duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(document.domain);%3E
```

This URL encodes the payload `test"/><img src=x onerror=alert(document.domain);>` which is decoded and inserted without escaping, leading to execution.

**Expected Output**: An alert box pops up displaying the document domain (duckduckgo.com), confirming JavaScript execution.

**Success Indicators**:
- Alert dialog appears with document domain
- Browser console shows no errors from sanitization
- Payload executes without redirection or blocking

## Attack Chain Summary

### Key Achievements

1. Successful injection of user-controlled input into DOM via innerHTML
2. Arbitrary JavaScript execution in victim browser context
3. Potential for session hijacking or data theft on error page visits

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
