---
id: proc-vk-endpoint-discover-001
tags:
  - recon
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:34.020Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-VK-Upload-Endpoint-for-Graffiti

## Summary

This procedure identifies the vulnerable upload endpoint in VK.com used for graffiti uploads, revealing the transport act with callback parameter and eval usage.

## Description

In the context of VK.com's document upload for graffiti, observe the endpoint to uncover the act=transport parameter that handles uploads via iframe, including an eval call on line 25 of the associated JavaScript and a sendData function for POST requests. This step is crucial for spotting the XSS potential in callback handling.

## Requirements

1. Access to VK.com with a valid session
2. Browser developer tools for inspecting network requests
3. Ability to initiate a graffiti upload flow

## Defense

Defensive measures and detection strategies:

- Monitor upload endpoints for unusual parameter patterns
- Implement Content Security Policy (CSP) to restrict eval usage

## Objectives

1. Locate the upload.php?act=transport endpoint
2. Note hash and callback parameters
3. Identify eval and sendData in JS code

## Instructions

### Step 1: Initiate Graffiti Upload

**Context**: Start a graffiti upload in VK.com to trigger the endpoint.

No specific command; inspect network tab in browser dev tools for the request to https://pu.vk.com/c415824/upload.php?act=transport&to_act=add_doc&hash=8dfd93e60c78ddb4a9cf914c27f7642c&rhash=8171a35e59a63aab65846a26345ddbf6&aid=1&mid=17274528&callback=getUploadSvg.

> Expected output: Request details showing callback and hash parameters.

### Step 2: Inspect JavaScript

**Context**: Examine the loaded JS for eval on line 25.

View source or use dev tools to confirm sendData function definition.

> Expected output: Code snippet with eval(parent.{callback}(function() { ... }))

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- endpoint-discovery
