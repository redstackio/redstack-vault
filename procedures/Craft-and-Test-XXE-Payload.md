---
tags:
  - xxe
  - payload-crafting
type: procedure
tools:
  - '[[tools/oxml-xxe]]'
  - '[[tools/EXIFTool]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-upload-image]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c7fef49f-1914-40a1-952c-cc66a543d3d0
created_at: '2025-12-13T09:00:33.716Z'
updated_at: '2025-12-13T09:00:33.716Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Test XXE Payload

## Summary

Manually craft XXE payloads in image metadata for reliable testing.

## Description

Using tools like oxml_xxe and EXIFTool, forge JPEG files with custom DTD references and test against the endpoint.

## Requirements

1. Image manipulation tools
2. Collaborator IDs

## Defense

- Validate and sanitize metadata
- Disable XML parsing for uploads

## Objectives

1. Achieve successful payload execution
2. Overcome initial failures

## Instructions

### Step 1: Forge Payload

**Context**: Create custom JPEG.

**Command** ([[commands/post-upload-image]]):
```bash
POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
Host: target.com
```

> Upload after crafting with EXIFTool or oxml_xxe.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/post-upload-image]]

## Tools Used

- [[tools/oxml-xxe]]
- [[tools/EXIFTool]]

## Tags

- [[xxe]]
- [[payload-crafting]]
