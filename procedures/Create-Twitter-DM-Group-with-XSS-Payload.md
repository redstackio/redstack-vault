---
id: proc-twitter-dm-create-xss-001
tags:
  - xss
  - stored-xss
  - twitter
  - dm
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.330Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Twitter DM Group with XSS Payload

## Summary

This procedure creates a Direct Message (DM) group on Twitter with a malicious XSS payload embedded in the group name, storing it unsanitized for later execution against other members.

## Description

In the Twitter DM system, group names are not properly sanitized for HTML/script content during storage. By setting the name to a payload like `<script>alert(1);//`, an attacker can inject JavaScript that executes in the context of any group member's browser when the name is rendered. This targets the web platform's JavaScript engine, affecting users on desktop or mobile web interfaces. Prerequisites include a Twitter account capable of creating groups (up to 150 members). Expected outcome: Payload stored and ready for triggers, potentially compromising multiple victims' sessions.

## Requirements

1. Active Twitter account with DM access
2. Web browser for interface interaction
3. At least one other user to invite (for testing triggers)

## Defense

Defensive measures and detection strategies:

- Implement server-side HTML escaping for all user-input fields like group names
- Use Content Security Policy (CSP) to block inline scripts in DM UI
- Monitor for anomalous JavaScript alerts or network requests from DM interactions

## Objectives

1. Store XSS payload in group metadata
2. Prepare for execution against group members
3. Validate payload persistence without immediate execution

## Instructions

### Step 1: Access DM Creation Interface

**Context**: Navigate to the Messages section to initiate group creation.

Log in to Twitter web, click the envelope icon for Messages, then select 'New message' and choose 'Create a group' or add multiple recipients.

> This opens the group setup dialog where the name can be set.

### Step 2: Set Malicious Group Name

**Context**: Inject the XSS payload during naming to store it unsanitized.

Enter the payload `<script>alert(1);//` as the group name. Add recipients and confirm creation.

> The payload is saved directly; no client-side validation blocks it. Test by viewing the group DM.

### Step 3: Verify Payload Storage

**Context**: Confirm the name renders without execution (until triggered).

Refresh the DM list or view group details. The name should display with the script tag visible in source but not yet executed.

> Success: Payload present in DOM as text; inspect element to confirm `<script>` tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[twitter]]
- [[dm]]
