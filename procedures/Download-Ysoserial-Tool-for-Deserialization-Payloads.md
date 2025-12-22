---
id: proc-uuid-001
tags:
  - rce
  - java-deserialization
  - tool-download
type: procedure
tools:
  - '[[tools/Ysoserial]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/wget-download-ysoserial]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:31.138Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download-Ysoserial-Tool-for-Deserialization-Payloads

## Summary

This procedure downloads the ysoserial JAR file from a GitHub repository, which is essential for generating serialized Java payloads used in deserialization exploits like CVE-2021-35464 in ForgeRock OpenAM.

## Description

Ysoserial is a proof-of-concept tool for generating payloads that exploit unsafe Java deserialization vulnerabilities. In the context of attacking ForgeRock OpenAM, it is used to create gadget chains (e.g., Click1) that lead to remote code execution when deserialized by the Jato framework. This step requires internet access and a Linux environment with wget installed. The download fetches a specific version compatible with the exploit.

## Requirements

1. Linux environment with wget and Java installed
2. Internet access to GitHub
3. No target access needed for this preparatory step

## Defense

Defensive measures and detection strategies:

- Monitor outbound network traffic for downloads from GitHub repositories known for exploit tools
- Implement application whitelisting to block unauthorized JAR executions
- Use endpoint detection to flag suspicious wget or curl commands downloading .jar files

## Objectives

1. Obtain ysoserial tool for payload generation
2. Prepare environment for deserialization exploit
3. Enable creation of RCE payloads targeting OpenAM

## Instructions

### Step 1: Fetch Ysoserial JAR

**Context**: Download the tool using wget to retrieve the JAR file directly from the repository.

**Command** ([[commands/wget-download-ysoserial]]):
```bash
wget https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

> This command downloads the ysoserial-0.0.6-SNAPSHOT-all.jar file. Expected output is a progress bar showing the download, followed by the file saved in the current directory. Verify with `ls -la ysoserial-0.0.6-SNAPSHOT-all.jar` to confirm the file exists and has the correct size.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/wget-download-ysoserial]]

## Tools Used

- [[tools/Ysoserial]]

## Tags

- rce
- java-deserialization
