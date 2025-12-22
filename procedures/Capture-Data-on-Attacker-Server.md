---
id: proc-smule-capture-data-001
name: Capture-Data-on-Attacker-Server
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.339Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - information-disclosure
  - csrf
commands: []
platforms:
  - Web
tools:
  - '[[tools/PHP]]'
  - '[[tools/Apache-htaccess]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---

# Capture-Data-on-Attacker-Server

## Summary

This procedure sets up an attacker-controlled server using PHP and .htaccess to intercept and log the CSRF token and email from the victim's requests triggered by the poisoned page, while mimicking Smule's responses to avoid detection.

## Description

The attacker runs a PHP script (check_email.php) configured to handle both OPTIONS (for CORS) and POST requests to /user/check_email. It captures headers like X-CSRF-Token and POST data (email), logs them, and returns a JSON response with appropriate headers (e.g., Set-Cookie, CSP) to simulate the legitimate endpoint. .htaccess rewrites URLs to route to the PHP script.

## Requirements

1. Apache server with PHP enabled on localhost:80
2. check_email.php script and .htaccess file in web root
3. Knowledge of Smule's response format for mimicry

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS to prevent localhost redirects
- Rate-limit and anomaly-detect requests to sensitive endpoints
- Use web application firewall (WAF) rules to block suspicious header manipulations

## Objectives

1. Intercept and store disclosed CSRF token and email
2. Respond convincingly to maintain victim interaction
3. Prepare captured data for account takeover

## Instructions

### Step 1: Configure .htaccess

**Context**: Set up URL rewriting to handle /user/check_email as PHP.

No command; create .htaccess:

```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^\.]+)$ $1.php [NC,L]
```

> Place in web root. Expected output: Requests to /user/check_email route to check_email.php.

### Step 2: Implement PHP Script

**Context**: Create script to log data and mimic response.

No command; write check_email.php to handle OPTIONS/POST, log $_POST['email'] and $_SERVER['HTTP_X_CSRF_TOKEN'], echo JSON {"email":true,"token":"[captured]","mail":"[email]"}, set headers like Access-Control-Allow-Origin: https://www.smule.com, Content-Security-Policy, Set-Cookie.

> For OPTIONS: Return 200 with CORS headers. For POST: Log and respond. Expected output: Captured data in PHP logs/file.

### Step 3: Start Server and Test

**Context**: Run Apache and verify capture.

No command; apachectl start or similar.

> Trigger from browser; check logs for token/email. Success: Data logged without browser errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]
- [[tools/Apache-htaccess]]

## Tags

- [[information-disclosure]]
- [[csrf]]
