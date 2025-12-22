---
data: alert(document.location);
tags:
  - xss
  - payload
type: command
executor: javascript
platforms:
  - Web
id: 4b13cbd9-129e-4efb-8021-40869987416c
created_at: '2025-12-14T03:16:14.047Z'
updated_at: '2025-12-14T03:16:14.047Z'
verified: false
validated: true
submitted: true
---
# alert-document-location

## Command

```javascript
alert(document.location);
```

## Description

JavaScript code embedded in SVG to pop an alert displaying the current document's URL, demonstrating XSS execution when the file renders.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses browser DOM | No |

## Examples

### Basic Usage

```javascript
alert(document.location);
```

## Expected Output

Alert box appears showing the webpage's location URL.

## Related

- [[Related Procedure: Create-Malicious-SVG-with-Embedded-JavaScript]]
