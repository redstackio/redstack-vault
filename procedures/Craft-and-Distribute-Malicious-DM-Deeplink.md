---
tags:
  - xss
  - deeplink
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 91db7e52-ea71-4cdc-b0f1-face864a8d21
created_at: '2025-12-13T23:56:20.417Z'
updated_at: '2025-12-13T23:56:20.417Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft and Distribute Malicious DM Deeplink

## Summary

This procedure involves creating a Twitter Direct Message deeplink with a malicious payload in the text parameter to set up for XSS exploitation, then distributing it via tweet.

## Description

By following Twitter's deeplinking guide, attackers craft URLs that inject unsanitized HTML into DMs. The payload bypasses partial escaping, enabling reflection in the DOM for potential code execution when victims interact.

## Requirements

1. Access to Twitter developer documentation
2. A Twitter account for tweeting
3. Basic URL encoding knowledge

## Defense

Defensive measures and detection strategies:

- Implement proper HTML sanitization on user inputs
- Monitor for suspicious deeplink patterns in tweets

## Objectives

1. Create injectable deeplink
2. Distribute to potential victims
3. Prepare for XSS triggering

## Instructions

### Step 1: Generate Deeplink

**Context**: Create the base deeplink structure.

Follow https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message to set parameters like recipient_id and welcome_message_id.

> This sets up the URL foundation.

### Step 2: Craft Payload

**Context**: Inject XSS payload into text parameter.

Set text to '%3C%3C/%3Cx%3E/script/test000%3E%3C%3C/%3Cx%3Esvg%20onload%3Dalert%28%29%3E%3C/%3E%3Cscript%3E1%3C%5Cx%3E2'.

> This encodes HTML tags for injection.

### Step 3: Tweet Deeplink

**Context**: Post the malicious URL.

Tweet 'https://twitter.com/messages/compose?recipient_id=988260476659404801&welcome_message_id=988274596427304964&text=%3C%3C/%3Cx%3E/script/test000%3E%3C%3C/%3Cx%3Esvg%20onload%3Dalert%28%29%3E%3C/%3E%3Cscript%3E1%3C%5Cx%3E2'.

> Victims clicking this trigger the flow.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- deeplink
