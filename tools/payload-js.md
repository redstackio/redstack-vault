---
url: null
tags:
  - javascript
  - xss
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.233Z'
id: 792a89f6-5b2e-4794-ab39-08071652c35e
validated: true
submitted: true
---
# payload-js

**Status**: Unverified

## Overview

Custom JavaScript file hosted externally and loaded via XSS to automate HTTP requests, parse responses, and perform privilege escalation in Weblate.

## Description

This tool is a simple JS script that runs in the browser context after XSS injection. It handles fetching admin endpoints, extracting CSRF tokens via HTML parsing, and submitting POST updates for escalation. Designed to work around HttpOnly cookies by leveraging the existing session.

## Features

- Feature 1: Authenticated fetch to Django admin paths
- Feature 2: HTML parsing for token extraction using regex/DOM
- Feature 3: Automated POST submission for permission changes

## Installation

### Requirements

- Web server to host the .js file (e.g., Apache, Nginx)
- No additional dependencies; pure vanilla JS

### Install Commands

```bash
# Create and host the file
mkdir /var/www/payload
cat > /var/www/payload/payload.js << EOF
// JS code for fetches and parsing
EOF
# Serve via HTTP
```

## Basic Usage

Host at `http://adversary-domain.com/payload.js` and inject via `<script src="..."></script>`.

### Common Options

N/A (static file)

## Examples

### Example 1: Basic Usage

Inject and load; script auto-runs on page load.

### Example 2: Advanced Usage

Add console.log for debugging:

```javascript
console.log('Payload executed');
fetch('/admin/...').then(...);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- External JS loads from unknown domains in browser network logs
- Anomalous fetches to /admin/ from client-side scripts
- Permission change logs without UI interaction

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Custom XSS Payloads]]

## References

- Weblate source code on GitHub
- Django CSRF documentation
