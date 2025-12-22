---
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:28.589263+00:00'
updated_at: '2023-04-10T20:37:36.294286+00:00'
platforms:
  - Windows
tags:
  - discovery
  - architecture
validated: true
---

# cmd-os-architecture-discovery-with-fallback

## Code

```cmd
wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE%
```

## Description

This code snippet queries the OS architecture using WMIC, with a fallback to the PROCESSOR_ARCHITECTURE environment variable if WMIC is unavailable or fails. It provides reliable bitness information (32-bit or 64-bit) for selecting compatible exploits in privilege escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables to substitute | N/A |

## Usage

Execute in Command Prompt during system reconnaissance to determine architecture. Use the output to choose 32-bit vs. 64-bit payloads or check for WoW64-related escalation paths.

## Detection

- Monitor for WMIC.exe executions in process creation logs (Event ID 4688).
- Environment variable access via echo commands may appear in command-line auditing.
- PowerShell transcription if run in hybrid environments.

## Related

- [[procedures/windows-os-information-gathering-for-privilege-escalation]]
