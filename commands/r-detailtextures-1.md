---
id: cmd-goldsrc-r-detailtextures
data: r_detailtextures 1
tags:
  - enable-feature
  - vulnerability-trigger
type: command
output: >-
  Detailed textures enabled; no explicit output, but feature activates for map
  loads.
executor: game_console
platforms:
  - Windows
  - Game (GoldSrc Engine)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.586Z'
verified: false
validated: true
submitted: true
---
# r-detailtextures-1

## Command

```bash
r_detailtextures 1
```

## Description

Console command in GoldSrc games like Counter-Strike to enable loading of detailed texture files (_detail.txt) for maps, which triggers parsing in hw.dll and can lead to stack overflow if files are malformed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `1` | Enable flag (sets cvar to true, activating detail textures) | Yes |

## Examples

### Basic Usage

```bash
r_detailtextures 1
```

### Disable Usage

```bash
r_detailtextures 0
```

## Expected Output

No console output; the cvar changes silently, and subsequent map loads will attempt to parse _detail.txt files, potentially causing crashes or RCE.

## Related

- [[commands/client-cmd-r-detailtextures-1]]
