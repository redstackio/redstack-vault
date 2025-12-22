---
data: 'steam://-console'
tags:
  - steam
  - uri
type: command
executor: bash
platforms:
  - Windows
id: 7aa83947-dc5c-4818-93d7-dbc85b9d9fd3
created_at: '2025-12-11T06:10:17.960Z'
updated_at: '2025-12-11T06:10:17.960Z'
verified: false
validated: true
submitted: true
---
# steam-open-console

## Command

```bash
steam://-console
```

## Description

Opens the Steam console, used in exploitation to access debugging features without confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-console` | Flag to open console | Yes |

## Examples

### Basic Usage

```bash
steam://-console
```

## Expected Output

Steam console window appears.

## Related

- [[commands/steam-open-game]]
- [[procedures/Exploit-XSS-with-JavaScript-and-Steam-URIs]]
