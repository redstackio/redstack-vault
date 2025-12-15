---
id: proc-uuid-001
name: Access-Public-Debug-Log-for-Information-Disclosure
tags:
  - information-disclosure
  - debug-log
  - file-discovery
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-debug-log]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[T1083.002]]'
updated_at: '2025-12-14T17:24:56.389Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[T1083.002]]'
---
# Access-Public-Debug-Log-for-Information-Disclosure

## Summary

This procedure demonstrates how to discover and access a publicly exposed debug.log file on a web server like ExactHosting, leading to information disclosure of debugging details. It was used in reconnaissance against Tucows services, revealing non-sensitive log data without proper access controls.

## Description

In this scenario, during reconnaissance of Tucows' infrastructure, an attacker identifies ExactHosting as a service provider. Common debug files such as debug.log are checked for public accessibility. Due to missing access controls (e.g., no .htaccess restrictions or server misconfiguration), the file is downloadable, exposing entries like error logs, request histories, and paths. While no sensitive data was present in this case, it could reveal application internals. The finding was reported via HackerOne (#3372277) with low impact.

## Requirements

1. Internet access to the target web server (e.g., ExactHosting domain)
2. Knowledge of common file paths (/debug.log)
3. HTTP client like curl or a web browser

## Defense

Defensive measures and detection strategies:

- Implement file access controls (e.g., deny access to .log files via .htaccess or nginx rules)
- Disable debug logging in production environments
- Monitor web server access logs for requests to sensitive paths like /debug.log
- Use web application firewalls (WAF) to block access to administrative or log files

## Objectives

1. Discover exposed files during reconnaissance
2. Retrieve debugging information to map the target's environment
3. Assess potential for further information leakage

## Instructions

### Step 1: Identify Target Endpoint

**Context**: During reconnaissance, enumerate Tucows services to locate ExactHosting instances. Use domain knowledge or tools to guess paths like /debug.log.

No specific command; manually check URLs in browser or via HTTP requests.

### Step 2: Fetch the Debug Log

**Context**: Attempt to download the debug.log file to confirm exposure and extract information.

**Command** ([[commands/curl-fetch-debug-log]]):
```bash
curl -s https://exacthosting.example.com/debug.log -o debug.log
```

> This command silently fetches the content of debug.log and saves it locally. Expected output is a file with log entries (e.g., timestamps, HTTP requests, errors). If successful, review for details like server paths or configs. In the reported case, no sensitive data was found, but exposure was confirmed.

### Step 3: Analyze Retrieved Data

**Context**: Inspect the log for useful information to inform further attacks.

Use standard text tools like cat or grep:

```bash
cat debug.log | grep "ERROR"
```

> Look for patterns indicating vulnerabilities, such as stack traces or internal IPs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]
- [[T1083.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-debug-log]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[debug-log]]
- [[file-discovery]]
- [[web]]
