---
id: b93accbc-928e-4104-ba02-742d1b5412d0
name: network-pivoting-with-sshuttle
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.718650+00:00'
updated_at: '2023-04-10T20:25:19.563728+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[sub-techniques/SSH|T1021.004 - SSH]]'
tags:
  - '[[tags/Network Pivoting Techniques]]'
  - '[[tags/sshuttle]]'
  - network-pivoting
  - lateral-movement
commands:
  - '[[commands/sshuttle-install-package-manager]]'
  - '[[commands/sshuttle-basic-connect]]'
  - '[[commands/sshuttle-connect-pivot-host]]'
  - '[[commands/sshuttle-connect-private-key]]'
  - '[[commands/sshuttle-exclude-subnet]]'
platforms:
  - Linux
tools:
  - '[[tools/sshuttle]]'
validated: true
---

# Network Pivoting with sshuttle

## Summary

This procedure demonstrates how to use sshuttle, a transparent proxy server, to create a VPN-like tunnel over SSH for network pivoting. By establishing a connection through a compromised pivot host, attackers can route traffic to internal networks, bypassing firewalls and accessing resources as if directly connected.

## Description

Network pivoting involves using an intermediate compromised system to reach otherwise inaccessible parts of a target network. Sshuttle achieves this by running on the attacker's local machine and leveraging SSH to forward traffic to the pivot host, which then proxies requests to the specified internal subnets. This method is stealthy as it uses encrypted SSH traffic and avoids traditional VPN setups. It is particularly useful in red team engagements for lateral movement after initial foothold, allowing tools like nmap or Metasploit to target internal IPs. The technique relies on having SSH credentials or keys for the pivot host and works best in Unix-like environments.

## Requirements

1. SSH access (username/password or key) to a compromised pivot host on the target network.
2. sshuttle installed on the attacker's local machine (Python 3 required).
3. Knowledge of internal subnets to tunnel (e.g., via prior reconnaissance).
4. Local machine with network connectivity to the pivot host's SSH port (default 22).

## Defense

- Implement strict SSH access controls, including key-based authentication only and IP whitelisting.
- Monitor for anomalous SSH connections and high-volume encrypted traffic from internal hosts.
- Use network segmentation to isolate pivot hosts and deploy IDS/IPS to detect proxy-like patterns.
- Enable logging for SSH sessions and audit for unusual commands or persistent connections.

## Objectives

1. Establish a transparent proxy tunnel to route traffic through the pivot host.
2. Access and enumerate internal network resources without direct connectivity.
3. Maintain stealthy lateral movement using encrypted SSH channels.
4. Enable further attacks like scanning or exploitation on internal segments.

## Instructions

### Step 1: Install sshuttle

**Context**: Begin by installing sshuttle on your local machine using the appropriate package manager for your Linux distribution. This ensures the tool is available for creating the tunnel.

**Command** ([[commands/sshuttle-install-package-manager]]):
```bash
# For Arch Linux
pacman -Sy sshuttle

# For Debian/Ubuntu
apt-get install sshuttle
```

> This installs sshuttle via system packages. Verify installation by running `sshuttle --version`. If package managers are unavailable, use `pip install sshuttle`.

### Step 2: Establish Basic Connection to Remote Network

**Context**: Connect to the pivot host and specify the internal subnet to tunnel. This forwards all traffic destined for the subnet through the SSH connection to the pivot.

**Command** ([[commands/sshuttle-basic-connect]]):
```bash
sshuttle -vvr user@10.10.10.10 10.1.1.0/24
```

> The `-vv` enables verbose logging, `-r` specifies the remote host. Replace `user@10.10.10.10` with your pivot credentials and `10.1.1.0/24` with the target subnet. Expected output includes connection establishment and traffic forwarding logs.

### Step 3: Connect to Pivot Host for Specific Subnet

**Context**: Use this variation when pivoting to a specific internal segment via a named or variable host. This is useful for dynamic environments where the pivot IP may vary.

**Command** ([[commands/sshuttle-connect-pivot-host]]):
```bash
sshuttle -vvr username@pivot_host 10.2.2.0/24
```

> Similar to basic connect but uses a hostname or variable for the pivot. Monitor verbose output for successful tunnel setup, indicated by messages like "Client interface: tun0" and no authentication errors.

### Step 4: Connect Using Private Key Authentication

**Context**: For enhanced security or when password auth is disabled, use an SSH private key to authenticate the tunnel connection. This avoids prompting for passwords during automated operations.

**Command** ([[commands/sshuttle-connect-private-key]]):
```bash
sshuttle -vvr root@10.10.10.10 10.1.1.0/24 -e "ssh -i ~/.ssh/id_rsa"
```

> The `-e` flag customizes the SSH command to use the specified key file. Ensure the key is added to SSH agent if needed. Success is shown by tunnel activation without auth failures.

### Step 5: Exclude Specific Networks from Tunneling

**Context**: Prevent local or unnecessary traffic from routing through the tunnel, such as excluding your own subnet to avoid loops or maintain direct internet access.

**Command** ([[commands/sshuttle-exclude-subnet]]):
```bash
sshuttle -vvr user@10.10.10.10 10.1.1.0/24 -x 192.168.1.0/24
```

> The `-x` option excludes the specified subnet from the tunnel. Add multiple `-x` flags for more exclusions. Verify by pinging an excluded IP directly and a tunneled IP via the proxy.
