---
tags:
  - parameter-manipulation
  - bypass-redirect
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
updated_at: '2025-12-14T00:11:15.815Z'
sub_techniques: []
id: fe120830-7bb4-42e6-9e24-a794189ffa54
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Country-Redirect-Parameter

## Summary

This procedure appends a query parameter to prevent automatic country redirection on Glassdoor pages, ensuring payloads can be injected and executed without interruption.

## Description

Glassdoor's platform redirects users based on geolocation, which can interfere with XSS testing. By adding countryRedirect=true, this behavior is disabled, allowing the filter.jobTitleFTS parameter to be modified freely. This is a preparatory step in the XSS exploit chain targeting interview pages.

## Requirements

1. Active browser session from the initial page load
2. Ability to edit URL parameters manually
3. Stable connection to avoid reload issues

## Defense

Defensive measures and detection strategies:

- Monitor for the presence of countryRedirect=true in logs, as it may indicate testing or malicious activity
- Enforce geolocation redirects server-side regardless of parameters

## Objectives

1. Suppress redirection to maintain control over the page state
2. Prepare the URL for payload injection
3. Verify no content changes occur

## Instructions

### Step 1: Append Parameter

**Context**: Modify the existing URL to include the anti-redirect flag, then reload the page.

Edit the URL in the browser:

```url
https://www.glassdoor.com/Interview/Accenture-Interview-Questions-E4138.htm?filter.jobTitleFTS=Business%20Analyst&countryRedirect=true
```

> The page should reload identically, but any subsequent geolocation checks are bypassed. Check the network tab in dev tools for no redirect requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[parameter-manipulation]]
- [[bypass-redirect]]
