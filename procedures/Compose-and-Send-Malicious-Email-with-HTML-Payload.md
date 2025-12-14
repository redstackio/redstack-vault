---
id: proc-uuid-1010132-1
tags:
  - xss
  - html-injection
  - email
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.578Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Compose-and-Send-Malicious-Email-with-HTML-Payload

## Summary

This procedure involves creating and sending an email to oneself with a malicious HTML payload in the subject field to test for improper escaping in the Hey.com email service, setting up conditions for later DOM reflection.

## Description

In the context of testing for DOM-based XSS in Hey.com, this procedure uses the email composition feature to inject HTML tags into the subject. The payload is designed to include a clickable link with JavaScript, which, if reflected unsanitized, could lead to XSS. The target environment is the web-based Hey.com application, requiring an authenticated session. Expected outcomes include the email being stored with the raw HTML in the subject, enabling reflection during searches.

## Requirements

1. Valid Hey.com account credentials
2. Web browser with access to https://app.hey.com/
3. Authenticated session in the email interface

## Defense

Defensive measures and detection strategies:

- Implement server-side HTML escaping for all user-controlled input in email subjects
- Enforce strict Content Security Policy (CSP) to block inline JavaScript
- Monitor for anomalous email subjects containing script tags via email processing logs

## Objectives

1. Inject HTML payload into email subject without triggering client-side validation
2. Deliver the email to the victim's inbox for later interaction
3. Prepare for reflection testing in search functionality

## Instructions

### Step 1: Initiate Email Composition

**Context**: Access the email writing interface to input the payload.

Navigate to https://app.hey.com/ and ensure you are logged in. Click the 'Write' button in the interface to open the composition window.

### Step 2: Set Recipient and Inject Payload

**Context**: Target the email to self and add the HTML payload to the subject.

Enter your own email address in the 'To' field. In the 'Subject' field, insert the payload: `TestPayload</a><a href="javascript:alert(1)">ClickHere</a>`.

### Step 3: Send the Email

**Context**: Submit the email to store the payload in the system.

Click the send button to deliver the email to your inbox.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
- [[email]]
