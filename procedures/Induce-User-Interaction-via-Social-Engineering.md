---
tags:
  - social-engineering
  - phishing
  - user-interaction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1566.002]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 7cc95022-762c-4882-9371-6defb5154fe9
created_at: '2025-12-14T17:30:35.375Z'
updated_at: '2025-12-14T17:30:35.375Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Induce User Interaction via Social Engineering

## Summary

This procedure uses social engineering tactics to lure a LinkedIn user into visiting the crafted phishing link and holding down the space key, which triggers the manipulated OAuth UI to advance without explicit consent.

## Description

Attackers deliver the phishing link through channels like email or social media, using urgent or legitimate-sounding pretexts related to LinkedIn account verification. The key interaction is instructing the user to "hold space" on the loaded page, exploiting the browser's focus on the authorization button via the URL hash. This simulates a press event, completing part of the OAuth flow. Success depends on the target's compliance and lack of suspicion. Expected outcome is the user unknowingly authorizing the app.

## Requirements

1. Access to communication channels (email, DMs) targeting LinkedIn users
2. Crafted phishing link from prior procedure
3. Basic social engineering skills to craft convincing messages

## Defense

Defensive measures and detection strategies:

- User training on recognizing suspicious keyboard instructions in auth flows
- Browser extensions to warn on hash manipulations in OAuth URLs
- Rate limiting on OAuth initiations from suspicious referrers

## Objectives

1. Deliver the link and elicit the visit
2. Prompt the space key hold to trigger UI event
3. Advance the OAuth process toward authorization

## Instructions

### Step 1: Craft and Send Phishing Message

**Context**: Create a pretext to make the link seem legitimate.

Write a message: "LinkedIn security update: Visit [link] and hold space key to confirm your session." Send via email or LinkedIn DM to targeted users.

### Step 2: Monitor User Engagement

**Context**: Wait for the user to visit and interact.

Use link trackers (e.g., URL shortener analytics) to confirm clicks. Follow up if needed to reinforce the space hold instruction.

### Step 3: Verify Interaction Trigger

**Context**: Ensure the space key hold simulates the button press.

In a test environment, confirm that holding space on the hashed page focuses and activates the auth button, logging the event if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
- [[user-interaction]]
