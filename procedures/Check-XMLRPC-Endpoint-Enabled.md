---
id: proc-check-xmlrpc
tags:
  - wordpress
  - xmlrpc
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/list-xmlrpc-methods]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.344Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Check-XMLRPC-Endpoint-Enabled

## Summary

This procedure verifies if the xmlrpc.php endpoint is enabled on a WordPress site by sending an XML-RPC request to list available methods, confirming exposure to brute force and DDoS risks.

## Description

WordPress enables xmlrpc.php by default for features like pingbacks, but it exposes methods such as system.listMethods, wp.getUsersBlogs, and pingback.ping without restrictions. This procedure targets web-facing WordPress installations to detect the endpoint's activity, which can lead to unauthorized access attempts or amplification attacks. Prerequisites include HTTP access to the target site.

## Requirements

1. Network access to the target WordPress site's /xmlrpc.php
2. Tool like curl or Burp Suite for sending POST requests
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Disable xmlrpc.php via plugins like Disable XML-RPC or server configuration
- Monitor for unusual POST requests to /xmlrpc.php in web server logs
- Implement rate limiting on XML-RPC endpoints

## Objectives

1. Confirm xmlrpc.php accessibility
2. Identify exploitable methods for further abuse
3. Assess vulnerability to brute force or DDoS

## Instructions

### Step 1: Send Method List Request

**Context**: This step checks endpoint status by calling system.listMethods, revealing available XML-RPC functions.

**Command** ([[commands/list-xmlrpc-methods]]):
```bash
curl -X POST http://www.iandunn.name/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  -d '<?xml version="1.0" encoding="utf-8"?><methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

> This command sends a POST with an empty params XML payload. Expected output is HTTP 200 with XML array of methods like system.multicall and pingback.ping, confirming the endpoint is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/list-xmlrpc-methods]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- wordpress
- xmlrpc
- reconnaissance
