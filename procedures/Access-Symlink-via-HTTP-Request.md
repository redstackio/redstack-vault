---
id: proc-uuid-004
tags:
  - path-traversal
  - http
  - file-read
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-symlink]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:26:17.378Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Access-Symlink-via-HTTP-Request

## Summary

This procedure sends an HTTP request to the symlink path, exploiting the server's lack of validation to read and retrieve sensitive file contents.

## Description

The statics-server follows symlinks without restrictions, allowing path traversal. Using curl to request the symlink URL results in the target file's contents being served directly.

## Requirements

1. Running statics-server on localhost:8080
2. Symlink present in served directory
3. curl installed

## Defense

Defensive measures and detection strategies:

- Implement symlink resolution checks in servers
- Log and monitor HTTP requests for suspicious paths
- Use WAF rules to block traversal patterns

## Objectives

1. Retrieve arbitrary file contents
2. Confirm vulnerability exploitation
3. Exfiltrate sensitive data like user accounts

## Instructions

### Step 1: Request the Symlink

**Context**: Fetch the file via the server's HTTP endpoint.

**Command** ([[commands/curl-access-symlink]]):
```bash
curl localhost:8080/passwdsym
```

> Sends GET to the symlink path. Expected output: /etc/passwd contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Sub-Techniques


## Commands Used

- [[commands/curl-access-symlink]]

## Tools Used

- [[tools/curl]]

## Tags

- path-traversal
- http
- file-read
