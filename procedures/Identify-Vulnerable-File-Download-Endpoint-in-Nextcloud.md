---
id: proc-nextcloud-endpoint-ident
tags:
  - nextcloud
  - endpoint-testing
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-nextcloud-download-test]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-13T23:52:25.035Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Vulnerable File Download Endpoint in Nextcloud

## Summary

This procedure identifies the vulnerable AJAX file download endpoint in Nextcloud by sending manipulated parameters to trigger error pages, revealing unescaped output and potential path disclosure.

## Description

In Nextcloud, the file download functionality in the files app uses an AJAX endpoint that inadequately escapes error messages. By setting parameters like `files` to a null byte and `dir` to invalid paths, an error is triggered, and the response includes unescaped content from the parameters. This can disclose the full server path and set up for further injection. The procedure requires a logged-in session and targets web-based Nextcloud instances running on PHP. Expected outcomes include confirmation of the vulnerability and path information for reconnaissance.

## Requirements

1. Valid Nextcloud user credentials for login
2. Network access to the Nextcloud web interface
3. Tools like curl or a browser for HTTP requests
4. Logged-in session cookie

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and escaping for all error messages
- Enforce Content-Security-Policy (CSP) to block inline scripts
- Monitor for anomalous requests to AJAX endpoints with special characters like null bytes
- Log and alert on error page accesses with manipulated parameters

## Objectives

1. Confirm the endpoint's susceptibility to parameter injection
2. Extract server path information for reconnaissance
3. Prepare for HTML injection in subsequent steps

## Instructions

### Step 1: Authenticate and Target Endpoint

**Context**: Log in to Nextcloud and prepare to test the file download endpoint to force an error condition.

**Command** ([[commands/curl-nextcloud-download-test]]):
```bash
curl -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid/path" -b "cookie=logged_in_session"
```

> This command sends a GET request with a null byte in `files` and an invalid directory in `dir`, triggering an error. The response should show an error page with reflected parameters and potentially the full path like `/var/www/nextcloud/...`.

### Step 2: Analyze Response for Vulnerability

**Context**: Inspect the HTTP response for unescaped output to confirm the issue.

Use browser dev tools or pipe the curl output to grep for path indicators:

```bash
echo "$(curl -s -X GET \"https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid/path\" -b \"cookie=logged_in_session\")" | grep -i path
```

> Look for server paths in the error message. Success is indicated by unescaped parameter reflection and path exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-nextcloud-download-test]]

## Tools Used


## Tags

- [[nextcloud]]
- [[endpoint-testing]]
- [[information-disclosure]]
