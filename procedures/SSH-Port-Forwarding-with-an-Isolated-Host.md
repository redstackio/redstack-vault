---
id: 6991b9b9-a7b1-4957-be03-b910338a9058
name: SSH-Port-Forwarding-with-an-Isolated-Host
type: procedure
verified: true
submitted: true
created_at: '2019-10-26T01:22:51.426952+00:00'
updated_at: '2023-05-26T00:53:26.716788+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
sub_techniques: []
tags:
  - '[[tags/Command & Control]]'
  - '[[tags/data encryption]]'
  - '[[tags/Pivot]]'
commands:
  - '[[commands/ssh-local-port-forwarding]]'
  - '[[commands/ssh-remote-port-forwarding]]'
platforms:
  - Linux
tools: []
validated: true
---

# SSH-Port-Forwarding-with-an-Isolated-Host

## Summary

This procedure demonstrates how to use SSH tunneling to access isolated networks via an intermediary host. It covers local port forwarding to connect from an attacker to an isolated target through the intermediary, and remote port forwarding to receive connections from the isolated network back to the attacker, enabling command and control in segmented environments.

## Description

SSH port forwarding, or tunneling, allows attackers to bypass network isolation by routing traffic through a compromised intermediary host. In scenarios where the target is in a restricted subnet accessible only via the intermediary, local forwarding enables the attacker to reach internal services. Conversely, remote forwarding facilitates outbound connections from the isolated network to the attacker, such as for reverse shells. This technique proxies connections, evading direct exposure and leveraging SSH's encryption for stealthy pivoting. It requires SSH access to the intermediary and is commonly used in post-exploitation for lateral movement and C2.

## Requirements

1. SSH client installed on the attacker's machine (e.g., OpenSSH on Linux).
2. Valid credentials or key-based authentication for the intermediary host.
3. Network access to the intermediary host from the attacker.
4. Knowledge of the isolated target's IP and ports for forwarding.
5. Listener setup on the attacker machine for remote forwarding scenarios.

## Defense

Defensive measures and detection strategies:

- Monitor SSH logs for unusual port forwarding attempts (e.g., -L or -R flags) using tools like auditd or fail2ban.
- Implement network segmentation with firewalls blocking unauthorized SSH tunneling (e.g., restrict SSH to specific IPs/ports).
- Use SSH hardening: Disable password auth, enforce key-based auth, and limit allowed commands via authorized_keys restrictions.
- Enable process monitoring for ssh processes with forwarding flags and correlate with network flows.

## Objectives

1. Establish a tunnel to access isolated hosts without direct connectivity.
2. Enable bidirectional communication for command execution or data exfiltration.
3. Maintain persistence and stealth through encrypted channels.

## Instructions

### Step 1: Set Up Local Port Forwarding

**Context**: Use local port forwarding to route traffic from the attacker's local port through the intermediary to an isolated target's service. This allows the attacker to interact with internal ports as if directly connected.

**Command** ([[commands/ssh-local-port-forwarding]]):
```bash
ssh -f -N -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT $_USER@$_TARGET_IP
```

> This command forks the SSH process into the background (-f), disables execution of remote commands (-N), and binds the local port ($_ATTACKER_PORT) to forward to the remote target's port ($_REMOTE_PORT) via the intermediary ($_TARGET_IP). Replace placeholders with actual values, e.g., for accessing port 80 on 10.10.10.11 via intermediary 10.10.10.10 on local port 8001:
>
> ```bash
> ssh -f -N -L 8001:10.10.10.11:80 root@10.10.10.10
> ```
>
> After running, connect to localhost:$_ATTACKER_PORT on the attacker machine to reach the isolated service. Verify with netstat or ss to confirm the listening port.

### Step 2: Set Up Remote Port Forwarding

**Context**: Use remote port forwarding to expose a port on the intermediary that tunnels traffic back to the attacker's local listener. This is useful for receiving reverse connections from isolated hosts, such as shells.

**Command** ([[commands/ssh-remote-port-forwarding]]):
```bash
ssh -f -N -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT $_USER@$_TARGET_IP
```

> This binds the remote port ($_REMOTE_PORT) on the intermediary to forward to the attacker's IP ($_REMOTE_IP) and local port ($_LOCAL_PORT). For example, to forward port 4444 on the intermediary to the attacker's localhost:4444 via intermediary 10.10.10.10:
>
> ```bash
> ssh -f -N -R 4444:127.0.0.1:4444 root@10.10.10.10
> ```
>
> Start a listener (e.g., nc -lvnp 4444) on the attacker before executing. From the isolated host, connect to the intermediary's $_REMOTE_PORT to reach the attacker. Check SSH logs or process list to confirm the tunnel is active.
