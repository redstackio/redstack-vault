---
id: proc-download-poc-001
tags:
  - poc-download
  - fastify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.272Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download-Fastify-Static-PoC-Archive

## Summary

This procedure downloads the proof-of-concept archive for the fastify-static open redirect vulnerability, providing the necessary files to set up and reproduce the exploit locally.

## Description

The fastify-static plugin vulnerability arises from improper path normalization in index.js lines 156-157, allowing // prefixed paths to craft scheme-relative redirects. Downloading the PoC enables local testing of this issue, which can lead to phishing or SSRF bypass, particularly in Firefox due to its handling of 301 redirects with // locations.

## Requirements

1. Internet access to download the archive
2. Local directory for extraction
3. Unzip utility (built-in on most systems)

## Defense

Defensive measures and detection strategies:

- Validate and normalize all user-supplied paths in static file plugins
- Disable automatic redirects or enforce absolute URLs with scheme validation
- Monitor for unusual 301 redirects in server logs

## Objectives

1. Acquire PoC files for vulnerability reproduction
2. Prepare environment for server setup
3. Enable testing of redirect exploitation

## Instructions

### Step 1: Download the Archive

**Context**: Fetch the ZIP file containing the vulnerable Fastify setup, including index.js with redirect: true and the run.sh script.

No command required; use browser or wget/curl to download fastify-static-poc.zip from the source (e.g., HackerOne report attachments).

> Manually download and save the file. Expected output: ZIP file in downloads folder.

### Step 2: Extract the Archive

**Context**: Unpack the files to access the PoC server code.

```bash
unzip fastify-static-poc.zip
```

> Extracts files like server.js, run.sh, and package.json. Expected output: Directory with PoC contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc-download]]
- [[fastify]]
