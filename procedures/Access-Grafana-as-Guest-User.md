---
tags:
  - grafana
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 8371fb70-802c-4334-a91d-837a2df77ec7
created_at: '2025-12-11T03:47:39.550Z'
updated_at: '2025-12-11T03:47:39.550Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Access Grafana as Guest User

## Summary

This procedure accesses an exposed Grafana instance as a guest user to view production dashboards containing confidential metrics.

## Description

Exploiting misconfigured access controls, attackers can navigate to the Grafana URL and browse dashboards without credentials, leading to unauthorized disclosure of sensitive company data.

## Requirements

1. Discovered Grafana URL
2. Web browser or curl for access
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Enforce authentication on Grafana instances
- Log and alert on guest access attempts

## Objectives

1. Gain access to dashboards
2. Extract confidential metrics
3. Identify further vulnerabilities

## Instructions

### Step 1: Test Access

**Context**: Verify the endpoint allows guest access.

**Command** ([[commands/curl-access-grafana]]):
```bash
curl -v https://discovered-grafana.snapchat.com
```

> Expect a 200 OK response with dashboard content.

### Step 2: Browse Dashboards

**Context**: Navigate through available dashboards.

> Use a web browser to explore and capture data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/curl-access-grafana]]

## Tools Used

- #curl

## Tags

- [[commands/curl-access-grafana]]
- #information-disclosure
