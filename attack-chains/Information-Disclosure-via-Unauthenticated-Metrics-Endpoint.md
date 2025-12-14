---
tags:
  - information-disclosure
  - metrics
  - reconnaissance
  - prometheus
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-metrics]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Access-Unprotected-Metrics-Endpoint]]'
step_count: 1
techniques:
  - '[[Software]]'
description: >-
  A simple reconnaissance attack exploiting an unauthenticated /metrics endpoint
  to disclose sensitive application metrics, aiding infrastructure
  reconnaissance.
skill_level: beginner
impact_level: medium
id: 00be0774-80c8-459d-99f5-affb23fa5e2e
created_at: '2025-12-14T17:25:18.160Z'
updated_at: '2025-12-14T17:25:18.160Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Information Disclosure via Unauthenticated Metrics Endpoint

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None (standard browser or curl)

### Target Environment

- Web platform
- Exposed metrics service (e.g., Prometheus) on port 80/443
- Publicly accessible HTTP/HTTPS endpoint

### Initial Access Requirements

- Internet access
- No credentials required (anonymous access)
- No prior access needed

## Detailed Attack Procedures

### Step 1: Access Metrics Endpoint
procedure: [[procedures/Access-Unprotected-Metrics-Endpoint]]

**Objective**: Retrieve sensitive metrics data from the unauthenticated /metrics endpoint to gain insights into the target's infrastructure, such as application performance, server details, and potential attack surfaces.

**Instructions**: Use [[commands/curl-fetch-metrics]] to fetch the metrics data from the target endpoint:

```bash
curl https://fax.wavecell.com/metrics
```

Alternatively, navigate directly to the URL in a web browser to view the raw metrics output.

**Expected Output**: Raw text output containing Prometheus-formatted metrics, including counters, gauges, and histograms for application health, request rates, and system resources (e.g., lines starting with # TYPE, # HELP, followed by metric_name value timestamp).

**Success Indicators**:
- HTTP 200 response with metrics data
- Presence of sensitive fields like server uptime, error rates, or internal service names
- No authentication prompt or error

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of internal metrics without authentication
2. Gained reconnaissance data on infrastructure for further attacks
3. Demonstrated misconfiguration in monitoring service exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Software]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
