---
tags:
  - web-access
  - initial-setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:15.818Z'
sub_techniques: []
id: d566b693-e294-4029-bcb0-1b01098554a0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Glassdoor-Interview-Page

## Summary

This procedure accesses the base Glassdoor interview questions page with an initial filter parameter to prepare for XSS testing on the filter.jobTitleFTS query parameter.

## Description

In the context of exploiting a reflected XSS vulnerability, this initial step involves loading a legitimate interview page URL with a benign filter value. This sets the stage for parameter manipulation without alerting the user or triggering redirects. The target is public-facing, requiring no authentication, and focuses on company-specific pages like Accenture's interviews.

## Requirements

1. Web browser with developer tools enabled (e.g., Chrome or Firefox)
2. Internet access to https://www.glassdoor.com
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement URL parameter logging to monitor unusual access patterns to interview pages
- Use web application firewalls (WAF) to flag repeated accesses with varying query parameters

## Objectives

1. Establish a baseline legitimate session on the vulnerable page
2. Confirm the filter.jobTitleFTS parameter is present and modifiable
3. Avoid any premature redirection or errors

## Instructions

### Step 1: Load Base URL

**Context**: Directly navigate to the interview page with an initial search term to simulate normal user behavior.

No command required; use the browser address bar:

```url
https://www.glassdoor.com/Interview/Accenture-Interview-Questions-E4138.htm?filter.jobTitleFTS=Business%20Analyst
```

> This loads the page filtered by "Business Analyst" job title. Inspect the page source to verify the parameter is reflected safely at this stage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[initial-setup]]
