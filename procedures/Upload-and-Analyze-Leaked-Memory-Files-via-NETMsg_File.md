---
id: proc-3
tags:
  - csgo
  - memory-leak
  - upload
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[LSASS Memory]]'
updated_at: '2025-12-14T17:23:54.627Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[LSASS Memory]]'
---
# Upload-and-Analyze-Leaked-Memory-Files-via-NETMsg_File

## Summary

This procedure requests the client to upload the leaked memory files to the server using NETMsg_File, allowing analysis for ASLR-breaking pointers.

## Description

After downloads, the server sends a NETMsg_File message to request file uploads. The client packages and sends the files containing uninitialized heap data, which the server receives and stores for parsing.

## Requirements

1. Active client connection from prior step
2. Server script handling NETMsg_File reception

## Defense

- Disable or validate file upload messages in client
- Encrypt or hash uploaded content
- Monitor for unexpected file transfers

## Objectives

1. Retrieve leaked heap contents
2. Prepare data for pattern-based analysis
3. Identify mixed sprayed objects

## Instructions

### Step 1: Request File Upload

**Context**: Server automatically sends NETMsg_File post-download to fetch leaked files.

No manual command; handled by poc.py script.

> Server logs incoming files. Expected output: Binary files received, e.g., 'leaked_file.bin' with 1337 bytes of heap data.

### Step 2: Initial Analysis

**Context**: Scan received files for known patterns from prior sprays.

Use Python to hexdump or grep for unique values like 0x1337ee00.

**Expected Output**: Patterns detected in leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[LSASS Memory]] OS Credential Dumping

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Python]]

## Tags

- csgo
- memory-leak
- upload
