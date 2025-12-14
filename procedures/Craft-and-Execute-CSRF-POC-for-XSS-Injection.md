---
id: proc-gratipay-csrf-poc-xss-001
tags:
  - csrf
  - xss
  - poc
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:26.388Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
---
id: proc-gratipay-csrf-poc-xss-001
name: Craft-and-Execute-CSRF-POC-for-XSS-Injection
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Execution]], [[Collection]]
techniques: [[JavaScript]], [[Drive-by Compromise]]
sub_techniques: []
tags: csrf, xss, poc, injection
platforms: Web
tools: [[tools/Burp-Suite]]
commands: []
---

# Craft-and-Execute-CSRF-POC-for-XSS-Injection

## Summary

This procedure involves creating a CSRF proof-of-concept (PoC) HTML file that submits a malicious search query to Gratipay, injecting an XSS payload to execute JavaScript in the victim's browser context, demonstrating session theft potential.

## Description

Exploiting the lack of CSRF tokens and input validation in Gratipay's search at https://gratipay.com/search, this crafts an auto-submitting form with payload `<script>alert(document.domain)</script>`. In a real attack, this could steal cookies via `document.cookie` or log keystrokes. Target: Authenticated web users; outcomes: Arbitrary JS execution leading to data exfiltration. Prerequisites: Intercepted request template from Burp Suite and an active session.

## Requirements

1. Intercepted search request details from Burp Suite
2. Text editor to create HTML PoC file
3. Browser with active Gratipay session
4. Local web server optional for hosting PoC

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms and searches
- Sanitize and encode user inputs to prevent XSS reflection
- Use Content Security Policy (CSP) to block inline scripts

## Objectives

1. Forge a request to inject XSS payload via CSRF
2. Trigger reflected XSS execution in victim browser
3. Confirm impact through alert or data theft simulation

## Instructions

### Step 1: Create CSRF HTML PoC

**Context**: Build the malicious form based on intercepted request.

Using a text editor, create an HTML file with an auto-submitting form targeting https://gratipay.com/search, setting the search parameter to `<script>alert(document.domain)</script>`.

Example PoC:

```html
<html>
<body>
<form action="https://gratipay.com/search" method="GET">
<input type="hidden" name="search" value="<script>alert(document.domain)</script>">
</form>
<script>document.forms[0].submit();</script>
</body>
</html>
```

> Save as csrf-poc.html; this mimics the search submission without user interaction.

### Step 2: Execute the PoC

**Context**: Load the PoC while authenticated to trigger the exploit.

Open the HTML file in a browser tab while logged into Gratipay. The form submits automatically.

> The browser navigates to Gratipay, reflects the payload, and executes the script.

### Step 3: Observe and Validate Execution

**Context**: Confirm XSS success and assess potential impact.

Look for the alert box showing the domain; in production, replace with `document.cookie` to exfiltrate session data.

> Success: Alert pops on gratipay.com domain, indicating same-origin execution for cookie access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- xss
- poc
- injection

