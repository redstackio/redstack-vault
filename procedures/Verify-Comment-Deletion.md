---
tags:
  - verification
  - deletion
  - impact
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 8acb9ea7-79c0-4523-bd72-5a7cfe4349db
created_at: '2025-12-14T17:28:28.712Z'
updated_at: '2025-12-14T17:28:28.712Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Comment-Deletion

## Summary

This procedure confirms the success of the attack by refreshing the site page after spam reporting, observing the automatic deletion of the target comment due to the reached threshold.

## Description

Once the report count hits the configured limit, IntenseDebate's system auto-deletes the comment without admin intervention. This step validates the vulnerability's impact: unauthorized content removal. Targets the post-report state; no tools needed. Expected outcome: Comment gone, proving abuse feasibility.

## Requirements

1. Completed spam reporting from prior procedure
2. Access to the site page
3. Web browser

## Defense

Defensive measures and detection strategies:

- Notify admins of threshold-based deletions
- Review deleted content logs
- Implement undo or appeal mechanisms for reports
- Correlate deletions with report sources

## Objectives

1. Validate exploitation success
2. Assess impact on content moderation
3. Highlight risks of low thresholds

## Instructions

### Step 1: Refresh Site Page

**Context**: Check for automatic changes post-threshold.

After 10 reports, reload the site's URL.

> Page refreshes; target comment is removed.

### Step 2: Confirm Removal

**Context**: Ensure deletion is permanent.

Search or scroll to verify absence; check moderation dashboard if accessible.

> No trace of comment; logs may show deletion reason as "reports exceeded threshold".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[deletion]]
- [[Impact]]
- [[web]]
