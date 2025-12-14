---
tags:
  - information-disclosure
  - stats
  - json
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-stats]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Software]]'
updated_at: '2025-12-14T17:26:17.221Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 016cfde7-0e36-4cb0-b326-209f2e9a8c5d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Software]]'
---
# Access-Stats-Endpoint

## Summary

This procedure accesses the JSON stats endpoint of InfluxDB to disclose instance statistics, including database counts and time-series data volumes, without authentication.

## Description

The /stats.json endpoint provides operational stats in JSON, revealing configuration and data scale. Exposed publicly, it supports reconnaissance of InfluxDB deployments in Go/Kubernetes environments.

## Requirements

1. Unprotected /stats.json
2. JSON-capable HTTP client

## Defense

Defensive measures and detection strategies:

- Require auth for stats endpoints
- Disable in non-dev environments
- Log JSON stat requests

## Objectives

1. Retrieve InfluxDB statistics
2. Expose data about stored series
3. Map instance configuration

## Instructions

### Step 1: Request Stats

**Context**: Get JSON-formatted instance info.

**Command** ([[commands/curl-access-stats]]):
```bash
curl https://influxdb.quality.gitlab.net/stats.json
```

> Outputs JSON like {"numDatabases": X, "numSeries": Y}, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Software]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/curl-access-stats]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[stats]]
- [[json]]
