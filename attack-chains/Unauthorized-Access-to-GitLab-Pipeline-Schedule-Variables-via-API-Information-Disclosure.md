---
id: ac-gitlab-pipeline-disclosure-001
name: >-
  Unauthorized Access to GitLab Pipeline Schedule Variables via API Information
  Disclosure
type: attack_chain
description: >-
  Multi-stage attack exploiting GitLab's pipeline schedules API to disclose
  sensitive custom variables to unauthorized authenticated users, enabling
  potential schedule hijacking and secret exposure.
verified: false
submitted: true
step_count: 2
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.687Z'
procedures:
  - '[[procedures/Setup-GitLab-Test-Project-and-Schedule]]'
  - '[[procedures/Exploit-GitLab-Pipeline-API-for-Variable-Disclosure]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Data from Information Repositories]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
tags:
  - gitlab
  - api
  - information-disclosure
  - secrets-leak
  - pipeline
platforms:
  - Web
  - GitLab
tools:
  - '[[tools/curl]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Data from Information Repositories]]'
---

# Unauthorized Access to GitLab Pipeline Schedule Variables via API Information Disclosure

Multi-stage attack chain demonstrating a complete attack workflow exploiting an information disclosure vulnerability in GitLab's pipeline schedules API. An unauthorized user with a personal access token can retrieve sensitive custom variables from pipeline schedules without project membership, violating access controls intended for owners and maintainers only.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Environment] --> B[Exploit API for Disclosure]
    B --> C[Analyze Exposed Secrets]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- GitLab instance (e.g., gitlab.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to GitLab API

### Initial Access Requirements

- Personal access token from a GitLab account (any authenticated user)
- Knowledge of target project ID and pipeline schedule ID
- No project membership required for exploitation

## Detailed Attack Procedures

### Step 1: Setup Test Project and Pipeline Schedule
procedure: [[procedures/Setup-GitLab-Test-Project-and-Schedule]]

**Objective**: Create a controlled environment with a project and pipeline schedule containing sensitive custom variables to simulate the vulnerability.

**Instructions**: Use the GitLab UI to create a new project named 'trigg' (project ID: 20618145) and configure a pipeline schedule (ID: 69918) with custom variables like VAR1=secretvalue, which should be restricted to owners/maintainers.

**Expected Output**: Confirmation of project and schedule creation, with variables set but not yet exposed.

**Success Indicators**:
- Project created successfully
- Pipeline schedule active with custom variables added

### Step 2: Exploit API to Retrieve Schedule Variables
procedure: [[procedures/Exploit-GitLab-Pipeline-API-for-Variable-Disclosure]]

**Objective**: As an unauthorized user, use a personal access token to query the API endpoint and disclose the custom variables.

**Instructions**: Authenticate with curl using the personal access token and target the API endpoint for the specific project and schedule IDs. Execute [[commands/curl-gitlab-pipeline-schedule-fetch]]:

```bash
curl --header "Private-Token: <your_access_token>" https://gitlab.com/api/v4/projects/20618145/pipeline_schedules/69918
```

Review the JSON response for the 'variables' array containing keys and unmasked values.

**Expected Output**: JSON object including {"variables": [{"key":"VAR1","value":"secretvalue"}]}.

**Success Indicators**:
- API response returns without 403/401 error
- Sensitive variable values visible in response

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable pipeline schedule with secrets
2. Unauthorized retrieval of custom variables via API
3. Demonstration of potential for schedule hijacking using exposed secrets

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Data from Information Repositories]] Data from Information Repositories

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
