---
tags:
  - interception
  - file-upload
type: procedure
tools:
  - '[[Burp Suite]]'
  - '[[curl]]'
tactics:
  - '[[TA0001]]'
commands:
  - '[[curl-execute-dir-command]]'
  - '[[curl-execute-type-command]]'
platforms:
  - Web
techniques:
  - '[[T1190]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 6b892fa1-e1c7-45e1-94c1-eecc1a392a55
created_at: '2025-12-11T06:04:35.093Z'
updated_at: '2025-12-11T06:04:35.093Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Intercept and Modify Avatar Upload Request

## Summary

This procedure uses a proxy tool to intercept the avatar upload HTTP request, allowing modification to bypass file type restrictions.

## Description

By configuring Burp Suite as a proxy, the upload request is captured. This enables editing of the request parameters, such as the filename and content, to upload a malicious ASP file. The vulnerability stems from insufficient validation of file extensions, bypassed by adding a trailing space.

## Requirements

1. Burp Suite installed and configured as proxy
2. Authenticated session on the target site
3. Knowledge of HTTP request structure

## Defense

Defensive measures and detection strategies:

- Implement strict file extension validation and content-type checking
- Monitor for anomalous upload requests via WAF logs

## Objectives

1. Capture the upload request
2. Prepare for filename and content modification
3. Enable bypass of upload restrictions

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept traffic.

Launch Burp Suite and configure your browser to use it as a proxy.

> Ensure interception is enabled.

### Step 2: Intercept Request

**Context**: Trigger and capture the avatar upload.

Initiate an avatar upload and use [[Burp Suite]] to capture and modify the HTTP request for uploading the avatar file.

> The request will appear in the Intercept tab for editing.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0001]]

### Techniques

- [[T1190]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[Burp Suite]]

## Tags

- [[interception]]
- [[file-upload]]
