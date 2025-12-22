---
data: 'steam://open/440'
tags:
  - steam
  - uri
type: command
executor: bash
platforms:
  - Windows
id: 4d12fb61-f938-4532-82c9-00c2fea3c228
created_at: '2025-12-11T06:10:18.099Z'
updated_at: '2025-12-11T06:10:18.099Z'
verified: false
validated: true
submitted: true
---
# steam-open-game

## Command

```bash
steam://open/440
```

## Description

Opens a specific game in Steam using its ID, exploited via chat links to launch without confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `440` | Game ID | Yes |

## Examples

### Basic Usage

```bash
steam://open/440
```

### Advanced Usage

```bash
steam://open/440 --parameters
```

## Expected Output

Launches the specified game without user confirmation.

## Related

- [[commands/steam-open-console]]
- [[procedures/Exploit-XSS-with-JavaScript-and-Steam-URIs]]
