---
tags:
  - information-disclosure
  - elmah-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:30:47.142Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: ace00f7f-12cd-4a8d-9070-d0bb9924bed8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
---
# Retrieve-ELMAH-Error-Log-List

## Summary

This procedure exploits the unprotected ELMAH endpoint to retrieve a paginated list of error logs, exposing API errors without authentication.

## Description

The /tmwebapi/elmah.axd endpoint in Yelp's Tailored Mail tool lacks access controls, allowing unauthenticated listing of logs. Using page and size parameters fetches batches of 100 logs, revealing over 75,000 entries with error details. This enables reconnaissance of internal API issues and leads to sensitive data extraction.

## Requirements

1. Access to the login endpoint confirmed
2. Browser or curl for GET requests
3. Understanding of pagination

## Defense

Defensive measures and detection strategies:

- Disable or authenticate ELMAH.axd endpoints
- Restrict error logging to internal networks
- Monitor for high-volume requests to debug paths

## Objectives

1. List recent error logs
2. Identify log IDs for details
3. Assess total log volume

## Instructions

### Step 1: Fetch Log List

**Context**: Send GET to ELMAH with pagination to retrieve logs.

**Command** ([[commands/curl-access-url]]):
```bash
curl https://proze.yelp.com/tmwebapi/elmah.axd?page=1&size=100
```

> Returns structured list of errors. Expected output: XML/HTML with 100 log entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[elmah-exploit]]
