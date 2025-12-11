---
tags:
  - gitlab
  - quick-action
  - exploit
type: procedure
tools: []
tactics:
  - '[[TA0009]]'
commands:
  - '[[gitlab-move-quick-action]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[T1190]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: be844d83-b15a-48a1-9d2f-5259287c8abf
created_at: '2025-12-06T06:57:46.328Z'
updated_at: '2025-12-06T06:57:46.328Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
---
# Execute GitLab Move Quick Action

## Summary

This procedure describes how to use the /move Quick Action in a GitLab issue comment to trigger the vulnerability, leading to serialization and exposure of project attributes.

## Description

The /move command, when used in an issue comment, references another project and causes GitLab to serialize its model without access checks, exposing sensitive data in the API response. This is done via a POST to the notes endpoint.

## Requirements

1. Existing GitLab issue
2. Knowledge of target project's full path
3. Permissions to comment on issues

## Defense

Defensive measures and detection strategies:

- Implement access controls on Quick Actions
- Monitor for unauthorized project references in comments

## Objectives

1. Trigger project model serialization
2. Force API response with sensitive data
3. Enable observation of exposed tokens

## Instructions

### Step 1: Enter Quick Action

**Context**: Input the command in the comment field.

**Command** ([[gitlab-move-quick-action]]):
```bash
/move <full path of any other project>
```

> This is entered as text in the GitLab UI comment box.

### Step 2: Submit Comment

**Context**: Post the comment to trigger the request.

Click 'Comment' to submit, initiating the POST request.

> Response is generated with serialized data.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0009]]

### Techniques

- [[T1190]]

### Sub-Techniques



## Commands Used

- [[gitlab-move-quick-action]]

## Tools Used



## Tags

- [[gitlab-move-quick-action]]
- [[gitlab-move-quick-action]]
- [[exploit]]
