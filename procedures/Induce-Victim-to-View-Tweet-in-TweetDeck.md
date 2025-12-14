---
id: proc-uuid-3
tags:
  - xss
  - social-engineering
  - tweetdeck
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:44.226Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Induce-Victim-to-View-Tweet-in-TweetDeck

## Summary

This procedure uses social engineering to get a victim to view the malicious tweet in TweetDeck and click the source info link, triggering the DOM parsing vulnerability.

## Description

The attacker shares the tweet link to entice interaction. In TweetDeck, expanding the tweet exposes the source link, which calls `TD.util.openURL($(n.getMainTweet().source).attr('href'))`, passing the payload to jQuery for HTML parsing. Prerequisites: Public tweet and victim using TweetDeck. Outcome: Payload processed as HTML.

## Requirements

1. Posted malicious tweet
2. Social engineering channel (DM, email, etc.)
3. Victim access to TweetDeck

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links
- Sanitize source rendering in TweetDeck JS
- Log and monitor click interactions on source links

## Objectives

1. Direct victim to TweetDeck view
2. Prompt click on source info
3. Initiate jQuery sink for payload

## Instructions

### Step 1: Share Tweet Link

**Context**: Lure victim with bait.

Send the tweet URL via a channel, using enticing text like 'Click here to get followers ❤️' in the tweet itself.

### Step 2: Victim Opens in TweetDeck

**Context**: Ensure interaction in vulnerable client.

Victim loads TweetDeck, searches or views the tweet, and expands details to see source info.

### Step 3: Trigger Source Click

**Context**: Execute the vulnerable function.

Victim clicks the source link, invoking the jQuery attr extraction on the unsanitized source.

**Expected Output**: jQuery parses payload as HTML elements.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- social-engineering
