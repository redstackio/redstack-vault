---
tags:
  - parameter-tampering
  - file-upload-bypass
  - proxy-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite-Pro]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f95518ab-d7b2-46ff-9e6f-c997d7424d9d
created_at: '2025-12-14T05:32:10.175Z'
updated_at: '2025-12-14T05:32:10.175Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Bypass-ImgNum-Parameter-with-Burp-Suite

## Summary

This procedure intercepts and modifies the LISTSERV logo upload POST request using Burp Suite to bypass the 'imgnum' parameter restriction, allowing uploads beyond the 10-slot limit with custom filenames, which can be repeated for DoS.

## Description

LISTSERV 16.0 enforces upload slots (1-10) only client-side via JavaScript, with no server validation. By capturing the multipart/form-data POST in Burp, changing 'imgnum' to arbitrary values (e.g., 'cow' or '50'), and appending the value to the 'logo' payload, the server saves files with custom names. Target: wa.cgi endpoint. Prerequisites: Active Burp proxy and captured request. Outcomes: Unlimited uploads, potential disk exhaustion if scaled.

## Requirements

1. Burp Suite Pro configured as browser proxy (e.g., 127.0.0.1:8080)
2. Authenticated session from prior setup
3. Test image file ready
4. Knowledge of multipart/form-data structure

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for 'imgnum' (restrict to 1-10 integers)
- Sanitize and reject non-numeric or appended payload data
- Monitor upload volume per user/IP; rate-limit or alert on anomalies
- Use file size/type checks and disk quota enforcement

## Objectives

1. Override slot limits for arbitrary uploads
2. Control filename via parameter injection
3. Enable scalable DoS through repetition

## Instructions

### Step 1: Intercept the POST Request

**Context**: Capture the legitimate upload to baseline the payload.

No command; Burp action:

With proxy active, submit the upload form. In Burp Proxy > HTTP history, find and send to Repeater.

> Expected output: Request editable in Repeater tab. Success if full multipart payload visible.

### Step 2: Modify imgnum Parameter

**Context**: Change the slot value to bypass limits.

No command; edit in Burp:

In the request body, update imgnum=1 to imgnum=cow (or 50).

> Expected output: Parameter updated. Success if request remains valid.

### Step 3: Append Value to Logo Payload

**Context**: Inject custom string into file data for naming persistence.

No command; payload edit:

In the 'logo' section, after binary image data, add --<boundary> and append 'cow' before closing boundary.

> Expected output: Hex view shows appended text. Success if payload doesn't corrupt image MIME.

### Step 4: Replay Modified Request

**Context**: Submit tampered data to server.

No command; forward in Burp:

Click 'Send' in Repeater.

> Expected output: Server response 200/302. Success if no validation error.

Repeat for DoS by automating in Burp Intruder with large files.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Pro]]

## Tags

- [[parameter-tampering]]
- [[file-upload-bypass]]
