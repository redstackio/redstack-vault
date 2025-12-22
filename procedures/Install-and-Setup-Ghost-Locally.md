---
tags:
  - setup
  - ghost-cms
  - local-deployment
type: procedure
tools:
  - '[[tools/ghost-cli]]'
tactics: []
commands:
  - '[[commands/ghost-install-local]]'
  - '[[commands/ghost-stop]]'
platforms:
  - Node.js
  - Web
techniques: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 05cb7fb1-03d5-466d-8c88-a4d4315fa0c1
created_at: '2025-12-14T04:39:09.670Z'
updated_at: '2025-12-14T04:39:09.670Z'
verified: false
validated: true
submitted: true
---
# Install-and-Setup-Ghost-Locally

## Summary

This procedure deploys a local Ghost CMS instance using Ghost CLI, setting up a SQLite database and starting the server to replicate the vulnerable environment for SSRF testing.

## Description

The local installation mode creates a development setup of Ghost, ideal for testing vulnerabilities like the oEmbed SSRF bypass. It prompts for configuration details such as database type and URL, defaulting to SQLite and http://localhost:2368. This allows authenticated access to the admin API without production risks.

## Requirements

1. Ghost CLI installed globally
2. Free port 2368 available
3. Local file system write permissions for database

## Defense

Defensive measures and detection strategies:

- Restrict local installations in production-like environments
- Monitor for unexpected Ghost processes on servers

## Objectives

1. Create a running Ghost instance with vulnerable oEmbed endpoint
2. Prepare for admin authentication
3. Enable SSRF exploitation testing

## Instructions

### Step 1: Run Local Install

**Context**: Initiate the local Ghost setup, which handles database creation and server startup.

**Command** ([[commands/ghost-install-local]]):
```bash
ghost install local
```

> Follow interactive prompts: select SQLite, set URL to http://localhost:2368. Expected output: Setup completion and server start message with admin URL.

### Step 2: Stop and Restart if Needed

**Context**: If the server needs restarting post-setup, stop it cleanly.

**Command** ([[commands/ghost-stop]]):
```bash
ghost stop
```

> Expected output: Confirmation of server shutdown. Restart with `ghost start local` if required.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used

- [[commands/ghost-install-local]]
- [[commands/ghost-stop]]

## Tools Used

- [[tools/ghost-cli]]

## Tags

- [[setup]]
- [[ghost-cms]]
- [[local-deployment]]
