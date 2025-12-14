---
id: proc-execute-rce-nextcloud
tags:
  - rce
  - webshell
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T03:16:02.595Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Execute-RCE-via-Web-Accessible-PHP-File

## Summary

This procedure executes arbitrary commands on the server by interacting with the uploaded PHP webshell, achieving full RCE and potential server takeover.

## Description

Once the PHP file is accessible, appending parameters like ?cmd= allows system() execution, running commands as the web server user (e.g., www-data). Impacts include data extraction, config modification, and further persistence. This also enables XSS by uploading HTML/JS files similarly. The attack relies on PHP interpretation in the data directory without restrictions.

## Requirements

1. Successful direct access to the PHP file
2. Knowledge of PHP webshell syntax for command injection
3. Target commands for testing (e.g., whoami, ls)

## Defense

Defensive measures and detection strategies:

- Disable PHP execution in data directories via .htaccess (php_flag engine off)
- Monitor web logs for direct /data/ accesses and unusual parameters
- Use integrity checks on uploaded files and anomaly detection in file system

## Objectives

1. Run arbitrary system commands for reconnaissance
2. Escalate to server compromise (e.g., extract data, modify configs)
3. Demonstrate impact including potential XSS via HTML uploads

## Instructions

### Step 1: Test Basic Execution

**Context**: Verify RCE by running a simple command.

Append ?cmd=whoami to the URL: https://www.ournextclouddomain.com/data/attacker/files/shell.php?cmd=whoami

> Output should show 'www-data' or similar.

### Step 2: Execute Advanced Commands

**Context**: Perform impactful actions like data extraction.

Use ?cmd=cat /etc/passwd or similar for exfiltration.

> Browser displays command output; chain commands for persistence (e.g., download additional tools).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] PHP

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- webshell
- nextcloud
