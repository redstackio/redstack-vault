---
tags:
  - shodan
  - reconnaissance
  - exposed-service
type: procedure
tools:
  - '[[tools/Shodan]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/shodan-search-docker]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:30.942Z'
sub_techniques: []
id: 8394e649-cf00-45a1-bd9b-30d14e755126
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Exposed Docker Registry with Shodan

## Summary

This procedure uses Shodan to scan for exposed Docker Registry HTTP API v2 instances on .mil domains in the US, identifying unauthenticated registries vulnerable to enumeration and exploitation.

## Description

In this attack scenario, an attacker leverages Shodan's search capabilities to find internet-exposed Docker Registries without authentication. The target environment is public-facing services on military domains (.mil), often misconfigured. Expected outcomes include identifying IP addresses of vulnerable registries, enabling further enumeration of confidential Docker images containing source code.

## Requirements

1. Shodan account with API access
2. Internet connectivity
3. Basic knowledge of search dorks

## Defense

Defensive measures and detection strategies:

- Restrict registry access to internal networks or VPN
- Implement authentication (e.g., token-based) on Docker Registry
- Monitor Shodan for exposures and use web application firewalls (WAF) to block scans

## Objectives

1. Identify exposed Docker Registries on specific domains
2. Gather IP and port details for follow-up attacks
3. Confirm lack of authentication

## Instructions

### Step 1: Perform Shodan Search

**Context**: Use a targeted dork to find Docker Registries on .mil domains.

**Command** ([[commands/shodan-search-docker]]):
```bash
shodan search 'ssl.cert.subject.cn:*.mil country:"US" http.status:200 product:"Docker Registry HTTP API"' --fields ip_str,port,hostnames
```

> This command queries Shodan for services matching the criteria, returning IPs, ports, and hostnames. Expected output is a list of matching devices, such as an IP with a .mil certificate.

### Step 2: Verify Exposure

**Context**: Manually check the identified IP for accessibility.

**Command** ([[commands/curl-basic-probe]]):
```bash
curl -I https://TARGET_IP/v2/
```

> Probes the registry root endpoint. Success if HTTP 200 or 401 (but no auth challenge for v2 endpoints).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/shodan-search-docker]]
- [[commands/curl-basic-probe]]

## Tools Used

- [[tools/Shodan]]

## Tags

- shodan
- reconnaissance
- docker
