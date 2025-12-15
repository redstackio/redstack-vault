---
id: ac-gitlab-milestones-leak-001
tags:
  - gitlab
  - access-control-bypass
  - information-disclosure
  - api
  - milestones
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Restricted-Public-GitLab-Project]]'
  - '[[procedures/Create-Milestone-in-GitLab-Project]]'
  - '[[procedures/Enumerate-Milestones-via-GitLab-Search-API]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:29.132Z'
description: >-
  Demonstrates improper access control in GitLab's search API, allowing
  non-project members to enumerate milestones in restricted public projects,
  potentially leaking sensitive information like security release details.
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
---
# Milestones Leak via GitLab Search API Access Control Bypass

Multi-stage attack chain demonstrating improper access control in GitLab's search API, where non-project members can access milestone details in public projects restricted to members only. This can lead to enumeration of sensitive project timelines, such as upcoming security patches or release dates.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Restricted Project] --> B[Create Milestone] --> C[Enumerate via API Bypass]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- GitLab instance (self-hosted or SaaS like gitlab.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to GitLab API

### Initial Access Requirements

- Valid GitLab account with project creation permissions
- API token (PRIVATE-TOKEN) for a non-project member user
- No prior project membership needed for the enumeration step

## Detailed Attack Procedures

### Step 1: Setup Restricted Public Project
procedure: [[procedures/Create-Restricted-Public-GitLab-Project]]

**Objective**: Create a public GitLab project and restrict all features to project members only, simulating a controlled environment where non-members should have no access to internal details like milestones.

**Instructions**: Access the project settings in the GitLab UI and configure visibility to public while disabling features for non-members.

**Expected Output**: Project created with ID (e.g., 12345) and all features set to 'Only Project Members'.

**Success Indicators**:
- Project visibility confirmed as public in settings
- Non-member users cannot view issues, merge requests, or other features via UI

### Step 2: Create Milestone
procedure: [[procedures/Create-Milestone-in-GitLab-Project]]

**Objective**: Add a milestone to the restricted project containing potentially sensitive information, which should not be accessible to non-members.

**Instructions**: Use the GitLab UI to create a new milestone with a title and description that might include sensitive details.

**Expected Output**: Milestone created with details like title 'milestone' and description 'milestone', assigned an internal ID (e.g., iid:1).

**Success Indicators**:
- Milestone visible in project milestones list for project members
- Non-members cannot see the milestone in the UI

### Step 3: Enumerate Milestones via Search API
procedure: [[procedures/Enumerate-Milestones-via-GitLab-Search-API]]

**Objective**: As a non-project member, use the search API to bypass restrictions and retrieve milestone details, demonstrating the access control flaw.

**Instructions**: Authenticate with a non-member's API token and query the search endpoint for the milestone term.

Execute [[commands/curl-gitlab-search-milestones]]:

```bash
curl --request GET --header "PRIVATE-TOKEN: <YOUR-TOKEN>" https://gitlab.example.com/api/v4/projects/<project-id>/search?search=milestone&scope=milestones
```

**Expected Output**: JSON array containing milestone details, e.g., {"id":123,"title":"milestone","description":"milestone",...}.

**Success Indicators**:
- API returns milestone data despite restrictions
- Sensitive details like due dates or descriptions are exposed

## Attack Chain Summary

### Key Achievements

1. Successfully restricted a public project to members only
2. Created hidden milestone content
3. Bypassed API controls to leak milestone information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Gather Victim Host Information]] Gather Victim Organization Information

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
