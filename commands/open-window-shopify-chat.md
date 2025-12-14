---
id: 123e4567-e89b-12d3-a456-426614174004
name: open-window-shopify-chat
type: command
executor: javascript
data: 'let ctx=window.open(''https://apple-business-chat-commerce.shopifycloud.com'')'
output: A new window object reference (ctx) if successful.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.696Z'
platforms:
  - Web
tags:
  - xss
  - window
verified: false
validated: true
submitted: true
---

# open-window-shopify-chat

## Command

```javascript
let ctx=window.open('https://apple-business-chat-commerce.shopifycloud.com')
```

## Description

Opens a new browser window to the Shopify Apple Business Chat domain, providing a target for cross-window postMessage communication in the XSS exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | The target URL to open (https://apple-business-chat-commerce.shopifycloud.com) | Yes |

## Examples

### Basic Usage

```javascript
let ctx = window.open('https://apple-business-chat-commerce.shopifycloud.com');
```

### Advanced Usage

```javascript
let ctx = window.open('https://apple-business-chat-commerce.shopifycloud.com', '_blank', 'width=800,height=600');
```

## Expected Output

A window object (ctx) referencing the new tab/window; if blocked by popup blocker, ctx may be null.

## Related

- [[Related Procedure|procedures/Modify-Store-Theme-to-Inject-Malicious-Script]]
