---
tags:
  - social-engineering
  - xss
  - twitter
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 89b265d8-f0e0-42d7-8624-3941b04877c5
created_at: '2025-12-14T03:15:53.070Z'
updated_at: '2025-12-14T03:15:53.070Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Induce-Victim-to-Follow-User-via-Malicious-Link

## Summary

This procedure uses social engineering to get the victim to click a malicious link and follow a targeted Twitter user, which is necessary to reach the vulnerable post-follow state in the intent endpoint.

## Description

Upon clicking the crafted link, the victim lands on Twitter's intent/favorite/complete page. Since they don't follow the tweet's author, a follow prompt appears. Inducing the follow action transitions the page to display the vulnerable return link. This step relies on phishing or pretexting to encourage interaction, setting up the XSS trigger.

## Requirements

1. Victim trust in the shared link (e.g., disguised as a tweet recommendation)
2. Access to communication channels for link delivery
3. Knowledge of victim's non-follow status for the target user

## Defense

Defensive measures and detection strategies:

- User education on suspicious links and unexpected follow prompts
- Rate limiting on intent endpoints to detect abuse
- Browser warnings for noreferrer links or unusual navigations

## Objectives

1. Ensure victim navigates to the intent page
2. Prompt and complete the follow action
3. Advance to the return link exposure

## Instructions

### Step 1: Deliver the Link

**Context**: Send the crafted URL to the victim via email, DM, or social post, using a convincing pretext like "Check out this tweet you might like."

No technical command; focus on social engineering.

### Step 2: Monitor Initial Interaction

**Context**: Confirm the victim clicks and reaches the page (e.g., via follow-back notification if controlled account).

Observe if the victim sees the follow button.

### Step 3: Encourage Follow Action

**Context**: If possible, follow up with a message urging "Follow the user to see the full tweet."

The victim clicks 'follow', updating the page.

> Success: Page shows 'return to previous site' after follow.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[social-engineering]]
- [[xss]]
- [[twitter]]
