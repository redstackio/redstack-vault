---
data: 'Meteor.call("getMessages",["7sJLzbjDL7iL56Lmc"], console.log)'
tags:
  - api
  - access-test
  - rocket-chat
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.558Z'
id: d7a5a7c6-8e69-4bf7-9176-2bdce3d5b3e3
verified: false
validated: true
submitted: true
---
# meteor-call-get-messages

## Command

```javascript
Meteor.call("getMessages",["7sJLzbjDL7iL56Lmc"], console.log)
```

## Description

Calls the Meteor method to retrieve a specific message by ID in Rocket.Chat, used to demonstrate access denial for validation in exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | "getMessages" Meteor method name | Yes |
| params | Array with message ID (e.g., ["7sJLzbjDL7iL56Lmc"]) | Yes |
| callback | Function like console.log for handling response | No |

## Examples

### Basic Usage

```javascript
Meteor.call("getMessages",["msgID123"], console.log)
```

### Advanced Usage

With error handling.

```javascript
Meteor.call("getMessages",["7sJLzbjDL7iL56Lmc"], (err, res) => { if (err) console.error(err); else console.log(res); });
```

## Expected Output

Error for unauthorized: {"isClientSafe": true, "error": "error-not-allowed", "reason": "Not allowed", "message": "error-not-allowed", "errorType": "Meteor.Error"}.

## Related

- [[Related Procedure|procedures/Exploit-MongoDB-Injection-with-Regex-on-rid]]
