---
tags:
  - verification
  - access-bypass
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 5a2da479-7e39-498c-93e0-3339091c7137
created_at: '2025-12-14T17:30:07.253Z'
updated_at: '2025-12-14T17:30:07.253Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Unauthorized-Blog-Creation-on-Lichess

## Summary

Check the new account's blog dashboard to confirm the unauthorized post exists and is manageable, validating the full bypass.

## Description

Post-creation, the blog appears in the ineligible account's profile, allowing further actions like publishing, which could spread unauthorized content and damage Lichess's reputation.

## Requirements

1. New account login
2. Access to blog section

## Defense

Defensive measures and detection strategies:

- Periodic audits of blog ownership
- Alert on blogs created outside eligibility
- User reporting mechanisms for suspicious content

## Objectives

1. Locate the created post
2. Test edit/publish functionality
3. Assess impact potential

## Instructions

### Step 1: Navigate to Blog Dashboard

**Context**: View account's blogs.

Log in as new account, go to profile or blog section (e.g., /@username/blog).

### Step 2: Inspect and Test

**Context**: Confirm presence and actions.

Locate the post, attempt to edit or publish.

**Expected Output**: Post listed, editable, and publishable.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[access-bypass]]
- [[web]]
