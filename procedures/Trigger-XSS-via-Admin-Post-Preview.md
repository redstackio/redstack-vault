---
tags:
  - xss
  - execution
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.627Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c42c71e1-9a9a-4966-a027-1d928a33c400
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Admin-Post-Preview

## Summary

This procedure triggers the stored XSS by having a victim preview the draft post in the WordPress admin interface, executing the injected JavaScript in the authenticated context.

## Description

The vulnerability arises from insufficient escaping in the Gutenberg block preview for invalid shortcodes. When an admin previews the draft, the browser renders the payload, allowing JS execution for actions like session hijacking or keylogging.

## Requirements

1. Saved draft post with payload
2. Victim access to WordPress admin
3. Ability to entice preview (e.g., via notification)

## Defense

Defensive measures and detection strategies:

- Sanitize shortcode output in previews
- Disable preview for untrusted drafts
- Monitor JS errors and unusual browser behavior in admin

## Objectives

1. Execute JS in victim's admin browser session
2. Steal sensitive data like cookies
3. Enable further admin compromise

## Instructions

### Step 1: Share Draft Access

**Context**: Provide the victim with a way to access the draft.

Send the draft post URL or notify via WordPress comments/emails.

> Use social engineering if needed to prompt preview.

### Step 2: Initiate Preview

**Context**: Victim performs the preview action.

In the admin dashboard, the victim clicks "Preview" on the draft post.

> The Gutenberg preview renders the invalid block, executing the onerror handler.

### Step 3: Observe Execution

**Context**: Confirm JS runs and assess impact.

Monitor for alert (prompt(1)) or adapt payload to exfiltrate data (e.g., send cookies to attacker server).

> Expected: JS executes; potential access to wp-admin cookies or CSRF tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[wordpress]]
