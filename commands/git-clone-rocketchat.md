---
id: cmd-git-clone-rocketchat
data: 'git clone git@github.com:RocketChat/Rocket.Chat.git'
tags:
  - setup
  - git
type: command
output: Cloning into 'Rocket.Chat'...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.921Z'
verified: false
validated: true
submitted: true
---
# git-clone-rocketchat

## Command

```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

## Description

Clones the official Rocket.Chat GitHub repository for local setup and testing of the vulnerable instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| git@github.com:RocketChat/Rocket.Chat.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

### Advanced Usage

```bash
git clone --depth 1 git@github.com:RocketChat/Rocket.Chat.git
```

## Expected Output

Cloned repository in local directory Rocket.Chat.

## Related

- [[commands/cd-rocketchat]]
