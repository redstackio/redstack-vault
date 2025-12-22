---
tags:
  - certificate-theft
  - docker
  - tls
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/cat-docker-server-pem]]'
  - '[[commands/cat-docker-server-key-pem]]'
platforms:
  - Linux
techniques:
  - '[[Data from Local System]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a6d5f7f6-8e42-406f-b515-448e4d1d4e99
created_at: '2025-12-14T04:08:48.116Z'
updated_at: '2025-12-14T04:08:48.116Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Extract Docker Certificates from Host

## Summary

This procedure retrieves the Docker daemon's TLS server certificate and private key from the host filesystem, mounted via container, to enable impersonation of the daemon on an external malicious server.

## Description

Docker daemons often use TLS for secure API access on TCP port 2376. The certs (/etc/docker/server.pem and server-key.pem) are stored on the host. With the host mounted in the executor, these can be read and exfiltrated. This allows creating a fake daemon that the Runner's client trusts, facilitating SSRF via redirects.

## Requirements

1. Mounted host filesystem at /h
2. Shell access in executor
3. External transfer method (e.g., paste or scp)

## Defense

Defensive measures and detection strategies:

- Store Docker certs in secure, non-mounted directories
- Use mutual TLS and client cert validation
- Audit access to /etc/docker logs for unauthorized reads
- Rotate certs periodically

## Objectives

1. Obtain TLS materials for daemon spoofing
2. Enable traffic hijacking
3. Support malicious server setup

## Instructions

### Step 1: Read Server Certificate

**Context**: Extract the public certificate PEM.

**Command** ([[commands/cat-docker-server-pem]]):
```bash
cat /h/etc/docker/server.pem
```

> Outputs the full PEM content; copy to attacker machine.

### Step 2: Read Private Key

**Context**: Extract the private key PEM for signing.

**Command** ([[commands/cat-docker-server-key-pem]]):
```bash
cat /h/etc/docker/server-key.pem
```

> Outputs the key; ensure secure transfer as it's sensitive.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/cat-docker-server-pem]]
- [[commands/cat-docker-server-key-pem]]

## Tools Used


## Tags

- certificate-theft
- docker
- tls
