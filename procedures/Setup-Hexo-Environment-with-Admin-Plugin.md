---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Setup-Hexo-Environment-with-Admin-Plugin
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.049Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - setup
  - hexo
  - node.js
commands:
  - '[[commands/hexo-server-deploy]]'
platforms:
  - Node.js
tools:
  - '[[tools/HexoJS]]'
  - '[[tools/Hexo-Admin]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Setup-Hexo-Environment-with-Admin-Plugin

## Summary

This procedure installs the Hexo static site generator and the vulnerable hexo-admin plugin version 3.9.0, setting up a local environment to demonstrate the stored XSS vulnerability in the post editor.

## Description

Hexo is a Node.js-based static blog framework, and hexo-admin provides an administrative UI for managing posts. The setup involves initializing a Hexo project and adding the plugin via npm from its GitHub repository. This environment allows authenticated access to the post creation interface where XSS can be injected without sanitization, persisting scripts in generated HTML. Prerequisites include Node.js and npm installed on the system.

## Requirements

1. Node.js (version 14 or higher) and npm installed
2. Git for cloning repositories if needed
3. Local directory for the Hexo project

## Defense

Defensive measures and detection strategies:

- Use updated versions of hexo-admin (post-3.9.0) with input sanitization
- Implement Content Security Policy (CSP) on the blog to block inline scripts
- Monitor admin panel logs for suspicious post content injections

## Objectives

1. Establish a reproducible local Hexo setup with the vulnerable plugin
2. Prepare for server startup and admin access
3. Enable testing of post editor without external dependencies

## Instructions

### Step 1: Initialize Hexo Project

**Context**: Create a new Hexo site directory and install core dependencies.

**Command** ([[commands/hexo-init]]):
No specific command; use npm to init.

```bash
npm init -y
npm install hexo-cli -g
hexo init myblog
cd myblog
npm install
```

> Initializes the Hexo project structure with source files and themes.

### Step 2: Install Hexo-Admin Plugin

**Context**: Add the vulnerable admin plugin to enable the post editor interface.

**Command** (npm install):

```bash
npm install hexo-admin@3.9.0 --save
```

> Installs version 3.9.0 from npm or GitHub, configuring it in _config.yml if needed.

### Step 3: Configure Admin Access

**Context**: Set up basic authentication for the admin panel in the Hexo config.

No command; edit _config.yml:

```yaml
admin:
  username: admin
  password: password
```

> Enables login to /admin route upon server start.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/hexo-server-deploy]]

## Tools Used

- [[tools/HexoJS]]
- [[tools/Hexo-Admin]]

## Tags

- setup
- hexo
- node.js
