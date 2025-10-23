---
id: 6038c7b2-3a08-49ec-a013-a9392cd6a014
name: Docker RunC Escape
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.195954+00:00'
updated_at: '2023-04-10T20:33:49.003611+00:00'
tags:
- '[[Breaking out of Docker via runC]]'
- '[[Container - Docker Pentest]]'
commands:
- '[[Build Docker Image for CVE-2019-5736 POC]]'
- '[[Run Docker Container for CVE-2019-5736 POC]]'
---

# Docker RunC Escape

## Summary

The Docker RunC Escape procedure demonstrates an attacker's ability to escape a Docker container and gain access to the underlying host system using the CVE-2019-5736 exploit. This technique can be used to evade container-level security measures and gain privileged access to the host operating syst

## Description

# Description

The Docker RunC Escape procedure demonstrates an attacker's ability to escape a Docker container and gain access to the underlying host system using the CVE-2019-5736 exploit. This technique can be used to evade container-level security measures and gain privileged access to the host operating system.

The technique abuses a vulnerability in the runC binary, which is used by Docker to start and stop containers. By exploiting this vulnerability, an attacker can execute arbitrary code outside of the container, giving them complete control over the host system. This technique is particularly dangerous in multi-tenant environments where multiple containers are running on the same host.

The business value of this procedure is that it highlights the importance of securing container environments and implementing strong access controls to prevent unauthorized access to host systems.

 

## Requirements

1. Access to a Docker container with runC installed

1. Knowledge of the CVE-2019-5736 exploit

1. Root privileges on the host system

 

## Defense

1. Implement strong access controls to prevent unauthorized access to host systems

1. Regularly update and patch container environments to prevent known vulnerabilities

1. Implement network segmentation to isolate container environments from the host system

 

## Objectives

1. Escape the Docker container and gain access to the host system

1. Execute arbitrary code on the host system

1. Demonstrate the impact of container-level security vulnerabilities

 

# Instructions

1. This command builds and runs a malicious Docker image with the CVE-2019-5736 vulnerability. The vulnerability allows attackers to overwrite the host RunC binary and gain root-level access to the host system.

 



**Code**: [[$ docker build -t cve-2019-5736:malicious_image_PO]]



> The `docker build` command builds a Docker image with the tag `cve-2019-5736:malicious_image_POC` using the Dockerfile located at `./RunC-CVE-2019-5736/malicious_image_POC`. The `docker run` command then runs the image with the `--rm` flag to remove the container after it exits. This exploit is designed to exploit the CVE-2019-5736 vulnerability in RunC, which allows an attacker to overwrite the host RunC binary and gain root-level access to the host system. The `Exploit for CVE-2019-5736` name of this command reflects its purpose to exploit this specific vulnerability.



**Command** ([[Build Docker Image for CVE-2019-5736 POC]]):

```bash
$ docker build -t cve-2019-5736:malicious_image_POC ./RunC-CVE-2019-5736/malicious_image_POC
```





**Command** ([[Run Docker Container for CVE-2019-5736 POC]]):

```bash
$ docker run --rm cve-2019-5736:malicious_image_POC
```



## Commands Used

- [[Build Docker Image for CVE-2019-5736 POC]]
- [[Run Docker Container for CVE-2019-5736 POC]]

## Tags

- [[Breaking out of Docker via runC]]
- [[Container - Docker Pentest]]


