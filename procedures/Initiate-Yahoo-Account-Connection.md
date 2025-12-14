---
tags:
  - csrf
  - account-connection
  - discourse
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5f4a212c-6d14-42e6-9b3e-a99dfee32c2e
created_at: '2025-12-14T17:33:24.597Z'
updated_at: '2025-12-14T17:33:24.597Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Yahoo-Account-Connection

## Summary

This procedure starts the Yahoo OpenID authentication workflow on a Discourse instance to set up for capturing the vulnerable callback in a CSRF attack scenario.

## Description

In the context of exploiting CSRF in Discourse's external account connection, the attacker accesses the account preferences page to trigger the Yahoo connection process. This involves navigating to the specific URL and clicking the connection option, which initiates a redirect to Yahoo for authentication. The goal is to prepare the environment for interception without completing the connection on the attacker's side. Prerequisites include having a registered account on the target Discourse site like try.discourse.org.

## Requirements

1. Browser access to the target Discourse instance (e.g., https://try.discourse.org)
2. Attacker's Yahoo account credentials
3. Burp Suite configured as a proxy for traffic interception

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing endpoints
- Monitor for unusual external auth connection attempts
- Use rate limiting on authentication workflows

## Objectives

1. Trigger the Yahoo OpenID authentication flow
2. Prepare for callback interception
3. Avoid completing the connection prematurely

## Instructions

### Step 1: Access Account Preferences

**Context**: Log in to the target Discourse site and navigate to the preferences to expose connection options.

No command executed; manually visit https://try.discourse.org/u/user/preferences/account in the browser.

> This loads the page with options for connecting external accounts like Yahoo.

### Step 2: Trigger Connection Workflow

**Context**: Initiate the authentication to generate the callback request.

No command executed; click the 'Connect Yahoo account' button.

> This redirects to Yahoo's OpenID endpoint for login, starting the workflow that will produce the vulnerable GET callback.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[account-connection]]
