---
id: proc-jira-credits-access-001
tags:
  - jira
  - information-disclosure
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
updated_at: '2025-12-14T17:25:18.202Z'
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
# Access-Jira-Credits-Page-for-Instance-Enumeration

## Summary

This procedure accesses the unauthenticated Jira credits page to enumerate instance details, version information, and developer credits, serving as an entry point for further discovery in vulnerable Jira Server deployments.

## Description

In vulnerable Jira Server instances (affected by issues like public.access.disabled misconfigurations), the credits page at /secure/JiraCreditsPage!default.jspa is accessible without authentication. This exposes basic instance metadata, which can reveal version numbers, build dates, and plugin details, aiding in targeted exploitation. The procedure targets web-based Jira installations and requires only HTTP access.

## Requirements

1. Network access to the Jira instance's web interface
2. Web browser or HTTP client like curl
3. Target Jira Server version prior to 9.0 or without authentication fixes

## Defense

Defensive measures and detection strategies:

- Enable strict public access controls in Jira (set public.access.disabled=true and verify)
- Monitor access logs for requests to /secure/JiraCreditsPage!default.jspa from unauthenticated IPs
- Implement web application firewall (WAF) rules to block unauth requests to admin paths

## Objectives

1. Enumerate Jira instance version and configuration details
2. Identify potential exposure points for chained attacks
3. Confirm lack of authentication on public pages

## Instructions

### Step 1: Navigate to Credits Page

**Context**: Directly access the credits page to retrieve exposed information without any login.

No specific command needed; use a browser or curl to fetch the page:

```bash
curl -X GET 'https://target.com/secure/JiraCreditsPage!default.jspa'
```

> This command fetches the HTML content, which includes details like Jira version (e.g., "Atlassian Jira v8.5.0"), build number, and credits. Successful output shows no 401/403 errors.

### Step 2: Analyze Response

**Context**: Parse the response for metadata indicating vulnerabilities.

Inspect the HTML for strings like "Jira Server" version or directory hints.

**Expected Output**: HTML with instance info; no auth redirect.

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

- [[jira]]
- [[information-disclosure]]
