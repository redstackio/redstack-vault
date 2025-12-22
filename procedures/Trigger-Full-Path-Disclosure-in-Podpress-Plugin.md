---
tags:
  - information-disclosure
  - wordpress
  - php
  - full-path-disclosure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-vulnerable-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:06.289Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b22c78ce-1b46-475c-89e9-cad1f766c93c
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Trigger Full Path Disclosure in Podpress Plugin

## Summary

This procedure exploits a syntax error or misconfiguration in the 'write.php' file of the Podpress WordPress plugin to disclose the server's full file path and the user account running the web server. It is primarily used in reconnaissance phases to gather host information that can facilitate further exploitation, such as path-based attacks.

## Description

The Podpress plugin, when installed on a WordPress site, includes a 'getid3/write.php' file that is directly accessible via the web. Due to a PHP syntax error or unnecessary exposure, requesting this file causes the server to output debugging information, including the absolute filesystem path (e.g., "/home/user/public_html/...") and the process user (e.g., "apache" or "www-data"). This disclosure occurs without authentication and can be triggered by any unauthenticated visitor. The target environment is a PHP-enabled web server hosting WordPress, typically on Linux/Unix systems. Expected outcomes include immediate visibility of sensitive path details, which could chain with other vulnerabilities like local file inclusion or privilege escalation.

## Requirements

1. Public HTTP access to the target WordPress site's plugin directory.
2. No authentication or special permissions needed.
3. Basic tools like curl or a web browser for making HTTP requests.
4. Knowledge of the vulnerable URL path: /wp-content/plugins/podpress/getid3/write.php.

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to unnecessary plugin files using .htaccess rules (e.g., deny execution of .php in plugin subdirectories).
- Update or disable the Podpress plugin, as it is outdated and vulnerable.
- Implement web application firewall (WAF) rules to block direct access to sensitive paths.
- Monitor server logs for anomalous requests to plugin files and enable PHP error logging to hide path disclosures.

## Objectives

1. Gather the server's absolute file path to understand the filesystem structure.
2. Identify the web server user for assessing privilege levels.
3. Collect reconnaissance data to support chained attacks without direct server access.

## Instructions

### Step 1: Access the Vulnerable Endpoint

**Context**: Directly request the write.php file to trigger the error and disclose server details. This simulates navigating to the URL in a browser but uses curl for scripting and logging.

**Command** ([[commands/curl-access-vulnerable-endpoint]]):
```bash
curl -s http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php
```

> This command sends a silent GET request to the vulnerable file. The '-s' flag suppresses progress output for cleaner results. Expected output includes PHP error messages revealing the full path, such as "Warning: fopen(/full/server/path/...): failed to open stream: No such file or directory in /full/server/path/to/write.php on line X" and the user context from server configuration.

### Step 2: Analyze the Disclosure

**Context**: Review the response for key indicators of success, extracting the path and user for documentation or further use.

**Command** ([[commands/curl-access-vulnerable-endpoint]]):
```bash
curl -s http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php | grep -i "path\|user"
```

> Pipe the output through grep to filter for path or user-related strings. Successful execution shows lines like the absolute path and running user, confirming the disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-vulnerable-endpoint]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[wordpress]]
- [[php]]
