---
tags:
  - xxe
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1f3810b5-cf79-4518-b438-3712b2e7080a
created_at: '2025-12-13T09:00:28.077Z'
updated_at: '2025-12-13T09:00:28.077Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Insert XXE Payload in XML

## Summary

This procedure details editing an XML file within an XLSX archive to inject an XXE payload that references local files, enabling exploitation when parsed.

## Description

By inserting a DOCTYPE declaration with an external entity, the XML parser can be tricked into resolving and disclosing file contents. This targets vulnerabilities where external entities are not disabled, leading to information disclosure on servers like AWS EC2.

## Requirements

1. Opened XLSX as ZIP archive
2. Text editor for XML
3. Knowledge of XXE payload structure

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers
- Use secure XML libraries like those with DTD disabled by default

## Objectives

1. Inject payload to read sensitive files
2. Maintain XLSX integrity
3. Prepare for upload and exploitation

## Instructions

### Step 1: Edit sheet1.xml

**Context**: Insert the malicious entity declaration.

Open xl/worksheets/sheet1.xml and add:

```xml
<!DOCTYPE foo [ <!ELEMENT foo ANY ><!ENTITY xxe PUBLIC "lol" "file:///etc/passwd" >]>
```

> This payload defines an entity that resolves to /etc/passwd contents.

Save and close the file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[payload-injection]]
