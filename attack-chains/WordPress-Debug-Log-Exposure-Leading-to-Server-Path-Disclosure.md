---
tags:
  - information-disclosure
  - wordpress
  - debug-log
  - path-disclosure
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-debug-log]]'
platforms:
  - Web
  - WordPress
complexity: low
procedures:
  - '[[procedures/Access-Exposed-WordPress-Debug-Log]]'
step_count: 1
techniques:
  - '[[Gather Victim Host Information]]'
description: >-
  Discovery of a publicly accessible WordPress debug.log file exposing sensitive
  server path information for reconnaissance.
skill_level: beginner
impact_level: low
id: cbd1bb72-0faf-4b0f-b984-5fce991f3c18
created_at: '2025-12-14T17:26:26.862Z'
updated_at: '2025-12-14T17:26:26.862Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# WordPress Debug Log Exposure Leading to Server Path Disclosure

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Exposed Debug Log] --> B[Extract Server Path Information]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- WordPress installation with WP_DEBUG enabled and logging active
- Publicly accessible web server (e.g., Apache/Nginx on Linux)
- No authentication required for the /wp-content/ directory

### Initial Access Requirements

- Internet access to the target domain
- No credentials needed
- Direct URL knowledge or directory browsing

## Detailed Attack Procedures

### Step 1: Access Exposed Debug Log
procedure: [[procedures/Access-Exposed-WordPress-Debug-Log]]

**Objective**: Retrieve the contents of the publicly exposed debug.log file to disclose the full server path and other configuration details.

**Instructions**: Identify the WordPress installation on the target domain, typically under /wp-content/. Use [[commands/curl-access-debug-log]] to fetch the debug.log file:

```bash
curl -s http://target.com/wp-content/debug.log | head -50
```

This command silently retrieves the first 50 lines of the log file, where server paths like "/var/www/html/wp-content/" are often logged in error messages.

**Expected Output**: Log entries containing PHP errors, warnings, or notices that reveal the absolute server file path, such as:
```
[12-Jan-2023 10:30:45 UTC] PHP Warning:  file_get_contents(/var/www/html/wp-content/themes/theme/file.php): failed to open stream in /var/www/html/wp-includes/functions.php on line 123
```

**Success Indicators**:
- HTTP 200 response with log file contents
- Visible absolute server paths in the output (e.g., /home/user/public_html/ or /var/www/)
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Successful access to sensitive debug information without authentication
2. Disclosure of server filesystem structure for further reconnaissance
3. Identification of potential attack vectors based on exposed paths

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
