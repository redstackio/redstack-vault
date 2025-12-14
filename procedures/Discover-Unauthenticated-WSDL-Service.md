---
tags:
  - unauth-access
  - recon
  - webservice
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.563Z'
sub_techniques: []
id: 04aedc68-7498-4e2d-8e2a-a11a75ed234f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-Unauthenticated-WSDL-Service

## Summary

This procedure involves scanning and identifying an unauthenticated browsable WSDL service on a non-standard port of the target domain, such as starbucks.com.cn, to expose API endpoints without authentication.

## Description

In the attack scenario, the target runs a web service on a non-standard port that exposes a WSDL file browsable without credentials. This allows attackers to understand service functions and prepare for further exploitation. The procedure targets web platforms with SOAP-based services and requires internet access to the domain. Expected outcomes include visibility into service operations, leading to data exposure or injection points.

## Requirements

1. Network access to the target domain (e.g., starbucks.com.cn)
2. Port scanning capabilities (e.g., nmap or browser-based discovery)
3. No authentication or credentials needed

## Defense

Defensive measures and detection strategies:

- Implement authentication on all web services, including WSDL endpoints
- Use web application firewalls (WAF) to block unauthorized access to admin or test services
- Monitor non-standard ports for unusual traffic

## Objectives

1. Identify exposed WSDL services for reconnaissance
2. Map service functions without authentication
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Scan for Non-Standard Ports

**Context**: Use port scanning to locate the WSDL service on non-standard ports.

**Command** (nmap scan):
```bash
nmap -p 1-65535 starbucks.com.cn
```

> This command scans all ports on the domain. Look for open non-standard ports hosting web services.

### Step 2: Access WSDL Endpoint

**Context**: Browse to the suspected endpoint to confirm browsability.

**Command** (curl request):
```bash
curl http://starbucks.com.cn:nonstandardport/service?wsdl
```

> Expected output is the XML WSDL file describing service functions, confirming unauthenticated access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unauth-access]]
- [[recon]]
