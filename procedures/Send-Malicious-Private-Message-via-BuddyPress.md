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
  - '[[commands/simple-xss-iframe-alert]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 24f5fcb8-7cdd-46eb-b7ff-056ce85c191e
created_at: '2025-12-14T00:11:16.605Z'
updated_at: '2025-12-14T00:11:16.605Z'
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
# Send Malicious Private Message via BuddyPress

## Summary

This procedure exploits a stored XSS vulnerability in BuddyPress by sending a private message with embedded malicious HTML and JavaScript that executes when viewed.

## Description

The vulnerability stems from improper sanitization in the message content field, allowing raw HTML rendering via triple mustache in the Nouveau template. This enables arbitrary JS execution in the victim's browser, potentially leading to account takeover if targeting an admin.

## Requirements

1. Registered user account on WordPress with BuddyPress
2. Access to target user's profile
3. Pre-crafted XSS payload

## Defense

Defensive measures and detection strategies:

- Update BuddyPress to patch the vulnerability
- Monitor for unusual message content or JS execution in logs

## Objectives

1. Store malicious payload in database
2. Prepare for XSS trigger on view
3. Enable arbitrary actions on victim's behalf

## Instructions

### Step 1: Navigate to Target Profile

**Context**: Access the profile to start messaging.

Navigate to the target user's profile page via the web interface.

> This sets up the messaging interface.

### Step 2: Initiate Private Message

**Context**: Begin composing the message.

Click on the private message button to open the composition form.

> Prepares the input fields for payload insertion.

### Step 3: Enter Subject and Payload

**Context**: Insert the malicious content.

Type any subject, then enter the payload in the message body using [[commands/simple-xss-iframe-alert]]:

```html
Test<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>
```

> The payload will be stored without escaping.

### Step 4: Send Message

**Context**: Submit to store in database.

Click send to submit the message.

> Message is now stored and ready to trigger on view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/simple-xss-iframe-alert]]

## Tools Used



## Tags

- xss
- buddypress
