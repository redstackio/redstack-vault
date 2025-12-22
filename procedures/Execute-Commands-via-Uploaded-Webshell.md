---
tags:
  - rce
  - command-execution
  - webshell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/whoami-windows]]'
  - '[[commands/cmd-c-whoami]]'
  - '[[commands/webshell-execute-arbitrary]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:24:08.170Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: cf3205b0-a015-4f70-9733-010b251dd07e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Execute-Commands-via-Uploaded-Webshell

## Summary

This procedure interacts with the uploaded ASPX webshell to execute arbitrary Windows commands, demonstrating RCE by retrieving server user context and running custom payloads.

## Description

The injected webshell uses C# to parse a query parameter (e.g., 68c2c8b1fc47766eaf43027a8eaca121) as a command, executes it via cmd.exe /c, and returns the output in the HTTP response. This confirms control over the IIS-hosted Windows server.

## Requirements

1. Successful webshell upload from prior procedure
2. Direct access to the webshell URL (e.g., /RServer/rdDownload/.../filename.aspx)
3. Browser or curl for querying the endpoint

## Defense

Defensive measures and detection strategies:

- Monitor IIS logs for unusual .aspx requests with query parameters
- Implement runtime application self-protection (RASP) to detect process spawning from web code
- Regularly scan web directories for anomalous .aspx files

## Objectives

1. Verify RCE with a simple command like whoami
2. Execute arbitrary commands to assess server access
3. Capture and analyze output for further exploitation

## Instructions

### Step 1: Test with whoami

**Context**: Confirm RCE by retrieving the current user.

Execute [[commands/whoami-windows]] by accessing the webshell URL with ?68c2c8b1fc47766eaf43027a8eaca121=whoami.

```cmd
whoami
```

> Response body shows the IIS app pool user, e.g., ████████ (redacted).

### Step 2: Run via cmd /c

**Context**: Use non-interactive mode for reliable execution.

Execute [[commands/cmd-c-whoami]] by appending ?68c2c8b1fc47766eaf43027a8eaca121=whoami to the URL.

```cmd
cmd.exe /c whoami
```

> Outputs current user identity without hanging the process.

### Step 3: Arbitrary Command Execution

**Context**: Demonstrate full RCE with custom commands.

Execute [[commands/webshell-execute-arbitrary]] by setting the query param to any command, e.g., ?68c2c8b1fc47766eaf43027a8eaca121=dir.

```cmd
cmd.exe /c dir
```

> Returns directory listing or other output in the HTTP response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques


## Commands Used

- [[commands/whoami-windows]]
- [[commands/cmd-c-whoami]]
- [[commands/webshell-execute-arbitrary]]

## Tools Used


## Tags

- rce
- command-execution
- webshell
