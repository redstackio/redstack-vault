---
id: 123e4567-e89b-12d3-a456-426614174005
name: git-clone-rocket-chat
type: command
executor: bash
data: 'git clone git@github.com:RocketChat/Rocket.Chat.git'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.422Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - setup
  - git
verified: false
validated: true
submitted: true
---

# git-clone-rocket-chat

## Command

```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

## Description

Clones the official Rocket.Chat repository from GitHub to set up the source for the vulnerable version. Used in environment preparation for vulnerability reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| git@github.com:RocketChat/Rocket.Chat.git | Repository URL via SSH | Yes |

## Examples

### Basic Usage

```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

### Advanced Usage

```bash
git clone https://github.com/RocketChat/Rocket.Chat.git  # HTTPS alternative
```

## Expected Output

Cloning into 'Rocket.Chat'...
remote: Enumerating objects: ..., done.
... (progress until completion)

## Related

- [[commands/git-checkout-rocket-chat-3-12-1]]
- [[procedures/Setup-Rocket-Chat-Vulnerable-Instance]]
