---
tags:
  - information-disclosure
  - sap
  - internal-network
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-sap-info]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
id: 45de774a-75df-4018-bfec-5770ed03c715
created_at: '2025-12-14T17:25:13.471Z'
updated_at: '2025-12-14T17:25:13.471Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Expose-SAP-Internal-Information-via-Public-Endpoints

## Summary

This procedure accesses unprotected SAP public info endpoints to disclose internal IP addresses, operating system details, and system configurations, providing attackers with valuable network topology information.

## Description

SAP systems often expose /sap/public/info endpoints for diagnostic purposes, but without access controls, they reveal sensitive details like backend server IPs, OS versions, and SAP module info. In JetBlue's case, endpoints at https://█████████.jetblue.com/sap/public/info and https://████.jetblue.com/sap/public/info are publicly accessible, aiding reconnaissance by mapping internal segments without authentication.

## Requirements

1. Target SAP subdomains publicly resolvable
2. HTTP client for GET requests
3. No login required

## Defense

Defensive measures and detection strategies:

- Disable or restrict /sap/public/info endpoints in SAP configuration
- Implement IP whitelisting or authentication wrappers
- Log and alert on repeated accesses to diagnostic endpoints

## Objectives

1. Fetch exposed SAP system information
2. Extract internal IPs and OS details
3. Use data for targeted internal attacks

## Instructions

### Step 1: Access Primary SAP Info Endpoint

**Context**: Retrieve details from the first exposed endpoint.

**Command** ([[commands/curl-access-sap-info]]):
```bash
curl -s https://█████████.jetblue.com/sap/public/info
```

> Returns HTML or plain text with SAP version, hostnames, and internal IPs. Look for sections like 'System Information' showing OS and network details.

### Step 2: Query Secondary Endpoint

**Context**: Cross-verify with another subdomain for comprehensive data.

**Command** ([[commands/curl-access-sap-info]]):
```bash
curl -s https://████.jetblue.com/sap/public/info
```

> Similar output, potentially revealing additional servers or configurations to build a fuller picture.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

## Commands Used

- [[commands/curl-access-sap-info]]

## Tools Used


## Tags

- information-disclosure
- sap
