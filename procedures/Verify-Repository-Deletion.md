---
id: uuid-verify-deletion
tags:
  - gitlab
  - verification
  - deletion-impact
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/gitlab-env-info]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Inhibit System Recovery]]'
updated_at: '2025-12-14T17:25:53.152Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Inhibit System Recovery]]'
---
# Verify-Repository-Deletion

## Summary

This procedure confirms the success of the exploit by checking for 404 errors on repository actions while the project remains listed, demonstrating data loss impact.

## Description

After mutation, attempt repository operations like creating an empty repo; the project 404s due to deleted storage but persists in the user dashboard. Optionally, run environment info for repro details. This highlights the vulnerability's severity: unauthorized destruction rendering projects inaccessible.

## Requirements

1. Successful mutation execution
2. Access to project page
3. Optional: Server access for rake command

## Defense

Defensive measures and detection strategies:

- Backup repositories regularly
- Monitor for sudden 404s on active projects

## Objectives

1. Validate repository inaccessibility
2. Observe lingering project in list
3. Document environment for report

## Instructions

### Step 1: Attempt Repository Action

**Context**: Test deletion impact.

No specific command; on project page, click 'Create empty repository' or view files.

> Expect 404 error; confirms deletion.

### Step 2: Check Project List

**Context**: Verify project visibility without access.

No specific command; go to dashboard > Your projects.

> Project listed but clicking leads to 404 on repo ops.

### Step 3: Gather Environment Info

**Context**: Provide details for reproduction.

Execute [[commands/gitlab-env-info]] on server:

```bash
sudo gitlab-rake gitlab:env:info
```

> Output includes versions (e.g., GitLab 12.10.0-ee, Ruby 2.6.5).

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Inhibit System Recovery]]

### Sub-Techniques


## Commands Used

- [[commands/gitlab-env-info]]

## Tools Used


## Tags

- gitlab
- verification
- deletion-impact
