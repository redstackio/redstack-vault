---
id: proc-uuid-4
tags:
  - content-spoofing
  - mime-type-manipulation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
updated_at: '2025-12-13T23:55:20.715Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Perform-Content-Spoofing-with-Extensions

## Summary

This procedure manipulates URL extensions in requests to spoof response MIME types, tricking browsers into downloading or executing reflected content as malicious files like XML, SWF, or EXE.

## Description

The server bases response content types on URL extensions without validation, reflecting request data accordingly. By using paths like /malicious.xml or /exploit.exe in GET/POST, attackers can force MIME spoofing (e.g., application/xml), leading to unintended browser handling and potential code execution on download.

## Requirements

1. Access to send custom requests (e.g., via curl or Burp)
2. Target endpoint echo.urbandictionary.biz
3. Knowledge of exploitable extensions

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type validation independent of URL extensions
- Use Content-Type headers explicitly and ignore extension inferences
- Scan for anomalous extension usage in logs

## Objectives

1. Spoof MIME for malicious file delivery
2. Induce browser download/execution
3. Demonstrate content type bypass

## Instructions

### Step 1: Craft Request with Extension

**Context**: Send GET/POST to path with spoofed extension.

**Instructions**: Use curl to test .xml extension.

```bash
curl -X POST https://echo.urbandictionary.biz/malicious.xml -d '<malicious>payload</malicious>'
```

> Response MIME: application/xml; browser may parse as XML, enabling XXE if chained.

### Step 2: Test Execution Extensions

**Context**: Try .swf or .exe for binary spoofing.

**Instructions**: Modify path to .exe.

```bash
curl -X GET https://echo.urbandictionary.biz/exploit.exe
```

> Browser prompts download as executable, risking user execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Malicious File]] User Execution: Malicious File

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[spoofing]]
- [[download]]
