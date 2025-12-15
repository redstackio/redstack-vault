---
tags:
  - xmlrpc
  - wordpress
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
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.555Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ad92650e-1a37-4770-af99-cdc2d8dbb848
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-XML-RPC-Endpoint-Accessibility

## Summary

This procedure checks if the xmlrpc.php endpoint on a WordPress site is enabled by sending an XML-RPC request to list available methods, confirming potential for abuse in DDoS or brute force attacks.

## Description

WordPress sites with xmlrpc.php enabled expose XML-RPC services that can be queried for methods like system.listMethods. A successful response lists exploitable functions such as pingback.ping, indicating the endpoint is active and vulnerable to misconfiguration-based attacks. This is common on public-facing sites like NordVPN's, often behind Cloudflare, and serves as the first step in assessing DDoS amplification or credential brute forcing risks.

## Requirements

1. Network access to the target domain (e.g., https://nordvpn.com)
2. Tool for sending custom HTTP POST requests (e.g., curl or Burp Suite)
3. Basic understanding of XML-RPC protocol

## Defense

Defensive measures and detection strategies:

- Disable xmlrpc.php via .htaccess or plugins like Disable XML-RPC
- Monitor for anomalous POST requests to /xmlrpc.php using WAF rules (e.g., Cloudflare)
- Rate-limit XML-RPC endpoints and log method calls for anomalies

## Objectives

1. Confirm xmlrpc.php accessibility and list methods
2. Identify exploitable functions for further attacks
3. Assess server response without triggering alerts

## Instructions

### Step 1: Send system.listMethods Request

**Context**: Craft and send an XML payload to query available XML-RPC methods, verifying endpoint status.

**Command** ([[commands/list-xmlrpc-methods]]):
```bash
curl -X POST https://nordvpn.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="utf-8"?><methodCall><methodName>system.listMethods</methodName><params></params></methodCall>' -v
```

> This command sends a POST with the XML payload. Expected output is an XML response with <array> containing method names like pingback.ping if enabled. Use -v for verbose HTTP details to confirm 200 OK.

### Step 2: Analyze Response

**Context**: Parse the response to confirm exploitable methods.

**Command** (grep for methods):
```bash
grep -o '<methodName>.*</methodName>' response.xml
```

> Filters the XML for method names. Success if methods like wp.getUsersBlogs (for brute force) or pingback.ping (for DDoS) appear.

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

- xmlrpc
- wordpress
- reconnaissance
