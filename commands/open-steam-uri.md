---
data: 'open("steam://xxx")'
tags:
  - javascript
  - uri
type: command
executor: javascript
platforms:
  - Web
id: 0300f26a-ddef-45df-b73e-20c3e58afc9a
created_at: '2025-12-11T06:10:17.668Z'
updated_at: '2025-12-11T06:10:17.668Z'
verified: false
validated: true
submitted: true
---
# open-steam-uri

## Command

```javascript
open("steam://xxx")
```

## Description

Opens a new window with a steam:// URI, used to execute Steam actions from JavaScript.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `steam://xxx` | Steam URI | Yes |

## Examples

### Basic Usage

```javascript
open("steam://open/440")
```

## Expected Output

Executes the Steam action without confirmation.

## Related

- [[commands/window-top-postmessage]]
- [[procedures/Abuse-OEMBED-for-JavaScript-Injection]]
