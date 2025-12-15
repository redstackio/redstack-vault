---
tags:
  - influxdb
  - discovery
  - permissions
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/influxdb-show-databases]]'
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:51.892Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 79c2a6cf-d819-4a4d-8359-f4ae461caff6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Confirm-Admin-Permissions-on-InfluxDB

## Summary

This procedure confirms admin-level access to InfluxDB by executing a SHOW DATABASES query via the Grafana proxy, listing all databases and indicating full privileges.

## Description

Admin users in InfluxDB can view all databases, including internal ones, whereas read-only users are restricted. By proxying this query, attackers validate the vulnerability's severity, paving the way for drops, dumps, or further manipulations.

## Requirements

1. Functional proxy endpoint with admin access
2. HTTP request tool (curl)
3. Awareness of expected database names in the environment

## Defense

Defensive measures and detection strategies:

- Rotate and secure InfluxDB credentials in Grafana config
- Restrict proxy queries to read-only operations
- Use SIEM to detect sensitive InfluxQL commands like SHOW DATABASES

## Objectives

1. Enumerate all accessible databases
2. Confirm unrestricted admin view
3. Assess scope for further attacks (e.g., DROP DATABASE)

## Instructions

### Step 1: Execute SHOW DATABASES Query

**Context**: Send the query to list databases, confirming admin perms.

**Command** ([[commands/influxdb-show-databases]]):
```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" \
  --data-urlencode "db=metrics" \
  --data-urlencode "q=SHOW DATABASES"
```

> This lists all DBs. Expected output: JSON array with databases like 'metrics', internal stores.

### Step 2: Analyze Response

**Context**: Check for comprehensive list indicating admin access.

No command; parse the JSON response manually.

> Success if all expected/internal DBs visible; failure if limited to 'metrics'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/influxdb-show-databases]]

## Tools Used


## Tags

- influxdb
- discovery
- permissions
