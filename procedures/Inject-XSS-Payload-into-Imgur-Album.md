---
tags:
  - xss
  - injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1bfd5c6e-c0b3-4008-acab-2480aba27170
created_at: '2025-12-14T00:11:25.394Z'
updated_at: '2025-12-14T00:11:25.394Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Imgur Album

## Summary

This procedure details injecting a stored XSS payload into Imgur's album creation feature by using HTML entities to bypass input filters.

## Description

The attacker creates an album and embeds a payload like "/>&lt;script>alert(1)&lt;/script>"/> in the album data. Due to insufficient sanitization, the payload is stored and later rendered on profile pages, executing JavaScript.

## Requirements

1. Imgur account with album creation access
2. Web browser or API tool for submission
3. Knowledge of HTML entities

## Defense

Defensive measures and detection strategies:

- Decode and sanitize all inputs for entities
- Use content security policy (CSP) to restrict script execution

## Objectives

1. Store malicious payload
2. Bypass filtering mechanisms
3. Set up for execution on profile load

## Instructions

### Step 1: Prepare Payload

**Context**: Encode the script tag using HTML entities.

Payload: "/>&lt;script>alert(1)&lt;/script>"/>

> Expected: Encoded string ready for injection.

### Step 2: Create Album

**Context**: Submit the payload via Imgur's album creation interface.

Execute [[commands/inject-xss-payload]] by pasting the payload into the album title or description field and saving.

```html
"/>&lt;script>alert(1)&lt;/script>"/>
```

> Expected: Album created successfully with payload intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/inject-xss-payload]]

## Tools Used



## Tags

- [[xss]]
- [[injection]]
