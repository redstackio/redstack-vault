---
tags:
  - xss
  - execution
  - cookie-theft
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:38.918Z'
sub_techniques: []
id: 2378a7e2-ac82-4c54-a46f-79dcdb100764
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Load-Malicious-URL-to-Execute-XSS-Payload

## Summary

This procedure simulates a victim accessing the malicious URL in a browser, triggering the reflected XSS payload execution to steal and display cookies, demonstrating the vulnerability's impact.

## Description

Once the crafted URL is loaded in a browser targeting the ORY Hydra error endpoint, the unsanitized query parameters are reflected into the HTML, causing the browser to parse and execute the embedded JavaScript. This occurs in the context of the authenticated session if the victim is logged in, allowing cookie exfiltration. The attack relies on social engineering to lure users to the URL during an OAuth error flow.

## Requirements

1. The malicious URL from the construction procedure
2. A web browser like Firefox
3. Network connectivity to auth2.zomato.com

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation on error endpoints
- Use HTTP-only and Secure flags on cookies to mitigate theft
- Implement browser-based protections like XSS auditors
- Log and alert on JavaScript execution attempts in error pages

## Objectives

1. Trigger the XSS payload execution in a browser context
2. Verify cookie theft by observing the output
3. Assess the potential for session hijacking

## Instructions

### Step 1: Open Browser

**Context**: Prepare the environment to load the URL securely for testing.

Launch Firefox browser.

### Step 2: Access the URL

**Context**: Simulate the victim by navigating to the malicious URL, causing the page to load and reflect the payload.

Paste the full malicious URL into the address bar and press Enter. The page renders, executing the marquee onfinish event.

### Step 3: Observe Execution

**Context**: Confirm the payload runs and interacts with the document.

A confirm dialog should pop up displaying the document.cookie value, proving successful XSS and cookie access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- xss
- browser-execution
- phishing
