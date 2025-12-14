---
id: proc-slack-url-manip-001
tags:
  - url-manipulation
  - rfi
  - slack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.499Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-and-Manipulate-Avatar-Upload-URL

## Summary

This procedure involves uploading a local image to generate a temporary S3 URL and then modifying the 'url' parameter to point to an external resource, simulating RFI in Slack's avatar feature.

## Description

Targeted at Slack's /account/photo endpoint, this procedure exploits the lack of URL validation to substitute external sources. It occurs in a web browser context, with the server fetching and potentially storing the image on AWS S3. Outcomes include displaying unauthorized images as avatars, though Slack views this as intended for sharing.

## Requirements

1. Access to the photo upload page from prior procedure
2. A local image file for initial upload
3. An external image URL (e.g., public logo)

## Defense

Defensive measures and detection strategies:

- Validate 'url' parameters against whitelists (e.g., only S3 domains)
- Log and monitor external URL fetches in S3 uploads

## Objectives

1. Generate valid upload URL
2. Tamper parameter without rejection
3. Enable external fetch

## Instructions

### Step 1: Upload Local File

**Context**: Create the base URL with 'url' parameter.

No command required; select and upload an image file.

> Redirects to crop page with S3 URL, e.g., https://[workspace].slack.com/account/photo?url=https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fslack-files2%2Favatar-temp%2F2014-05-30%2F2364428212.jpg.

### Step 2: Edit URL Parameter

**Context**: Replace S3 path with external.

No command required; modify browser URL to e.g., https://[workspace].slack.com/account/photo?url=https://www.google.co.in/images/srpr/logo11w.png.

> URL updates; no validation error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-manipulation]]
- [[rfi]]
- [[slack]]
