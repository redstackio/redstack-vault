---
tags:
  - file-upload
  - parameter-modification
  - bypass
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
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a7e69004-b6d8-4ab4-a310-7a29f90365dc
created_at: '2025-12-14T05:32:13.253Z'
updated_at: '2025-12-14T05:32:13.253Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Gravatar-URL-for-Arbitrary-Upload

## Summary

This procedure exploits the lack of validation on the 'url' parameter in the Gravatar photo option by modifying it to fetch and set arbitrary non-image files as profile photos.

## Description

The profile photo change feature at https://auth.ratelimited.me uses a 'url' parameter to fetch content for Gravatar integration, but without checks for image types or safe sources. By intercepting the request and altering the URL to point to, e.g., a .txt file hosted elsewhere, attackers bypass direct upload restrictions. This allows setting malicious or arbitrary content as the profile photo, though no code execution is achieved in this scenario. Requires an intercepted request from the prior step.

## Requirements

1. Intercepted HTTP request from the Gravatar photo option
2. Burp Suite with the request paused
3. Control over or knowledge of a remote URL hosting non-image content (e.g., http://example.com/malicious.txt)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL parameters to restrict to trusted domains (e.g., only Gravatar)
- Enforce content-type checks on fetched resources to ensure images only
- Log and scan for unusual URL patterns in profile updates

## Objectives

1. Bypass image-only upload restrictions
2. Set arbitrary file types as profile photos
3. Demonstrate vulnerability impact on user profiles

## Instructions

### Step 1: Locate URL Parameter

**Context**: Identify the 'url' field in the intercepted request body.

In Burp Suite's intercept tab, inspect the request parameters.

> Look for the 'url' parameter, typically in POST data or query string.

### Step 2: Modify and Forward

**Context**: Replace the URL with an arbitrary one and submit.

Edit the 'url' value to a non-image URL, e.g., http://attacker.com/test.txt.

> Click 'Forward' in Burp to send the modified request; observe the response for success.

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

- [[file-upload]]
- [[web]]
