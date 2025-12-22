---
tags:
  - xss
  - api-exploitation
type: procedure
tools:
  - '[[tools/Apache-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3740ed68-4068-470c-91ec-0a1bc32e8978
created_at: '2025-12-11T03:47:48.789Z'
updated_at: '2025-12-11T03:47:48.789Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Configure Malicious ZenTao Server

## Summary

This procedure sets up a malicious mock ZenTao API server using a web server like Apache to deliver JSON payloads containing javascript: URLs and HTML-injected IDs, exploiting the lack of validation in GitLab's ZenTao integration for stored XSS.

## Description

The procedure involves hosting a server that mimics the ZenTao API endpoint /api.php/v1/issues/story-1, returning a JSON response with malicious 'web_url' and 'id' fields. This targets the vulnerability in GitLab's serializer code, which fails to validate or encode these fields properly, leading to XSS when rendered in the issue details page. It requires a web server capable of URL rewriting and serving JSON with the correct Content-Type.

## Requirements

1. Access to a web server like Apache with .htaccess support
2. Ability to host files publicly or accessible by the GitLab instance
3. Knowledge of JSON payload structure for ZenTao API responses

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in integrations to block javascript: schemes
- Enhance HTML sanitization in API serializers
- Monitor for unusual API requests to external servers in GitLab logs

## Objectives

1. Deliver malicious payloads to exploit XSS in GitLab
2. Enable arbitrary JavaScript execution on victim users
3. Facilitate potential account takeover

## Instructions

### Step 1: Setup Web Server

**Context**: Configure the web server to handle requests to the mock API endpoint.

Use [[tools/Apache-Web-Server]] with .htaccess to redirect /api.php/v1/issues to /zentao/issue.json.

> Create .htaccess with RewriteCond and RewriteRule for URL rewriting.

### Step 2: Create Malicious JSON Payload

**Context**: Prepare the JSON file with injected values.

Create issue.json with content including 'web_url': 'javascript:alert(document.domain)' and 'id': '<img src=x style=width:100%;height:100%>'.

> Ensure Content-Type is set to application/json.

### Step 3: Host and Test Server

**Context**: Deploy and verify the server responds correctly.

Host the server at a domain like https://joaxcar.com and test by requesting /api.php/v1/issues/story-1 to confirm malicious JSON is returned.

> Use a browser or curl to validate the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Apache-Web-Server]]

## Tags

- #xss
- #api-exploitation
