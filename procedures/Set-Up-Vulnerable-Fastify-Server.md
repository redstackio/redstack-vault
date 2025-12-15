---
id: uuid-setup-server
tags:
  - setup
  - fastify
  - node.js
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/bash-run-sh]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:36.810Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Vulnerable-Fastify-Server

## Summary

This procedure sets up a local Fastify server using the vulnerable fastify-static plugin mounted at the root with { redirect: true }, enabling reproduction of the DoS and open redirect vulnerabilities.

## Description

The fastify-static plugin serves static files in a Fastify application. When mounted at '/' with redirect enabled, it processes req.raw.url directly in the Node.js URL constructor at index.js line 439, leading to crashes on invalid inputs. This setup requires downloading the provided vulnerable code and running the initialization script on a local Node.js environment.

## Requirements

1. Node.js installed (version compatible with Fastify, e.g., v14+).
2. Access to download fastify-dos.zip containing the vulnerable code.
3. Local port 3000 available.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all URL inputs before passing to Node.js URL API.
- Implement global error handling with try/catch around URL parsing.
- Monitor server logs for TypeError exceptions and unusual crash patterns.

## Objectives

1. Replicate the exact vulnerable configuration for testing.
2. Verify server startup without errors.
3. Prepare environment for DoS and redirect exploitation.

## Instructions

### Step 1: Download and Extract Vulnerable Code

**Context**: Obtain the source code from the attachment to ensure the exact vulnerable setup.

**Command** ([[commands/bash-run-sh]]):
```bash
# Assume fastify-dos.zip is downloaded and extracted
cd fastify-dos
```

> Extract the zip file manually or via unzip command, then navigate to the directory.

### Step 2: Start the Server

**Context**: Run the setup script to launch Fastify with fastify-static mounted vulnerably.

**Command** ([[commands/bash-run-sh]]):
```bash
bash run.sh
```

> This installs dependencies if needed and starts the server on http://localhost:3000. Expected output: "Server running on http://localhost:3000".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/bash-run-sh]]

## Tools Used

- [[tools/curl]]

## Tags

- setup
- fastify
- node.js
