---
tags:
  - information-disclosure
  - phpinfo
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-endpoint]]'
platforms:
  - Web
  - Windows
  - PHP
techniques:
  - '[[Client Configurations]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 33d97ce3-c394-461c-a26b-11bd3000d288
created_at: '2025-12-14T17:29:56.705Z'
updated_at: '2025-12-14T17:29:56.705Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Access-Exposed-phpinfo-File

## Summary

This procedure directly accesses an exposed phpinfo.php file to disclose detailed server configuration, including OS, PHP settings, extensions, and environment variables, without requiring authentication.

## Description

Exposed phpinfo.php files are common misconfigurations from debugging setups, revealing sensitive details that assist in tailoring exploits (e.g., targeting specific PHP extensions or Windows vulnerabilities). In this case, accessing https://h2f54.n1.ips.mtn.co.ug/dashboard/phpinfo.php yields information on Windows Server 2012 R2 and PHP environment. The approach uses simple HTTP requests via browser or curl, with no exploitation needed. Prerequisites are knowledge of the file path from prior discovery. Outcomes include raw data for analysis, potentially aiding RCE or further recon.

## Requirements

1. URL of the exposed phpinfo.php (e.g., from directory brute-force)
2. Web browser or curl tool
3. Direct network access to the endpoint

## Defense

Defensive measures and detection strategies:

- Delete or restrict access to phpinfo.php files post-development
- Implement authentication on admin directories
- Scan for exposed sensitive files using tools like Nuclei

## Objectives

1. Extract server OS and PHP configuration details
2. Identify loaded extensions for potential exploits
3. Gather environment variables for attack chaining

## Instructions

### Step 1: Direct Browser Access

**Context**: Use a browser to load the phpinfo.php URL and inspect the output.

Navigate to https://h2f54.n1.ips.mtn.co.ug/dashboard/phpinfo.php.

> The page renders PHP info tables; search for keywords like "OS", "extensions", or "variables" to confirm disclosure.

### Step 2: Command-Line Verification with Curl

**Context**: Use [[commands/curl-access-endpoint]] to fetch and parse the content non-interactively.

Execute [[commands/curl-access-endpoint]] to retrieve the page:

```bash
curl -s https://h2f54.n1.ips.mtn.co.ug/dashboard/phpinfo.php
```

> Output displays HTML with sections on server info; grep for specifics like `grep -i "server"` to isolate Windows Server 2012 R2 details.

### Step 3: Analyze Disclosed Information

**Context**: Review extracted data for actionable intel.

Save output to a file and parse for extensions or paths.

> Success if no 401/403 errors and sensitive info (e.g., PHP version, env vars) is visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Client Configurations]] Gather Victim Host Information: Client Configurations

### Sub-Techniques


## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[phpinfo]]
- [[Reconnaissance]]
