---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - gitlab
  - api
  - information-leak
  - private-project-leak
type: attack_chain
tools:
  - '[[tools/Curl-for-API-Testing]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Setup-Victim-and-Attacker-Projects-in-GitLab]]'
  - '[[procedures/Prepare-Merge-Request-and-Access-Token-in-GitLab]]'
  - '[[procedures/Exploit-IDOR-in-GitLab-Status-Check-API]]'
step_count: 3
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:20.686Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  the GitLab API to access and leak sensitive information from external status
  checks in private projects across the instance.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
---
# IDOR in GitLab External Status Check API to Leak Private Project Data

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in the GitLab API endpoint for external status check responses. An authenticated attacker can manipulate the 'external_status_check_id' parameter to access status checks from any project on the instance, leaking sensitive data such as private project names, IDs, status check configurations, external URLs, protected branches, and access rules.

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
    A[Setup Environment] --> B[Prepare Attack Resources]
    B --> C[Exploit IDOR and Exfiltrate Data]
    C --> D[Objective: Leak Private Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Curl-for-API-Testing]]

### Target Environment

- GitLab instance (self-hosted or SaaS)
- Required services/ports: HTTPS (443) for GitLab web and API access
- Network access requirements: Direct internet access to the GitLab domain

### Initial Access Requirements

- Authenticated user account with project creation permissions
- Administrative access to create multiple users (for simulation)
- No prior elevated privileges needed beyond standard authenticated access

## Detailed Attack Procedures

### Step 1: Setup Environment
procedure: [[procedures/Setup-Victim-and-Attacker-Projects-in-GitLab]]

**Objective**: Create victim and attacker users, private projects, and configure external status checks to simulate the target scenario.

**Instructions**: Log in as an admin to create users, then as victim01 create a private project and status check. Switch to attacker01 and repeat for the attacker's project, noting the project ID.

**Expected Output**: Two private projects with configured external status checks (IDs 1 for victim, 2 for attacker).

**Success Indicators**:
- Victim project created with status check 'Victim status check' pointing to 'https://victim.hidden.com'
- Attacker project created with status check and project ID recorded as ATTACKID

### Step 2: Prepare Attack Resources
procedure: [[procedures/Prepare-Merge-Request-and-Access-Token-in-GitLab]]

**Objective**: In the attacker's project, create a branch, merge request, and personal access token to enable API interactions.

**Instructions**: Create a new branch in attacker_project, generate a merge request (IID 1), and create a personal access token named TOKEN with sufficient scopes (e.g., api, read_api).

**Expected Output**: Merge request created with IID 1, and a valid access token generated.

**Success Indicators**:
- New branch and merge request visible in the project
- Personal access token created and copied for use

### Step 3: Exploit IDOR and Exfiltrate Data
procedure: [[procedures/Exploit-IDOR-in-GitLab-Status-Check-API]]

**Objective**: Use API calls to first obtain the correct SHA, verify own access, then exploit IDOR to leak victim's status check data.

**Instructions**: Use [[commands/curl-gitlab-status-check-error-sha]] to get the correct SHA from an error response. Then execute [[commands/curl-gitlab-status-check-own]] to confirm own data access. Finally, run [[commands/curl-gitlab-status-check-victim]] with the victim's ID (1) to leak unauthorized info.

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=a&external_status_check_id=2' \
  --header 'Authorization: Bearer <TOKEN>'
```

Follow with the correct SHA in subsequent calls.

**Expected Output**: Error response revealing SHA, then JSON with own status check details, and finally JSON leaking victim's private project data including name, ID, external URL, protected branches, and access rules.

**Success Indicators**:
- Correct SHA obtained from error
- Unauthorized victim data leaked in response, confirming IDOR

## Attack Chain Summary

### Key Achievements

1. Simulated victim and attacker environments with private projects and status checks
2. Prepared API access via merge request and token
3. Exploited IDOR to leak sensitive configuration from private projects

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Web Session Cookie]] Data from Information Repositories
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T12:00:00Z*
