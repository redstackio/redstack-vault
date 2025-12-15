---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - verification
  - snippet
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:57.641Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Unauthorized-Snippet-Creation-in-GitLab

## Summary

This procedure checks the victim's GitLab account for the newly created snippet, confirming the success of the CSRF bypass exploit.

## Description

After the malicious page is visited, inspect the Snippets section in the victim's GitLab account to locate the unauthorized snippet. This validates that the GraphQL mutation executed without CSRF token, using the victim's session. Applicable to any GitLab instance; expected outcome is presence of the test snippet, indicating vulnerability.

## Requirements

1. Access to victim's GitLab account (or their cooperation)
2. Knowledge of the snippet details used in the payload

## Defense

Defensive measures and detection strategies:

- Regularly audit account activity for unexpected changes
- Enable notifications for snippet creation
- Use API rate limiting and logging for mutations

## Objectives

1. Confirm mutation execution
2. Validate bypass of CSRF checks
3. Assess potential for further exploitation

## Instructions

### Step 1: Access Victim's Snippets

**Context**: Log into GitLab and navigate to the Snippets page.

No command; go to https://gitlab.com/users/[username]/snippets

> Look for new entries post-exploit.

### Step 2: Inspect Snippet Details

**Context**: Open the snippet to verify title, content, and creation time.

**Expected Output**: Snippet titled "Tesssst Snippet" with content "This snippet was created via CSRF exploit." and recent timestamp.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[gitlab]]
