---
data: 'open("steam://xxx")'
tags:
  - steam
  - uri
type: command
executor: javascript
platforms:
  - Web
  - Windows
id: 159395b8-673f-4c10-b5a7-211f1d44e738
created_at: '2025-12-14T00:11:25.289Z'
updated_at: '2025-12-14T00:11:25.289Z'
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

Opens a steam:// URI to test effects in the embedded Steam context, used for rapid testing of privileged actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `uri` | The steam:// URI to open | Yes |

## Examples

### Basic Usage

```javascript
open("steam://console")
```

### Advanced Usage

```javascript
open("steam://run/12345")
```

## Expected Output

Executes the steam:// action, such as opening a game or console.

## Related

- [[procedures/Escalating-with-Steam-URI-Schemes]]
- [[commands/steam-console]]
