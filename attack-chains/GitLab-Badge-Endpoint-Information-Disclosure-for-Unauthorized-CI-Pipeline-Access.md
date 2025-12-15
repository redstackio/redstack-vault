---
tags:
  - information-disclosure
  - gitlab
  - ci-cd
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-GitLab-Project-with-CI]]'
  - '[[procedures/Restrict-GitLab-Project-Visibility]]'
  - '[[procedures/Access-GitLab-Badge-Endpoint-Unauthorized]]'
step_count: 3
techniques:
  - '[[T1213.003]]'
updated_at: '2025-12-14T17:29:36.661Z'
description: >-
  An attack chain exploiting missing authorization checks in GitLab badge
  endpoints to disclose sensitive CI pipeline status and coverage information to
  unauthorized users, even in restricted projects.
skill_level: intermediate
impact_level: high
id: 9e95d09e-940d-4413-9286-17f415ea994b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# GitLab Badge Endpoint Information Disclosure for Unauthorized CI Pipeline Access

Multi-stage attack chain demonstrating how to exploit GitLab's badge endpoints to leak CI pipeline status and coverage details to unauthorized users, bypassing visibility restrictions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Restricted Project] --> B[Configure CI Restrictions]
    B --> C[Access Badge Endpoints]
    C --> D[Disclose Pipeline Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- GitLab account with project creation privileges
- Web browser or curl for accessing endpoints

### Target Environment

- GitLab instance (self-hosted or SaaS)
- Required services: GitLab CI/CD Pipelines
- Network access: Public internet access to GitLab URLs

### Initial Access Requirements

- Valid GitLab user account for setup (attacker simulates victim project)
- No special credentials needed for unauthorized access step
- Prior access: Ability to create and configure projects

## Detailed Attack Procedures

### Step 1: Setup GitLab Project with CI
procedure: [[procedures/Setup-GitLab-Project-with-CI]]

**Objective**: Create a public GitLab project, configure CI pipelines, and push initial code to establish a baseline for testing restrictions.

**Instructions**: Log in to GitLab, create a new project under namespace 'test/cibadges', enable CI/CD, add a basic .gitlab-ci.yml file, and commit/push code to trigger a pipeline.

**Expected Output**: A new project with an initial successful pipeline run.

**Success Indicators**:
- Project created and visible in GitLab dashboard
- CI pipeline executes on push

### Step 2: Restrict Project Visibility and Pipelines
procedure: [[procedures/Restrict-GitLab-Project-Visibility]]

**Objective**: Limit project access to members only and disable public builds to simulate a restricted environment where pipeline info should not be accessible.

**Instructions**: In project settings, set visibility to 'Project Members Only' and in CI/CD settings, disable 'Public pipelines' to restrict build visibility.

**Expected Output**: Updated project settings confirming restrictions.

**Success Indicators**:
- Project requires login for full access
- Pipeline visibility set to private/internal

### Step 3: Access Badge Endpoint as Unauthorized User
procedure: [[procedures/Access-GitLab-Badge-Endpoint-Unauthorized]]

**Objective**: As a non-authenticated user, request badge SVGs to extract pipeline status and coverage, revealing sensitive info despite restrictions.

**Instructions**: Use a browser or curl to access the badge URLs like https://example.gitlab.com/test/cibadges/badges/master/pipeline.svg for status or /badges/master/coverage.svg for coverage. Parse the returned SVG for details.

**Expected Output**: SVG image containing build status (e.g., passed/failed) and coverage percentage.

**Success Indicators**:
- SVG renders with pipeline details without authentication
- Coverage or status info visible for restricted branches

## Attack Chain Summary

### Key Achievements

1. Established a controlled GitLab project with CI pipelines
2. Applied visibility restrictions to mimic real-world private setups
3. Successfully disclosed pipeline information to unauthorized parties via badges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1213.003]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2024-10-01T00:00:00Z*
