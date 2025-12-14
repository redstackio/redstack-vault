---
id: 32391dbb-5187-42b6-8afe-14f605b6c412
name: Trigger-Path-Traversal-with-curl-on-IPFS-URL
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.043Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - path-traversal
  - curl-trigger
  - data-leak
commands:
  - '[[commands/curl-trigger-ipfs-vuln]]'
platforms:
  - Linux
tools:
  - '[[tools/curl]]'
  - '[[tools/grep]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---

# Trigger-Path-Traversal-with-curl-on-IPFS-URL

## Summary

This procedure executes curl on a dummy IPFS URL with verbose output, capturing the path traversal-induced file leak in DNS host resolution errors.

## Description

With IPFS_PATH set, curl attempts to resolve the IPFS CID by reading from the 'gateway' symlink, leading to traversal and file content insertion into a generated DNS query. The grep filters the error to reveal the leak. Targets Linux with curl 7.81.0+ IPFS support.

## Requirements

1. IPFS_PATH exported to exploit dir
2. Symlink setup complete
3. curl installed with IPFS protocol support

## Defense

Defensive measures and detection strategies:

- Patch curl to versions without this vuln or disable IPFS support
- Log curl invocations and inspect verbose outputs for anomalies
- Network monitoring for invalid DNS queries with file-like hostnames

## Objectives

1. Force curl to read and leak arbitrary file content
2. Capture evidence of successful traversal in error logs
3. Demonstrate impact on sensitive data exposure

## Instructions

### Step 1: Run curl and Grep Output

**Context**: Trigger the vuln by fetching a non-existent IPFS CID, redirecting stderr to capture the host error containing leaked data.

**Command** ([[commands/curl-trigger-ipfs-vuln]]):
```bash
curl -v ipfs://dummycid 2>&1 | grep -A1 "Could not resolve host"
```

> Verbose curl on dummy URL; grep shows the error line and next. Expected output: "Could not resolve host: [leaked content].invalid".

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-ipfs-vuln]]

## Tools Used

- [[tools/curl]]
- [[tools/grep]]

## Tags

- [[path-traversal]]
- [[curl-trigger]]
- [[data-leak]]
