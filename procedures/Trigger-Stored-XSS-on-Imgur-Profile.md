---
tags:
  - xss
  - execution
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/visit-profile-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: f16adfd3-2359-4e92-8b61-1999e24427e9
created_at: '2025-12-14T00:11:25.392Z'
updated_at: '2025-12-14T00:11:25.392Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS on Imgur Profile

## Summary

This procedure involves visiting the Imgur profile page to trigger the execution of a stored XSS payload, demonstrating arbitrary code execution.

## Description

After injecting the payload into an album, accessing the profile URL (e.g., https://username.imgur.com/) loads the album content, decodes the entities, and executes the script, potentially allowing cookie theft or other malicious actions.

## Requirements

1. Injected payload in an album
2. Web browser
3. Profile URL knowledge

## Defense

Defensive measures and detection strategies:

- Regularly audit stored content for malicious scripts
- Implement output encoding on rendering

## Objectives

1. Execute stored payload
2. Confirm vulnerability impact
3. Demonstrate code execution

## Instructions

### Step 1: Access Profile

**Context**: Navigate to the profile to load the album.

Execute [[commands/visit-profile-url]] by browsing to https://username.imgur.com/.

```bash
echo "Visit https://username.imgur.com/"
```

> Expected: Page loads and script executes.

### Step 2: Verify Execution

**Context**: Check for alert or other indicators.

Observe the alert(1) popup.

> Expected: JavaScript alert confirms success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/visit-profile-url]]

## Tools Used



## Tags

- [[xss]]
- [[Execution]]
