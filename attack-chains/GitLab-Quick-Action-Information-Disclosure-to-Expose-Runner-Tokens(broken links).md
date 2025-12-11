---
tags:
  - gitlab
  - information-disclosure
  - runner-token
  - quick-action
  - "#bug-bounty"
type: attack_chain
tools: []
tactics:
  - "[[Initial Access|TA0001 - Initial Access]]"
  - "[[Collection|TA0009 - Collection]]"
commands:
  - "[[gitlab-move-quick-action]]"
platforms:
  - Web
  - GitLab
complexity: low
procedures:
  - "[[Create GitLab Project]]"
  - "[[Create Issue in GitLab Project]]"
  - "[[Execute GitLab Move Quick Action]]"
  - "[[Observe Exposed Project Data]]"
step_count: 4
techniques:
  - "[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[Data from Information Repositories|T1213 - Data from Information Repositories]]"
description: Multi-stage attack chain exploiting GitLab's Quick Actions to disclose sensitive runner tokens from unauthorized projects
skill_level: beginner
impact_level: high
id: 76de05c2-dd0d-48bf-926f-d80f21ac294e
created_at: 2025-12-06T06:57:46.281Z
updated_at: 2025-12-06T06:57:46.281Z
verified: false
validated: true
submitted: true
mitre_tactics:
  - "[[TA0001]]"
  - "[[TA0009]]"
mitre_techniques:
  - "[[T1190]]"
  - "[[T1213]]"
---
# GitLab Quick Action Information Disclosure to Expose Runner Tokens

Multi-stage attack chain demonstrating how to exploit a vulnerability in GitLab's Quick Actions feature to disclose sensitive information, including runner tokens, from projects without proper access. This allows attackers to register unauthorized runners, access secret variables, and potentially deploy arbitrary code.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Project] --> B[Create Issue]
    B --> C[Execute /move Command]
    C --> D[Observe Exposed Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (GitLab UI only)

### Target Environment

- GitLab.com or self-hosted GitLab instance
- Web browser access
- No specific ports required

### Initial Access Requirements

- Valid GitLab account
- Ability to create projects and issues

## Detailed Attack Procedures

### Step 1: Create Project
**Procedure**: [Create-GitLab-Project](../procedures/Create-GitLab-Project.md)

**Objective**: Set up a project to host the issue where the Quick Action will be executed.

**Expected Output**: A new project created in GitLab.

Use the GitLab UI to create a new project.

**Success Indicators**:
- Project appears in your GitLab dashboard
- You have owner access to the project

### Step 2: Create Issue
**Procedure**: [Create-Issue-in-GitLab-Project](../procedures/Create-Issue-in-GitLab-Project.md)

**Objective**: Create an issue within the project to use as a platform for submitting the Quick Action comment.

**Expected Output**: A new issue created in the project.

Use the GitLab UI to create a new issue in the project.

**Success Indicators**:
- Issue is visible in the project's issues list
- You can add comments to the issue

### Step 3: Execute /move Quick Action
**Procedure**: [Execute-GitLab-Move-Quick-Action](../procedures/Execute-GitLab-Move-Quick-Action.md)

**Objective**: Submit the /move Quick Action in an issue comment to trigger the serialization and exposure of the target project's model attributes.

**Expected Output**: A comment posted with the Quick Action, triggering a POST request.

Enter the Quick Action using [[gitlab-move-quick-action]] in the issue comment field:

```
/move <full path of any other project>
```

Submit the comment, which sends a POST request to /:namespace/:project/notes.

**Success Indicators**:
- Comment appears in the issue
- Network request shows the POST to the notes endpoint

### Step 4: Observe Exposed Data
**Procedure**: [Observe-Exposed-Project-Data](../procedures/Observe-Exposed-Project-Data.md)

**Objective**: Inspect the JSON response from the Quick Action to extract sensitive data like runner tokens.

**Expected Output**: JSON response containing serialized project data, including runners_token and runners_token_encrypted.

Monitor the network response for the POST request and observe the exposed data.

**Success Indicators**:
- JSON includes sensitive attributes
- Runner tokens are visible (encrypted and unencrypted)

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to project model attributes
2. Exposure of runner tokens for potential runner registration
3. Pathway to accessing secret variables and code deployment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques
- [Exploit Public-Facing Application](../techniques/Exploit%20Public-Facing%20Application.md)
- [Data from Information Repositories](../techniques/Data%20from%20Information%20Repositories.md)

### MITRE ATT&CK Tactics

- [Initial Access](../tactics/Initial%20Access.md)
- [Collection](../tactics/Collection.md)

*Last updated: 2025-12-09*
