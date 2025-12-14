---
tags:
  - setup
  - ghost-cms
type: procedure
tools:
  - '[[tools/ghost-cli]]'
tactics: []
commands:
  - '[[commands/npm-install-ghost-cli]]'
platforms:
  - Node.js
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c7b64b86-9684-445c-ab06-68f26322e4af
created_at: '2025-12-14T04:39:09.674Z'
updated_at: '2025-12-14T04:39:09.674Z'
verified: false
validated: true
submitted: true
---
# Install-Ghost-CLI-Globally

## Summary

This procedure installs the Ghost CLI tool globally using npm, enabling local management and installation of Ghost CMS instances for vulnerability testing.

## Description

Ghost CLI is the official command-line interface for deploying and configuring Ghost blogging platform. In this attack scenario, it's used to set up a vulnerable local instance to test the SSRF bypass in the oEmbed endpoint. The installation requires Node.js and npm; once installed, it allows running `ghost` commands for local setups without affecting production environments.

## Requirements

1. Node.js (v14+) and npm installed on the system
2. Internet access for package download
3. Administrative privileges for global npm install

## Defense

Defensive measures and detection strategies:

- Monitor npm global installations for unauthorized tools
- Use containerized environments to isolate testing setups

## Objectives

1. Prepare the environment for Ghost CMS deployment
2. Enable local instance management
3. Ensure reproducibility of the vulnerable setup

## Instructions

### Step 1: Install Ghost CLI

**Context**: Globally install the latest version of Ghost CLI to access Ghost management commands.

**Command** ([[commands/npm-install-ghost-cli]]):
```bash
npm install ghost-cli@latest -g
```

> This command downloads and installs the ghost-cli package globally. Expected output includes progress logs and a success message like "+ ghost-cli@1.x.x added". Verify by running `ghost --version`.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used

- [[commands/npm-install-ghost-cli]]

## Tools Used

- [[tools/ghost-cli]]

## Tags

- [[setup]]
- [[ghost-cms]]
