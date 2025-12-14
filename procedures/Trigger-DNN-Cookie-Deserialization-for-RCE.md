---
id: proc-005
tags:
  - deserialization
  - rce
  - reverse-shell
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:23:49.733Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
---
# Trigger-DNN-Cookie-Deserialization-for-RCE

## Summary

This procedure sends the RCE payload in the DNNPersonalization cookie to execute the reverse shell command on the target server.

## Description

Similar to file read trigger, but with base64-encoded XML for process execution. Deserialization invokes the PowerShell command, downloading and running the reverse shell to connect to the listener.

## Requirements

1. Base64 XML payload from RCE generation
2. Active netcat listener on port 7575
3. Target reachable via HTTP

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all incoming cookies
- Monitor for process creation of powershell.exe with network activity
- Implement EDR for anomalous deserialization attempts

## Objectives

1. Execute arbitrary command via deserialization
2. Establish reverse shell
3. Gain interactive access

## Instructions

### Step 1: Send RCE Request

**Context**: Use the base64 payload to start the process.

**Command** (curl-send-rce-cookie):
```bash
curl -H "Cookie: DNNPersonalization=<BASE64_XML>" http://lonidoor.mtn.ci/__
```

> Replace <BASE64_XML>; success if shell connects to listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[PowerShell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- deserialization
- web-exploit
