---
id: uuid-4
tags:
  - email-access
  - source-view
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Email
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:50.052Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-and-View-Email-Source

## Summary

This procedure retrieves the confirmation email and views its raw HTML source in a context where JavaScript can execute, such as a browser-based email client.

## Description

The email contains the reflected payload in its HTML body. Viewing the source renders it as HTML, enabling JS execution to steal cookies like the XSRF token.

## Requirements

1. Access to the recipient email account
2. Email client supporting raw HTML view (e.g., Gmail's "Show original")
3. Browser environment for rendering

## Defense

Defensive measures and detection strategies:

- Strip scripts from emails server-side
- Advise users not to view email sources in browsers
- Detect JS execution in email contexts

## Objectives

1. Locate and open the email
2. Access raw source for payload rendering
3. Trigger execution environment

## Instructions

### Step 1: Check Inbox

**Context**: Wait for and retrieve the email.

Manual check.

> Open your email inbox and search for the Nextcloud confirmation email, typically arriving within 1-2 minutes.

### Step 2: View Raw Source

**Context**: Expose the HTML for execution.

Use client features.

> In the email client, right-click the message and select "View Source" or "Show Original". This loads the HTML in a viewable format.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email]]
- [[html]]
