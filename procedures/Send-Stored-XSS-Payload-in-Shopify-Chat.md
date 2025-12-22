---
id: proc-uuid-2
name: Send Stored XSS Payload in Shopify Chat
tags:
  - xss
  - stored-xss
  - payload-injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.347Z'
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
# Send Stored XSS Payload in Shopify Chat

## Summary

This procedure injects a malicious javascript: URI into the Shopify Chat, exploiting insufficient URL sanitization to store a payload that renders as a clickable link, setting up for XSS execution.

## Description

The chat feature on Shopify store homepages or Shopify Ping fails to validate or escape user-inputted URLs, allowing javascript: schemes to be stored and displayed. The payload disguises the malicious URI by appending a benign HTTPS URL with comments. This affects both self-XSS and admin views. Prerequisites include an active chat app. Expected outcome: Payload stored and visible as a link to tricked victims.

## Requirements

1. Installed and active Shopify Chat app
2. Access to chat interface as a user
3. Victim (self or admin) to view the chat

## Defense

Defensive measures and detection strategies:

- Implement strict URL scheme whitelisting (e.g., block javascript:)
- Sanitize chat inputs with HTML entity encoding
- Monitor chat logs for suspicious URLs

## Objectives

1. Store unsanitized payload in chat messages
2. Render payload as clickable link for victims
3. Enable potential JavaScript execution on click

## Instructions

### Step 1: Access Chat Interface

**Context**: Open the chat on the target store to input the payload.

Navigate to the Shopify store homepage or Shopify Ping interface where chat is enabled.

### Step 2: Input Malicious Payload

**Context**: Enter the PoC payload to test the vulnerability.

In the chat input field, type: `javascript:alert(1)//https://dqdqdqdqdq.myshopify.com` and send the message.

> The // comments out the trailing URL, making the javascript: scheme active while appearing legitimate.

**Expected Output**: Message sent successfully, displayed as a hyperlink in chat history.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored without alteration.

Refresh the page or view chat in another session; the link should remain clickable.

**Expected Output**: Link persists in chat, inspect element shows no escaping.

**Success Indicators**:
- Payload renders as URL without errors
- Hovering shows javascript: scheme

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[payload-injection]]
- [[shopify]]
