---
tags:
  - persistence
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.635Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1a7f4946-0eef-445b-8c3a-6c3b4cb53b99
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-WordPress-Post-as-Draft

## Summary

This procedure saves the WordPress post containing the malicious shortcode as a draft, ensuring the payload persists without publishing and alerting users.

## Description

After injection, saving as a draft stores the unsanitized content in the database. This step is crucial for stored XSS as it allows the payload to remain hidden until previewed, targeting admin users who review drafts.

## Requirements

1. Edited post with payload in Gutenberg editor
2. WordPress admin access

## Defense

Defensive measures and detection strategies:

- Implement auto-sanitization on save
- Audit draft posts regularly for suspicious content
- Use role-based restrictions on draft creation

## Objectives

1. Persist the injected payload in the database
2. Avoid publication to evade detection
3. Enable future preview triggering

## Instructions

### Step 1: Prepare to Save

**Context**: Ensure the post is in draft status and payload is intact.

Review the post content in the editor.

> Confirm the payload `"><img src=1 onerror=prompt(1)>` is present.

### Step 2: Execute Save

**Context**: Use the draft save function to store the post.

Click the "Save Draft" button in the WordPress editor toolbar.

> WordPress will persist the post; no JS execution occurs at this stage.

### Step 3: Confirm Persistence

**Context**: Verify the draft is saved and accessible.

Navigate to Posts > All Posts and check for the draft.

> Expected: Draft appears in list; editing it shows the payload unchanged.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[wordpress]]
