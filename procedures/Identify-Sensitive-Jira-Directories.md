---
id: proc-jira-directory-identify-001
tags:
  - jira
  - directory-discovery
  - unauthenticated-access
type: procedure
tools:
  - '[[tools/curl]]'
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
updated_at: '2025-12-14T17:25:18.200Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-Sensitive-Jira-Directories

## Summary

This procedure inspects responses from the Jira credits page to identify sensitive directories and API endpoints, enabling discovery of unprotected resources in unauthenticated contexts.

## Description

Upon accessing the credits page, attackers can analyze embedded links, scripts, or metadata to uncover paths like /rest/menu/latest/admin. This step leverages the lack of access controls in vulnerable Jira Server setups (JRASERVER-73060) to map the attack surface without authentication.

## Requirements

1. Successful access to the credits page from prior step
2. Ability to inspect HTTP responses (browser dev tools or curl -v)
3. Basic knowledge of web application structure

## Defense

Defensive measures and detection strategies:

- Remove or restrict metadata exposure in static pages
- Log and alert on anomalous directory traversals or API probes
- Use content security policies to limit script/resource loading

## Objectives

1. Extract potential sensitive paths from page content
2. Confirm exposure of internal directories
3. Prepare for API exploitation

## Instructions

### Step 1: Inspect Credits Page Response

**Context**: Use verbose output to capture headers and body for directory clues.

Execute with curl for detailed inspection:

```bash
curl -v 'https://target.com/secure/JiraCreditsPage!default.jspa'
```

> Verbose mode (-v) shows full request/response, including any referenced paths in HTML or JS. Look for /rest/ endpoints or admin-related strings.

### Step 2: Manual Enumeration

**Context**: Search response for keywords like "rest", "admin", or "menu".

Use grep on saved output:

```bash
curl 'https://target.com/secure/JiraCreditsPage!default.jspa' | grep -i 'rest\|admin'
```

> Expected output: Lines hinting at endpoints like /rest/menu/latest/admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[directory-discovery]]
- [[jira]]
