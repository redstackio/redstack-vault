---
tags:
  - idor
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-quora-channel-target]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.609Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c53b0b09-154a-48fb-8467-9a137bdd75f5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-for-Victim-Channel-Targeting

## Summary

This procedure alters a captured Quora edit request by replacing window_id and _lm_window_id with a victim's channel, exploiting IDOR to deliver responses to arbitrary users.

## Description

Quora's server_call_POST endpoints use window_id for channel-based message delivery without verifying ownership. By swapping these parameters in the POST data, attackers route updates (including malicious ones) to victims' channels, fetched via periodic JSONP polls to tch.quora.com/updates. This chains with XSS for non-interactive delivery. Prerequisites: Captured request and enumerated channel; outcomes: Request modified for targeting without server rejection.

## Requirements

1. Captured normal edit curl command
2. Valid victim channel name
3. Attacker's session cookies

## Defense

Defensive measures and detection strategies:

- Server-side validation of window_id against user session
- Audit logs for mismatched channel targeting
- CSRF tokens tied to specific channels

## Objectives

1. Bypass channel ownership checks
2. Route malicious updates to victims
3. Enable silent payload delivery

## Instructions

### Step 1: Edit Parameters in Curl

**Context**: Replace channel IDs in the captured request.

**Command** ([[commands/curl-quora-channel-target]]):
```bash
# Modify data: change window_id=dep3204-1727465467565139446 to dep3501-3261853912009855464 and _lm_window_id similarly
curl 'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' ... --data '...&window_id=dep3501-3261853912009855464&...&_lm_window_id=dep3501-3261853912009855464&...'
```

> Expected output: Valid modified command; test with dry-run to ensure syntax.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/curl-quora-channel-target]]

## Tools Used

- [[tools/curl]]

## Tags

- idor
- web
