---
data: var s = d.querySelector("#submit")
tags:
  - dom
  - select
  - button
type: command
executor: javascript
platforms:
  - Web
id: ad053f27-c354-4a8b-a37b-4606e819d0c1
created_at: '2025-12-14T17:23:20.641Z'
updated_at: '2025-12-14T17:23:20.641Z'
verified: false
validated: true
submitted: true
---
# select-submit-button

## Command

```javascript
var s = d.querySelector("#submit")
```

## Description

This JavaScript command selects the submit button element with ID 'submit' from the iframe's DOM in the WordPress plugin editor form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| d | Iframe document object | Yes |
| "#submit" | CSS selector for the button | Yes |

## Examples

### Basic Usage

```javascript
var s = d.querySelector("#submit")
```

### Advanced Usage

```javascript
var s = d.querySelector("input[type='submit']")
```

## Expected Output

Variable s set to the button element, ready for .click() invocation.

## Related

- [[commands/click-submit-button]]
