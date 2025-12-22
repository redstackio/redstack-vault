---
id: ac-uuid-001
tags:
  - jwt-leak
  - broken-access-control
  - improper-authentication
  - jira
  - hackerone
type: attack_chain
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Jira-Test-Environment]]'
  - '[[procedures/Access-HackerOne-Integration-Config-as-Basic-User]]'
  - '[[procedures/Extract-and-Use-JWT-to-Claim-Integration]]'
  - '[[procedures/Exploit-Linked-Integration-for-Unauthorized-Access]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.178Z'
description: >-
  Attack chain exploiting broken access control in the HackerOne for Jira plugin
  to leak a JWT token, claim the integration, and gain unauthorized access to
  private Jira projects.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized-JWT-Leak-in-HackerOne-Jira-Integration-for-Project-Access-Escalation

Multi-stage attack chain demonstrating a complete attack workflow exploiting the HackerOne for Jira integration plugin.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Access Config Page]
    B --> C[Extract JWT and Claim]
    C --> D[Exploit Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Developer-Tools]]

### Target Environment

- Jira Cloud instance
- HackerOne for Jira app installed from Atlassian Marketplace
- Basic user privileges in Jira

### Initial Access Requirements

- Access to create or invite users in Jira
- Attacker's HackerOne account
- No admin privileges required for exploitation

## Detailed Attack Procedures

### Step 1: Setup Environment
procedure: [[procedures/Setup-Jira-Test-Environment]]

**Objective**: Create a controlled Jira instance with restricted projects and users to simulate the attack surface.

**Instructions**: Follow the procedure to set up the instance, add a basic user, create private projects, and install the app. Verify user permissions using [[commands/jira-check-project-permissions]]:

```bash
curl -u basic-user:password -X GET "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER_PROJECTS"
```

**Expected Output**: JSON showing `havePermission: false` for basic user.

**Success Indicators**:
- Jira instance created with 8 projects (5 private)
- Basic user added with limited roles
- App installed successfully

### Step 2: Access Config Page
procedure: [[procedures/Access-HackerOne-Integration-Config-as-Basic-User]]

**Objective**: Gain unauthorized access to the integration configuration page as a basic user to expose the JWT.

**Instructions**: Log in as the basic user and navigate to the config endpoint. Use browser dev tools to inspect the page for the JWT link.

**Expected Output**: Page loads with setup prompt containing clickable JWT link.

**Success Indicators**:
- Config page accessible without admin checks
- JWT token visible in link

### Step 3: Extract and Use JWT
procedure: [[procedures/Extract-and-Use-JWT-to-Claim-Integration]]

**Objective**: Extract the JWT and use it to claim the integration on the attacker's HackerOne account.

**Instructions**: Copy the JWT from the link `https://hackerone.com/apps/atlassian/claim-app?jwt=<TOKEN>` and visit it in a browser logged into HackerOne.

**Expected Output**: Integration claimed successfully, linking HackerOne to Jira.

**Success Indicators**:
- HackerOne account linked to Jira instance
- No permission errors during claim

### Step 4: Exploit Access
procedure: [[procedures/Exploit-Linked-Integration-for-Unauthorized-Access]]

**Objective**: Perform unauthorized actions like creating issues in private projects or leaking data.

**Instructions**: Use the linked integration to create issues or link reports. Validate access with [[commands/jira-check-browse-edit-permissions]]:

```bash
curl -u basic-user:password -X GET "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=BROWSE_PROJECTS,EDIT_ISSUES"
```

**Expected Output**: Despite API denial, integration allows actions via over-privileged system user.

**Success Indicators**:
- Issues created in private projects
- Project names leaked
- Admin DoS by claiming integration

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls to obtain admin JWT as basic user
2. Claimed integration without permissions, enabling privilege escalation
3. Accessed and manipulated private Jira projects
4. Demonstrated persistent DoS on admin linking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Credentials In Files]] Credentials In Files
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

---

*Last updated: 2023-10-01T00:00:00Z*
