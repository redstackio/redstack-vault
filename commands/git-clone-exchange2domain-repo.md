---
id: 8cdf8653-7b9c-4dcb-ba9b-564e86865d6d
name: git-clone-exchange2domain-repo
type: command
executor: bash
data: 'git clone https://github.com/Ridter/Exchange2domain.git'
output: null
created_at: '2023-04-06T03:56:08.023226+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# git-clone-exchange2domain-repo

## Command

```bash
git clone https://github.com/Ridter/Exchange2domain.git
```

## Description

Clones the Exchange2domain repository from GitHub, which contains scripts for enumerating Active Directory users via Exchange server coercion. Use this as the first step before running enumeration attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/Ridter/Exchange2domain.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/Ridter/Exchange2domain.git
```

## Expected Output

Cloning into 'Exchange2domain'...
remote: Enumerating objects: 50, done.
remote: Total 50 (delta 0), reused 0 (delta 0), pack-reused 50
Receiving objects: 100% (50/50), done.

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
