---
tags:
  - auth-bypass
  - browser-exploit
  - path-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:02.010Z'
sub_techniques: []
id: 2b371308-65d2-4951-87a2-e8a72992d86c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Demonstrate-Authentication-Bypass-via-Browser

## Summary

This procedure exploits the identified redirect flaw by accessing protected PHP pages without authentication, causing the browser to ignore the redirect and render sensitive content, resulting in unauthorized access.

## Description

In the Shopify PHP API context, this targets endpoints like index.php and login.php. Without a valid session, the redirect to login.php is issued but not enforced due to missing exit(), allowing the full page to load and disclose paths or API data. This is a low-effort web-based exploit requiring only a browser.

## Requirements

1. Direct network access to the target web application
2. No authentication credentials
3. Modern web browser to handle HTTP redirects

## Defense

Defensive measures and detection strategies:

- Enforce proper redirect termination in all auth code
- Implement client-side checks or additional auth layers (e.g., tokens)
- Monitor access logs for requests to protected pages without sessions

## Objectives

1. Gain unauthorized access to protected API pages
2. Observe information disclosure from rendered content
3. Validate the full impact of the vulnerability

## Instructions

### Step 1: Access Protected Endpoint

**Context**: Navigate to the vulnerable page without a session to trigger the flawed redirect.

Open a browser and visit the index.php endpoint (e.g., http://target.com/shopify_php_api/index.php) without logging in.

> Expected output: Browser ignores the 302 redirect to login.php and displays the page content, bypassing auth.

### Step 2: Verify Disclosure

**Context**: Inspect the loaded page for sensitive information or paths.

Check the response for full path disclosure or API data that should be protected.

> Expected output: Exposure of server paths (e.g., /var/www/shopify_php_api/index.php) and unauthorized resource access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- exploitation
- web-bypass
