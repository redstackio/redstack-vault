---
tags:
  - verification
  - nsfw
  - reddit
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c8240883-5b0a-4145-9233-93b8d375a84e
created_at: '2025-12-14T17:27:57.275Z'
updated_at: '2025-12-14T17:27:57.275Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-NSFW-Content-Block

## Summary

This procedure confirms that the over18 preference is disabled by attempting to access an NSFW subreddit, resulting in a consent prompt.

## Description

As part of the CSRF attack chain, this step validates the initial restricted state. Visiting an NSFW subreddit (e.g., r/nsfw) should trigger Reddit's protection mechanism, displaying a dialog asking for confirmation. This baseline ensures the subsequent CSRF exploit can demonstrate the bypass.

## Requirements

1. Disabled over18 preference
2. Web browser
3. Known NSFW subreddit URL

## Defense

Defensive measures and detection strategies:

- Implement strict age verification beyond simple toggles
- Log access attempts to NSFW content for underage accounts

## Objectives

1. Confirm NSFW access restriction
2. Observe consent prompt
3. Baseline for exploit validation

## Instructions

### Step 1: Navigate to NSFW Subreddit

**Context**: Test the block by directly visiting restricted content.

Enter https://www.reddit.com/r/nsfw (replace with any NSFW subreddit) in the browser address bar.

> Expected: A prompt appears stating 'You must be over eighteen to view this community' or similar, requiring confirmation.

### Step 2: Decline and Confirm Block

**Context**: Ensure the block is enforced by not confirming.

Click 'No' or close the prompt without enabling.

> Expected: Redirected away from content; no NSFW visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[nsfw]]
- [[reddit]]
