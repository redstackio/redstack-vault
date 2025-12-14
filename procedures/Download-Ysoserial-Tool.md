---
tags:
  - tool-download
  - ysoserial
type: procedure
tools:
  - '[[tools/ysoserial]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/wget-ysoserial-download]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:31:18.983Z'
sub_techniques: []
id: 925d50cd-7671-48b3-8225-e11731f89742
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Download-Ysoserial-Tool

## Summary

This procedure downloads the ysoserial JAR file, a tool essential for generating Java deserialization payloads used in exploiting unsafe deserialization vulnerabilities like CVE-2021-35464 in ForgeRock OpenAM.

## Description

Ysoserial is a proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization. In the context of attacking ForgeRock OpenAM, it is used to create gadget chains that lead to remote code execution. This step ensures the attacker has the necessary tool before proceeding to payload generation. The download is from a GitHub repository fork optimized for certain gadgets like Click1.

## Requirements

1. Internet access to GitHub
2. wget or equivalent download tool installed
3. Linux/Unix-like environment for command execution

## Defense

Defensive measures and detection strategies:

- Monitor outbound network traffic for downloads from GitHub repositories related to security tools
- Implement application whitelisting to prevent execution of unsigned JAR files
- Use endpoint detection to flag unusual Java executions

## Objectives

1. Acquire ysoserial for subsequent payload creation
2. Prepare environment for deserialization exploit
3. Ensure tool integrity before use

## Instructions

### Step 1: Fetch Ysoserial JAR

**Context**: Download the specific version of ysoserial that supports the Click1 gadget chain needed for the OpenAM exploit.

**Command** ([[commands/wget-ysoserial-download]]):
```bash
wget https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

> This command uses wget to retrieve the JAR file directly from the GitHub blob URL. Expected output is the file saved locally; verify with `ls -la ysoserial-0.0.6-SNAPSHOT-all.jar` to confirm size and permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/wget-ysoserial-download]]

## Tools Used

- [[tools/ysoserial]]

## Tags

- tool-download
- ysoserial
