---
id: cmd-uuid-7
data: >-
  win.postMessage('{"method":"configure","args":[{"parallaxBackgroundImage":"https://hackerone.com/favicon.ico"}]}','*')
tags:
  - config
  - postmessage
  - override
type: command
output: Configuration updated
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.147Z'
verified: false
validated: true
submitted: true
---
# configure-postMessage-example

## Command

```javascript
win.postMessage('{"method":"configure","args":[{"parallaxBackgroundImage":"https://hackerone.com/favicon.ico"}]}','*');
```

## Description

Demonstrates postMessage to override configuration, like background image, highlighting persistent risks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | 'configure' | Yes |
| args | Config object array | Yes |
| targetOrigin | '*' | Yes |

## Examples

### Basic Usage

```javascript
win.postMessage('{"method":"configure","args":[{"theme":"black"}]}','*');
```

### Advanced Usage

```javascript
// With image override as above
```

## Expected Output

Background image changes to specified URL.

## Related

- [[Related Procedure|procedures/Inject-Malicious-Key-Binding-via-postMessage]]
