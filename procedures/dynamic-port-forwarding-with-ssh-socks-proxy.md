---
type: procedure
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Connection Proxy]]'
sub_techniques: []
tags:
  - network
  - pivot
  - tunnel
commands:
  - '[[commands/proxychains-redirect-application-traffic-through-socks-proxy]]'
  - '[[commands/ssh-dynamic-port-forwarding-through-remote-host]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Proxychains]]'
  - '[[tools/openssh]]'
verified: true
validated: true
---

# Dynamic Port Forwarding with an SSH SOCKS Proxy

## Summary

This procedure establishes a dynamic SOCKS proxy using SSH port forwarding to tunnel network traffic through a compromised host, enabling pivoting to internal networks or bypassing firewalls. It allows authenticated SSH users to forward traffic from local applications, exposing services bound to loopback interfaces or local networks, even if the SSH session is restricted to non-interactive shells like SFTP.

## Description

SSH dynamic port forwarding creates a SOCKS proxy on the attacker's local machine, routing traffic through the target host to reach otherwise inaccessible resources. This technique is useful in red team engagements for lateral movement, command and control, or exfiltrating data from segmented networks. The target environment requires SSH server access with TCP forwarding enabled (default in most OpenSSH configurations). On Linux or Windows targets with SSH services, this can expose internal services listening on 127.0.0.1 or private IPs. Proxychains or direct proxy configuration in tools like Burp Suite routes application traffic through the SOCKS proxy. Success allows transparent pivoting without direct exposure of the attacker's IP.

## Requirements

1. Valid SSH credentials (username/password or key) for the target host.
2. Network access to the target's SSH port (default 22).
3. Local port available on the attacker's machine for the SOCKS proxy (e.g., 1080 or 9050 to match proxychains defaults).
4. Installed tools: OpenSSH client and optionally Proxychains for Linux-based attackers.
5. For Windows targets, ensure OpenSSH server is running; client-side works with native OpenSSH or PuTTY.

## Defense

- Disable TCP forwarding in sshd_config by setting `AllowTcpForwarding no` and restart the SSH service.
- Use network segmentation to limit SSH access to bastion hosts only.
- Monitor SSH logs for dynamic forwarding flags (`-D`) and anomalous connection patterns using tools like Fail2Ban or SIEM.
- Implement host-based firewalls to block unauthorized outbound connections from SSH sessions.
- Enable SSH auditing with `LogLevel VERBOSE` to detect proxy usage.

## Objectives

1. Establish a persistent SOCKS proxy tunnel via SSH to the target host.
2. Route application traffic (e.g., browser, scanner) through the proxy for internal pivoting.
3. Bypass firewall restrictions to access local or internal services on the target.

## Instructions

### Step 1: Establish SSH Dynamic Port Forwarding

**Context**: Connect to the target SSH server and bind a local port as a SOCKS proxy. This step creates the tunnel without executing remote commands, running in the background to avoid interrupting the session.

**Command** ([[commands/ssh-dynamic-port-forwarding-through-remote-host]]):
```bash
ssh -f -N -D $_PORT $_USERNAME@$_TARGET_IP
```

> The `-f` flag backgrounds the process, `-N` prevents remote command execution, and `-D` enables dynamic SOCKS forwarding on the local port. Use port 9050 if integrating with Proxychains defaults, or 1080 for SOCKS5. Verify the connection with `netstat -tlnp | grep $_PORT` to confirm the listener is active. If authentication fails, check credentials or key permissions.

### Step 2: Route Application Traffic Through the SOCKS Proxy

**Context**: Direct traffic from tools or applications through the established proxy to pivot via the target host. This can be done via Proxychains for command-line tools or manual configuration for GUI applications like Burp Suite.

**Command** ([[commands/proxychains-redirect-application-traffic-through-socks-proxy]]):
```bash
proxychains $_PROGRAM
```

> Replace `$_PROGRAM` with the target application (e.g., `firefox`, `nmap`, `curl`). Ensure `/etc/proxychains.conf` is configured for `socks5 127.0.0.1 $_PORT`. Proxychains intercepts TCP connections and routes them through the proxy. For Burp Suite, navigate to User Options > Connections > Upstream Proxy and set SOCKS Proxy Host to `127.0.0.1` and Port to `$_PORT` (SOCKS v5). Test with a curl to an internal IP: `proxychains curl http://internal.target/`. If traffic fails, check proxy binding and firewall rules on the target.
