---
tags:
  - csrf-execution
  - account-disruption
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:30.084Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 801dd4a6-f46d-4ce8-a9f3-5db35467524f
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-Request-to-Disconnect-Twitter

## Summary

This procedure details the automatic submission of the forged GET request to Zomato's vulnerable endpoint, resulting in the unauthorized disconnection of the Twitter integration.

## Description

Once the malicious page loads in the victim's browser, the form submits a GET request to the endpoint lacking CSRF protections. The request uses the victim's session for authentication, exploiting the absence of token validation. This leads to immediate disruption of the Twitter linkage, potentially affecting user notifications and data sync.

## Requirements

1. Victim's browser session active on Zomato
2. Malicious form loaded and submitting
3. No intervening browser security features

## Defense

Defensive measures and detection strategies:

- Require POST for state changes and validate CSRF tokens
- Log and alert on disconnect actions from non-Zomato referers
- Use SameSite cookies to prevent cross-site requests

## Objectives

1. Submit forged request using victim's credentials
2. Bypass anti-CSRF controls
3. Confirm integration unlinkage

## Instructions

### Step 1: Trigger Form Submission

**Context**: Ensure the page auto-submits upon load.

The HTML form, with JavaScript submit(), sends the GET to https://www.zomato.com/php/disconnect_twitter_profile.php. Include header X-Requested-With: XMLHttpRequest if using fetch for better mimicry.

### Step 2: Validate Request Format

**Context**: Mimic the original request to avoid detection.

Confirm no parameters are needed beyond the session; test locally if possible.

### Step 3: Verify Impact

**Context**: Check the outcome on the victim's side.

Instruct victim (or simulate) to log into Zomato and observe Twitter is disconnected.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-execution]]
- [[account-disruption]]
