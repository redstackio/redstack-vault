---
type: procedure
description: >-
  Modifies the user's .bashrc to alias sudo to a fake script that captures sudo
  passwords while masquerading as the legitimate sudo command, enabling
  persistence and credential theft on Linux systems.
verified: true
submitted: false
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Boot or Logon Autostart Execution|T1547 - Boot or Logon
    Autostart Execution]]
  - '[[techniques/Masquerading|T1036 - Masquerading]]'
  - >-
    [[techniques/Modify Authentication Process|T1556 - Modify Authentication
    Process]]
sub_techniques:
  - >-
    [[sub-techniques/Boot or Logon Autostart Execution: .bash_profile and
    .bashrc|T1547.001 - .bash_profile and .bashrc]]
  - >-
    [[sub-techniques/Masquerading: Rename System Utilities|T1036.003 - Rename
    System Utilities]]
tags:
  - linux-persistence
  - backdoor
  - credential-theft
  - sudo-masquerading
commands:
  - '[[commands/create-sudo-alias-in-bashrc]]'
  - '[[commands/make-fakesudo-executable]]'
  - '[[commands/test-fakesudo-with-echo]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Implement-Sudo-Backdoor-via-Bashrc-Alias

## Summary

This procedure establishes persistence on a compromised Linux user account by creating a fake 'sudo' script that intercepts and logs sudo passwords to a file, then executes the real sudo command. The fake script is aliased to 'sudo' in the user's .bashrc file, ensuring it runs every time a new shell session starts. This allows attackers to steal elevated credentials transparently while maintaining access and escalating privileges over time.

## Description

The technique leverages shell profile modification to hijack the sudo command, a common utility for privilege escalation. By placing a malicious script in the user's home directory (e.g., ~/.hidden/fakesudo) and aliasing it in .bashrc, the backdoor activates on login without requiring root privileges initially. When the user attempts to run sudo, the script prompts for the password, logs it to /tmp/pass.txt, briefly delays to mimic failure, displays an error message, and then invokes the legitimate /usr/bin/sudo with the provided arguments. This masquerades as a failed sudo attempt while capturing credentials for later retrieval. The approach is stealthy, as it doesn't alter system-wide files and blends with normal user behavior. It targets environments where users frequently use sudo, such as development or admin workstations, and can lead to full system compromise if the stolen password grants root access.

## Requirements

1. Local user access on the target Linux system with write permissions to the home directory (~/.bashrc and subdirectories).
2. Bash or Zsh shell environment (procedure appends to both .bashrc and .zshrc for compatibility).
3. No root privileges needed for setup, but the backdoor relies on the user having sudo access to be effective.
4. Basic tools like echo, chmod, and cat (standard on Linux).

## Defense

- Monitor shell profile files (.bashrc, .zshrc) for unauthorized modifications using file integrity monitoring tools like AIDE or OSSEC.
- Implement application whitelisting to prevent execution of unsigned scripts in user directories.
- Enable sudo logging (e.g., via /etc/sudoers with logfile directive) and audit for unusual failures or delays in sudo prompts.
- Use multi-factor authentication (MFA) for sudo to mitigate password theft.
- Regularly scan for suspicious aliases in shell configs and hidden directories like ~/.hidden.

## Objectives

1. Establish persistence by ensuring the backdoor executes on every user login.
2. Capture sudo passwords for potential privilege escalation and lateral movement.
3. Maintain stealth by masquerading as legitimate sudo behavior to avoid detection.
4. Enable ongoing access to the system for data exfiltration or further attacks.

## Instructions

### Step 1: Create the Fake Sudo Script

**Context**: This step deploys the core backdoor payload—a bash script that mimics sudo to steal passwords. The script is placed in a hidden directory to evade casual inspection. Use the provided code snippet to create the file.

**Code** ([[codes/Bash-Fake-Sudo-Password-Logger]]):

Embed the code into ~/.hidden/fakesudo by copying it directly or using cat > ~/.hidden/fakesudo << 'EOF' followed by the script content.

> This creates the executable script that will handle password capture. Ensure the directory ~/.hidden exists (mkdir -p ~/.hidden if needed). The script logs passwords to /tmp/pass.txt, which should be retrieved later by the attacker.

### Step 2: Make the Fake Sudo Script Executable

**Context**: Grants execute permissions to the script so it can run when aliased. This is a prerequisite for the alias to function properly.

**Command** ([[commands/make-fakesudo-executable]]):
```bash
chmod u+x ~/.hidden/fakesudo
```

> Running this command sets the user execute bit on the fakesudo file. Expected output: No output if successful; verify with ls -l ~/.hidden/fakesudo showing -rwxr--r-- or similar.

### Step 3: Add Sudo Alias to Shell Profile

**Context**: Appends an alias to .bashrc (and .zshrc for compatibility) so that every new shell session redirects 'sudo' calls to the fake script. This ensures persistence across logins.

**Command** ([[commands/create-sudo-alias-in-bashrc]]):
```bash
echo "alias sudo=~/.hidden/fakesudo" >> ~/.bashrc
```

> This appends the alias line to the end of .bashrc. If using Zsh, manually add the same line to .zshrc or extend the command. Expected output: No output; verify by grepping .bashrc for 'alias sudo'.

### Step 4: Test the Backdoor

**Context**: Validates the setup by running a sudo command through the alias, confirming password capture without alerting the user.

**Command** ([[commands/test-fakesudo-with-echo]]):
```bash
fakesudo echo 'You do not have the necessary permissions to run this command'
```
(Or use the full alias: sudo echo 'test')

> When executed, it prompts for the sudo password, logs it to /tmp/pass.txt, displays 'Sorry, try again.' after a 2-second delay, and then runs the real sudo (which may succeed or fail based on the actual password). Check /tmp/pass.txt for the captured password. Success is indicated by the password appearing in the log file.
