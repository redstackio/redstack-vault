---
id: proc-send-xss-message-rocket-chat
tags:
  - xss
  - stored-xss
  - message-injection
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
updated_at: '2025-12-13T23:52:38.760Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Send-Stored-XSS-Message-in-Rocket-Chat

## Summary

This procedure involves sending a crafted XSS payload as a message in a Rocket.Chat channel, where it is stored server-side and parsed into malicious HTML, setting up execution upon victim viewing.

## Description

Once the payload is crafted, it is sent via the chat interface. The Rocket.Chat server processes the message using its Markdown and AutoLinker parsers, storing the resulting HTML without sufficient sanitization. This stored payload remains in the chat history, ready to be rendered maliciously in victims' browsers.

## Requirements

1. Authenticated access to a Rocket.Chat workspace
2. Permissions to post messages in a target channel
3. Crafted payload from prior procedure

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs on server-side before storage
- Rate-limit message posting and scan for suspicious patterns (e.g., nested URLs)
- Log and alert on parsing anomalies

## Objectives

1. Inject payload into persistent storage
2. Ensure server-side parsing generates exploitable HTML
3. Position for victim interaction

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the target Rocket.Chat instance and select a channel with potential victims.

Open the web interface at https://target-rocket-chat.com and join or create a channel.

> Expected: Access to the message input field.

### Step 2: Paste and Send Payload

**Context**: Input the crafted payload directly into the chat composer.

Type or paste the payload and hit send:

```text
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[] target=_blank data-x=`.)
```

> Explanation: The message is transmitted to the server, parsed, and stored. Inspect the sent message in the UI to confirm visibility.

### Step 3: Verify Storage

**Context**: Confirm the message persists in the channel history.

Refresh the page or view from another session.

**Expected Output**: Malicious message displayed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[message-injection]]

