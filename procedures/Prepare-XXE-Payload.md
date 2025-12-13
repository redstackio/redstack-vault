---
tags:
  - xxe
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/craft-xxe-xml-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 119b0436-bcf0-4fd0-a7fa-a893fa866fa5
created_at: '2025-12-13T09:00:27.834Z'
updated_at: '2025-12-13T09:00:27.834Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare XXE Payload

## Summary

This procedure involves crafting a malicious XML payload designed to exploit XML External Entity (XXE) vulnerabilities by injecting external entity references that can lead to file disclosure, SSRF, or DoS attacks.

## Description

In this procedure, an attacker creates an XML file with a DOCTYPE declaration that defines an external entity. When processed by a vulnerable XML parser, this entity is expanded, potentially disclosing sensitive files or making unauthorized requests. This is particularly effective in file upload features that parse uploaded XML without disabling external entities. The target environment is a web application handling XML uploads, with expected outcomes including data exfiltration.

## Requirements

1. Access to a text editor or command line for file creation
2. Knowledge of the target's XML processing behavior
3. No special tools required beyond basic utilities

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set XMLResolver to null in Java)
- Monitor for unusual file access patterns or outbound requests in server logs

## Objectives

1. Create a payload that triggers XXE expansion
2. Prepare for upload to exploit the vulnerability
3. Achieve potential disclosure of sensitive information

## Instructions

### Step 1: Craft the XML Payload

**Context**: Generate an XML file with an external entity referencing a sensitive local file.

**Command** ([[commands/craft-xxe-xml-payload]]):

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' > malicious.xml
```

> This command creates an XML file that attempts to read and include the contents of /etc/passwd when parsed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/craft-xxe-xml-payload]]

## Tools Used



## Tags

- [[xxe]]
- [[payload-crafting]]
