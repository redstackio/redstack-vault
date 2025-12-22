---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: View-Reset-Link-in-Daemon-Logs
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:36.694Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Data from Information Repositories]]'
sub_techniques:
  - '[[Sharepoint]]'
tags:
  - log-access
  - information-disclosure
  - phabricator
commands: []
platforms:
  - Web
tools: []
skill_level: medium
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---

# View-Reset-Link-in-Daemon-Logs

## Summary

This procedure accesses Phabricator's daemon logs via the web UI to retrieve the uncensored password reset link for the admin account, exploiting the lack of access controls on log visibility.

## Description

Due to a vulnerability in Phabricator, daemon logs are exposed through the web interface to normal users. When mail delivery fails, entries include full reset URLs/tokens (e.g., https://phabricator.example.com/reset?token=abc123). This information disclosure enables the attacker to bypass email and directly obtain the sensitive data. The logs must be recent, as tokens are time-limited.

## Requirements

1. Authenticated normal user session
2. Recent password reset request during mail disruption
3. Web UI access to daemon logs (e.g., /config/log/ or similar endpoint)

## Defense

Defensive measures and detection strategies:

- Restrict log access to admin users only via role-based access control (RBAC)
- Implement log sanitization to redact tokens and sensitive data
- Use centralized logging with encryption and anomaly detection for access patterns

## Objectives

1. Locate the failed mail delivery log entry
2. Extract the full password reset URL/token
3. Confirm the link's validity before use

## Instructions

### Step 1: Navigate to Logs

**Context**: Access the daemon log viewer in the Phabricator UI.

No command required; from the dashboard, go to Config > Logs or the dedicated daemon log page.

> The UI displays recent log entries. Expected output: Scrollable list of logs, searchable by timestamp or keyword.

### Step 2: Search for Reset Entry

**Context**: Identify the log from the failed reset attempt.

No command required; filter logs by time (around the request submission) or keywords like 'password reset' or 'mail failed'.

> Look for an entry like 'Failed to send reset to admin@example.com: token=abc123 url=https://...'. Success: Plain-text link visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- [[Sharepoint]] Share Configuration Repository

## Commands Used

- None

## Tools Used

- None

## Tags

- [[log-access]]
- [[information-disclosure]]
- [[phabricator]]
