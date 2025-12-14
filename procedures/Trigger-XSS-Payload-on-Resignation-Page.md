---
id: proc-uuid-5678
name: Trigger-XSS-Payload-on-Resignation-Page
tags:
  - xss-execution
  - javascript-trigger
  - session-compromise
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.933Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-on-Resignation-Page

## Summary

This procedure triggers the execution of the injected JavaScript payload on the Pixiv Sketch resignation success page by loading the malicious URL and interacting with the reflected content, leading to arbitrary code execution in the victim's browser.

## Description

Once the malicious URL is visited after account resignation, the javascript: payload in next_url is reflected into the page's 'Back To Page' button or automatic redirect. Clicking the button or waiting for the redirect executes the script, popping an alert or running custom code to steal session data. This compromises the user's browser context, allowing theft of cookies, local storage, or impersonation of user actions.

## Requirements

1. Victim must visit the malicious URL post-resignation
2. Web browser with JavaScript enabled
3. No additional tools; manual interaction suffices

## Defense

Defensive measures and detection strategies:

- Block javascript: URIs in all redirect and link parameters
- Implement client-side validation for redirects
- Log and alert on unexpected JavaScript execution via browser dev tools or WAF
- Educate users on phishing risks during account deletion

## Objectives

1. Execute the injected JavaScript in victim browser
2. Demonstrate impact via alert or data exfiltration
3. Achieve session compromise for further attacks

## Instructions

### Step 1: Deliver URL to Victim

**Context**: Use social engineering (e.g., email, link sharing) to get the victim to the success page via the malicious URL after they initiate resignation.

No command; send the URL: `https://sketch.pixiv.net/resign_request/success?next_url=javascript%3Aalert%2F%2F(document.domain)`

> Ensure the victim completes resignation first to reach the success state.

### Step 2: Interact to Execute Payload

**Context**: On page load, the payload may execute via redirect; otherwise, click 'Back To Page' to trigger.

In browser, load the URL and click the button.

> Expected: Alert box shows 'sketch.pixiv.net'. For real attacks, replace alert with code to steal document.cookie and exfil to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[javascript-execution]]
