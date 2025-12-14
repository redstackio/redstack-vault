---
data: >-
  onIgnoreTag:function(e, t){return"!--[if"=== e ||"![endif]--"=== e ||"-->"===
  t ? t :void 0;}
tags:
  - xss
  - sanitization
type: command
output: Unsanitized tag content for matching comments
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.161Z'
id: d2a9904f-b672-49a6-8d4b-95da9d598fa8
verified: false
validated: true
submitted: true
---
# js-xss-onIgnoreTag-bypass

## Command

```javascript
onIgnoreTag:function(e, t){return"!--[if"=== e ||"![endif]--"=== e ||"-->"=== t ? t :void 0;}
```

## Description

Custom js-xss configuration function that skips sanitization for IE-specific comment tags, enabling XSS bypass by returning raw content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| e | Tag name (e.g., '--[if') | Yes |
| t | Tag content (e.g., '-->') | Yes |

## Examples

### Basic Usage

```javascript
const xss = new XSS.FilterXSS({ onIgnoreTag });
// Processes HTML, ignoring specified comments
```

### Advanced Usage

```javascript
// In Judge.me context, applied to email HTML
xss.process("<! [endif]--onerror=...");
// Returns unsanitized due to match
```

## Expected Output

Raw tag content for matching e/t, allowing injection of attributes like onerror.

## Related

- [[commands/xss-payload-injection]]
