---
tags:
  - saml
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:52.151Z'
sub_techniques: []
id: 1fa430ca-e19d-4e88-b64b-20c32706acbd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-SAML-ACS-Endpoint

## Summary

This procedure locates the SAML assertion consumer service (ACS) endpoint on a WordPress site using the OneLogin SAML-SSO plugin, enabling subsequent exploitation of authentication bypass vulnerabilities.

## Description

In the attack scenario, attackers scan or inspect the target WordPress installation to identify if the OneLogin SAML-SSO plugin is active and pinpoint its ACS endpoint at `/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs`. This endpoint processes SAML responses for authentication. The procedure assumes public access to the site and focuses on confirming the plugin's presence without authentication. Expected outcomes include endpoint confirmation, allowing forged response submission leading to admin access.

## Requirements

1. Public HTTP access to the target WordPress site
2. Basic knowledge of WordPress plugin structures
3. Tools for web enumeration (e.g., browser or curl)

## Defense

Defensive measures and detection strategies:

- Monitor plugin directories for unauthorized access attempts
- Enable web application firewall (WAF) rules to block suspicious endpoint probes
- Regularly audit installed plugins for known vulnerabilities

## Objectives

1. Confirm presence of vulnerable OneLogin SAML-SSO plugin
2. Identify exact ACS endpoint URL
3. Prepare for SAML response forgery

## Instructions

### Step 1: Enumerate Plugin Directory

**Context**: Check if the OneLogin SAML-SSO plugin is installed by accessing the plugin path.

No specific command; use a browser or curl to GET `/wp-content/plugins/onelogin-saml-sso/` and look for directory listing or 403/200 response indicating presence.

> If the directory is accessible or returns a non-404, the plugin is likely installed. Expected output: Confirmation of plugin files.

### Step 2: Verify ACS Endpoint

**Context**: Test the specific ACS endpoint for responsiveness.

Use curl to send a simple GET request:

```bash
curl -v 'https://target.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs'
```

> This should return a response (e.g., error or blank page) confirming the endpoint exists. Expected output: HTTP response without 404.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[saml]]
- [[recon]]
