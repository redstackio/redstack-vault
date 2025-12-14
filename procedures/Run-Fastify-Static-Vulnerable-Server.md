---
id: proc-run-server-001
tags:
  - server-setup
  - fastify
  - poc
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/run-fastify-static-poc]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.267Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Run-Fastify-Static-Vulnerable-Server

## Summary

This procedure launches a local Fastify server configured with the vulnerable fastify-static plugin mounted at root and redirect option set to true, reproducing the open redirect flaw for testing.

## Description

The vulnerability occurs when fastify-static mishandles paths like //google.com/%2e%2e, failing to normalize them and issuing a 301 redirect to an arbitrary site. This setup mirrors the reported issue in index.js lines 156-157, allowing exploitation for phishing or bypassing SSRF protections in OAuth flows.

## Requirements

1. Node.js installed (v14+ recommended)
2. Extracted PoC archive with run.sh
3. Port 3000 available

## Defense

Defensive measures and detection strategies:

- Set redirect: false in fastify-static or use a custom handler with path validation
- Implement URL parsing to block scheme-relative or external redirects
- Log all redirect attempts and alert on // prefixed paths

## Objectives

1. Initialize vulnerable server instance
2. Expose the open redirect endpoint
3. Verify server readiness for exploitation

## Instructions

### Step 1: Navigate to PoC Directory

**Context**: Change to the extracted PoC folder to access the setup files.

```bash
cd fastify-static-poc
```

> Prepares environment. Expected output: Prompt in PoC directory.

### Step 2: Execute Startup Script

**Context**: Run the bash script to install dependencies and start the server with vulnerable config.

**Command** ([[commands/run-fastify-static-poc]]):
```bash
bash run.sh
```

> Installs Fastify and fastify-static via npm, then launches server on port 3000 with static files served from root and redirect enabled. Expected output: "Server listening on http://localhost:3000".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/run-fastify-static-poc]]

## Tools Used


## Tags

- [[server-setup]]
- [[fastify]]
- [[poc]]
