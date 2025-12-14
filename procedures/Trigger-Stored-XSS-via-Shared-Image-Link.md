---
tags:
  - xss
  - cookie-theft
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0da1d95c-18cb-417a-868e-43b65de313d5
created_at: '2025-12-14T03:16:37.360Z'
updated_at: '2025-12-14T03:16:37.360Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Trigger-Stored-XSS-via-Shared-Image-Link

## Summary

This procedure triggers the stored XSS payload by sharing the link to the maliciously uploaded SVG image, causing execution in the victim's browser and enabling theft of session cookies for potential account hijacking.

## Description

After uploading the SVG, the attacker obtains a shareable preview link from the gallery. When a victim clicks the link and views the image, the browser renders the SVG, executing the embedded JavaScript in the forum's context. This allows access to the victim's cookies, which can be exfiltrated to the attacker's server. The attack relies on social engineering to lure victims and exploits the forum's rendering without isolation.

## Requirements

1. Access to the uploaded image's preview URL (e.g., https://community.ubnt.com/t5/image/serverpage/image-id/0i9D3EF39FC6246359/image-size/thumb/is-preview/true?v=1.0&px=100).
2. Communication channel to share the link with victims (e.g., email, social media).
3. Server endpoint to capture exfiltrated data.

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered content from user uploads, stripping executable scripts.
- Implement referrer checks or same-origin policies for image rendering.
- Educate users on phishing risks and monitor for unusual data exfiltration traffic.
- Use browser sandboxing or no-script extensions for admins.

## Objectives

1. Induce victim to load the malicious image.
2. Execute XSS to access and steal authentication cookies.
3. Enable session hijacking with stolen credentials.

## Instructions

### Step 1: Obtain Shareable Link

**Context**: After upload, retrieve the public preview URL for the image from the gallery page.

No command required; copy the link such as https://community.ubnt.com/t5/image/serverpage/image-id/0i9D3EF39FC6246359/image-size/thumb/is-preview/true?v=1.0&px=100.

> This URL points to the thumbnail or full image, which includes the SVG content.

### Step 2: Distribute Link to Victim

**Context**: Share the link via a trusted-looking message to entice the victim to click and view the image.

No command required; send via email or forum reply: "Check out this image: [link]".

> Upon access, the victim's browser fetches and renders the SVG, triggering the script to send cookies to the attacker's endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[cookie-theft]]
- [[session-hijacking]]
