---
id: proc-uuid-001
tags:
  - ssrf
  - recon
  - apache-solr
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-solr-presence]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.450Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Apache-Solr-Presence-via-Admin-Endpoint

## Summary

This procedure verifies the exposure of Apache Solr on a target web server by querying the admin cores endpoint, confirming the presence of vulnerable versions for SSRF exploitation.

## Description

In an attack scenario targeting public-facing web applications, this step involves sending a crafted GET request to the Solr admin endpoint to retrieve core information in JSON format. It targets environments where Solr is integrated with IIS or similar web servers, allowing attackers to fingerprint the service without authentication. Successful execution indicates the target is running Solr prior to version 8.8.2, vulnerable to CVE-2021-27905.

## Requirements

1. Network access to the target domain over HTTPS/HTTP
2. [[tools/curl]] installed for request execution
3. Target exposing Solr admin paths without restrictions

## Defense

Defensive measures and detection strategies:

- Restrict access to Solr admin endpoints via IP allowlisting or authentication
- Monitor access logs for unusual GET requests to /solr/admin/cores
- Upgrade Solr to version 8.8.2 or later to patch SSRF

## Objectives

1. Confirm Solr service availability and core details
2. Fingerprint the environment for further exploitation
3. Validate no immediate access controls

## Instructions

### Step 1: Send Verification Request

**Context**: Execute a GET request to the Solr admin endpoint to retrieve JSON-formatted core information, spoofing browser headers to evade basic filters.

**Command** ([[commands/curl-verify-solr-presence]]):
```bash
curl -i -s -k -X $'GET' -H $'Host: www.example.com' -H $'User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36' -H $'Accept-Language: en' -H $'Connection: close' -H $'Accept-Encoding: gzip' -H $'Content-Length: 6' --data-binary $'TEST\x0d\x0a' $'https://www.example.com/solr/admin/cores?wt=json'
```

> This command sends a GET request with spoofed headers and minimal binary data. Expected output is a 200 OK response with JSON containing core names and status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-solr-presence]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- recon
- apache-solr
