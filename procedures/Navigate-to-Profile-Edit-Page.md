---
tags:
  - web
  - initial-access
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
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 75c3a33f-2e31-4012-aa5d-a5bba191c1fa
created_at: '2025-12-11T06:10:22.290Z'
updated_at: '2025-12-11T06:10:22.290Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Navigate to Profile Edit Page

## Summary

This procedure involves accessing the profile edit page on a web platform to initiate modifications, such as uploading a profile picture, as a precursor to exploiting upload vulnerabilities.

## Description

In web applications like HackerOne, navigating to the profile edit page allows users to update personal information, including profile pictures. This step is essential for setting up request interception in subsequent exploitation phases, targeting endpoints without proper input validation.

## Requirements

1. Valid user account on the target platform
2. Web browser with network access to the platform
3. No special tools required for this step

## Defense

Defensive measures and detection strategies:

- Monitor access logs for unusual navigation patterns to edit endpoints
- Implement rate limiting on profile edit accesses

## Objectives

1. Gain access to the upload interface
2. Prepare for request modification
3. Verify endpoint accessibility

## Instructions

### Step 1: Access the URL

**Context**: Directly navigate to the profile edit page to load the upload form.

Access https://hackerone.com/settings/profile/edit in your browser.

> This loads the page allowing profile picture selection and upload initiation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[web]]
- [[initial-access]]
