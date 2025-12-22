---
type: procedure
description: >-
  Create a secure tunnel using SSH to forward traffic from a local port to a
  remote destination, enabling network pivoting and evasion of security
  controls.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
  - '[[techniques/Connection Proxy/T1090.001|T1090.001 - Internal Proxy]]'
sub_techniques: []
tags:
  - '[[tags/Local Port Forwarding]]'
  - '[[tags/Network Pivoting Techniques]]'
  - '[[tags/SSH]]'
commands:
  - '[[commands/ssh-create-local-port-forward]]'
platforms:
  - Linux
  - Unix
  - macOS
tools:
  - '[[tools/OpenSSH]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# SSH-Local-Port-Forwarding

## Summary

SSH Local Port Forwarding establishes a secure tunnel that forwards traffic from a specified local port on the attacker's machine to a remote host and port via an SSH connection to a compromised server. This technique is commonly used in red team operations to pivot into internal networks, access restricted services, and bypass firewalls or network segmentation by encapsulating traffic within encrypted SSH sessions.

## Description

In scenarios where direct access to internal resources is blocked, attackers with SSH access to a bastion host or compromised server can use local port forwarding to create a conduit for traffic. The SSH client on the attacker's machine listens on a local port and redirects incoming connections through the encrypted tunnel to the target destination behind the pivot host. This method leverages SSH's built-in tunneling capabilities without requiring additional tools, making it stealthy and effective for lateral movement. It is particularly useful in environments with strict egress filtering, as the traffic appears as legitimate SSH activity. Success allows access to services like internal databases or admin panels that would otherwise be unreachable.

## Requirements

1. Valid SSH credentials (username and password, or SSH key) for the pivot host.
2. Network connectivity from the attacker's machine to the pivot host (typically over port 22).
3. The pivot host must have network access to the target internal destination.
4. OpenSSH client installed on the attacker's machine.
5. Administrative privileges may be needed on the local machine to bind to privileged ports (below 1024).

## Defense

- Monitor SSH logs for unusual tunneling activity, such as frequent or long-lived connections with port forwarding flags.
- Implement network segmentation to limit the pivot host's access to internal resources.
- Use SSH configuration to disable tunneling (AllowTcpForwarding no in sshd_config) or restrict it to specific users/IPs.
- Deploy intrusion detection systems (IDS) to alert on anomalous outbound connections from bastion hosts.
- Enforce multi-factor authentication (MFA) and key-based auth with strict key management for SSH access.

## Objectives

1. Establish a pivot point to access internal network resources not directly reachable from the internet.
2. Evade detection by encapsulating traffic in SSH encryption to bypass firewalls and monitoring.
3. Maintain persistent access for further enumeration or exploitation within the target environment.

## Instructions

### Step 1: Verify SSH Access to Pivot Host

**Context**: Before setting up the tunnel, confirm that you can connect to the pivot host using SSH. This ensures credentials and network access are valid, preventing errors during tunnel creation.

**Command** ([[commands/ssh-test-connection]]):
```bash
ssh -o ConnectTimeout=10 user@pivot-host
```

> This command tests the SSH connection with a timeout. If successful, you will see the remote shell prompt or a message indicating login. Exit immediately after verification to avoid leaving an open session. Expected output includes a successful authentication message and shell access; failure indicates credential or network issues.

### Step 2: Create the Local Port Forward Tunnel

**Context**: Use the SSH client to bind a local port and forward traffic through the pivot host to the internal target. Replace placeholders with actual values: bind to localhost if no specific interface is needed, choose an unused local port (e.g., 8080), specify the internal host (e.g., 10.0.0.50), and the target port (e.g., 80 for HTTP).

**Command** ([[commands/ssh-create-local-port-forward]]):
```bash
ssh -L localhost:8080:10.0.0.50:80 user@pivot-host -N -f
```

> The -L flag sets up local forwarding, -N prevents executing a remote command (keeps tunnel open), and -f backgrounds the process. Expected output is minimal (no errors); verify with `netstat -tlnp | grep 8080` showing the port listening. Traffic sent to localhost:8080 will now route through the pivot to the internal host:80.

### Step 3: Test the Tunnel

**Context**: Validate the forward by sending test traffic through the local port. This confirms the tunnel is operational and reaches the intended destination.

**Command** ([[commands/curl-test-tunnel]]):
```bash
curl -v http://localhost:8080
```

> This sends an HTTP request through the tunnel. Expected output includes the internal web server's response (e.g., HTML content or status 200); errors like connection refused indicate misconfiguration or firewall blocks on the internal side. Use tools like telnet for non-HTTP ports.
