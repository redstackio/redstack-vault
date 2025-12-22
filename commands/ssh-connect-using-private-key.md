---
type: command
executor: bash
data: ssh -i $_PRIVATE_KEY -l $_USER $_TARGET_IP
output: >-
  root@kali:~# ssh -i id_rsa -l bob 10.10.10.10

  The authenticity of host '10.10.10.10 (10.10.10.10)' can't be established. 

  ECDSA key fingerprint is SHA256:lwH7db30salekhX8rTgJTq79lawse2cXftewhu8LsEs.

  Are you sure you want to continue connecting (yes/no)? yes

  Warning: Permanently added '10.10.10.10' (ECDSA) to the list of known hosts.

  Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-23-generic x86_64)

   * Documentation:  https://help.ubuntu.com/ 
  New release '14.04.5 LTS'
  available.                                                                   

  Run 'do-release-upgrade' to upgrade to it. 


  Last login:Fri Feb 16 14:50:29 2018 from 10.10.14.3
platforms:
  - Linux
tags:
  - ssh
  - access
verified: true
validated: true
---

# ssh-connect-using-private-key

## Command

```bash
ssh -i $_PRIVATE_KEY -l $_USER $_TARGET_IP
```

## Description

Establishes an SSH connection to a remote host using a specified private key file for authentication. This is useful for passwordless access in automated scripts or when passwords are unknown.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PRIVATE_KEY | Path to the private key file (e.g., id_rsa) | Yes |
| $_USER | Username to authenticate as | Yes |
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -i | Flag to specify the identity (private key) file | Built-in |
| -l | Flag to specify the login username | Built-in |

## Examples

### Basic Usage

```bash
ssh -i id_rsa -l root 10.10.10.10
```

### Advanced Usage

Connect on a non-standard port:

```bash
ssh -i key.pem -l user -p 2222 10.10.10.10
```

## Expected Output

Initial connection may prompt for host authenticity verification. Upon success, it drops into an interactive shell on the remote host, showing a welcome message or prompt.

## Related

- [[procedures/connect-to-ssh-server-with-private-key]]
