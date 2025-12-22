---
id: 123e4567-e89b-12d3-a456-426614174003
name: Host-Malicious-Phishing-Content-on-Taken-Over-Subdomain
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.863Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - phishing
  - subdomain-takeover
commands: []
platforms:
  - Web
  - AWS
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Host-Malicious-Phishing-Content-on-Taken-Over-Subdomain

## Summary

After claiming a subdomain, this procedure deploys malicious scripts or pages on the controlled origin to facilitate phishing, cookie theft, or redirects, leveraging the trusted domain for credibility.

## Description

With control of saostatic.uber.com via CloudFront, the attacker configures the origin server to serve HTTP/HTTPS content, including a proof-of-concept page and a PHP script (prepareuberattack.php) that captures SSO parameters. SSL is obtained via Let's Encrypt using the legitimate domain, enabling secure phishing. Targets SSO-enabled web apps; requires server setup. Outcomes: Ability to steal session data during victim interactions.

## Requirements

1. Controlled origin server (e.g., Apache/Nginx on EC2)
2. Claimed subdomain resolving to origin
3. Domain validation for SSL (via DNS challenge)

## Defense

Defensive measures and detection strategies:

- Implement subdomain monitoring with certificate transparency logs (e.g., crt.sh)
- Use HSTS preloading for .uber.com to prevent HTTP fallback
- Scan for anomalous content on subdomains with WAF rules

## Objectives

1. Deploy cookie-capturing scripts
2. Secure the subdomain with valid SSL
3. Enable stealthy victim interaction

## Instructions

### Step 1: Configure Origin Server

**Context**: Set up web server to handle requests from CloudFront.

**Command** (Nginx example):
```bash
server {
    listen 443 ssl;
    server_name saostatic.uber.com;
    root /var/www/html;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
}
```

> Restart server (nginx -s reload). Upload files like prepareuberattack.php to root.

### Step 2: Obtain SSL Certificate

**Context**: Use Let's Encrypt for trusted HTTPS.

**Command** (Certbot):
```bash
certbot certonly --standalone -d saostatic.uber.com
```

> Expected: Certificates generated; configure in server. Test HTTPS access.

### Step 3: Deploy Malicious Content

**Context**: Place phishing script to capture data.

**Command** (Upload):
```bash
scp prepareuberattack.php user@origin:/var/www/html/
```

> Script outputs captured URL/Cookies when visited. Verify by accessing /prepareuberattack.php.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- Certbot, SCP

## Tags

- [[Phishing]]
- [[subdomain-takeover]]
