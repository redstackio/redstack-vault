---
id: 0886eebf-303d-443d-8881-4e74d7c05f72
name: install-slowhttptest-on-ubuntu
type: command
executor: bash
data: sudo apt-get install slowhttptest
output: null
created_at: '2020-09-06T18:43:30.675346+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - installation
  - DoS
verified: true
validated: true
---

# install-slowhttptest-on-ubuntu

## Command

```bash
sudo apt-get install slowhttptest
```

## Description

This command installs the slowhttptest tool on Ubuntu or other Debian-based Linux distributions using the apt package manager. It is the first step in setting up the environment for Slow HTTP DoS testing, including Slow Read attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevates privileges for package installation | Yes |
| `apt-get` | Debian package management tool | Built-in |
| `install` | Installs the specified package | Built-in |
| `slowhttptest` | The Slow HTTP DoS testing tool package | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install slowhttptest
```

### Advanced Usage

```bash
sudo apt-get update && sudo apt-get install slowhttptest
```

(Precede with `apt-get update` to refresh package lists if needed.)

## Expected Output

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  slowhttptest
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 50.0 kB of archives.
After this operation, 150 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu focal/universe amd64 slowhttptest amd64 1.6-1 [50.0 kB]
Fetched 50.0 kB in 1s (50.0 kB/s)  
Selecting previously unselected package slowhttptest.
(Reading database ... 123456 files and directories currently installed.)
Preparing to unpack .../slowhttptest_1.6-1_amd64.deb ...
Unpacking slowhttptest (1.6-1) ...
Setting up slowhttptest (1.6-1) ...

## Related

- [[procedures/Slow-Read-DoS-Attack]]
- [[commands/slowhttptest-slow-read-dos]]
