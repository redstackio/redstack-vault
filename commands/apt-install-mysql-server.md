---
id: 2139a407-fd2e-4580-8bdf-8c82a67adb29
name: apt-install-mysql-server
type: command
executor: bash
data: sudo apt-get install mysql-server-5.7
output: null
created_at: '2023-04-06T03:56:34.392828+00:00'
updated_at: '2023-04-10T20:22:52.410936+00:00'
platforms:
  - Linux
tags:
  - installation
  - database
verified: true
validated: true
---

# apt-install-mysql-server

## Command

```bash
sudo apt-get install mysql-server-5.7
```

## Description

This command installs the MySQL server package version 5.7 on Debian-based Linux distributions like Ubuntu or Kali Linux, useful for setting up a local test environment to replicate SQL injection vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Run with superuser privileges | Yes |
| apt-get | Package manager | Built-in |
| install | Install action | Built-in |
| mysql-server-5.7 | Specific MySQL server package | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install mysql-server-5.7
```

### With Update

```bash
sudo apt-get update && sudo apt-get install mysql-server-5.7
```

## Expected Output

Reading package lists... Done
Building dependency tree       
Reading state information... Done
... (progress)
Setting up mysql-server-5.7 (5.7.XX) ...

Success indicated by no errors and MySQL service ready to start.

## Related

- [[procedures/MySQL-Union-Based-Injection-to-Extract-Column-Names]]
