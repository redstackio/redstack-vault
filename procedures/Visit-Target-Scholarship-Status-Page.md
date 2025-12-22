---
tags:
  - web-access
  - initial-access
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.934Z'
sub_techniques: []
id: c34d0193-82a4-446a-9a9a-b23f271bf67c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Visit-Target-Scholarship-Status-Page

## Summary

This procedure initiates access to the vulnerable web application page used for checking scholarship status, setting the stage for subsequent exploitation of SQL injection vulnerabilities.

## Description

In the context of a .NET ASP.NET web application, navigate to the status checking endpoint. This step requires no authentication and exposes input fields vulnerable to injection. Expected outcomes include loading the form, allowing inspection for client-side restrictions.

## Requirements

1. Modern web browser (e.g., Chrome, Firefox)
2. Internet access to the target URL
3. No prior credentials or setup needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to monitor access patterns
- Log all requests to public-facing pages and alert on anomalous user agents

## Objectives

1. Establish initial foothold on the target application
2. Verify page accessibility and form presence
3. Prepare for input manipulation

## Instructions

### Step 1: Open Browser and Navigate

**Context**: Launch a browser session and directly access the target endpoint to load the vulnerable form.

No command required; use browser navigation bar:

```plaintext
https://██████████/████/candidate_app/status_scholarship.aspx
```

> This loads the page with SSN and birth date fields. Confirm the form renders correctly without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[web-access]]
- [[initial-access]]
