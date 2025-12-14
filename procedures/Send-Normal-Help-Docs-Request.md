---
id: proc-normal-help-docs
tags:
  - reconnaissance
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Fiddler]]'
  - '[[tools/ZAP]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/help-docs-normal-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.669Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Send-Normal-Help-Docs-Request

## Summary

This procedure sends a standard authenticated request to the /help_docs endpoint with a legitimate URL to verify functionality and establish a baseline response before attempting SSRF exploitation.

## Description

Using an authenticated session, craft a GET request to /help_docs with the 'url' parameter set to a valid external resource like https://search.gov/manual/account.html. This tests the endpoint's normal behavior, including headers and cookies, and confirms the server fetches and returns content without issues. Proxy tools are essential for inspection and replay.

## Requirements

1. Authenticated session cookies from prior login
2. Proxy tool to modify and send requests
3. Knowledge of required headers like X-CSRF-Token

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URL domains in the parameter
- Log all /help_docs requests and monitor for unusual patterns
- Rate-limit endpoint access to prevent abuse

## Objectives

1. Confirm endpoint accessibility and response format
2. Capture baseline response time and body
3. Identify any protections for later bypass

## Instructions

### Step 1: Prepare Authenticated Request

**Context**: Set up the request with all necessary headers and cookies.

Configure proxy (e.g., Burp Suite) to include session cookies.

### Step 2: Execute Normal Request

**Context**: Send the GET request to baseline the endpoint.

**Command** ([[commands/help-docs-normal-get]]):
```bash
curl -X GET "https://search.usa.gov/help_docs?url=https%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: ja,en-US;q=0.7,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br" -H "Referer: https://search.usa.gov/account" -H "X-NewRelic-ID: VgYAV1BRCxABU1JUBAUCXlI=" -H "X-CSRF-Token: /2jDOc6aYEZA5VealIrF44qJZtY0iDiTsALu8HYA+OOIewuKHREwyh6M0wGa2WC9amTPX4vPMjj0YQIjys3nNA==" -H "X-Requested-With: XMLHttpRequest" -H "Connection: close" -H "Cookie: _ga=GA1.2.924676610.1553290937; _gid=GA1.2.1047460386.1553290937; _ga=GA1.3.924676610.1553290937; _gid=GA1.3.1047460386.1553290937; _session_id=a0d5ecbfa9404ea9ffad4cb3ea771dea; user_credentials=1055608db95b714d9ae2ef05a4e1b83aa138ad5fca67422f02ca795ec2a74179bb15c610dd33f5e6f200be0de0e812a8fe3d59a0027b290b5377ab2a65da1f19%3A%3A5992"
```

> This command fetches the legitimate content; expect a 200 OK with the manual page body.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/help-docs-normal-get]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]
- [[tools/ZAP]]

## Tags

- reconnaissance
- web
