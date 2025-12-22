---
id: proc-002
tags:
  - xss
  - html-injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.392Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-HTML-in-Chat-Message

## Summary

This procedure details sending a chat message with a malicious HTML payload, such as a base href tag, to exploit lack of sanitization in the chat system, setting up the second-order XSS for email propagation.

## Description

The attack targets a chat messaging system where user input is stored and later rendered in email notifications without proper HTML escaping. By injecting `<base href=//un4.gi>`, the payload modifies all relative links in the email to point to the attacker's domain (un4.gi). This is a stored XSS variant because the payload persists in the conversation and affects downstream email rendering from the official server (Air University Service Desk). Prerequisites include an active chat session; outcomes enable link hijacking for phishing when the recipient views the notification.

## Requirements

1. Authenticated access to the chat interface from Step 1
2. Control over an external domain for redirection (e.g., un4.gi)
3. Recipient account details (e.g., another test account) to start a conversation

## Defense

Defensive measures and detection strategies:

- Sanitize all user-generated content with HTML entity encoding before storage or rendering
- Use Content Security Policy (CSP) to restrict base tags and external hrefs in emails
- Scan chat messages for suspicious HTML patterns and quarantine

## Objectives

1. Deliver the payload to a conversation without UI rejection
2. Ensure the payload is stored server-side for email inclusion
3. Trigger an email notification to the recipient

## Instructions

### Step 1: Create New Conversation

**Context**: Initiate a chat with a test recipient to provide context for the payload.

No command required; use web UI:

- In the chat interface, select 'New Conversation'.
- Add the recipient's username or ID.
- Proceed to the message input field.

> Conversation opens; note the channelID from the URL (e.g., sysparm_channelID=████) for later use.

### Step 2: Send Malicious Payload

**Context**: Input and submit the HTML injection payload to exploit the lack of sanitization.

No command required; enter directly in message box:

- Type: `<base href=//un4.gi>`
- Click 'Send'.

> Message sends; it may render normally in chat but alters email links due to second-order nature.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (enabling HTML manipulation for potential script execution)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
