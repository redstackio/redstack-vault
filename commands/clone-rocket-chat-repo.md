---
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
updated_at: '2025-12-14T03:46:14.800Z'
id: aa3cd8ac-4e65-4c51-8065-d2e27ced0d51
verified: false
validated: true
submitted: true
---
# clone-rocket-chat-repo

## Command

```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

## Description

Clones the official Rocket.Chat repository for setting up a vulnerable instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| git@github.com:RocketChat/Rocket.Chat.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

## Expected Output

Progress bars for cloning files, ending with directory creation.

## Related

- [[commands/cd-rocket-chat]]
