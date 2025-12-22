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
id: 99d43fac-bc57-4d14-a7f8-69b49096e1a0
created_at: '2025-12-14T05:32:13.250Z'
updated_at: '2025-12-14T05:32:13.250Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-No-Photo-URL-for-Arbitrary-Upload

## Summary

This procedure extends the Gravatar exploit to the 'no photo' option, confirming the unvalidated 'url' parameter affects multiple photo change paths for arbitrary content upload.

## Description

Similar to the Gravatar option, the 'no photo' feature in https://auth.ratelimited.me's profile photo change uses an unchecked 'url' parameter. Intercepting and modifying this allows fetching arbitrary files, bypassing restrictions and highlighting inconsistent validation. This step verifies the vulnerability's scope without achieving code execution, using the same interception setup.

## Requirements

1. Intercepted HTTP request from the 'no photo' option
2. Burp Suite active for modification
3. Arbitrary URL ready for testing

## Defense

Defensive measures and detection strategies:

- Apply uniform URL validation across all photo options
- Use allowlists for fetchable domains and content types
- Monitor profile change logs for external URL usage

## Objectives

1. Confirm vulnerability in alternative photo options
2. Demonstrate consistent bypass across features
3. Assess broader application impact

## Instructions

### Step 1: Trigger No Photo Option

**Context**: Select the 'no photo' choice to generate the interceptable request.

In the profile photo interface, choose 'no photo' and let the request hit the proxy.

> The request pauses in Burp, exposing the 'url' parameter.

### Step 2: Alter URL and Submit

**Context**: Tamper with the parameter to test arbitrary content.

Change 'url' to a non-image endpoint, e.g., http://attacker.com/evil.txt.

> Forward the request and check if the profile updates without errors.

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
