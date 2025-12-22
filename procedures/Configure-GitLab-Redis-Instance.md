---
id: proc-configure-gitlab-redis
tags:
  - redis
  - setup
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T04:09:00.710Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
---

# Configure GitLab Redis Instance

## Summary

This procedure sets up a Redis server on localhost:6379 using TCP socket as required for GitLab integration, enabling the SSRF payload to target it for queue manipulation.

## Description

In the context of exploiting GitLab's mirroring feature, Redis must be configured to listen on 127.0.0.1:6379 via TCP to allow internal git:// SSRF requests to inject commands. This setup follows GitLab's official documentation and assumes a Linux environment. Prerequisites include root or sudo access on the GitLab host.

## Requirements

1. Linux server with GitLab installed
2. Root/sudo access to install and configure Redis
3. GitLab configured to use Redis for queues (default in many setups)

## Defense

Defensive measures and detection strategies:

- Restrict Redis to Unix sockets only, disabling TCP binding
- Firewall rules to block external access to port 6379
- Monitor Redis logs for unexpected MULTI/EXEC transactions

## Objectives

1. Establish Redis as a target for SSRF injection
2. Ensure compatibility with GitLab's Resque queue system
3. Verify internal accessibility without external exposure

## Instructions

### Step 1: Install Redis

**Context**: Install Redis if not present, following GitLab docs.

**Command** (apt-get install):
```bash
sudo apt-get update && sudo apt-get install redis-server
```

> Installs Redis package on Debian-based systems. Expected output: Package installed successfully.

### Step 2: Configure TCP Socket

**Context**: Edit /etc/redis/redis.conf to bind to localhost:6379.

**Command** (sed edit):
```bash
sudo sed -i 's/^bind 127.0.0.1/#bind 127.0.0.1/' /etc/redis/redis.conf && sudo sed -i 's/^port 6379/port 6379/' /etc/redis/redis.conf
```

> Enables TCP on port 6379. Expected output: Config file updated; restart Redis with `sudo systemctl restart redis-server`.

### Step 3: Verify Configuration

**Context**: Test Redis responsiveness.

**Command** (redis-cli ping):
```bash
redis-cli -h 127.0.0.1 -p 6379 ping
```

> Pings Redis. Expected output: PONG.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[redis]]
- [[setup]]

