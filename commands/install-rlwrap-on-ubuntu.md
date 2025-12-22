---
id: 0a35dc17-9d4e-468a-999b-48e5375f0d9b
name: install-rlwrap-on-ubuntu
type: command
executor: bash
data: sudo apt-get install rlwrap
output: null
created_at: '2023-04-06T03:56:24.983041+00:00'
updated_at: '2023-04-10T20:25:31.247390+00:00'
platforms:
  - Linux
tags:
  - installation
  - rlwrap
verified: true
validated: true
---

# install-rlwrap-on-ubuntu

## Command

```bash
sudo apt-get install rlwrap
```

## Description

Installs rlwrap, a readline wrapper for adding command history and editing to tools like netcat during reverse shell handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Run with elevated privileges | Yes |
| apt-get | Package manager | Built-in |
| install | Install action | Built-in |
| rlwrap | Package name | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install rlwrap
```

### Update Before Install

```bash
sudo apt-get update && sudo apt-get install rlwrap
```

## Expected Output

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  rlwrap
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/58.4 kB of archives.
After this operation, 200 kB of additional disk space will be used.
Selecting previously unselected package rlwrap.
(Reading database ... 12345 files and directories currently installed.)
Preparing to unpack .../rlwrap_0.45+dfsg-1_amd64.deb ...
Unpacking rlwrap (0.45+dfsg-1) ...
Setting up rlwrap (0.45+dfsg-1) ...

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
- [[commands/rlwrap-nc-connect-to-host]]
