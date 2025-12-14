---
tags:
  - verification
  - profile-check
  - disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.082Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1460b86f-a393-4912-b5cb-08fd782edebe
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-User-Profile-Email-Hiding

## Summary

This procedure verifies that user emails obtained via GraphQL are not visible on public profiles, confirming the information disclosure.

## Description

After querying emails, navigate to a user's public profile (e.g., https://gitlab.com/username) to compare visibility. GitLab profiles show only public info like username and avatar, hiding emails by design. This step validates the vulnerability's impact in a web-based GitLab environment, requiring no special tools. Outcomes include proof of private data exposure via API but not UI.

## Requirements

1. Username from GraphQL query results
2. Web browser
3. Internet access to gitlab.com

## Defense

Defensive measures and detection strategies:

- Ensure consistent visibility rules across API and UI
- Block public access to sensitive profile fields
- Use DLP tools to scan for email leaks in API responses

## Objectives

1. Confirm email privacy on public profiles
2. Validate disclosure exclusivity to API
3. Assess risk for targeted attacks

## Instructions

### Step 1: Navigate to Profile

**Context**: Use a fetched username to access the public profile page.

No command required; browser navigation.

> Enter https://gitlab.com/[username] in the address bar, replacing [username] with a value from the query (e.g., https://gitlab.com/root).

### Step 2: Inspect Profile Content

**Context**: Check for email presence to confirm hiding.

Scroll through the profile sections.

> The page displays username, avatar, bio, and activity, but no email field. Compare against the GraphQL email (e.g., root@example.com) to verify it's absent, proving disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- profile-verification
- email-privacy
- web-ui
