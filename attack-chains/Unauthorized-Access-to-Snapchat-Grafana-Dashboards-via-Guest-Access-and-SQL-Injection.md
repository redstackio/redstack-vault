---
tags:
  - grafana
  - fuzzing
  - information-disclosure
  - sqli
type: attack_chain
tools:
  - '[[tools/ffuf]]'
  - '[[tools/curl]]'
  - '[[tools/sqlmap]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/ffuf-fuzz-urls]]'
  - '[[commands/curl-access-grafana]]'
  - '[[commands/sqlmap-test-injection]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-Grafana-Instance-via-Fuzzing]]'
  - '[[procedures/Access-Grafana-Dashboards-as-Guest-User]]'
  - '[[procedures/Exploit-SQL-Injection-in-Custom-Grafana-Module]]'
step_count: 3
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting an exposed Grafana instance with guest access
  and SQL Injection for unauthorized data access
skill_level: intermediate
impact_level: high
id: 467ae446-89f3-46b5-9fad-934e46b00e0a
created_at: '2025-12-11T06:10:16.948Z'
updated_at: '2025-12-11T06:10:16.948Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1595]]'
  - '[[T1190]]'
---
# Unauthorized Access to Snapchat Grafana Dashboards via Guest Access and SQL Injection

Multi-stage attack chain demonstrating discovery and exploitation of an exposed production Grafana instance at Snapchat, allowing unauthorized access to confidential dashboards and potential data manipulation via SQL Injection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance via Fuzzing] --> B[Initial Access as Guest]
    B --> C[Exploit SQL Injection]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ffuf]]
- [[tools/curl]]
- [[tools/sqlmap]]

### Target Environment

- Web-based Grafana instance
- Exposed on public internet
- Services: Grafana

### Initial Access Requirements

- Internet access
- No credentials needed for guest access
- Knowledge of target domain (e.g., snapchat.com)

## Detailed Attack Procedures

### Step 1: Discover Grafana Instance via Fuzzing - [[procedures/Discover-Grafana-Instance-via-Fuzzing]]

**Objective**: Identify exposed Grafana endpoints by fuzzing URL patterns related to Snapchat projects.

**Instructions**: Use [[commands/ffuf-fuzz-urls]] to fuzz potential Grafana paths:

```bash
ffuf -u https://FUZZ.snapchat.com -w wordlist.txt -fc 200
```

Look for responses indicating a Grafana instance, such as login pages or dashboard URLs.

**Expected Output**: List of discovered URLs, including the Grafana instance endpoint.

**Success Indicators**:
- Valid HTTP 200 responses for Grafana-related paths
- Confirmation of accessible instance

### Step 2: Access Grafana Dashboards as Guest User - [[procedures/Access-Grafana-Dashboards-as-Guest-User]]

**Objective**: Gain unauthorized access to production dashboards containing confidential metrics.

**Instructions**: Navigate to the discovered Grafana URL and access as a guest user using [[commands/curl-access-grafana]] for programmatic access:

```bash
curl -i https://discovered-grafana.snapchat.com/login
```

Explore dashboards visible to guests, revealing hundreds of production metrics.

**Expected Output**: HTTP responses showing dashboard data without authentication.

**Success Indicators**:
- Ability to view confidential dashboards
- No authentication prompts for guest access

### Step 3: Exploit SQL Injection in Custom Grafana Module - [[procedures/Exploit-SQL-Injection-in-Custom-Grafana-Module]]

**Objective**: Identify and exploit SQL Injection in a custom module for potential data extraction or manipulation.

**Instructions**: Test the vulnerable module using [[commands/sqlmap-test-injection]]:

```bash
sqlmap -u "https://grafana.snapchat.com/custom-module?param=vulnerable" --batch --dbs
```

If successful, enumerate databases or execute queries.

**Expected Output**: Detection of SQL Injection and potential database listings.

**Success Indicators**:
- Confirmation of SQL Injection vulnerability
- Ability to extract or manipulate data

## Attack Chain Summary

### Key Achievements

1. Discovery of exposed Grafana instance
2. Unauthorized access to confidential dashboards
3. Potential for further compromise via SQL Injection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
