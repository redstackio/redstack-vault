---
tags:
  - information-disclosure
  - gitlab-badge
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-gitlab-badge]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[T1213.003]]'
updated_at: '2025-12-14T17:29:36.656Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: defe1f42-509e-4b40-9559-27b0e96f5f5e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Access-GitLab-Badge-Endpoint-Unauthorized

## Summary

This procedure demonstrates accessing GitLab's pipeline and coverage badge endpoints without authentication, leaking sensitive build information from restricted projects.

## Description

Badge endpoints like /badges/<branch>/pipeline.svg and /badges/<branch>/coverage.svg lack authorization checks, allowing any user (anonymous for public projects, guests for private) to retrieve SVG images embedding the latest pipeline status and coverage for any branch. This works even if pipelines are private or the repository is disabled, leading to information disclosure across project types.

## Requirements

1. Target GitLab project URL (e.g., https://example.gitlab.com/test/cibadges)
2. Knowledge of branch names (e.g., master)
3. No authentication required for access

## Defense

Defensive measures and detection strategies:

- Implement authorization middleware for badge routes in GitLab
- Monitor anomalous SVG requests in access logs
- Disable or restrict badge generation for private pipelines

## Objectives

1. Retrieve unauthorized pipeline status and coverage data
2. Parse disclosed information for reconnaissance
3. Validate bypass of visibility controls

## Instructions

### Step 1: Identify Badge URLs

**Context**: Construct the endpoint paths for the target project and branch.

For pipeline status: https://example.gitlab.com/test/cibadges/badges/master/pipeline.svg
For coverage: https://example.gitlab.com/test/cibadges/badges/master/coverage.svg
Replace 'example.gitlab.com' with the actual instance and 'master' with the branch.

### Step 2: Fetch Badge Without Authentication

**Context**: Use curl to request the SVG as an unauthorized user.

Execute [[commands/curl-fetch-gitlab-badge]] to verify:

```bash
curl -s https://example.gitlab.com/test/cibadges/badges/master/pipeline.svg > pipeline.svg
curl -s https://example.gitlab.com/test/cibadges/badges/master/coverage.svg > coverage.svg
```

> The command downloads the SVG files; open them in a browser or text editor to view embedded status (e.g., <text>passed</text>) and coverage (e.g., 85.2%).

### Step 3: Analyze Disclosed Information

**Context**: Extract and interpret the leaked data.

Inspect the SVGs for details like build success/failure, branch name, and coverage percentage, confirming disclosure despite restrictions.

**Expected Output**: SVG content revealing pipeline metrics.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-gitlab-badge]]

## Tools Used


## Tags

- information-disclosure
- gitlab-badge
