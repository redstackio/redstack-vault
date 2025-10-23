---
id: 2a44eb9d-6221-4be7-af69-071bcee49486
name: Kubernetes Privileged Containers Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.178858+00:00'
updated_at: '2023-04-10T20:34:04.585809+00:00'
tags:
- '[[Information Gathering]]'
- '[[Kubernetes]]'
- '[[Privileged Containers]]'
commands:
- '[[List all files in /dev directory]]'
---

# Kubernetes Privileged Containers Information Gathering

## Summary

Kubernetes privileged containers are containers that run with elevated privileges on the host node. Attackers can abuse privileged containers to gain access to sensitive information and resources. By running commands such as 'ls /dev' and 'cat /dev/kmsg' within a privileged container, attackers can

## Description

# Description

Kubernetes privileged containers are containers that run with elevated privileges on the host node. Attackers can abuse privileged containers to gain access to sensitive information and resources. By running commands such as 'ls /dev' and 'cat /dev/kmsg' within a privileged container, attackers can gather information about the host node's devices and kernel messages, respectively. This information can be used to further exploit the Kubernetes cluster and compromise its security.

 

## Requirements

1. Access to a Kubernetes cluster with privileged containers

 

## Defense

1. Disable privileged containers if they are not needed

1. Monitor for suspicious activity within privileged containers

1. Implement RBAC policies to limit access to privileged containers

 

## Objectives

1. Gather information about the host node's devices and kernel messages

1. Identify potential vulnerabilities and attack paths within the Kubernetes cluster

 

# Instructions

1. kubectl exec -it <pod-name> --privileged -- ls /dev

 



**Code**: [[/dev]]



> This command runs the 'ls' command within a privileged container to list the host node's devices.



**Command** ([[List all files in /dev directory]]):

```bash
ls /dev
```



2. kubectl exec -it <pod-name> --privileged -- cat /dev/kmsg

 



**Code**: [[/dev/kmsg]]



> This command runs the 'cat' command within a privileged container to read the kernel messages on the host node.

## Commands Used

- [[List all files in /dev directory]]

## Tags

- [[Information Gathering]]
- [[Kubernetes]]
- [[Privileged Containers]]


