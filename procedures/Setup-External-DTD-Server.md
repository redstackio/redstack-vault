---
tags:
  - xxe
  - server-setup
type: procedure
tools:
  - '[[tools/Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: d9add44c-d600-4661-bb26-5e0d37182c79
created_at: '2025-12-13T09:00:27.985Z'
updated_at: '2025-12-13T09:00:27.985Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup External DTD Server

## Summary

This procedure sets up an attacker's web server to host an external DTD file required for XXE exploitation, allowing the payload to load and exfiltrate data.

## Description

Hosting the xxe.dtd file on a controlled web server enables the XXE vulnerability to reference external entities, facilitating attacks like file reading or SSRF in the target WordPress installation.

## Requirements

1. Web server software (e.g., Apache or Nginx)
2. xxe.dtd file from PoC
3. Server reachable from target

## Defense

Defensive measures and detection strategies:

- Block outbound requests to unknown servers
- Monitor server logs for suspicious DTD requests

## Objectives

1. Host DTD file accessibly
2. Ensure reachability for exploitation

## Instructions

### Step 1: Place DTD File

**Context**: Position the file at server root.

Copy xxe.dtd to the root directory of [[tools/Web-Server]].

> Makes it available for the XXE payload to fetch.

### Step 2: Verify Accessibility

**Context**: Test if the file can be retrieved.

Access the DTD via a browser or curl from another machine.

> Confirms setup before proceeding to upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Server]]

## Tags

- xxe
- server-setup
