---
tags:
  - setup
  - vulnerable-env
  - docker
  - php-fpm
  - nginx
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/docker-build-vulnerable-env]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 88af4e0a-391c-43b6-8f37-ea74cfa0d415
created_at: '2025-12-14T17:23:49.477Z'
updated_at: '2025-12-14T17:23:49.477Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Vulnerable-PHP-FPM-and-Nginx-Environment

## Summary

This procedure sets up a Docker-based environment with a vulnerable PHP version (pre-CVE-2019-11043 patch) and Nginx configured to expose the FastCGI PATH_INFO flaw, enabling safe testing of the buffer underflow exploit.

## Description

The setup replicates real-world deployments where php-fpm runs behind Nginx. The Dockerfile from the phuip-fpizdam repository builds PHP 7.3.x (vulnerable) with fpm_main.c unpatched. Nginx config includes the fastcgi_split_pathinfo directive with a regexp that can be broken by encoded newlines, allowing empty PATH_INFO to trigger the underflow. This environment runs on localhost:80, isolating the test from production systems.

## Requirements

1. Docker installed on a Linux host
2. Access to the phuip-fpizdam GitHub repository for the Dockerfile
3. Basic knowledge of Docker and web server configs

## Defense

Defensive measures and detection strategies:

- Patch PHP to version addressing CVE-2019-11043
- Configure Nginx to validate and sanitize PATH_INFO inputs, rejecting encoded newlines
- Monitor php-fpm logs for buffer errors or unusual memory access patterns

## Objectives

1. Establish a testable vulnerable stack
2. Verify Nginx-php-fpm integration
3. Prepare for exploit triggering without risking live systems

## Instructions

### Step 1: Clone Repository and Build Docker Image

**Context**: Download the exploit repo containing the vulnerable Dockerfile and build the image.

**Command** ([[commands/docker-build-vulnerable-env]]):
```bash
git clone https://github.com/neex/phuip-fpizdam.git
cd phuip-fpizdam
docker build -t vulnerable-php-fpm .
```

> This clones the repo, navigates to it, and builds the image using the provided Dockerfile, which installs vulnerable PHP and configures Nginx.

### Step 2: Run the Container

**Context**: Start the container to expose the vulnerable service on port 80.

**Command** ([[commands/docker-build-vulnerable-env]]):
```bash
docker run -d -p 80:80 --name vuln-php vulnerable-php-fpm
```

> Launches the container in detached mode, mapping host port 80 to container port 80. Expected output: Container ID and running status.

### Step 3: Verify Setup

**Context**: Confirm the environment is vulnerable and responsive.

**Command** ([[commands/curl-trigger-empty-pathinfo]]):
```bash
curl http://localhost/ -v
```

> Basic GET request should return a PHP response or default page, with verbose logs showing Nginx forwarding to php-fpm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-build-vulnerable-env]]
- [[commands/curl-trigger-empty-pathinfo]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- vulnerable-env
