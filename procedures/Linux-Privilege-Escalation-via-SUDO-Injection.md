---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
sub_techniques:
  - '[[Setuid and Setgid]]'
tags:
  - linux-privilege-escalation
  - sudo
  - sudo_inject
platforms:
  - Linux
commands:
  - '[[commands/sudo-trigger-and-interrupt]]'
  - '[[commands/run-sudo-inject-exploit]]'
  - '[[commands/sudo-gain-root-shell]]'
tools:
  - '[[tools/sudo_inject]]'
validated: true
---

# Linux-Privilege-Escalation-via-SUDO-Injection

## Summary

This procedure exploits a vulnerability in sudo configurations using the sudo_inject tool to bypass password authentication and gain root privileges on a Linux system. By creating an invalid sudo token and injecting malicious commands, an attacker can execute elevated commands without providing credentials, enabling persistence and lateral movement.

## Description

Sudo is a common mechanism on Linux systems for granting users temporary elevated privileges. If the sudoers configuration is insecure or exploitable, attackers with local access can abuse it to inject commands that run with root privileges. This procedure uses the sudo_inject tool, which leverages a specific technique to interrupt the sudo authentication process, create an invalid token, and then inject and execute a payload via an exploit script. This allows escalation from a standard user to root without knowing the sudo password. The technique is particularly effective in environments where users have sudo access but password prompts are enforced. It maps to MITRE ATT&CK for abusing elevation controls like setuid mechanisms in sudo.

## Requirements

1. Local shell access to the target Linux machine as a non-root user with sudo privileges (even if password-protected).
2. The sudo_inject tool installed or available on the target (downloaded and made executable).
3. Basic knowledge of bash scripting and file permissions.
4. Write access to a temporary directory for the exploit script.

## Defense

- Restrict sudoers file access to root only and monitor for modifications using file integrity tools like AIDE or auditd.
- Enable sudo logging (e.g., via /etc/sudoers with logfile directive) and review logs for failed authentications or unusual interruptions.
- Implement least privilege: Avoid granting NOPASSWD sudo access and use precise command allowances in sudoers.
- Regularly audit sudo configurations with tools like sudo-lint and apply security patches for known sudo vulnerabilities.

## Objectives

1. Bypass sudo password authentication to gain root shell access.
2. Establish persistence through elevated command execution.
3. Enable lateral movement by leveraging root privileges for network access or further exploitation.

## Instructions

### Step 1: Trigger Sudo Prompt and Create Invalid Token

**Context**: Start a sudo command to trigger the authentication prompt, then interrupt it to generate an invalid sudo token. This token is exploited by the subsequent injection, allowing bypassed authentication.

**Command** ([[commands/sudo-trigger-and-interrupt]]):
```bash
sudo whatever
```

> Run the command to prompt for a password. Immediately press Ctrl+C to interrupt without entering credentials. This creates the invalid token needed for the exploit. The "whatever" is a placeholder; any invalid command works to trigger the prompt.

### Step 2: Execute the Sudo Inject Exploit Script

**Context**: Run the exploit script from the sudo_inject tool, which uses the invalid token to inject and execute malicious commands with elevated privileges. The script must be prepared in advance by cloning the sudo_inject repository and setting up exploit.sh.

**Command** ([[commands/run-sudo-inject-exploit]]):
```bash
sh exploit.sh
```

> Ensure exploit.sh is in the current directory and executable (chmod +x exploit.sh). The script will process the invalid token and perform the injection. Wait approximately 1 second after execution to allow the injection to take effect.

### Step 3: Gain Root Shell Access

**Context**: With the injection complete, invoke sudo again to obtain a root shell without a password prompt, verifying successful privilege escalation.

**Command** ([[commands/sudo-gain-root-shell]]):
```bash
sudo -i
```

> This should drop you into a root shell (# prompt) without requiring a password. Verify with `id` command, which should show uid=0(root).

## Expected Output

Successful execution results in a root shell prompt, confirmed by running `id` showing root privileges. Look for no password prompt on the final sudo invocation and output from the exploit script indicating injection success.
