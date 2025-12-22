---
tags:
  - idor
  - access-control-bypass
  - github
  - private-repo-leak
  - code-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - GitHub Enterprise Server
complexity: medium
procedures:
  - '[[procedures/Identify-Target-Private-Repository]]'
  - '[[procedures/Obtain-Target-Repository-Branches-Tags-or-Commits]]'
  - '[[procedures/Create-Diff-to-Leak-Private-Code]]'
step_count: 3
techniques:
  - '[[T1213.003]]'
description: >-
  An attack chain exploiting improper access controls in GitHub Enterprise
  Server's repository diff functionality to leak limited code from private
  repositories using authenticated access.
skill_level: intermediate
impact_level: high
id: 03e706f8-58a8-438c-a2ef-8408d484d934
created_at: '2025-12-14T17:30:58.331Z'
updated_at: '2025-12-14T17:30:58.331Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# IDOR in GitHub Enterprise Server Diff Feature for Unauthorized Private Repo Code Access

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in GitHub Enterprise Server's repository comparison feature to disclose limited code from private repositories.

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
    A[Identify Target Repo] --> B[Gather Repo Details]
    B --> C[Trigger Diff to Leak Code]
    C --> D[Exfiltrate Code Snippets]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or API client for GitHub interactions

### Target Environment

- GitHub Enterprise Server versions prior to 3.18 (specifically vulnerable in <3.14.17, <3.15.12, <3.16.8, <3.17.5)
- Required services/ports: HTTPS (443) for web interface
- Network access requirements: Authenticated access to any repository on the instance

### Initial Access Requirements

- Valid authenticated user account with access to at least one repository
- Prior knowledge of the target private repository's name
- No elevated privileges required beyond basic authentication

## Detailed Attack Procedures

### Step 1: Identify Target Private Repository
procedure: [[procedures/Identify-Target-Private-Repository]]

**Objective**: Locate a private repository owned by another user to target for unauthorized access.

**Instructions**: Use social engineering, previous interactions, or internal knowledge to identify the name of a private repository you do not have access to. No direct technical commands are needed; this step relies on reconnaissance of repository names through shared contexts or leaks.

**Expected Output**: The exact name of the target private repository.

**Success Indicators**:
- Target repository name confirmed
- Attacker lacks explicit access permissions to it

### Step 2: Obtain Target Repository Branches, Tags, or Commit SHAs
procedure: [[procedures/Obtain-Target-Repository-Branches-Tags-or-Commits]]

**Objective**: Gather specific identifiers (branches, tags, or commit SHAs) from the target private repository to enable the diff trigger.

**Instructions**: Leverage any available indirect sources such as commit references in public issues, webhooks, or external leaks to obtain branch names (e.g., 'main'), tags (e.g., 'v1.0'), or commit SHAs. If partial access exists via shared resources, query these details manually through the GitHub UI or API where possible without direct repo access.

**Expected Output**: List of usable branches, tags, or commit SHAs for the target repo.

**Success Indicators**:
- At least one valid branch, tag, or SHA obtained
- Identifiers confirmed as belonging to the private repo

### Step 3: Create Diff to Leak Private Code
procedure: [[procedures/Create-Diff-to-Leak-Private-Code]]

**Objective**: Exploit the diff functionality to retrieve and disclose limited code snippets from the private repository.

**Instructions**: Navigate to the repository comparison feature in the GitHub Enterprise Server web interface using your accessible repository as the base. Specify the target private repository name along with the obtained branches/tags/commits to generate the diff. The system will render limited code content from the private repo in the comparison view due to improper access checks.

**Expected Output**: Diff view displaying unauthorized code snippets from the private repository.

**Success Indicators**:
- Code from private repo visible in diff output
- Confirmation of leak without triggering alerts

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls on private repositories using authenticated session
2. Disclosed limited source code without direct permissions
3. Demonstrated IDOR in repository diff feature affecting GitHub Enterprise Server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1213.003]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---
*Last updated: 2024-10-01T00:00:00Z*
