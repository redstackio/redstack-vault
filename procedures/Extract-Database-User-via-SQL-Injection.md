---
tags:
  - sqli
  - mysql
  - error-based
  - user-extraction
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.200Z'
sub_techniques: []
id: 3ae4f487-ecb1-4eeb-958b-5fa63a5bccdc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Database-User-via-SQL-Injection

## Summary

This procedure uses an error-based SQL injection to retrieve the current MySQL database user from a vulnerable web parameter, helping identify privileges and potential lateral movement opportunities.

## Description

Building on a confirmed injection point with poor sanitization of single quotes, this targets the user() function within an updatexml payload. Applicable to public-facing web apps like government subdomains, it leverages MySQL's error reporting to exfiltrate user details without direct query execution. Prerequisites include version confirmation from prior steps; outcomes inform privilege escalation risks.

## Requirements

1. Validated SQLi endpoint from previous extraction
2. Web browser for payload delivery
3. Understanding of MySQL system functions

## Defense

Defensive measures and detection strategies:

- Enforce least-privilege database users
- Disable detailed error reporting in production
- Log and alert on injection attempts targeting user() or similar functions

## Objectives

1. Identify the database username and host
2. Assess user privileges for further attacks
3. Gather intel for targeted exploitation

## Instructions

### Step 1: Inject User Extraction Payload

**Context**: Modify the payload to use user() instead of version() to leak the current user in the error response.

Visit the URL: https://subdomain.airforce.mil/page?id=' and updatexml(null,concat(0x0a,user()),null)-- -@hackerone.mil

> The payload causes an XPath error embedding the user output. Look for the user string in the error details on the response page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Web-Browser]]

## Tags

- [[sqli]]
- [[mysql]]
- [[error-based]]
