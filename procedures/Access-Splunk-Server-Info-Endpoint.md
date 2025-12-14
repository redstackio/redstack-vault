---
id: proc-splunk-info-disclosure
name: Access-Splunk-Server-Info-Endpoint
tags:
  - information-disclosure
  - splunk
  - cve-2018-11409
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-splunk-server-info]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:25:13.140Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Access-Splunk-Server-Info-Endpoint

## Summary

This procedure exploits CVE-2018-11409 in Splunk Enterprise versions through 7.0.1 by accessing the unauthenticated `/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json` endpoint to disclose sensitive information such as the Splunk license key, server version, and other configuration details. It is primarily used for reconnaissance in penetration testing or red teaming against exposed Splunk instances.

## Description

The vulnerability stems from inadequate access controls on the Splunk server info endpoint, allowing any unauthenticated user with network access to retrieve JSON-formatted data containing critical server information. This can reveal the license key, which might be reusable on other instances, server hostname, build details, and more. In the reported incident on a U.S. Department of Defense domain, the endpoint was accessed directly via a browser, leading to medium-severity information disclosure. The attack requires no privileges and works over HTTPS on the default Splunk web port (8000). Expected outcomes include obtaining data that aids in further targeting, such as identifying outdated versions or license details for social engineering.

## Requirements

1. Network connectivity to the target Splunk web interface (e.g., https://target:8000)
2. Basic HTTP client like curl or a web browser
3. Knowledge of the Splunk base URL; no credentials or prior access needed

## Defense

Defensive measures and detection strategies:

- Upgrade Splunk to version 7.0.2 or later to patch CVE-2018-11409
- Implement authentication and authorization on all Splunk endpoints using role-based access controls (RBAC)
- Deploy web application firewalls (WAF) to block unauthenticated access to admin endpoints
- Monitor access logs for requests to `/splunkd/__raw/services/server/info` and alert on anomalous IP sources
- Restrict Splunk web interface exposure to trusted networks via firewalls or VPN

## Objectives

1. Gather sensitive server configuration data without authentication
2. Identify Splunk license keys for potential reuse or analysis
3. Perform reconnaissance to map the target's Splunk deployment for follow-on attacks

## Instructions

### Step 1: Request the Server Info Endpoint

**Context**: Directly query the vulnerable endpoint to retrieve JSON data containing sensitive information. Use curl for scripted access or a browser for manual verification. Ignore SSL warnings if self-signed certificates are in use with the `-k` flag.

**Command** ([[commands/curl-splunk-server-info]]):
```bash
curl -k "https://splunk.example.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json"
```

> This command sends an HTTP GET request to the endpoint, bypassing any potential SSL issues. On success, it outputs JSON with fields like `license.key`, `version`, and `serverName`. If the endpoint is protected, expect a 401/403 error; otherwise, sensitive data is exposed immediately.

### Step 2: Parse and Analyze Response

**Context**: Review the JSON output to extract key details such as the license key, which can be used for further reconnaissance or exploitation attempts.

**Command** (Manual parsing or use jq for automation):
```bash
curl -k "https://splunk.example.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json" | jq '.serverInfo.license.key'
```

> Install jq if needed (`apt install jq` on Debian-based systems). This filters the license key from the response. Success is indicated by the key value being printed; use this data to assess impact, e.g., checking if the key is active elsewhere.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/curl-splunk-server-info]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[splunk]]
- [[cve-2018-11409]]
- [[Reconnaissance]]
