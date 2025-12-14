---
tags:
  - wordpress
  - xmlrpc
  - verification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/xmlrpc-system-listmethods]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.326Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f0955f2c-f994-40dc-a722-8d90b62ec5f3
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-xmlrpc-php-Endpoint

## Summary

This procedure checks if the xmlrpc.php endpoint is enabled on a WordPress site by sending an XML-RPC request to list available methods, confirming vulnerability to pingback-based attacks.

## Description

In WordPress installations, xmlrpc.php is often left enabled, exposing XML-RPC methods like pingback.ping that can be abused for DDoS. This step uses a system.listMethods call to verify the endpoint's availability without triggering resource-intensive actions. It targets public-facing WordPress sites and requires no authentication. Successful verification indicates potential for further exploitation leading to uncontrolled resource consumption on the attacker-controlled server when used in botnets.

## Requirements

1. Network access to the target WordPress site
2. Tool like Burp Suite or curl for HTTP POST requests
3. Knowledge of the target URL (e.g., http://target.com)

## Defense

Defensive measures and detection strategies:

- Disable xmlrpc.php via .htaccess or WordPress plugins
- Monitor for XML-RPC requests in web server logs (e.g., unusual POST to /xmlrpc.php)
- Implement rate limiting on the endpoint

## Objectives

1. Confirm xmlrpc.php is enabled and responsive
2. Identify exposed XML-RPC methods like pingback.ping
3. Assess potential for DDoS abuse

## Instructions

### Step 1: Send system.listMethods Request

**Context**: Invoke the XML-RPC method to list all available functions, verifying the endpoint processes requests successfully.

**Command** ([[commands/xmlrpc-system-listmethods]]):
```bash
curl -X POST http://target.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -H "Accept: */*" \
  -H "Accept-Language: en" \
  -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

> This command sends a POST request with an empty params XML payload. Expected output is an XML response with a <params> array listing methods; success if pingback.ping is included and no faults occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/xmlrpc-system-listmethods]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- wordpress
- xmlrpc
- verification
