---
data: s.click();
tags:
  - dom
  - submit
type: command
executor: javascript
platforms:
  - Web
id: 5de6d989-1933-4cf6-9f90-803d163db530
created_at: '2025-12-14T17:23:20.624Z'
updated_at: '2025-12-14T17:23:20.624Z'
verified: false
validated: true
submitted: true
---
# click-submit-button

## Command

```javascript
s.click();
```

## Description

This JavaScript command programmatically clicks the selected submit button (s), triggering the form submission to save changes in the WordPress plugin editor.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s | Button element | Yes |

## Examples

### Basic Usage

```javascript
s.click();
```

### Advanced Usage

```javascript
s.click(); // Followed by event listeners if needed
```

## Expected Output

Form submits, saving the file; may trigger a page reload or success message in the iframe.

## Related

- [[commands/select-submit-button]]
