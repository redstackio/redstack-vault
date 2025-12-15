---
tags:
  - information-disclosure
  - metrics
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-metrics]]'
platforms:
  - Web
techniques:
  - '[[Software]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: d084a7c4-ef96-43ae-9aa8-bec7d43bf83f
created_at: '2025-12-14T17:25:18.158Z'
updated_at: '2025-12-14T17:25:18.158Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Access-Unprotected-Metrics-Endpoint

## Summary

This procedure exploits an unauthenticated /metrics endpoint, commonly used by monitoring tools like Prometheus, to disclose sensitive application and infrastructure metrics. It enables attackers to perform reconnaissance by revealing details such as server load, error rates, and service configurations without any access controls.

## Description

In this attack scenario, the target web application exposes a /metrics endpoint publicly, likely due to a misconfiguration in the monitoring service. By directly accessing this endpoint via HTTP GET, an attacker can retrieve formatted metrics data that provides insights into the backend infrastructure. This was observed on fax.wavecell.com, where visiting https://fax.wavecell.com/metrics returned unredacted sensitive data. The procedure assumes a web-based target with no authentication on the endpoint and can be executed from any network with internet access. Expected outcomes include raw metric exports that could reveal internal system states, aiding in targeted exploitation or further reconnaissance.

## Requirements

1. Internet connectivity to reach the target domain
2. Basic tools like curl or a web browser
3. Knowledge of the target URL (e.g., discovered via external reports or scanning)

## Defense

Defensive measures and detection strategies:

- Implement authentication and authorization on all monitoring endpoints (e.g., basic auth or IP whitelisting for Prometheus)
- Use network-level controls like firewalls to restrict access to /metrics to internal networks only
- Monitor access logs for anomalous GET requests to /metrics and alert on unauthenticated fetches
- Regularly audit exposed services with tools like Nuclei or manual checks

## Objectives

1. Disclose sensitive metrics data for infrastructure reconnaissance
2. Identify potential weaknesses in application performance or configuration
3. Facilitate follow-on attacks by mapping internal services

## Instructions

### Step 1: Verify Endpoint Accessibility

**Context**: Confirm the /metrics endpoint is publicly accessible and returns data without authentication.

**Command** ([[commands/curl-fetch-metrics]]):
```bash
curl -s https://fax.wavecell.com/metrics | head -20
```

> This command silently fetches the metrics and displays the first 20 lines to quickly inspect for sensitive data like # TYPE http_requests_total or server uptime metrics. Expected output includes Prometheus exposition format with help texts and type declarations.

### Step 2: Analyze Retrieved Metrics

**Context**: Parse the full output to extract actionable intelligence, such as high error rates indicating vulnerable components.

**Command** ([[commands/curl-fetch-metrics]]):
```bash
curl -s https://fax.wavecell.com/metrics > metrics.txt
cat metrics.txt | grep -E '^(# TYPE|# HELP|go_)|error'
```

> Save the full response to a file and grep for key indicators like Go runtime metrics (go_ prefix) or error counters. Successful execution reveals infrastructure details without further interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-metrics]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[metrics]]
- [[Reconnaissance]]
