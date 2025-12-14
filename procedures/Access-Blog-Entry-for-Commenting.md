---
id: proc-access-blog-comment
tags:
  - xss
  - recon
  - concrete-cms
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.592Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Blog Entry for Commenting

## Summary

This procedure locates and opens a blog entry in Concrete CMS that allows user comments, providing the input vector for injecting XSS payloads via the Rich Text editor.

## Description

Concrete CMS uses the Elemental theme by default for blog posts. Entries with comments enabled expose a form powered by the Conversations module. This step identifies such a page to prepare for payload insertion. No authentication is required if anonymous commenting is allowed, but the site must have blogging features active.

## Requirements

1. Target site with Concrete CMS and active blog
2. Comments enabled on at least one post
3. Web browser

## Defense

Defensive measures and detection strategies:

- Disable anonymous commenting
- Rate-limit comment submissions
- Log access to comment forms

## Objectives

1. Identify vulnerable comment input point
2. Load the comment form with Rich Text editor
3. Prepare for payload injection

## Instructions

### Step 1: Navigate to Blog

**Context**: Find and open a blog post that supports comments.

No command; use browser navigation:

- Visit the site's blog section (e.g., /blog/)
- Select any entry with a "Add Comment" form
- Use default Elemental theme if applicable

> Expected: Page loads with visible comment section.

### Step 2: Confirm Editor

**Context**: Ensure the Rich Text editor is active.

Inspect the form:

- Look for the TinyMCE editor interface
- Verify Source button availability

> Expected: Editor ready for input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- [[xss]]
- [[recon]]
