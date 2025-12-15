---
id: 123e4567-e89b-12d3-a456-426614174001
name: Trigger Open Redirect with Single Quote
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.219Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - open-redirect
  - phishing
  - url-rewrite
commands:
  - '[[commands/http-get-trigger-open-redirect]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Trigger Open Redirect with Single Quote

## Summary

This procedure exploits an open redirect vulnerability on marketplace.informatica.com by crafting a URL that includes a single quote in the path. The site's flawed URL rewrite rule mishandles the quote, stripping it and issuing a 302 redirect to a protocol-relative URL, allowing redirection to arbitrary external sites. This can be used to enhance phishing attacks by making malicious links appear to originate from the legitimate domain.

## Description

The vulnerability stems from a URL rewrite rule that processes requests containing single quotes by redirecting to the same URL minus the quote, using a protocol-relative Location header (e.g., //external-site.com). Attackers can test this by accessing a URL like https://marketplace.informatica.com//google.com?q=ohdear&a'b (URL-encoded single quote as %27), which triggers a GET request to //google.com?q=ohdear&a' and results in a redirect to //google.com?q=ohdear&a. The target environment is a web application behind BigIP, accessible over standard HTTP/HTTPS. Expected outcomes include successful redirection, confirming the vulnerability for further exploitation in phishing campaigns.

## Requirements

1. Network access to marketplace.informatica.com over HTTP/HTTPS (ports 80/443)
2. An HTTP client like curl or a browser for testing
3. No authentication credentials required

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all redirect URLs to ensure they point to trusted domains only
- Implement strict URL encoding/decoding rules in rewrite configurations to handle special characters like single quotes
- Monitor access logs for unusual 302 redirects to protocol-relative or external domains
- Use Web Application Firewall (WAF) rules to block requests with unescaped single quotes in paths

## Objectives

1. Trigger the open redirect to confirm vulnerability presence
2. Redirect users to a controlled external site to simulate phishing
3. Demonstrate the impact on user trust by mimicking legitimate redirects

## Instructions

### Step 1: Craft and Send Malicious Request

**Context**: Prepare a URL with a single quote in the path to exploit the rewrite rule. This step sends the request and observes the redirect behavior.

**Command** ([[commands/http-get-trigger-open-redirect]]):
```bash
curl -X GET 'https://marketplace.informatica.com//google.com?q=ohdear&a%27b' -H 'Host: marketplace.informatica.com' -H 'Connection: close' -i
```

> This command sends an HTTP GET request to the crafted path //google.com?q=ohdear&a'b (with %27 for the single quote). The server processes it via the flawed rewrite, stripping the quote and responding with a 302 redirect to //google.com?q=ohdear&a. Expected output includes the 302 status, Location header, and server details like BigIP.

### Step 2: Verify Redirect

**Context**: Follow the redirect or inspect the Location header to confirm redirection to the arbitrary site.

**Command** ([[commands/http-get-trigger-open-redirect]] with follow redirect):
```bash
curl -X GET 'https://marketplace.informatica.com//google.com?q=ohdear&a%27b' -H 'Host: marketplace.informatica.com' -H 'Connection: close' -L -i
```

> Adding -L flag follows the redirect. Success is indicated by the client landing on the external site (e.g., google.com in this test), validating the open redirect for phishing use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/http-get-trigger-open-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[url-rewrite]]
