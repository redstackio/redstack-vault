---
tags:
  - xss
  - url-crafting
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0a6eb2b2-b981-4353-a952-caea5707b8bd
created_at: '2025-12-14T03:15:53.073Z'
updated_at: '2025-12-14T03:15:53.073Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Twitter-Intent-URL-for-XSS

## Summary

This procedure involves constructing a malicious URL targeting Twitter's intent favorite complete endpoint, embedding a JavaScript payload in the original_referer parameter to enable reflected XSS upon user interaction.

## Description

The attack exploits the lack of sanitization in the original_referer parameter. By using a javascript: URI as the referer and nullifying the actual referrer with rel='noreferrer', the payload is preserved and reflected in the 'return to previous site' link. This requires a tweet_id from a user the victim does not follow to force a follow interaction. Successful execution leads to JS in the victim's Twitter context, enabling cookie theft or phishing overlays.

## Requirements

1. Valid tweet_id (e.g., 572435913768366080) from a non-followed user
2. URL encoding knowledge for the payload
3. Method to share the link (email, chat)

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled parameters in redirects (e.g., validate against whitelist of schemes)
- Implement Content Security Policy (CSP) to block inline JavaScript
- Monitor for anomalous referer patterns or javascript: URIs in logs

## Objectives

1. Deliver a clickable link that sets up the XSS payload
2. Ensure null referrer to preserve the malicious original_referer
3. Prepare for victim interaction to trigger reflection

## Instructions

### Step 1: Select Target Tweet and User

**Context**: Choose a tweet_id from a user the victim isn't following to ensure the follow prompt appears.

Use Twitter's search or API to find a suitable tweet_id. Example: 572435913768366080.

### Step 2: Encode JavaScript Payload

**Context**: Create a harmless test payload like alert(1), then URL-encode it for the parameter.

Encoded payload: javascript:alert%281%29

### Step 3: Construct and Embed URL

**Context**: Build the full intent URL and wrap in HTML anchor with rel='noreferrer'.

```html
<a href="https://twitter.com/intent/favorite/complete?tweet_id=572435913768366080&already_favorited=false&original_referer=javascript:alert%281%29" rel="noreferrer" target="_blank">Favorite this interesting tweet!</a>
```

> This sends a null referrer, preserving the parameter. Share via phishing email or message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss]]
- [[twitter]]
- [[url-crafting]]
