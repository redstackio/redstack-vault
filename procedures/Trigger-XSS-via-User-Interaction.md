---
id: proc-uber-xss-trigger-interaction
tags:
  - xss
  - user-interaction
  - oauth
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
updated_at: '2025-12-14T17:24:35.190Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-User-Interaction

## Summary

This procedure induces a user to visit the malicious OAuth URL and interact with the consent buttons, triggering a server-side redirect to the javascript: URI and executing the XSS payload in the browser context.

## Description

Upon visiting the crafted URL, the Uber endpoint displays an authorization consent page. Clicking Allow or Deny causes the server to issue a 302 redirect via Location header to the unvalidated redirect_uri. In browsers like Opera Mini or Firefox with 302 handling disabled, this executes the embedded JS, such as alerting document.domain, enabling theft of session cookies or page manipulation for account hijacking.

## Requirements

1. Crafted malicious URL from prior procedure
2. Target user access to vulnerable browser
3. Social engineering to get user to visit and click

## Defense

Defensive measures and detection strategies:

- Implement JS execution safeguards in redirect handling (e.g., open in new tab or validate URI before redirect)
- Log and alert on consent interactions with suspicious redirect_uris
- Educate users on phishing links in OAuth flows
- Browser-level: Enable strict redirect policies

## Objectives

1. Initiate OAuth flow to reach consent stage
2. Trigger redirect on button click
3. Execute JS payload for proof-of-concept or exploitation

## Instructions

### Step 1: Distribute and Visit URL

**Context**: Lure the user to the malicious URL to start the OAuth process.

Send the URL via email, link, or messaging. User visits https://login.uber.com/oauth/authorize?... in their browser.

> Expected: Uber consent page loads, prompting for Allow/Deny.

### Step 2: Interact to Trigger Redirect

**Context**: Simulate or observe user clicking the button to fire the redirect.

Click Allow or Deny on the consent page.

> Expected: Server responds with Location: javascript://... header; browser executes alert(document.domain) in vulnerable setups.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[user-interaction]]
- [[oauth]]
