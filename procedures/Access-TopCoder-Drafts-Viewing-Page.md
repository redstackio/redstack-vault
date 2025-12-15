---
id: proc-access-drafts-page
tags:
  - recon
  - web
  - idor
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-drafts]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:33.584Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Access-TopCoder-Drafts-Viewing-Page

## Summary

This procedure involves navigating to the TopCoder wiki's drafts viewing page to inspect personal drafts and understand the deletion functionality, setting the stage for IDOR exploitation.

## Description

In the TopCoder wiki application, users can view their drafts at a specific endpoint. This step requires authenticated access and allows observation of how drafts are listed and deleted. No vulnerabilities are exploited here, but it reveals draft IDs necessary for subsequent steps. The target environment is a Java/Struts-based web application.

## Requirements

1. Valid TopCoder wiki credentials
2. Browser or HTTP client like curl
3. Network access to https://apps.topcoder.com/wiki

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on draft viewing endpoints
- Log all access to user-specific pages for anomaly detection

## Objectives

1. Identify personal draft IDs
2. Observe the deletion interface
3. Confirm authenticated session

## Instructions

### Step 1: Authenticate and Navigate to Drafts Page

**Context**: Log in to the TopCoder wiki and access the drafts page to view functionality.

**Command** ([[commands/curl-get-drafts]]):
```bash
curl -c cookies.txt -b cookies.txt -X GET "https://apps.topcoder.com/wiki/users/viewmydrafts.action" -H "Cookie: JSESSIONID=your_session"
```

> This command fetches the drafts page using stored cookies for authentication. Expected output includes HTML with draft listings and IDs.

### Step 2: Inspect Page for Draft IDs

**Context**: Examine the response to extract draft IDs from the page source or network tab.

No specific command; use browser dev tools or grep on the curl output:

```bash
grep -o 'draftId=[0-9]*' response.html
```

> Extracts visible draft IDs for use in deletion tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-drafts]]

## Tools Used


## Tags

- recon
- web
