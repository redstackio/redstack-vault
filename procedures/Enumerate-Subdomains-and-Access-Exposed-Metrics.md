---
id: proc-uuid-1234-5678
tags:
  - information-disclosure
  - metrics-endpoint
  - reconnaissance
  - web
  - ruby
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-head-request-to-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:25:13.350Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Enumerate-Subdomains-and-Access-Exposed-Metrics

## Summary

This procedure involves enumerating subdomains to identify exposed directories like /metrics and accessing them to disclose internal application data, such as garbage collection cycles in Ruby-based web apps, enabling reconnaissance without authentication.

## Description

In this attack scenario, attackers target public-facing web applications by probing subdomains for unprotected endpoints. The /metrics path, often used for monitoring tools like Prometheus, was found accessible on https://gopher.hey.com, revealing sensitive details about the application's internal operations, including durations of garbage collection cycles. This low-impact disclosure can assist in mapping the target's tech stack and performance characteristics for advanced exploitation. Prerequisites include public network access and basic HTTP tools; no credentials are needed due to the lack of authentication at the load balancer.

## Requirements

1. Network access to the target subdomain (e.g., https://gopher.hey.com)
2. HTTP client tool like curl or a web browser
3. Knowledge of common exposed paths (/metrics, /health, etc.)

## Defense

Defensive measures and detection strategies:

- Implement authentication and authorization on all internal endpoints, including metrics
- Use web application firewalls (WAF) to filter access to sensitive paths
- Monitor access logs for anomalous requests to /metrics or similar directories
- Apply rate limiting and IP whitelisting at the load balancer

## Objectives

1. Discover and access unauthenticated endpoints for information gathering
2. Extract internal metrics to understand application behavior
3. Aid in broader reconnaissance without triggering alerts

## Instructions

### Step 1: Enumerate Subdomain Directories

**Context**: Probe the target subdomain to identify exposed paths like /metrics through directory brute-forcing or manual guessing.

**Command** ([[commands/curl-head-request-to-endpoint]]):
```bash
curl -I https://gopher.hey.com/metrics
```

> This HEAD request checks if the endpoint exists and is accessible, returning headers without the body. Expected output includes a 200 OK status if vulnerable, confirming exposure.

### Step 2: Retrieve Metrics Data

**Context**: Fetch the full content of the metrics endpoint to disclose garbage collection details.

**Command** ([[commands/curl-head-request-to-endpoint]] adapted for GET):
```bash
curl https://gopher.hey.com/metrics
```

> This GET request downloads the metrics data. Successful output displays key-value pairs like GC cycle durations, e.g., "gc_duration_seconds{type=\"minor\"} 0.045", providing insights into Ruby's memory management.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/curl-head-request-to-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- information-disclosure
- metrics-endpoint
- reconnaissance
- web
- ruby
