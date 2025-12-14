---
id: ac-who-cron-dos-001
tags:
  - access-control
  - dos
  - gcp
  - appengine
  - cron-job
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - GCP
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Cron-Configuration-for-Internal-Endpoints]]'
  - '[[procedures/Test-Access-to-Internal-Cron-Endpoint]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:28.957Z'
description: >-
  Attack chain exploiting misconfigured access controls on an internal cron job
  endpoint in the WHO COVID-19 Mobile App, allowing unauthorized triggering of
  resource-intensive operations for potential denial-of-service.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Public Access to Internal Cron Job Endpoint for DoS in WHO COVID-19 App

Multi-stage attack chain demonstrating the discovery and exploitation of improper access controls on the /internal/cron/refreshCaseStats endpoint in the WHO COVID-19 Mobile App. The vulnerability arose from a GCP project migration that broke production environment checks, making the endpoint publicly accessible. Attackers can trigger resource-intensive case statistics refresh operations, leading to backend overload and potential DoS without exposing sensitive data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Review Cron Config] --> B[Test Endpoint Access]
    B --> C[Trigger DoS via Repeated Requests]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web application hosted on Google Cloud Platform (GCP) App Engine
- Access to public GitHub repository for configuration files
- No specific ports required; standard HTTPS (443)

### Initial Access Requirements

- Public internet access
- No credentials needed due to misconfiguration
- Ability to read GitHub repositories

## Detailed Attack Procedures

### Step 1: Review Cron Configuration
procedure: [[procedures/Review-Cron-Configuration-for-Internal-Endpoints]]

**Objective**: Identify internal endpoints exposed in cron schedules by examining public configuration files.

**Instructions**: Access the publicly available cron.yaml file on GitHub to locate scheduled internal endpoints. Navigate to the specific line revealing the endpoint and its schedule.

**Expected Output**: Identification of the /internal/cron/refreshCaseStats endpoint scheduled every 5 minutes.

**Success Indicators**:
- Endpoint URL and schedule details extracted
- Confirmation of internal designation

### Step 2: Test Access to Internal Endpoint
procedure: [[procedures/Test-Access-to-Internal-Cron-Endpoint]]

**Objective**: Verify unauthorized access to the internal cron endpoint and measure its resource intensity.

**Instructions**: Use [[commands/curl-test-internal-cron-access-verbose]] to send a GET request to the endpoint and observe the response time and status.

```bash
time curl -v https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

Repeat requests to simulate DoS by overwhelming the backend with the 'refreshCaseStats' operation.

**Expected Output**: 200 OK response after ~20 seconds, indicating successful unauthorized execution.

**Success Indicators**:
- Response time exceeds 10 seconds, confirming resource-intensive operation
- No authentication prompt or error for unauthorized access

## Attack Chain Summary

### Key Achievements

1. Discovered misconfigured internal endpoint via public GitHub cron.yaml
2. Confirmed public accessibility and resource drain potential
3. Demonstrated DoS risk through repeated endpoint triggers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
