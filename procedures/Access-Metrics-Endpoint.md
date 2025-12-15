---
tags:
  - information-disclosure
  - metrics
  - prometheus
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-metrics]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Software]]'
updated_at: '2025-12-14T17:26:17.227Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0887f314-af16-44c2-8a84-fb5912f31f15
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Software]]'
---
# Access-Metrics-Endpoint

## Summary

This procedure retrieves exposed application and system metrics from the InfluxDB metrics endpoint in Prometheus format, disclosing operational details like CPU usage and goroutine counts.

## Description

Public /metrics/ endpoints without auth reveal performance data, aiding in resource mapping or DoS planning. In Go/InfluxDB setups, this includes runtime metrics, useful for reconnaissance on Kubernetes clusters.

## Requirements

1. Target with open /metrics/
2. curl for GET request

## Defense

Defensive measures and detection strategies:

- Authenticate metrics endpoints (e.g., basic auth)
- Expose only via internal networks or VPN
- Monitor for scraping attempts

## Objectives

1. Collect system/application metrics
2. Reveal resource utilization
3. Identify internal states for targeting

## Instructions

### Step 1: Fetch Metrics

**Context**: Get Prometheus exposition data.

**Command** ([[commands/curl-access-metrics]]):
```bash
curl https://influxdb.quality.gitlab.net/metrics/
```

> Returns text with # HELP comments and metric values like go_memstats_heap_alloc_bytes.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Software]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/curl-access-metrics]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[metrics]]
- [[prometheus]]
