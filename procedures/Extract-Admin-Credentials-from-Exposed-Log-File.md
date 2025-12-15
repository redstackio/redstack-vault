---
id: proc-log-credential-extraction
tags:
  - information-disclosure
  - credential-access
  - log-exposure
  - md5-hash
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-fetch-log]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:30:07.431Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Admin-Credentials-from-Exposed-Log-File

## Summary

This procedure demonstrates how to access a publicly exposed web log file to extract sensitive information, including an admin username and MD5-hashed password, which can be cracked offline to achieve account takeover in a PHP-based web application.

## Description

In scenarios where web applications log sensitive operations like password changes without proper access controls, attackers can directly retrieve these logs via HTTP requests. This procedure targets such misconfigurations, as seen in the Acronis DeviceLock application, where the log file at https://www.devicelock.com/log.txt contained details from a password change event. The extracted MD5 hash (e.g., 2bca2f877b7a727861b59f4a4039d2e9) can be subjected to dictionary or brute-force attacks using tools like Hashcat to recover the plaintext password, leading to admin access compromise. Prerequisites include basic web access; no authentication is needed due to the public exposure.

## Requirements

1. Internet connectivity to reach the target URL.
2. A web browser or command-line HTTP client like curl.
3. Optional: Hash cracking tool (e.g., Hashcat) for post-extraction analysis.

## Defense

Defensive measures and detection strategies:

- Implement access controls (e.g., .htaccess restrictions or server-side authentication) on log files to prevent public access.
- Sanitize logs to exclude sensitive data like passwords or hashes before writing to files.
- Monitor web server access logs for unusual requests to sensitive paths like /log.txt.
- Use secure logging practices, such as rotating logs and storing them in non-public directories.

## Objectives

1. Retrieve the exposed log file containing credential data.
2. Parse the log for admin login and MD5 hash.
3. Prepare extracted data for offline cracking to enable account takeover.

## Instructions

### Step 1: Fetch the Log File

**Context**: Use an HTTP client to download the publicly accessible log file, confirming no access restrictions are in place.

**Command** ([[commands/curl-fetch-log]]):
```bash
curl https://www.devicelock.com/log.txt -o extracted_log.txt
```

> This command performs a GET request to the log URL and saves the response to a local file. Expected output is the raw log content if successful (HTTP 200); errors like 403/404 indicate access controls or non-existence.

### Step 2: Inspect and Extract Credentials

**Context**: Review the downloaded log for sensitive entries, identifying the admin login and MD5 hash from password change logs.

**Command** (Manual inspection or grep):
```bash
grep -i "md5=" extracted_log.txt
```

> This filters the log for MD5-related entries. Expected output: Lines like 'login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9', revealing the credentials for further cracking.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-log]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[credential-access]]
