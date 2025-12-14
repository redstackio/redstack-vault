---
tags:
  - recon
  - idor
  - steam
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:29:56.671Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bc110000-68d3-4fce-8b44-1015b0ead72b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-Forum-and-Discussion-IDs-from-Page-Source

## Summary

This procedure involves inspecting the HTML source of a Steam forum discussion page to extract GroupId, forumId, and discussionId, which are required to craft IDOR exploitation requests.

## Description

The Steam Community forum pages embed identifiers in JavaScript variables and HTML attributes. By viewing the page source as a member and searching for patterns like 'forumtopic_', attackers can parse these IDs without additional tools. This reconnaissance step enables direct object referencing in subsequent API calls, bypassing frontend restrictions.

## Requirements

1. Member access to the target forum discussion
2. Web browser with developer tools (e.g., Firefox Inspector)
3. Basic HTML parsing knowledge

## Defense

Defensive measures and detection strategies:

- Obfuscate or dynamically generate IDs in client-side code
- Implement server-side validation to prevent ID-based bypassing
- Monitor for unusual page source access patterns in logs

## Objectives

1. Identify key identifiers for the vulnerable endpoint
2. Prepare parameters for comment fetching requests
3. Ensure IDs correspond to restricted content

## Instructions

### Step 1: Access Discussion Page

**Context**: Navigate to the target discussion using a member account to load the necessary HTML.

Log in to Steam as a member and visit the forum discussion URL, e.g., https://steamcommunity.com/groups/groupname/discussions/discussionId.

### Step 2: Inspect and Extract IDs

**Context**: Use browser tools to find and copy the embedded IDs.

Right-click the page and select 'View Page Source'. Search (Ctrl+F) for 'forumtopic_' to locate strings like 'ForumTopic_103582791461362746_1692659135923574526_1692659769940104935'. Parse to get GroupId (first number), forumId (second), discussionId (third).

**Expected Output**: Three IDs ready for use in POST parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- idor
- steam
