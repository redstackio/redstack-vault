---
id: proc-uuid-001
name: Configure-Target-Site-with-Client-Cert-Auth
tags:
  - tls
  - authentication
  - setup
type: procedure
tools:
  - '[[tools/curl]]'
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
updated_at: '2025-12-14T17:30:58.735Z'
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
# Configure-Target-Site-with-Client-Cert-Auth

## Summary

This procedure sets up a target web server to require client certificate authentication for accessing protected resources, simulating a secure endpoint vulnerable to certificate reuse attacks.

## Description

In this attack scenario, the target site (targetsite.tld) is configured to use mutual TLS (mTLS) where clients must present a valid certificate for authentication. This is common in APIs or internal services. The setup ensures that direct access to /secretfile requires the cert, but redirects from untrusted sites can bypass intended restrictions if the client (curl) reuses the cert. Prerequisites include a web server like Apache or Nginx and a CA for issuing client certs.

## Requirements

1. Web server software (e.g., Apache with mod_ssl or Nginx with SSL module)
2. Root/admin access to the target server
3. Certificate Authority (CA) setup for issuing client certificates
4. HTTPS enabled on port 443

## Defense

Defensive measures and detection strategies:

- Implement strict redirect policies to avoid following external URLs
- Use certificate pinning or host-specific cert validation in clients
- Monitor for anomalous certificate usage across domains via TLS logs

## Objectives

1. Enforce client cert auth on protected paths
2. Create a testable endpoint for vulnerability demonstration
3. Ensure compatibility with curl's TLS handling

## Instructions

### Step 1: Install and Configure Web Server

**Context**: Set up HTTPS with mTLS on the target server.

For Apache, edit ssl.conf:

```bash
# Enable SSLVerifyClient require for protected paths
SSLVerifyClient require
SSLVerifyDepth 1
SSLCACertificateFile /path/to/ca.crt
</Location /secretfile>
```

Restart Apache:

```bash
sudo systemctl restart apache2
```

> This configures the server to demand client certs for /secretfile. Expected output: Server restarts without errors.

### Step 2: Create Protected Resource

**Context**: Add a secret file accessible only with valid cert.

```bash
echo "This is secret content" | sudo tee /var/www/secretfile
```

> Places the file in the web root. Test with curl --cert to verify auth works.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- tls
- authentication
- setup
