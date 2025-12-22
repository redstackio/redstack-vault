---
id: uuid-identify
tags:
  - recon
  - django
  - oracle
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-identify-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-12-05T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:24.955Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Django-HasKey-Usage

## Summary

This procedure involves reconnaissance to identify Django application endpoints that utilize the HasKey lookup on JSON fields with user-controlled input, specifically targeting Oracle backends vulnerable to CVE-2024-53908.

## Description

In Django applications using Oracle databases, the HasKey lookup in django.db.models.fields.json allows checking for keys in JSON fields. When used directly with untrusted lhs (left-hand side, the key name), it can lead to SQL injection if the input is interpolated without sanitization into Oracle's SQL. This procedure focuses on black-box or source code review to find such usages, such as in filters like MyModel.objects.filter(jsonfield__has_key=user_input, 'key'). Applications using the __has_key syntax are safe, but direct HasKey calls are not. Expected outcomes include pinpointing injectable parameters for further exploitation.

## Requirements

1. Access to the web application network
2. Tools for HTTP probing (e.g., curl or browser dev tools)
3. Basic knowledge of Django ORM and Oracle SQL

## Defense

Defensive measures and detection strategies:

- Use parameterized queries and avoid direct lookup with user input
- Implement web application firewalls (WAF) to detect SQL injection patterns
- Log and monitor database queries for anomalies in JSON functions

## Objectives

1. Discover endpoints accepting key names for JSON lookups
2. Confirm Oracle backend usage via error messages
3. Prepare for payload injection

## Instructions

### Step 1: Probe Application Endpoints

**Context**: Send requests to potential API or form endpoints to identify those handling JSON key inputs.

**Command** ([[commands/curl-identify-endpoint]]):
```bash
curl -X GET "http://target.com/api/items?filter_key=testkey" -v
```

> This command sends a GET request with a test key. Look for responses indicating JSON processing or Oracle errors like ORA-40441 (invalid JSON).

### Step 2: Analyze Responses for Vulnerabilities

**Context**: Check for signs of direct HasKey usage, such as delayed responses or partial SQL errors when using special characters in the key.

**Command** ([[commands/curl-identify-endpoint]]):
```bash
curl -X GET "http://target.com/api/items?filter_key='" -v
```

> Inject a single quote to trigger potential SQL errors. Successful identification shows database-level errors confirming unsanitized interpolation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-identify-endpoint]]

## Tools Used


## Tags

- [[recon]]
- [[web]]
