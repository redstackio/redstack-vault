---
tags:
  - nextcloud
  - audit-log
  - verify
  - logging-flaw
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ac54270a-0c36-4666-a13b-f222c43c4166
created_at: '2025-12-14T17:29:09.975Z'
updated_at: '2025-12-14T17:29:09.975Z'
verified: false
validated: true
submitted: true
---
# Verify-Audit-Log-Entries

## Summary

This procedure reviews the Nextcloud admin audit log after share modifications to confirm the vulnerability, where unsetting expiration produces a useless entry.

## Description

After performing set and unset actions on a share's expiration, the audit log is examined for completeness. The set action logs properly, but the unset results in an incomplete trail, violating audit requirements and potentially hiding actions. Access the log via admin tools in the web interface.

## Requirements

1. Enabled audit log in Nextcloud
2. Administrative access to view logs
3. Recent share actions performed for reference

## Defense

Defensive measures and detection strategies:

- Enable detailed logging and rotate logs regularly
- Use SIEM integration to detect log gaps
- Test logging periodically for all admin actions

## Objectives

1. Locate entries for share expiration changes
2. Identify the logging deficiency in the unset action
3. Document the incomplete audit trail

## Instructions

### Step 1: Access Audit Log Viewer

**Context**: Navigate to the log interface to search for relevant events.

No command required; use the web UI:

- Log in as admin
- Go to Settings > Logging or Audit Log app
- Filter by time or keywords like "share" or "expiration"

> Log entries list appears, showing timestamps and actions.

### Step 2: Analyze Entries

**Context**: Compare logs for set vs. unset actions to spot the flaw.

No command required; use the web UI:

- Review entry for setting expiration (should be detailed)
- Check entry for unsetting (expect vague or missing details)

> The unset entry is useless, confirming the vulnerability (e.g., logs "share updated" without specifics).

## MITRE ATT&CK Mapping

### Tactics

- None

### Techniques

- None

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[nextcloud]]
- [[audit-log]]
