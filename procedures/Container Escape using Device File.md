---
id: 4cbef978-384b-447c-b43d-b86929ed35a7
name: Container Escape using Device File
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.219792+00:00'
updated_at: '2023-04-10T20:33:49.336526+00:00'
tags:
- '[[Breaking out of containers using a device file]]'
- '[[Container - Docker Pentest]]'
commands:
- '[[List file permissions outside container]]'
- '[[Receive file inside container]]'
- '[[Send file outside container]]'
---

# Container Escape using Device File

## Summary

Containerization is a popular method to deploy and run applications. However, a misconfigured or vulnerable container can lead to a complete compromise of the host system. One way to escape a container is by using a device file. An attacker can use the fdpasser command to gain access to the host sy

## Description

# Description

Containerization is a popular method to deploy and run applications. However, a misconfigured or vulnerable container can lead to a complete compromise of the host system. One way to escape a container is by using a device file. An attacker can use the fdpasser command to gain access to the host system. This technique can be used to bypass security controls and execute malicious code on the host system.

Technical Explanation: The fdpasser command is used to pass file descriptors between processes. An attacker can use this command to pass the file descriptor of the host device file to the container. By doing so, the attacker can access the host system from within the container.

Business Value: Containerization provides an efficient and scalable way to deploy and run applications. However, a misconfigured or vulnerable container can lead to a complete compromise of the host system. By understanding the risks associated with containerization, organizations can take steps to secure their infrastructure and prevent attacks.

 

## Requirements

1. Access to a vulnerable or misconfigured container

1. Ability to execute the fdpasser command

 

## Defense

1. Disable unnecessary device files or restrict access to them

1. Implement container security best practices, such as using secure images and limiting container privileges

1. Regularly monitor and audit container activity for suspicious behavior

 

## Objectives

1. Gain access to the host system from within a container

1. Bypass security controls

1. Execute malicious code on the host system

 

# Instructions

1. This command allows sending and receiving file descriptors between different processes or containers. The 'fdpasser' command can be used to send and receive file descriptors between different processes or containers. In order to use this command, you need to have root privileges in the container. The command has two modes of operation: 'send' and 'recv'.

 



**Code**: [[https://github.com/FSecureLABS/fdpasser
In contain]]



> To receive a file descriptor, run the following command in the container as root:

./fdpasser recv /moo /etc/shadow

To send a file descriptor from outside the container as UID 1000, run the following command:

./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo

After sending or receiving the file descriptor, you can verify the change by running the following command outside the container:

ls -la /etc/shadow

The output should show the updated permissions for the file.



**Command** ([[Receive file inside container]]):

```bash
./fdpasser recv /moo /etc/shadow
```





**Command** ([[Send file outside container]]):

```bash
./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo
```





**Command** ([[List file permissions outside container]]):

```bash
ls -la /etc/shadow
```



## Commands Used

- [[List file permissions outside container]]
- [[Receive file inside container]]
- [[Send file outside container]]

## Tags

- [[Breaking out of containers using a device file]]
- [[Container - Docker Pentest]]


