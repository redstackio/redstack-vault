---
id: proc-test-ssrf-error-portscan
tags:
  - ssrf
  - port-scanning
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-xmlrpc-error-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:09.758Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Vulnerability Scanning]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Test-SSRF-with-Error-Responses-for-Port-Scanning

## Summary

This procedure leverages SSRF in the XML-RPC pingback endpoint to perform blind port scanning by analyzing differential error responses (faultCodes) from the server when targeting open vs. closed ports on arbitrary hosts.

## Description

By sending requests to non-existent domains or specific ports and observing the server's XML fault codes—16 for access errors and 17 for non-found URIs—attackers can infer port states without direct interaction. This is particularly useful for scanning internal networks behind proxies, discovering backend services, and assessing DoS potential in environments like ASP.NET/IIS.

## Requirements

1. Confirmed SSRF vulnerability from prior procedure
2. HTTP client for repeated POST requests
3. List of target IPs/ports to scan

## Defense

Defensive measures and detection strategies:

- Normalize error responses to avoid information leakage
- Rate-limit XML-RPC requests to prevent scanning
- Log and alert on repeated faultCode occurrences
- Use network segmentation to limit internal access from web servers

## Objectives

1. Differentiate open/closed ports via error codes
2. Map internal network services
3. Identify potential for further exploitation like DoS

## Instructions

### Step 1: Prepare Scan Targets

**Context**: Identify IPs and ports for testing, such as internal hosts (e.g., 127.0.0.1:3306) or external for validation.

No command; compile a list manually.

### Step 2: Execute Error-Based Scan

**Context**: Send SSRF requests to test ports and capture responses for faultCode analysis.

**Command** ([[commands/curl-xmlrpc-error-test]]):
```bash
curl -X POST https://target.com/xmlrpc/pingback/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://non.existent:80/</string></value></param><param><value><string>https://target.com/web/guest/home/</string></value></param></params></methodCall>'
```

> Replace :80/ with target port (e.g., :22/). Expected output: XML with <faultCode>16</faultCode> for closed/inaccessible or 17 for open/non-found. Repeat for multiple ports to build a scan map.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

- [[Vulnerability Scanning]]

## Commands Used

- [[commands/curl-xmlrpc-error-test]]

## Tools Used


## Tags

- ssrf
- port-scanning
