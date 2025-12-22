---
id: 6b223b97-82e4-4174-81c0-834f2d727f96
type: command
executor: bash
data: hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET $_SERVICE
output: >-
  Hydra v9.5 (c) 2023 by van Hauser/THC - Please do not use in military or
  secret service organizations, or for illegal purposes (this is educational).


  [22][ssh] host: 10.10.10.10   login: admin   password: password123

  1 of 1 target successfully completed, 1 valid password found

  None of the login-names found on first pass will be tested again.

  All 1 targets completed.
created_at: '2019-08-28T21:17:21.173096+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - network
verified: true
validated: true
---

# hydra-brute-force-network-service

## Command

```bash
hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET $_SERVICE
```

## Description

Brute-forces login credentials for network services like SSH, FTP, or Telnet by attempting combinations from username and password lists against the specified service on the target host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L $_USERNAME_LIST | Path to file containing usernames | Yes |
| -P $_PASSWORD_LIST | Path to file containing passwords | Yes |
| $_TARGET | Target IP address or hostname | Yes |
| $_SERVICE | Service protocol (e.g., ssh, ftp, telnet) | Yes |
| -t | Number of parallel tasks (default: 16) | No |
| -V | Verbose output | No |

## Examples

### Basic Usage

```bash
hydra -L users.txt -P passwords.txt 10.10.10.10 ssh
```

### With Parallel Tasks

```bash
hydra -t 32 -L users.txt -P passwords.txt 10.10.10.10 ftp
```

## Expected Output

When successful, Hydra reports valid credentials in the format: [port][service] host: target   login: username   password: password
Followed by a summary of targets completed and passwords found.

## Related

- [[tools/Hydra]]
- [[procedures/Brute-Force-Network-Service-Login-with-Hydra]]
