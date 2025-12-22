---
tags:
  - xss
  - discovery
  - slack
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2bf34f76-2b6b-4f6f-bee3-5a78a9d632bb
created_at: '2025-12-13T23:55:38.196Z'
updated_at: '2025-12-13T23:55:38.196Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Discover-javascript-Link-Insertion-in-Editing-Mode

## Summary

This procedure identifies the lack of validation for javascript: URIs in Slack's Markdown editor during editing mode, setting the stage for stored XSS exploitation.

## Description

In Slack's team.slack.com, the Markdown editor in post editing mode does not sanitize javascript: schemes, unlike public links on slack-files.com. By noticing such links in old articles and testing insertions, attackers can confirm the vulnerability. This enables stored XSS where scripts execute in the team's domain context upon clicking during edits.

## Requirements

1. Access to Slack team.slack.com with post editing permissions
2. Browser like Google Chrome for testing
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement URI scheme validation in all editors (block javascript:)
- Monitor for unusual link insertions in WebSocket traffic
- Educate users on avoiding suspicious shared posts

## Objectives

1. Confirm vulnerability existence
2. Understand insertion points
3. Prepare for payload delivery

## Instructions

### Step 1: Review Existing Content

**Context**: Scan old articles or posts for existing javascript: links to hypothesize the issue.

No command required; manually inspect via browser dev tools.

> Look for unescaped URIs in rendered Markdown.

### Step 2: Test Insertion

**Context**: Attempt direct insertion in the editor to verify lack of protection.

Use the Markdown editor to input `[Test](javascript:alert('XSS'))` and preview.

> Expected: Link renders clickable without sanitization; click triggers alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[xss]]
- [[Discovery]]
