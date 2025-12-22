---
id: proc-uuid-1
tags:
  - xss
  - injection
  - slack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Slack Apps
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.632Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Slack-App-Name

## Summary

This procedure exploits the lack of input sanitization in Slack's app name field to inject a stored XSS payload, which persists in the app configuration and executes when the app page is viewed.

## Description

In the context of Slack app management, the app name field on the edit page (https://api.slack.com/apps/[appid]/general) allows arbitrary HTML and JavaScript injection due to insufficient validation and output encoding. The payload is stored server-side and rendered unsafely on the viewing page (https://[workspace].slack.com/apps/[appid]), enabling execution in the browser of any user who accesses it. This can lead to session hijacking or data exfiltration in a collaborative environment like Slack.

## Requirements

1. Authenticated Slack account with app editing permissions
2. Knowledge of the target app ID (e.g., A21B3V9GA)
3. Web browser for manual interaction

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping for app metadata fields
- Use Content Security Policy (CSP) to restrict script execution on app pages
- Monitor for anomalous app name changes via audit logs

## Objectives

1. Store malicious JavaScript in the app name for persistence
2. Break out of HTML attributes to inject executable code
3. Enable execution in victim browsers without further interaction

## Instructions

### Step 1: Access App Edit Page

**Context**: Log in and navigate to the vulnerable configuration interface to locate the injectable field.

No specific command; manually enter https://api.slack.com/apps/[appid]/general in the browser address bar.

> The page loads the app details form. Locate the 'Name' field.

### Step 2: Enter and Save Payload

**Context**: Craft a payload that closes the HTML attribute and injects a script tag to test execution.

Manually input the payload in the 'Name' field: `'><script>alert(/Bhati/)</script>` and click 'Save changes'.

> Upon saving, the payload is persisted. No immediate execution occurs here, but it sets up the stored XSS.

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
- [[stored-xss]]
- [[slack]]
