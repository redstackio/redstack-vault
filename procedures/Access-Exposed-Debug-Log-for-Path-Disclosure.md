---
id: proc-uuid-123
tags:
  - information-disclosure
  - debug-log
  - path-disclosure
  - web-recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.734Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access Exposed Debug Log for Path Disclosure

## Summary

This procedure exploits an exposed debug.log file on a web server, such as the Nextcloud website, to disclose sensitive server directory paths without authentication. It enables attackers to map the internal file structure for reconnaissance, potentially leading to path traversal or file inclusion attacks.

## Description

The attack targets misconfigured web servers where debug logging is enabled in production and sensitive log files are placed in publicly accessible directories (e.g., /wp-content/). By directly accessing the file via its URL, an attacker can view log entries containing full server paths, revealing details like web root locations, configuration files, and absolute file system paths. This information disclosure vulnerability stems from inadequate access controls and failure to restrict debug features in live environments. The procedure assumes a public-facing web application built on PHP/WordPress, as seen in the Nextcloud demo site.

## Requirements

1. Web browser with internet access
2. Knowledge of the target URL (e.g., https://nextcloud.com/wp-content/debug.log)
3. No special privileges or tools required

## Defense

Defensive measures and detection strategies:

- Implement strict access controls (e.g., .htaccess deny rules) on log and debug files in web directories.
- Disable debug logging in production environments and rotate/secure logs properly.
- Use web application firewalls (WAF) to block direct access to sensitive file extensions like .log.
- Monitor server access logs for unusual requests to /wp-content/ or similar paths.

## Objectives

1. Retrieve and view the contents of an exposed debug log file.
2. Identify disclosed server paths to understand the target's file system structure.
3. Gather reconnaissance data to facilitate subsequent exploits.

## Instructions

### Step 1: Navigate to the Exposed Debug Log URL

**Context**: Directly access the file to check if it is publicly available, bypassing any expected authentication.

No command required; perform this in a browser:

Open your web browser and navigate to `https://nextcloud.com/wp-content/debug.log`.

> This action loads the file if exposed. Expected output includes raw log text with timestamps, errors, and path references.

### Step 2: Verify Lack of Authentication

**Context**: Confirm the file's public accessibility to validate the vulnerability's severity.

No command required; perform this in a browser:

Refresh the page or open in an incognito window. Check for any prompts or blocks.

> Successful execution shows the file loading without credentials. If blocked, the vulnerability may not be present.

### Step 3: Review and Extract Log Contents

**Context**: Analyze the log for sensitive details like full directory paths to complete the disclosure.

No command required; perform this in a browser:

Use the browser's search (Ctrl+F) to find paths (e.g., search for "/var/" or "wp-content").

> Expected output reveals paths such as "/home/www/nextcloud/wp-content/debug.log", exposing server internals.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- debug-log
- path-disclosure
