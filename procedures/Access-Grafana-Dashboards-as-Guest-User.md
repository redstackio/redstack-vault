---
tags:
  - grafana
  - information-disclosure
type: procedure
tools:
  - '[[tools/ffuf]]'
  - '[[tools/curl]]'
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ffuf-fuzz-urls]]'
  - '[[commands/curl-access-grafana]]'
  - '[[commands/sqlmap-test-injection]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 1dc7aa2e-bc7a-48d7-a2c9-64b82d20b56b
created_at: '2025-12-11T06:10:16.652Z'
updated_at: '2025-12-11T06:10:16.652Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Access Grafana Dashboards as Guest User

## Summary

This procedure exploits guest access misconfigurations in Grafana to view production dashboards containing confidential data without authentication.

## Description

Once a Grafana instance is discovered, accessing it as a guest user allows browsing of exposed dashboards, revealing sensitive metrics. This is common in misconfigured production environments.

## Requirements

1. Discovered Grafana URL
2. Web access
3. No credentials required

## Defense

Defensive measures and detection strategies:

- Disable guest access in Grafana configurations
- Monitor unauthorized access logs

## Objectives

1. Gain access to dashboards
2. Extract confidential metrics
3. Identify further vulnerabilities

## Instructions

### Step 1: Access Login Page

**Context**: Verify the instance allows guest access.

**Command** ([[commands/curl-access-grafana]]):
```bash
curl -i https://discovered-grafana.snapchat.com/login
```

> Check for guest login options or direct dashboard access.

### Step 2: Browse Dashboards

**Context**: Navigate to dashboard endpoints.

**Command** ([[commands/curl-access-grafana]]):
```bash
curl https://discovered-grafana.snapchat.com/dashboards
```

> Retrieve and parse dashboard data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-access-grafana]]

## Tools Used

- [[tools/curl]]

## Tags

- [[commands/curl-access-grafana]]
- [[information-disclosure]]
