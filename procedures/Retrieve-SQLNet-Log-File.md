---
tags:
  - information-disclosure
  - oracle
  - file-access
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:21.943Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: fbec5f8e-588a-44bd-993c-8b8b7a94708a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Retrieve-SQLNet-Log-File

## Summary

This procedure involves directly accessing an exposed SQLNet log file on a web server, disclosing sensitive internal network information such as IP addresses, hostnames, and usernames. In the Uber vulnerability, the file at /OA_HTML/bin/sqlnet.log was publicly accessible due to improper access controls on an Oracle-related endpoint.

## Description

SQLNet logs, part of Oracle database connectivity, often contain diagnostic details including connection attempts, errors, and network identifiers. When placed in a web-accessible directory without protection, attackers can retrieve it via simple HTTP GET requests. This leads to reconnaissance gains, revealing internal infrastructure. The attack targets misconfigured web servers hosting Oracle applications, requiring only the full path to the file.

## Requirements

1. Prior access to the internal site (e.g., via auth bypass)
2. Knowledge of the log file path (/OA_HTML/bin/sqlnet.log)
3. Web browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Restrict web server directories to prevent exposure of log files (e.g., via .htaccess or nginx location blocks)
- Store logs outside web roots and use proper file permissions (e.g., 600 for logs)
- Implement logging and alerting for direct file access attempts to sensitive paths
- Regularly scan for exposed files using tools like dirbuster or automated crawlers

## Objectives

1. Download the SQLNet log file
2. Extract internal network details
3. Assess impact on reconnaissance

## Instructions

### Step 1: Construct and Request the File URL

**Context**: Append the known log path to the base site URL to attempt direct retrieval.

Visit https://lab.usuppliers.uber.com/OA_HTML/bin/sqlnet.log in a browser, or use curl:

```bash
curl https://lab.usuppliers.uber.com/OA_HTML/bin/sqlnet.log
```

> The response will be plain text log entries. Successful access shows content without 403/404 errors.

### Step 2: Analyze Disclosed Information

**Context**: Parse the log for sensitive data to understand the exposure.

Save the output to a file (e.g., curl -o sqlnet.log) and grep for keywords like IP addresses (regex for \d+\.\d+\.\d+\.\d+), hostnames, or usernames.

**Expected Output**: Log text revealing Uber internal IPs (e.g., private ranges), hostnames (e.g., internal servers), and one username (e.g., oracle user).

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
- oracle
- file-access
