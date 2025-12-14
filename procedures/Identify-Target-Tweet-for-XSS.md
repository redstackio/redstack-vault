---
tags:
  - recon
  - twitter
  - tweet-id
type: procedure
tools:
  - '[[tools/twitterdetect]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:20.498Z'
sub_techniques: []
id: 09e155c7-a298-47d1-9906-0cc9b84cc6f7
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-Target-Tweet-for-XSS

## Summary

This procedure identifies a suitable tweet for XSS exploitation, ensuring the victim follows the author but has not favorited the tweet to maximize interaction likelihood.

## Description

In the context of Twitter's intent favorite XSS, select a tweet ID where the victim is a follower but the tweet is unfavorited. This setup encourages the victim to engage with the favorite intent without prior action. Use manual inspection or tools like twitterdetect.html for probing followed/favorited status via side-channel behaviors.

## Requirements

1. Access to victim's Twitter follows (via observation or prior recon)
2. Knowledge of specific tweet IDs
3. Web browser for verification

## Defense

Defensive measures and detection strategies:

- Monitor unusual tweet interactions or favorite attempts
- Implement rate limiting on intent endpoints
- Educate users on suspicious links

## Objectives

1. Locate exploitable tweet
2. Confirm victim's interaction potential
3. Prepare for payload integration

## Instructions

### Step 1: Research Victim's Follows

**Context**: Determine accounts the victim follows to select relevant tweets.

Browse the victim's Twitter profile or use side-channel tools to identify followed users.

### Step 2: Select Unfavorited Tweet

**Context**: Find a tweet from a followed user that remains unfavorited.

Search for tweet ID (e.g., 440322224407314432) and verify status; use [[tools/twitterdetect]] if needed for probing.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/twitterdetect]]

## Tags

- [[recon]]
- [[twitter]]
