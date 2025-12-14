---
tags:
  - setup
  - hexo
  - installation
type: procedure
tools:
  - '[[tools/hexo]]'
  - '[[tools/hexo-admin]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hexo-server-deploy]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.711Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0bec9bbf-f9e0-4ec0-a053-687f19b2c301
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-and-Setup-Hexo-with-Admin-Plugin

## Summary

This procedure sets up a local Hexo static blog environment with the vulnerable hexo-admin plugin, enabling access to the post editor for XSS injection.

## Description

Hexo is a Node.js-based static site generator, and the hexo-admin plugin provides a web-based admin interface for managing posts. In version 3.9.0, this setup exposes the post content field to stored XSS due to missing sanitization. The procedure involves installing dependencies, configuring the plugin, and starting the local server to host the blog at localhost:4000.

## Requirements

1. Node.js and npm installed on the system
2. Git for cloning repositories if needed
3. Local directory for the blog project

## Defense

Defensive measures and detection strategies:

- Update to a patched version of hexo-admin if available
- Implement content security policy (CSP) to block inline scripts
- Monitor for anomalous admin panel access logs

## Objectives

1. Establish a functional Hexo blog instance with admin access
2. Verify server startup and admin panel availability
3. Prepare environment for post creation and exploitation

## Instructions

### Step 1: Install Hexo and Plugin

**Context**: Install the core Hexo generator and the hexo-admin plugin to enable the vulnerable editor.

**Command** ([[commands/hexo-server-deploy]]):
No initial command; use npm for installation.

```bash
npm install hexo-cli -g
hexo init myblog
cd myblog
npm install
npm install hexo-admin --save
```

> Initializes a new Hexo site, installs dependencies, and adds the admin plugin to _config.yml.

### Step 2: Start Development Server

**Context**: Launch the local server to access the admin interface.

**Command** ([[commands/hexo-server-deploy]]):

```bash
hexo server -d
```

> Starts the server in deploy mode, generating and serving static files at http://localhost:4000.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/hexo-server-deploy]]

## Tools Used

- [[tools/hexo]]
- [[tools/hexo-admin]]

## Tags

- setup
- hexo
- node.js
