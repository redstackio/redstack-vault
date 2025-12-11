---
data: ssh git@10.26.0.5
tags:
  - ssh
  - connect
type: command
executor: bash
platforms:
  - Linux
id: 8940fc7a-0f9d-4f28-bbf4-30ab55c067f4
created_at: '2025-12-11T03:47:39.645Z'
updated_at: '2025-12-11T03:47:39.645Z'
verified: false
validated: true
submitted: true
---
# ssh-git-connect

## Command

```bash
ssh git@10.26.0.5
```

## Description

Connects to the GitLab server as git user using the injected SSH key, used after key upload to gain RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git@10.26.0.5` | Specifies user and host | Yes |

## Examples

### Basic Usage

```bash
ssh git@target
```

### Advanced Usage

```bash
ssh -i custom_key git@target
```

## Expected Output

Shell access on the server, prompting for commands.

## Related

- [[procedures/Gain-SSH-Shell-Access]]
- [[tools/ssh]]
