---
tags:
  - crlf-injection
  - url-crafting
  - node-js
type: procedure
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/define-poc-url]]'
verified: false
platforms:
  - Node.js
  - JavaScript
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.498Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 728b43cd-c35b-4980-8b45-15ea0cca776a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-CRLF-Injection-URL-for-Node.js

## Summary

This procedure crafts a malicious URL string exploiting CRLF injection in Node.js hostname parsing, setting the stage for whitelist bypass by embedding newline characters after a whitelisted domain.

## Description

In scenarios where Node.js applications use legacy URL parsing for hostname validation, attackers can inject CRLF (\r\n) into user-supplied URLs to terminate the hostname early. This procedure defines a POC URL like 'http://test1.com\r\ntest2.com', where 'test1.com' passes whitelists but the full intent targets 'test2.com'. Prerequisites include a Node.js environment and knowledge of the target's whitelist. Expected outcome: A string ready for parsing that demonstrates the injection.

## Requirements

1. Node.js installed (any version with legacy url module)
2. Basic JavaScript knowledge for string manipulation
3. Access to the application's URL input point

## Defense

Defensive measures and detection strategies:

- Migrate to modern URL constructor for parsing
- Sanitize inputs to remove CRLF characters before validation
- Implement strict URL validation libraries like 'validator.js'

## Objectives

1. Create an injectable URL string to split hostname parsing
2. Prepare for demonstration of legacy parser flaw
3. Enable bypass of hostname-based access controls

## Instructions

### Step 1: Define the POC URL String

**Context**: Construct the URL with CRLF injection to manipulate subsequent parsing.

**Command** ([[commands/define-poc-url]]):
```javascript
const poc_url = 'http://test1.com\r\ntest2.com';
```

> This sets poc_url to a string where \r\n follows 'test1.com', injecting a newline. Expected output: The variable poc_url holds the malicious string without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/define-poc-url]]

## Tools Used


## Tags

- [[crlf-injection]]
- [[url-crafting]]
