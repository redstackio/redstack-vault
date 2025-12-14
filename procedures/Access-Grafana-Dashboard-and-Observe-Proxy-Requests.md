---
tags:
  - grafana
  - reconnaissance
  - proxy
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/influxql-flake-rate-query]]'
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.898Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 722895eb-6e92-4c5e-b135-045c3a315c1e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Grafana-Dashboard-and-Observe-Proxy-Requests

## Summary

This procedure involves accessing a public Grafana dashboard in a Kubernetes environment and monitoring network requests to identify proxied InfluxQL queries to the backend InfluxDB, revealing the datasource configuration.

## Description

In Kubernetes test-infra setups, Grafana dashboards like velodrome.k8s.io expose metric visualizations that proxy requests to InfluxDB. By inspecting network traffic, attackers can observe the proxy endpoint (/api/datasources/proxy/4/query) and parameters (db=metrics, q=InfluxQL query), setting the stage for privilege testing. This step requires no authentication and assumes public exposure.

## Requirements

1. Web browser with network inspection tools (e.g., Chrome DevTools)
2. Direct internet access to the Grafana URL (http://velodrome.k8s.io/)
3. Basic understanding of HTTP requests and query parameters

## Defense

Defensive measures and detection strategies:

- Restrict Grafana to authenticated access only
- Monitor for unusual proxy query volumes or patterns in Grafana logs
- Use network segmentation to limit public exposure of monitoring tools

## Objectives

1. Confirm accessibility of the Grafana dashboard
2. Identify the InfluxDB proxy endpoint and query format
3. Gather baseline for privilege escalation testing

## Instructions

### Step 1: Load Grafana Dashboard

**Context**: Navigate to the target Grafana instance to trigger initial requests.

**Command** ([[No specific command, manual browser action]]):

Open http://velodrome.k8s.io/ in a web browser and interact with a dashboard panel showing metrics.

> This loads the page and initiates proxy requests. Expected output: Dashboard renders with charts.

### Step 2: Monitor Network Requests

**Context**: Use developer tools to capture proxied InfluxDB queries.

**Command** ([[commands/influxql-flake-rate-query]]):

Observe GET requests in the Network tab, such as:

```bash
# Example observed request (not executed directly)
GET /api/datasources/proxy/4/query?db=metrics&q=SELECT%201-(sum(%22consistent_builds%22)/sum(%22builds%22))%20FROM%20%22flakes_daily%22%20WHERE%20time%20%3E%20now()%20-%2030d%20AND%20%22job%22%20=~%20/...&epoch=ms
```

> Explanation: Captures the proxy format. Expected output: Request details showing InfluxQL payload and successful JSON response with metrics.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/influxql-flake-rate-query]]

## Tools Used


## Tags

- grafana
- reconnaissance
- proxy
