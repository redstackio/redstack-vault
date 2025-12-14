---
tags:
  - information-disclosure
  - grafana
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-grafana-metrics]]'
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Vulnerability Scanning]]'
id: 8b9a278e-5641-4881-969d-65db0dc0d25f
created_at: '2025-12-14T17:25:13.473Z'
updated_at: '2025-12-14T17:25:13.473Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Access-Grafana-Metrics-Without-Authentication

## Summary

This procedure exploits a misconfigured Grafana instance by directly accessing the /metrics endpoint without authentication, disclosing sensitive server resource metrics that can reveal internal infrastructure details for further reconnaissance.

## Description

Grafana, a monitoring and visualization tool, exposes Prometheus-compatible metrics at /metrics by default. In this scenario, JetBlue's instance at https://████.jetblue.com/metrics lacks authentication, allowing any unauthenticated user to retrieve data on CPU, memory, disk usage, and other server internals. This information can assist attackers in identifying resource bottlenecks or planning denial-of-service attacks. The procedure assumes public accessibility and uses simple HTTP requests to fetch the data.

## Requirements

1. Public internet access to the target subdomain
2. Basic HTTP client like curl or a web browser
3. No credentials needed due to misconfiguration

## Defense

Defensive measures and detection strategies:

- Enable authentication on Grafana instances using reverse proxies like Nginx
- Restrict /metrics endpoint to internal networks via firewall rules
- Monitor access logs for anomalous requests to /metrics from external IPs

## Objectives

1. Retrieve unauthenticated Grafana metrics
2. Analyze exposed server resource data
3. Map internal infrastructure for advanced attacks

## Instructions

### Step 1: Probe the Metrics Endpoint

**Context**: Verify if the /metrics endpoint is publicly accessible and fetch initial data.

**Command** ([[commands/curl-access-grafana-metrics]]):
```bash
curl -s https://████.jetblue.com/metrics | head -20
```

> This command silently fetches the metrics output and displays the first 20 lines, showing key-value pairs like # HELP go_threads_number Number of OS threads created and # TYPE go_threads_number gauge. Successful execution reveals raw metrics without errors.

### Step 2: Parse and Analyze Metrics

**Context**: Extract useful information from the response for reconnaissance.

**Command** ([[commands/curl-access-grafana-metrics]]):
```bash
curl -s https://████.jetblue.com/metrics | grep 'go_info' -A 5
```

> Filters for Go runtime info, outputting details like language version and environment, helping identify the tech stack.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used

- [[commands/curl-access-grafana-metrics]]

## Tools Used


## Tags

- information-disclosure
- grafana
