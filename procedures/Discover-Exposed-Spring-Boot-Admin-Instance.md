---
id: proc-uuid-001
tags:
  - reconnaissance
  - enumeration
  - spring-boot
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-path]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:44.412Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Exposed Spring Boot Admin Instance

## Summary

This procedure involves reconnaissance to identify publicly accessible Spring Boot Admin dashboards by enumerating common administrative paths on a target web application, enabling the discovery of misconfigured instances vulnerable to unauthorized access.

## Description

In scenarios where Spring Boot applications are deployed with default configurations, the Admin dashboard may be exposed without authentication restrictions or behind weak defaults. This procedure simulates attacker reconnaissance by probing for typical endpoints like /admin or /applications, confirming exposure through HTTP responses. It targets web environments and assumes public accessibility, leading to the identification of potential entry points for further exploitation.

## Requirements

1. Network access to the target domain or IP over HTTP/HTTPS
2. Web browser or command-line HTTP client like curl
3. Basic knowledge of Spring Boot Admin default paths

## Defense

Defensive measures and detection strategies:

- Restrict admin interfaces to internal networks via firewall rules or IP whitelisting
- Implement web application firewalls (WAF) to block probes on sensitive paths
- Monitor access logs for anomalous requests to /admin or similar endpoints

## Objectives

1. Confirm the presence of an exposed Spring Boot Admin instance
2. Gather initial intelligence on the target's administrative exposure
3. Validate public accessibility without authentication prompts

## Instructions

### Step 1: Probe Common Admin Paths

**Context**: Enumerate standard Spring Boot Admin endpoints to detect exposure.

**Command** ([[commands/curl-check-path]]):
```bash
curl -I http://target.com/admin
```

> This sends a HEAD request to check for the endpoint's existence. A 200 OK or redirect indicates exposure; 404 suggests it's not present or protected.

### Step 2: Verify Response Content

**Context**: Inspect the response for Spring Boot Admin indicators.

**Command** ([[commands/curl-check-path]]):
```bash
curl http://target.com/admin | grep -i "spring boot admin"
```

> Look for titles, headers, or content confirming the dashboard. Successful detection means the instance is publicly accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-check-path]]

## Tools Used

- [[tools/curl]]

## Tags

- reconnaissance
- enumeration
- spring-boot
