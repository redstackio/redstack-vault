---
tags:
  - access-bypass
  - internal-tool
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.145Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: a938952e-709f-4e7c-afed-b5bd2fcf9905
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Tailored-Mail-Login

## Summary

This procedure directly accesses the login endpoint of Yelp's internal Tailored Mail admin tool, bypassing root-level redirects to confirm the application's exposure.

## Description

By appending /app/login to the subdomain, attackers can load the admin interface without authentication, revealing the internal ASP.NET-based tool. This step uncovers the presence of the Tailored Mail application and prepares for further endpoint discovery. Expected outcome: Visible login page indicating unauthenticated access to internals.

## Requirements

1. Successful completion of subdomain verification
2. Web browser or curl
3. HTTPS support

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all internal paths
- Use path-based access controls in web servers
- Log and alert on direct internal endpoint hits

## Objectives

1. Load internal admin login page
2. Confirm tool exposure
3. Enable endpoint enumeration

## Instructions

### Step 1: Direct Login Access

**Context**: Request the specific login path to avoid root redirect.

**Command** ([[commands/curl-access-url]]):
```bash
curl -i https://proze.yelp.com/app/login
```

> Returns HTML of the login form. Expected output: 200 OK with Tailored Mail admin content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[access-bypass]]
- [[internal-tool]]
