---
tags:
  - reconnaissance
  - tomcat
  - vulnerability-identification
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-incomplete-post]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 22701f9f-9605-4dea-b00d-a89ed69b0fa0
created_at: '2025-12-13T09:01:22.518Z'
updated_at: '2025-12-13T09:01:22.518Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Apache Tomcat Server

## Summary

This procedure involves scanning a target web server to identify if it is running a vulnerable version of Apache Tomcat susceptible to HTTP Request Smuggling via Client-Side Desync.

## Description

The procedure targets web applications to detect Apache Tomcat versions 8.5.7 to 8.5.63 or 9.0.0-M11 to 9.0.43, which fail to properly handle Content-Length in POST requests, leading to potential desynchronization and data leakage. It uses simple HTTP requests to fingerprint the server.

## Requirements

1. Network access to the target web server
2. Tool like curl for sending HTTP requests
3. Knowledge of target URL or IP

## Defense

Defensive measures and detection strategies:

- Regularly update Apache Tomcat to patched versions
- Monitor HTTP traffic for anomalous POST requests with mismatched Content-Length

## Objectives

1. Confirm presence of Apache Tomcat
2. Verify version is within vulnerable range
3. Prepare for exploitation

## Instructions

### Step 1: Send Header Request

**Context**: Send a HEAD request to retrieve server headers.

**Command** ([[commands/curl-send-incomplete-post]]):
```bash
curl -I http://target.com
```

> This command fetches headers; look for 'Server: Apache-Coyote/1.1' indicating Tomcat.

### Step 2: Verify Version

**Context**: Manually check the version against known vulnerable ranges.

> If headers don't reveal version, probe with additional requests or tools to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-incomplete-post]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Reconnaissance]]
- [[tomcat]]
