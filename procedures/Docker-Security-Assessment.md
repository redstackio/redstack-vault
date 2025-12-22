---
id: 10e5af62-1f5e-47e3-887e-0a396f3c4afa
name: Docker-Security-Assessment
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.870357+00:00'
updated_at: '2023-04-10T20:33:48.499038+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Impact|TA0040 - Impact]]'
  - '[[tactics/Resource-Development|TA0042 - Resource Development]]'
techniques:
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
  - >-
    [[techniques/Container-Administration-Command|T1609 - Container
    Administration Command]]
  - '[[techniques/Deploy-Container|T1610 - Deploy Container]]'
  - >-
    [[techniques/Exploitation-for-Client-Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/Stage-Capabilities|T1608 - Stage Capabilities]]'
  - '[[techniques/System-Shutdown-Reboot|T1529 - System Shutdown/Reboot]]'
sub_techniques: []
tags:
  - '[[tags/Container - Docker Pentest]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/dockscan-basic-scan]]'
  - '[[commands/dockscan-generate-html-report]]'
  - '[[commands/deepce-enumerate-docker]]'
  - '[[commands/deepce-exploit-privileged-container]]'
  - '[[commands/deepce-exploit-sock-shadow]]'
  - '[[commands/deepce-exploit-docker-whoami]]'
platforms:
  - Linux
  - Docker
tools:
  - '[[tools/dockscan]]'
  - '[[tools/deepce]]'
validated: true
---

# Docker-Security-Assessment

## Summary

The Docker Security Assessment procedure enables security professionals to evaluate the security posture of Docker environments by scanning for vulnerabilities and misconfigurations using dockscan, followed by enumeration and potential exploitation of identified weaknesses using deepce. This approach helps identify risks such as exposed Docker sockets, privileged containers, and exploitable configurations that could allow container escape or host compromise.

## Description

This procedure targets Docker deployments to discover and exploit common security issues in containerized environments. It begins with vulnerability scanning to detect outdated images, misconfigurations, and exposed services, then proceeds to enumerate running containers and attempt exploits like privileged mode abuse, socket manipulation, and direct Docker API interactions. Applicable in red team assessments or penetration testing of containerized applications, it requires access to the host or a compromised container. Success reveals potential attack paths from container to host, aiding in securing Docker setups against real-world threats like unauthorized access or privilege escalation.

## Requirements

1. Host access with Docker installed and running containers
2. Access to the Docker socket (/var/run/docker.sock) or API endpoint
3. Installed tools: dockscan and deepce (cloned from respective repositories)
4. Network access if using remote vulnerability databases for dockscan
5. Valid credentials for privilege escalation attempts in deepce exploits

## Defense

- Regularly update Docker images and apply security patches to containers
- Restrict Docker socket access using file permissions and avoid exposing it via TCP
- Run containers in non-privileged mode and limit capabilities with --cap-drop
- Implement runtime monitoring with tools like Falco or Docker Bench for Security
- Use network policies to isolate containers and audit API access logs

## Objectives

1. Scan Docker environment for vulnerabilities and generate assessment reports
2. Enumerate containers, images, and configurations to identify misconfigurations
3. Attempt exploitation of common Docker weaknesses to assess potential impact
4. Document findings to recommend hardening measures for secure deployment

## Instructions

### Step 1: Perform Basic Docker Vulnerability Scan

**Context**: Initiate a basic scan of the Docker environment to identify immediate vulnerabilities and misconfigurations by connecting to the local Docker socket.

**Command** ([[commands/dockscan-basic-scan]]):
```bash
dockscan unix:///var/run/docker.sock
```

> This command audits the Docker installation for security issues such as vulnerable images or exposed ports. It provides console output highlighting risks without generating a file report.

### Step 2: Generate Detailed HTML Vulnerability Report

**Context**: Extend the scan to produce a comprehensive HTML report, incorporating a remote vulnerability database for deeper analysis of image vulnerabilities.

**Command** ([[commands/dockscan-generate-html-report]]):
```bash
dockscan -r html -o myreport -v tcp://example.com:5422
```

> The report is saved as 'myreport.html' and includes detailed findings on container security. Replace 'tcp://example.com:5422' with a valid vulnerability feed endpoint if available.

### Step 3: Enumerate Docker Environment

**Context**: Use deepce to gather information on running containers, images, and host details without immediate exploitation, building reconnaissance for targeted attacks.

**Command** ([[commands/deepce-enumerate-docker]]):
```bash
./deepce.sh
```

> This runs the full enumeration mode, outputting details like container lists, mounts, and potential escape vectors. Review output for exploitable features like privileged flags.

### Step 4: Attempt Privileged Container Exploitation

**Context**: Target privileged containers to escalate access using provided credentials, simulating an attacker gaining higher privileges within or beyond the container.

**Command** ([[commands/deepce-exploit-privileged-container]]):
```bash
./deepce.sh --no-enumeration --exploit PRIVILEGED --username deepce --password deepce
```

> Skips enumeration to directly exploit privileged mode. Substitute actual username and password; success grants elevated shell or access to host resources.

### Step 5: Exploit Docker Socket for Shadow File Access

**Context**: Leverage exposed Docker sockets to read sensitive files like /etc/shadow, demonstrating information disclosure risks from socket misconfigurations.

**Command** ([[commands/deepce-exploit-sock-shadow]]):
```bash
./deepce.sh --no-enumeration --exploit SOCK --shadow
```

> This attempts to mount and read the shadow file via socket exploitation. Output includes hashed passwords if successful, useful for offline cracking.

### Step 6: Exploit Docker API for Command Execution

**Context**: Use the Docker API vulnerability to execute arbitrary commands inside containers, verifying remote code execution capabilities.

**Command** ([[commands/deepce-exploit-docker-whoami]]):
```bash
./deepce.sh --no-enumeration --exploit DOCKER --command "whoami>/tmp/hacked"
```

> Executes 'whoami' and writes output to /tmp/hacked inside a container. Check the file for the executing user, indicating successful RCE.
