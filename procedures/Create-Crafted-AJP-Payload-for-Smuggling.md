---
tags:
  - payload-crafting
  - ajp
  - smuggling
type: procedure
tools:
  - '[[tools/xxd]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/xxd-dump-payload]]'
platforms:
  - Linux
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2687f05b-05d4-449b-bdc7-0da313b33fbb
created_at: '2025-12-13T09:01:21.828Z'
updated_at: '2025-12-13T09:01:21.828Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Crafted AJP Payload for Smuggling

## Summary
This procedure creates a binary payload file for exploiting HTTP Request Smuggling in mod_proxy_ajp, including AJP attributes to set request paths for file disclosure.

## Description
The payload (e.g., data2) contains crafted AJP request data, such as setting javax.servlet.include.path_info to /WEB-INF/web.xml, allowing smuggling to read internal files when sent to the vulnerable server.

## Requirements
1. Binary editor or tool to generate AJP protocol data
2. Knowledge of AJP packet structure
3. File system access to create and view the payload

## Defense
Defensive measures and detection strategies:
- Disable or restrict mod_proxy_ajp if not needed
- Use web application firewalls to detect malformed requests

## Objectives
1. Generate a valid AJP smuggling payload
2. Verify payload contents via hex dump
3. Prepare for exploitation in subsequent steps

## Instructions

### Step 1: Generate Payload File
**Context**: Create the binary file 'data2' with AJP data including smuggling attributes.

Manually craft or use a script to generate the binary content.

### Step 2: Verify Payload
**Context**: Display the hex dump to confirm the payload structure.

**Command** ([[commands/xxd-dump-payload]]):
```bash
xxd data2
```

> This shows the hexadecimal representation, including AJP protocol and attributes like path_info=/WEB-INF/web.xml.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/xxd-dump-payload]]

## Tools Used
- [[tools/xxd]]

## Tags
- payload-crafting
- ajp
- smuggling
