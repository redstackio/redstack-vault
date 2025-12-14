---
id: proc-190870-inject
tags:
  - xss
  - injection
  - nextcloud
  - spreed
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.161Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Spreed User Name

## Summary

This procedure involves injecting a malicious JavaScript payload into the user name field of the Nextcloud Spreed (Calling) plugin, exploiting insufficient input sanitization to store XSS for later execution in victim browsers.

## Description

In the context of a Nextcloud instance with the Spreed plugin, attackers with account access can modify their display name to include HTML/JS tags. Due to lack of proper escaping when rendering names in call rooms, the payload persists and executes when victims interact with rooms. This is particularly effective in older browsers like IE without CSP support, but works in modern browsers via events like hover. Prerequisites include a valid Nextcloud user account and enabled Spreed plugin; outcomes include stored malicious code ready for propagation.

## Requirements

1. Valid login credentials for a Nextcloud account.
2. Access to the Spreed plugin interface for profile editing.
3. Web browser to perform manual injection.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping for user names in Spreed.
- Enforce Content Security Policy (CSP) to block inline scripts and unsafe eval.
- Monitor for anomalous JavaScript alerts or network requests from client-side in logs.

## Objectives

1. Persist a JavaScript payload in the user name field.
2. Ensure the payload evades basic validation.
3. Prepare for room-based propagation to victims.

## Instructions

### Step 1: Access Spreed Profile Settings

**Context**: Log in and navigate to the area where user name can be edited in the Spreed plugin.

Log in to your Nextcloud account and open the Spreed (Calling) interface. Locate the user profile or settings section for display name modification.

### Step 2: Inject Malicious Payload

**Context**: Enter the XSS payload into the name field to test for vulnerability.

Modify the name field with a payload like `'><img src=a onerror=alert(1)>` or `'><script>alert(3)</script>`. Save the changes.

> The payload uses HTML tag breakage and event handlers to execute JS on render. Expected output: Name saves without rejection, confirming lack of sanitization.

### Step 3: Verify Injection

**Context**: Check if the payload is stored by viewing your profile.

Refresh the Spreed interface and inspect the name display. Look for raw HTML/JS in the source if possible.

> Success if the payload appears unescaped; no immediate execution expected here.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- stored-xss
