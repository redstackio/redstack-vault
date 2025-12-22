---
type: procedure
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Connection Proxy]]'
  - '[[Standard Application Layer Protocol]]'
sub_techniques:
  - '[[Web Protocols]]'
tags:
  - network-pivoting
  - socks-proxy
  - ssh
commands:
  - '[[commands/ssh-create-dynamic-port-forwarding]]'
  - '[[commands/ssh-create-background-socks-proxy]]'
  - '[[commands/ssh-escape-to-add-dynamic-forwarding]]'
tools: []
platforms:
  - Linux
  - macOS
  - Unix
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SSH-Tunneling-for-SOCKS-Proxy

## Summary

This procedure demonstrates how to use SSH tunneling to create a dynamic SOCKS proxy, allowing traffic to be forwarded through a compromised host for network pivoting, bypassing firewalls, and accessing internal resources indirectly. It covers basic port forwarding, background execution, and adding forwarding to an existing session, enabling attackers to route tools like nmap or curl through the proxy for lateral movement.

## Description

SSH tunneling leverages the Secure Shell protocol to encapsulate and forward network traffic securely, often used in offensive operations to pivot from a foothold host to deeper network segments. By establishing a dynamic port forwarding tunnel (SOCKS proxy), applications on the attacker's machine can route traffic as if originating from the remote host, evading direct exposure and detection. This technique is particularly effective in environments with strict egress filtering, where direct connections to internal IPs are blocked. The procedure assumes access to a target host via valid credentials and focuses on SOCKS5-compatible forwarding. Success enables tools to interact with internal services without alerting network monitors, but requires careful port selection to avoid conflicts.

## Requirements

1. Valid SSH credentials (username/password or key) for the target host.
2. Network connectivity to the target host on TCP port 22 (SSH).
3. OpenSSH client installed on the attacker's machine (standard on Linux/macOS).
4. Local ports available on the attacker's machine (e.g., 8080, 9000) for binding the proxy.

## Defense

- Monitor SSH logs for unusual port forwarding flags (-D, -L, -R) and background processes (-f, -N).
- Implement network segmentation to restrict SSH access to bastion hosts only.
- Use intrusion detection systems (IDS) to flag anomalous outbound traffic patterns from SSH sessions.
- Enforce SSH certificate-based authentication and disable password logins to prevent credential-based pivots.

## Objectives

1. Establish a SOCKS proxy tunnel through the target host for traffic forwarding.
2. Enable background operation to maintain the tunnel without blocking the terminal.
3. Add dynamic forwarding to an existing SSH session for opportunistic pivoting.
4. Route application traffic (e.g., browser, scanners) through the proxy to access internal networks.

## Instructions

### Step 1: Create Basic Dynamic Port Forwarding

**Context**: This step sets up a simple SOCKS proxy by binding a local port to forward traffic dynamically through the SSH connection. It requires an interactive SSH session and is ideal for quick testing, but ties up the terminal.

**Command** ([[commands/ssh-create-dynamic-port-forwarding]]):
```bash
ssh -D 8080 user@target-host
```

> The -D flag enables dynamic forwarding, creating a SOCKS proxy on local port 8080. Replace 'user' with the target username and 'target-host' with the IP or hostname. Once connected, configure your browser or tool (e.g., proxychains) to use localhost:8080 as the SOCKS proxy. This forwards all proxied traffic via the SSH tunnel to the remote host's network.

**Expected Output**: Standard SSH login prompt followed by a shell on the remote host if credentials are valid. No explicit proxy confirmation, but successful proxy usage is verified by routing traffic (e.g., curl --socks5 localhost:8080 http://internal-site).

### Step 2: Create Background SOCKS Proxy Tunnel

**Context**: For non-interactive use, run the SSH tunnel in the background without executing a remote shell. This allows the proxy to persist while freeing the terminal, useful for long-running pivots.

**Command** ([[commands/ssh-create-background-socks-proxy]]):
```bash
ssh -N -f -D 9000 user@target-host
```

> The -N flag prevents remote command execution, -f backgrounds the process, and -D 9000 binds the SOCKS proxy to local port 9000. After running, check the process with 'ps aux | grep ssh' to confirm it's active. Use tools like proxychains or browser settings to route traffic through localhost:9000. Kill the tunnel with 'kill $(pgrep -f "ssh.*-D 9000")' when done.

**Expected Output**: No output if successful; the command returns to the prompt immediately. Verify with 'netstat -tuln | grep 9000' showing the port listening, and test proxy functionality by attempting a connection to an internal resource.

### Step 3: Add Dynamic Forwarding to Existing SSH Session

**Context**: If an SSH session is already established (e.g., for reconnaissance), use the escape sequence to dynamically add a SOCKS proxy without reconnecting. This is the "Konami" trick for stealthy pivoting mid-session.

**Command** ([[commands/ssh-escape-to-add-dynamic-forwarding]]):
```bash
# In an active SSH session, press Enter, then ~C to enter command mode
-D 1090
```

> Press Enter to ensure a clean line, then ~ (tilde) followed by C to escape to SSH command mode (not visible). Type '-D 1090' and press Enter to add dynamic forwarding on local port 1090. Return to the session with another Enter. This modifies the existing connection without dropping it, allowing immediate proxy use on localhost:1090.

**Expected Output**: In command mode, confirmation like "port 1090: Connection successful" or similar; the session resumes normally. Test by configuring a tool to use the new proxy and accessing restricted resources.
