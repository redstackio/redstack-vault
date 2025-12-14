---
tags:
  - mediawiki
  - access-control
  - dos
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-access-mediawiki-config]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: daf25a80-edaa-412a-8580-18d98d52592b
created_at: '2025-12-14T17:28:58.922Z'
updated_at: '2025-12-14T17:28:58.922Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-MediaWiki-Config-Page-Without-Auth

## Summary

This procedure exploits improper access control in MediaWiki installations where the configuration page (/mw-config/index.php) is publicly accessible without authentication, allowing attackers to view sensitive setup options and restart the installation, leading to service disruption or denial of service.

## Description

MediaWiki, a popular wiki platform often used for knowledge bases, includes a configuration interface at /mw-config/index.php intended for initial setup and administrative tasks. In vulnerable deployments, this endpoint lacks proper access restrictions, enabling any unauthenticated user to reach it via direct navigation. The page exposes a 'restart installation' button that, when activated, resets the wiki's configuration process, potentially wiping settings and causing the application to restart. This can result in temporary downtime or complete service denial, especially impactful on critical assets like DoD systems. The attack requires only HTTP access to the target and exploits a configuration error rather than a code flaw.

## Requirements

1. Network connectivity to the target MediaWiki web server (HTTP/HTTPS on ports 80/443)
2. Knowledge of the base URL of the MediaWiki instance
3. A web browser or HTTP client like curl for verification and interaction

## Defense

Defensive measures and detection strategies:

- Enforce authentication and authorization on all administrative endpoints, including /mw-config/, using MediaWiki's built-in access controls or web server rules (e.g., Apache .htaccess or Nginx location blocks)
- Monitor web server logs for unauthorized access attempts to /mw-config/ paths, alerting on suspicious GET/POST requests without valid sessions
- Regularly audit MediaWiki configurations post-installation to ensure sensitive directories are protected
- Implement web application firewalls (WAF) to block direct access to setup endpoints

## Objectives

1. Gain unauthorized access to the MediaWiki configuration interface
2. Trigger the installation restart to disrupt service availability
3. Demonstrate potential for denial of service on the target system

## Instructions

### Step 1: Verify Public Accessibility

**Context**: Confirm that the configuration page is exposed without authentication by sending an HTTP request to the endpoint.

**Command** ([[commands/curl-access-mediawiki-config]]):
```bash
curl -i https://target-domain.com/mw-config/index.php
```

> This command performs a HEAD request with headers to retrieve the response status and content. Expected output includes a 200 OK status and HTML body containing the configuration form, indicating no auth redirect (e.g., no 302 to login). If successful, the response will show elements like the 'restart installation' button in the HTML.

### Step 2: Interact and Restart Installation

**Context**: Use a browser to load the page and execute the restart action, as the button requires user interaction.

**Command** (No CLI equivalent; use browser):

Navigate to `https://target-domain.com/mw-config/index.php` in a web browser.

> Locate and click the 'restart installation' button on the loaded page. This submits a form that reinitializes the MediaWiki setup. Expected output: The page refreshes or redirects, and the wiki becomes temporarily unavailable (e.g., 503 or blank page), confirming the DoS impact. Verify by attempting to access the main wiki page, which should fail during restart.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-mediawiki-config]]

## Tools Used


## Tags

- [[mediawiki]]
- [[access-control]]
- [[dos]]
