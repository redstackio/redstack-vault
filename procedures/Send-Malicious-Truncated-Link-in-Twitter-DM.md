---
tags:
  - phishing
  - twitter-dm
  - link-truncation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Twitter
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:28:12.914Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 66c3a380-1a8f-4318-b5d7-3fa03a1c7e50
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Send-Malicious-Truncated-Link-in-Twitter-DM

## Summary

This procedure involves crafting and sending direct messages on Twitter containing long malicious URLs that truncate after 38 characters, making them appear as legitimate YouTube links to trick victims into clicking and initiating a phishing chain.

## Description

In the attack scenario, a compromised Twitter account sends DMs to reciprocal followers or users with open DMs. The URL begins with 'accounts.youtube.com/accounts/SetSID' followed by long parameters, truncating to 'accounts.youtube.com/accounts/SetSI...' which looks benign. This exploits Twitter's UI limitation without full URL previews, leading to clickjacking. Prerequisites include control of a Twitter account with followers.

## Requirements

1. Compromised or controlled Twitter account with reciprocal followers
2. Internet access to send DMs
3. Crafted malicious URL with Google SetSID endpoint and redirect parameters

## Defense

Defensive measures and detection strategies:

- Enable Twitter's link preview or warn users about truncated links
- Monitor for unusual DM volumes from accounts
- Educate users to hover/expand links before clicking

## Objectives

1. Lure victim to click disguised phishing link
2. Initiate redirect chain for credential capture
3. Achieve initial access via social engineering

## Instructions

### Step 1: Craft Malicious URL

**Context**: Build a long URL starting with the Google SetSID endpoint to force logout/relogin, including 'continue' parameter pointing to a malicious redirect like getmorefollowers.biz.

No specific command; manually construct URL in Twitter DM composer.

> Example URL: https://accounts.youtube.com/accounts/SetSID?ss=1&continue=https%3A%2F%2Fgetmorefollowers.biz&...

### Step 2: Send DM via Twitter Interface

**Context**: Target reciprocal followers to ensure delivery and higher click rates.

Use Twitter's DM feature to send the message with embedded URL.

> Expected: DM delivered; link truncates in display.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[twitter-dm]]
- [[link-truncation]]
