---
id: proc-uuid-123
tags:
  - xss
  - self-xss
  - javascript-url
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-document-domain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.030Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Self-XSS-via-Javascript-URL

## Summary

This procedure demonstrates executing a self-XSS payload on a Quora profile page by constructing and pasting a javascript: URL into the browser address bar, which triggers JavaScript in the current page context. It highlights browser-native behavior rather than a site-specific vulnerability, limiting impact to the user's own session.

## Description

In this attack scenario, the target is the Quora profile page (e.g., https://www.quora.com/profile/Username/). The technique exploits the browser's support for javascript: URLs, allowing arbitrary code execution when pasted into the address bar while on the page. The payload uses alert(document.domain) to prove execution in the Quora domain context. Prerequisites include a standard web browser and access to the profile page. Expected outcomes are a self-executing alert with no persistence or cross-user impact; Quora classified this as non-applicable due to reliance on browser functionality.

## Requirements

1. Web browser like Chrome with javascript: protocol enabled (default)
2. Navigational access to the target Quora profile page
3. No special permissions or tools beyond a standard browser session

## Defense

Defensive measures and detection strategies:

- Educate users on avoiding pasting untrusted URLs into address bars
- Browser extensions like NoScript can block javascript: execution
- Site-side: No mitigation needed as it's not a server flaw, but monitor for unusual reports

## Objectives

1. Demonstrate self-XSS execution in the current browser context
2. Verify domain context via alert popup
3. Highlight limitations of self-XSS to user-only impact

## Instructions

### Step 1: Prepare the Target Page

**Context**: Load the Quora profile page to establish the execution context.

Navigate to https://www.quora.com/profile/Username/ in the browser.

> Ensure the page is fully loaded without errors.

### Step 2: Construct and Execute Payload

**Context**: Build and trigger the javascript: URL to execute the self-XSS.

**Command** ([[commands/javascript-alert-document-domain]]):
```javascript
javascript:alert(document.domain)// https://www.quora.com/profile/Username/
```

> Paste this into the browser address bar and press Enter. The // comments out the appended URL, preventing navigation issues. Expected output: Alert popup with 'www.quora.com', confirming execution in Quora's domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-document-domain]]

## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- xss
- self-xss
- javascript-url
