---
id: proc-discover-wsdl
tags:
  - reconnaissance
  - wsdl
  - soap
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:15:10.097Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Discover Browsable WSDL Service

## Summary

This procedure involves scanning and accessing a target domain to identify exposed WSDL files for SOAP web services, enabling reconnaissance of API endpoints without authentication.

## Description

In the context of the Starbucks API on starbucks.com.cn, the attacker locates a WSDL service on a non-standard port, which is browsable and reveals service functions. This step maps the attack surface for further exploitation, such as unauthenticated data access. Prerequisites include public access to the domain and basic web navigation tools.

## Requirements

1. Internet access to the target domain (starbucks.com.cn)
2. Web browser or curl for HTTP requests
3. Knowledge of common API ports and paths (e.g., /wsdl or non-standard ports)

## Defense

Defensive measures and detection strategies:

- Restrict WSDL access to authenticated users or internal networks
- Use web application firewalls (WAF) to block unauthorized endpoint access
- Monitor logs for unusual requests to API ports

## Objectives

1. Identify exposed SOAP/WSDL services
2. Enumerate available functions for potential vulnerabilities
3. Confirm unauthenticated access

## Instructions

### Step 1: Scan for API Endpoints

**Context**: Use directory enumeration or direct port scanning to find the WSDL service on non-standard ports.

**Command** (Manual browser access or curl):
```bash
curl http://starbucks.com.cn:nonstandardport/?wsdl
```

> This retrieves the WSDL XML if the service is browsable. Expected output: XML describing service operations.

### Step 2: Parse WSDL Content

**Context**: Review the WSDL to list functions like user listing or data queries.

**Command** (Use browser or XML viewer):
```bash
# Open in browser or use xmllint for parsing
xmllint --format wsdl.xml
```

> Expected output: Formatted XML with <operation> tags showing functions.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[wsdl]]
- [[soap]]
