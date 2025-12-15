---
id: proc-uuid-2
tags:
  - payload-generation
  - encoding
  - xaml
type: procedure
tools:
  - '[[tools/ConsoleApplication1]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cd-to-poc-build]]'
  - '[[commands/consoleapp-encode-payload]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:32.067Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Generate-Encoded-XAML-Payload

## Summary

This procedure builds the PoC encoder and generates a base64-encoded XAML string from the modified t.xml, preparing it for injection into SharePoint's deserialization vulnerability.

## Description

The ConsoleApplication1.exe from the PoC encodes the XAML payload into a format suitable for the hiddenSpanDataValue parameter. This step occurs on a Windows machine after PoC preparation and results in a long string starting with '__' that triggers deserialization and command execution upon injection.

## Requirements

1. PoC repository cloned and t.xml edited
2. Visual Studio or build tools to compile ConsoleApplication1 (if not pre-built)
3. Windows command prompt access

## Defense

Defensive measures and detection strategies:

- Monitor for compilation of unknown executables in temp directories
- Scan for base64-encoded strings in HTTP traffic resembling XAML payloads
- Implement input validation on SharePoint parameters to reject encoded data

## Objectives

1. Compile and run the payload encoder
2. Produce injectable encoded string
3. Enable RCE via deserialization

## Instructions

### Step 1: Navigate to Build Directory

**Context**: Change to the directory containing the compiled ConsoleApplication1.exe.

**Command** ([[commands/cd-to-poc-build]]):
```bash
cd c:\CVE-2019-0604\ConsoleApplication1\ConsoleApplication1\bin\Debug\
```

> This sets the working directory for running the encoder. Expected output: Prompt changes to the Debug folder.

### Step 2: Encode the Payload

**Context**: Run the executable to process t.xml and output the encoded string.

**Command** ([[commands/consoleapp-encode-payload]]):
```bash
ConsoleApplication1.exe c:/CVE-2019-0604/t.xml
```

> The tool reads t.xml and generates the encoded payload. Expected output: Encoded string like __bp4b7135009700370047005600d600e200... printed to console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/cd-to-poc-build]]
- [[commands/consoleapp-encode-payload]]

## Tools Used

- [[tools/ConsoleApplication1]]

## Tags

- payload-generation
- encoding
- xaml
