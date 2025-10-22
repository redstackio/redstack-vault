---
id: 1918ab28-fd0d-407d-bc04-7f701e08bfdd
name: Server-Side Request Forgery for Docker Containers and Images Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.765663+00:00'
updated_at: '2023-04-10T20:24:04.996667+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Deploy Container|T1610 - Deploy Container]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Docker]]'
commands:
- '[[List Containers Using curl]]'
- '[[List Docker Containers]]'
- '[[List Images Using curl]]'
- '[[Run Bash in Docker Container]]'
---

# Server-Side Request Forgery for Docker Containers and Images Enumeration

## Summary

This procedure utilizes Server-Side Request Forgery (SSRF) to enumerate Docker containers and images. The attacker sends a malicious request to the server, tricking it into making a request to the Docker API. This allows the attacker to discover and enumerate all running containers and images on th

## Description

# Description

This procedure utilizes Server-Side Request Forgery (SSRF) to enumerate Docker containers and images. The attacker sends a malicious request to the server, tricking it into making a request to the Docker API. This allows the attacker to discover and enumerate all running containers and images on the target system. This technique can be used for reconnaissance purposes in order to identify potential targets for further exploitation.

Technical Details: The attacker sends a request to the server with a malicious URL that points to the Docker API. The server, believing the request to be legitimate, makes a request to the specified URL and returns the response to the attacker. The response contains information about all running containers and images on the target system.

Business Value: This procedure can be used by attackers to gather information about the target environment, allowing them to identify potential targets for further exploitation. It is important for organizations to be aware of this technique and take steps to prevent it from being used against them.

## Requirements

1. Access to the target system

1. Authenticated access to the Docker API

## Defense

1. Implement input validation on all user-supplied input to prevent SSRF attacks

1. Use a web application firewall (WAF) to detect and block malicious requests

1. Restrict access to the Docker API to only trusted hosts and users

## Objectives

1. Enumerate all running Docker containers on the target system

1. Enumerate all Docker images on the target system

# Instructions

1. To list all Docker containers and images, use the following commands:

**Code**: [[http://127.0.0.1:2375/v1.24/containers/json

Simpl]]

> 1. To list all running and stopped Docker containers, use the command 'docker ps -a'.

2. To list all Docker images, use the command 'docker images'.

Note: You can use additional arguments with these commands to filter the output and get more specific information about the containers and images.

**Command** ([[List Docker Containers]]):

```bash
http://127.0.0.1:2375/v1.24/containers/json
```

**Command** ([[Run Bash in Docker Container]]):

```bash
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock bash
```

**Command** ([[List Containers Using curl]]):

```bash
curl --unix-socket /var/run/docker.sock http://foo/containers/json
```

**Command** ([[List Images Using curl]]):

```bash
curl --unix-socket /var/run/docker.sock http://foo/images/json
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Deploy Container|T1610 - Deploy Container]]

## Commands Used

- [[List Containers Using curl]]
- [[List Docker Containers]]
- [[List Images Using curl]]
- [[Run Bash in Docker Container]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Docker]]
