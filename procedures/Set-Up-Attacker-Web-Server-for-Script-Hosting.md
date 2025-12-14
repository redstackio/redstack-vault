---
tags:
  - c2
  - script-hosting
  - apache
type: procedure
tools:
  - '[[tools/Web-Server]]'
  - '[[tools/Apache]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/host-alert-payload]]'
  - '[[commands/configure-htaccess-rewrite]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:56:19.817Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 5671afc0-af40-4614-845a-2f122f28b255
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Set-Up-Attacker-Web-Server-for-Script-Hosting

## Summary

This procedure configures an attacker-controlled web server to host JavaScript payloads at paths mimicking GitLab's assets, using .htaccess redirects for consistency, enabling execution when loads are redirected by the injected <base> tag.

## Description

To exploit the redirection, the server must serve JS at expected paths or redirect all to a single payload file. This uses Apache for simplicity, hosting alert(document.domain) to prove domain context. Applies to any HTTP server; detects via network logs.

## Requirements

1. Domain with DNS pointed to server (e.g., joaxcar.com)
2. Apache or compatible web server installed
3. Access to filesystem for file placement

## Defense

Defensive measures and detection strategies:

- Block or monitor requests to suspicious domains from client-side
- Use CSP with strict-src to prevent external JS
- Scan for anomalous server responses in proxy logs

## Objectives

1. Host JS payload executable in GitLab context
2. Redirect all asset requests to payload
3. Ensure compatibility with webpack paths

## Instructions

### Step 1: Create Payload File

**Context**: Place JS that executes on load.

**Command** ([[commands/host-alert-payload]]):

Create /hack.js with:

```javascript
alert(document.domain)
```

> Save in web root. Expected: File serves as JS MIME type.

### Step 2: Configure Redirection

**Context**: Use .htaccess to handle multiple paths.

**Command** ([[commands/configure-htaccess-rewrite]]):

In .htaccess:

```apache
RewriteEngine on
RewriteCond %{REQUEST_URI} !^/hack.js$
RewriteRule .* /hack.js [L,R=302]
```

> Restart Apache if needed. Expected: curl http://domain/nonexistent -> 302 to /hack.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/host-alert-payload]]
- [[commands/configure-htaccess-rewrite]]

## Tools Used

- [[tools/Apache]]
- [[tools/Web-Server]]

## Tags

- redirection
- payload-delivery
