---
tags:
  - gitlab
  - setup
  - roles
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T05:32:13.168Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ba31f073-7899-4957-ba48-0c36d2194772
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Setup-GitLab-Projects-and-Roles

## Summary

This procedure sets up the necessary GitLab environment, including a private project with Reporter role assignment and a source project for the attacking Reporter user, enabling the subsequent privilege escalation attack.

## Description

In a GitLab instance, create a private project and assign the target user Reporter role, which grants read access but not design upload permissions. Then, as the Reporter, create a personal project to serve as the source for attaching designs. This setup exploits the permission model where Reporters can create and manage their own projects but should be restricted from writing designs to others' private projects. Expected outcome: Environment ready for issue creation and migration without alerting on setup actions.

## Requirements

1. Administrative or project owner access to create the private project
2. Reporter account credentials for project creation
3. Access to GitLab web UI via browser

## Defense

Defensive measures and detection strategies:

- Monitor project member additions for unusual role assignments
- Enable audit logs for project creation and role changes in GitLab
- Use role-based access controls strictly and review Reporter permissions periodically

## Objectives

1. Establish a private target project with limited Reporter access
2. Create a source project under Reporter control for design attachment
3. Validate access levels without triggering alerts

## Instructions

### Step 1: Create Private Project

**Context**: As admin or owner, set up the target private project.

**Instructions**: Log in to GitLab, navigate to New Project > Blank project, name it (e.g., 'Private Target'), set visibility to Private, and create it.

> After creation, go to Project > Members > Invite member, search for the Reporter user, assign Reporter role, and send invitation.

### Step 2: Create Reporter Source Project

**Context**: Switch to Reporter account to build the attack source.

**Instructions**: Log in as Reporter, go to New Project > Blank project, name it 'Reporter Project', set visibility (e.g., Internal), and create.

> Confirm project appears in dashboard and Reporter can access Issues section.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[setup]]
- [[roles]]
