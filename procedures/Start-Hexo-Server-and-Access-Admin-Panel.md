---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Start-Hexo-Server-and-Access-Admin-Panel
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.043Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - server-start
  - admin-access
  - hexo
commands:
  - '[[commands/hexo-server-deploy]]'
platforms:
  - Web
  - Node.js
tools:
  - '[[tools/HexoJS]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Start-Hexo-Server-and-Access-Admin-Panel

## Summary

This procedure launches the local Hexo development server in deploy mode and navigates to the admin panel, providing access to the vulnerable post editor for XSS exploitation.

## Description

After setup, the Hexo server must be started to host the static site and enable the hexo-admin interface at /admin. The -d flag generates files before serving, ensuring the blog is ready. This step assumes local execution and grants authenticated access to post management, where the lack of sanitization allows XSS injection.

## Requirements

1. Hexo project directory with admin plugin installed
2. Port 4000 available
3. Browser for accessing localhost

## Defense

Defensive measures and detection strategies:

- Restrict admin panel access via IP whitelisting or VPN
- Enable HTTPS and monitor for unauthorized local server startups
- Use firewall rules to block external access to port 4000

## Objectives

1. Activate the Hexo runtime and admin UI
2. Verify server accessibility
3. Position for post creation and injection

## Instructions

### Step 1: Start Development Server

**Context**: Launch Hexo server to serve the site and admin panel locally.

**Command** ([[commands/hexo-server-deploy]]):

```bash
hexo server -d
```

> Starts the server, generates static files if needed, and hosts at http://localhost:4000. Expected output: INFO Server is running at http://localhost:4000.

### Step 2: Navigate to Admin Panel

**Context**: Access the administrative interface for post management.

No command; use browser:

Open http://localhost:4000/admin and log in with configured credentials.

> Loads the dashboard with sections for posts, pages, etc.

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

## Tags

- server-start
- admin-access
- hexo
