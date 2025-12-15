---
tags:
  - information-disclosure
  - wordpress
  - debug-log
  - path-disclosure
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-debug-log]]'
platforms:
  - Web
  - WordPress
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f76326b4-362c-4037-b6d6-fb0fa5b5f7b2
created_at: '2025-12-14T17:26:26.857Z'
updated_at: '2025-12-14T17:26:26.857Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access Exposed WordPress Debug Log

## Summary

This procedure involves directly accessing a publicly exposed debug.log file in a WordPress installation to disclose sensitive server path information, aiding in reconnaissance for potential further attacks.

## Description

WordPress sites with WP_DEBUG enabled in wp-config.php and WP_DEBUG_LOG set to true generate a debug.log file in the /wp-content/ directory. If the web server lacks proper access controls (e.g., no .htaccess restrictions or directory permissions), this file becomes publicly readable via HTTP. Attackers can request the file directly, revealing logged errors that include absolute server paths, database details, or plugin configurations. This low-severity issue was reported on wonderdynamics.com, where the full server path was exposed, allowing reconnaissance without authentication. The procedure assumes the target is a standard WordPress setup on Apache or Nginx.

## Requirements

1. Valid target domain with WordPress installed and debug logging enabled
2. Network connectivity to the target's HTTP/HTTPS port (80/443)
3. Basic HTTP client (e.g., curl, browser, or wget)

## Defense

Defensive measures and detection strategies:

- Disable WP_DEBUG and WP_DEBUG_LOG in wp-config.php for production environments
- Add .htaccess rules to deny access to debug.log: `RedirectMatch 403 ^/wp-content/debug.log`
- Monitor web server access logs for requests to /wp-content/debug.log
- Use web application firewalls (WAF) to block access to sensitive files
- Regularly scan for exposed files using tools like Nuclei or manual directory enumeration

## Objectives

1. Retrieve and parse the debug.log contents to extract server paths
2. Gather ancillary information like PHP versions or plugin errors for vulnerability assessment
3. Enable further reconnaissance, such as targeting exposed directories

## Instructions

### Step 1: Identify and Access the Debug Log File

**Context**: Confirm the presence of the debug.log by requesting the standard WordPress path. This step accomplishes initial information disclosure by fetching the file contents.

**Command** ([[commands/curl-access-debug-log]]):
```bash
curl -s http://target.com/wp-content/debug.log | head -50
```

> This command performs a silent GET request to the debug.log file and displays the first 50 lines. Successful output includes timestamped log entries with error details, often embedding the full server path (e.g., "/var/www/html/"). If the file is large, pipe to grep for paths: `curl -s http://target.com/wp-content/debug.log | grep -i 'warning' | head -5`. Expect 200 OK status; a 404 indicates the file is not present or protected.

### Step 2: Analyze Extracted Information

**Context**: Review the log contents for sensitive details beyond paths, such as database credentials in errors or custom configurations.

No specific command needed; manually inspect output or save to file:
```bash
curl -s http://target.com/wp-content/debug.log > debug.log && cat debug.log | grep -E 'path|var|home|error'
```

> This saves the full log and filters for path-related entries. Look for indicators like absolute paths starting with /var/, /home/, or Windows-style C:\, confirming server OS and directory structure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-debug-log]]

## Tools Used


## Tags

- information-disclosure
- wordpress
- debug-log
- path-disclosure
- reconnaissance
