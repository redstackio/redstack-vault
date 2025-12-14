---
id: proc-verify-xmlrpc-access
tags:
  - wordpress
  - reconnaissance
  - xmlrpc
type: procedure
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-xmlrpc]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.556Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# Verify-WordPress-xmlrpc.php-Accessibility

## Summary

This procedure checks if the xmlrpc.php endpoint is enabled on a WordPress site, a common misconfiguration that exposes the application to further attacks like DoS and brute force.

## Description

WordPress enables xmlrpc.php by default, allowing XML-RPC communications for features like pingbacks and remote publishing. However, without proper restrictions, it can be scanned and exploited. This procedure sends a test method call to verify accessibility, confirming the vulnerability in web-based PHP environments. Prerequisites include network access to the target site; expected outcomes are an XML response indicating the endpoint is live.

## Requirements

1. Network access to the target WordPress site (HTTP/HTTPS)
2. curl or similar HTTP client installed
3. Target URL of the WordPress installation

## Defense

Defensive measures and detection strategies:

- Disable xmlrpc.php via plugins like Disable XML-RPC or server configuration
- Monitor access logs for repeated POST requests to /xmlrpc.php
- Implement rate limiting on the endpoint using web application firewalls (WAF)

## Objectives

1. Confirm xmlrpc.php is enabled and responsive
2. Identify potential for DoS or brute force exploitation
3. Gather methods list for further reconnaissance

## Instructions

### Step 1: Send Test XML-RPC Request

**Context**: Craft a simple method call to system.listMethods to probe the endpoint without authentication.

**Command** ([[commands/curl-check-xmlrpc]]):
```bash
curl -s -X POST http://target.com/xmlrpc.php -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

> This command sends a POST request with XML payload. If enabled, expect an XML response listing available methods like demo.sayHello and wp.getUsersBlogs. A 404 or empty response indicates it's disabled.

### Step 2: Validate Response

**Context**: Parse the output to confirm vulnerability.

**Command** ([[commands/grep-xml-methods]]):
```bash
curl -s -X POST http://target.com/xmlrpc.php -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>' | grep -o 'methodName>.*<'
```

> Look for methods related to pingbacks (pingback.ping) or logins (wp.getUsersBlogs) to confirm exploitability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-check-xmlrpc]]
- [[commands/grep-xml-methods]]

## Tools Used


## Tags

- [[wordpress]]
- [[xmlrpc]]
- [[recon]]
