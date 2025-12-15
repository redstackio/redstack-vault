---
tags:
  - phishing
  - drive-by
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4345c9cb-c1ee-46a6-ab7f-403e64047249
created_at: '2025-12-14T17:33:12.336Z'
updated_at: '2025-12-14T17:33:12.336Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Induce-Victim-to-Visit-Malicious-Page-and-Trigger-CORS-Request

## Summary

This procedure lures a victim to the malicious webpage and prompts them to execute JavaScript that initiates a credentialed cross-origin request, exploiting the CORS flaw in the victim's browser session.

## Description

Targeting authenticated niche.co users, the attacker distributes the spoofed domain URL via email, social media, or ads. Upon visit, a button triggers the 'cors()' function, sending an XMLHttpRequest to the API with withCredentials=true. The attack relies on social engineering; outcomes include successful request initiation if the victim is logged in.

## Requirements

1. Malicious page hosted and accessible
2. Social engineering channels (e.g., email lists of potential victims)
3. Victim must have an active niche.co session

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Browser extensions to block cross-origin credentialed requests
- Server-side logging of unexpected Origins

## Objectives

1. Gain execution in victim's browser context
2. Trigger the exploit without suspicion
3. Ensure request carries victim's cookies

## Instructions

### Step 1: Distribute Malicious URL

**Context**: Use phishing to direct victim to the page.

Craft an email or message: "Check out this niche.co related tool at https://niche.co.evil.net/malicious.html"

> Personalize to increase click rate; track opens if possible.

### Step 2: Trigger JavaScript Execution

**Context**: Prompt victim interaction to run the code.

The page displays a button: <button onclick="cors()">Click to Exploit</button>. Victim clicks, executing:

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://www.niche.co/api/v1/users/*****', true);
xhr.withCredentials = true;
xhr.send();
```

> Replace ***** with a guessed or known user ID; alert shows initial success.

### Step 3: Monitor for Trigger

**Context**: Confirm execution from attacker's side.

Watch for subsequent requests (e.g., data fetch in next step).

> Expected: No direct feedback, but chain proceeds on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[Phishing]]
- [[drive-by]]
- [[javascript-execution]]
