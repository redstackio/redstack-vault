---
tags:
  - webserver
  - nginx
type: procedure
tools:
  - '[[tools/Nginx]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T04:08:55.270Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bd21eda2-93e6-4cec-97b6-81f2cc09d29a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Install and Configure Nginx Webserver

## Summary

Install and configure Nginx as a webserver on the public server to host PHP scripts that facilitate HTTP redirects in the SSRF chain.

## Description

Nginx serves the initial request from Bitwarden's icon fetcher, executing a PHP redirect to an internal subdomain. This chains the external fetch to an internal target via DNS manipulation. Configuration includes enabling PHP processing for dynamic redirects.

## Requirements

1. Ubuntu/Debian-based server
2. Root or sudo access
3. PHP-FPM installed for script execution

## Defense

Defensive measures and detection strategies:

- Scan for unauthorized webservers on public IPs
- Log and alert on unusual HTTP redirects (e.g., to internal domains)
- Use Nginx access logs with anomaly detection

## Objectives

1. Host static and dynamic content for exploitation
2. Process redirects without exposing internals
3. Ensure compatibility with Bitwarden's HTTP client

## Instructions

### Step 1: Install Nginx and PHP

**Context**: Base installation to run the webserver and scripts.

```bash
apt update && apt install nginx php-fpm -y
```

> Starts Nginx; configure php-fpm socket if needed.

### Step 2: Configure Virtual Host

**Context**: Set up site for the domain.

Edit /etc/nginx/sites-available/default:

```nginx
server {
    listen 80;
    server_name www.yourdomain.com;
    root /var/www/html;
    index index.php;
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
    }
}
```
Then `nginx -t && systemctl reload nginx`.

> Expected: Site responds with PHP info page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Nginx]]
- [[tools/PHP]]

## Tags

- webserver
- nginx
