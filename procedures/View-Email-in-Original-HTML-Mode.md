---
tags:
  - xss
  - email-viewer
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 25f96748-0e88-4d83-a9e1-6527c1667668
created_at: '2025-12-14T03:15:53.261Z'
updated_at: '2025-12-14T03:15:53.261Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# View-Email-in-Original-HTML-Mode

## Summary

This procedure accesses a received malicious email in the Respondly web application and selects the 'original HTML' view to render unsanitized content, exposing the javascript: URI hyperlink for potential exploitation.

## Description

Respondly's email viewing feature includes an 'original HTML' option that fails to sanitize hyperlinks, allowing javascript: URIs to remain executable. An authenticated user navigates to the email list, opens the target message, and switches to this view. This step is crucial as it bypasses any default sanitization in standard views, setting up the XSS trigger. Expected outcomes include the hyperlink being rendered clickable in the browser.

## Requirements

1. Valid authentication credentials for the Respondly web application
2. The malicious email must already be received in the team's inbox
3. Browser access to the Respondly interface

## Defense

Defensive measures and detection strategies:

- Disable or restrict 'original HTML' view options for untrusted emails
- Enforce content security policies (CSP) to block inline JavaScript execution
- Log and alert on access to raw HTML views for sensitive emails

## Objectives

1. Render the email content without sanitization
2. Expose the malicious hyperlink for user interaction
3. Maintain the payload integrity for execution

## Instructions

### Step 1: Access and Render the Email

**Context**: Log in to Respondly and select the view mode that preserves raw HTML to avoid sanitization of the javascript: URI.

Navigate to the Respondly dashboard, locate the received email in the inbox, open it, and choose the 'original HTML' view option from the interface menu. The email body will load in the browser, displaying the hyperlink as crafted.

> Ensure the view is selected correctly; standard views may strip the payload.

**Expected Output**: The email displays with the intact hyperlink, ready for clicking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[email-viewer]]
- [[bypass]]
