---
id: proc-wordpress-escalate-compromise
tags:
  - wordpress
  - privilege-escalation
  - shell-upload
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-shell-access]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:28:36.646Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Remote File Copy]]'
---
# Escalate-WordPress-Access-to-Server-Compromise

## Summary

This procedure details logging into a compromised WordPress admin account to upload malicious files (e.g., PHP shells via plugins/themes), gaining remote code execution (RCE) and full server control, including subdomains.

## Description

With admin access, attackers exploit WordPress's file upload features to inject webshells. Target: WordPress on shared hosting. Outcomes: Arbitrary command execution, data exfiltration, and lateral movement to other sites on the server.

## Requirements

1. Valid admin credentials for WordPress dashboard
2. Basic PHP knowledge for shell creation
3. Browser or curl for shell interaction post-upload

## Defense

Defensive measures and detection strategies:

- Restrict file uploads to vetted plugins/themes only
- Use web application firewalls (WAF) to scan uploads for malicious code
- Monitor file changes in wp-content and server logs for anomalous executions

## Objectives

1. Achieve RCE on the web server
2. Pivot to subdomains and full server access
3. Maintain persistence via backdoors

## Instructions

### Step 1: Upload Malicious Payload

**Context**: Access the dashboard, go to Appearance > Theme Editor or Plugins > Add New, and upload a ZIP with a shell.php file.

**Command** (N/A - Manual UI):
Upload and activate, then note the URL like /wp-content/themes/malicious/shell.php.

> Successful upload allows activation without errors.

### Step 2: Interact with Shell

**Context**: Use curl or browser to execute commands via the shell.

**Command** ([[commands/curl-shell-access]]):
```bash
curl "https://nextcloud.com/wp-content/themes/malicious/shell.php?cmd=id"
```

> Output shows server user (e.g., "uid=33(www-data)"). Escalate by running further commands like ls / to explore.

### Step 3: Pivot to Subdomains

**Context**: From the shell, scan and access other virtual hosts.

**Command** ([[commands/curl-shell-access]]):
```bash
curl "https://nextcloud.com/wp-content/themes/malicious/shell.php?cmd=cat /etc/hosts"
```

> Reveals subdomains; use to upload shells elsewhere.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (PHP equivalent for web)
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

- N/A

## Commands Used

- [[commands/curl-shell-access]]

## Tools Used

- N/A

## Tags

- [[rce]]
- [[shell-upload]]
- [[privilege-escalation]]
