---
tags:
  - admin-access
  - post-creation
type: procedure
tools:
  - '[[tools/hexo-admin]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.709Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d5832a2-38e0-4515-8cce-5121e1d7bbad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Admin-Panel-and-Create-Post

## Summary

This procedure navigates the hexo-admin interface to create a new blog post, positioning the attacker to target the vulnerable content field.

## Description

The hexo-admin plugin exposes a web UI at /admin for post management. Accessing this allows creation of new posts where the content is not sanitized, leading to stored XSS. No authentication is enforced by default in local setups, making it straightforward for an insider or compromised admin.

## Requirements

1. Running Hexo server on localhost:4000
2. Browser access to the local network
3. No prior credentials needed in default config

## Defense

Defensive measures and detection strategies:

- Enable authentication in hexo-admin config
- Restrict admin panel to authenticated users only
- Log all admin actions for anomaly detection

## Objectives

1. Load the admin dashboard successfully
2. Navigate to posts and initiate new post creation
3. Set up post metadata like title for the exploit

## Instructions

### Step 1: Navigate to Admin Panel

**Context**: Access the web-based admin interface provided by the plugin.

No command; browser action.

> Open http://localhost:4000/admin in a web browser. The dashboard should load with navigation options.

### Step 2: Create New Post

**Context**: Enter the posts section to start editing a new entry.

No command; UI interaction.

> Click 'Posts' in the sidebar, then 'New Post'. Set the title to 'Test XSS here' and proceed to the content editor.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/hexo-admin]]

## Tags

- web-ui
- post-management
