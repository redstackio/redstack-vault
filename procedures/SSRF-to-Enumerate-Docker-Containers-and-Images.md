---
id: 1918ab28-fd0d-407d-bc04-7f701e08bfdd
name: SSRF-to-Enumerate-Docker-Containers-and-Images
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.765663+00:00'
updated_at: '2023-04-10T20:24:04.996667+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Deploy Container|T1610 - Deploy Container]]'
sub_techniques: []
tags:
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF URL for Cloud Instances]]'
  - '[[tags/SSRF URL for Docker]]'
commands:
  - '[[commands/curl-list-docker-containers-via-tcp-socket]]'
  - '[[commands/curl-list-docker-containers-via-unix-socket]]'
  - '[[commands/curl-list-docker-images-via-unix-socket]]'
  - '[[commands/docker-run-bash-with-docker-socket-mount]]'
platforms:
  - Linux
  - Docker
tools: []
validated: true
---

# SSRF-to-Enumerate-Docker-Containers-and-Images

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability to enumerate running and stopped Docker containers and images on a target system. By crafting malicious requests that trick the vulnerable server into querying the local Docker API, an attacker can retrieve sensitive information about containerized environments, aiding in reconnaissance for further exploitation.

## Description

Server-Side Request Forgery (SSRF) allows an attacker to induce the target server to make unintended HTTP requests to internal resources. In this case, the technique targets the Docker daemon's API, typically exposed on localhost port 2375 (TCP) or via a Unix socket at /var/run/docker.sock. If the server application processes user-supplied URLs without proper validation, the attacker can supply Docker API endpoints like /v1.24/containers/json to list containers or /v1.24/images/json to list images. This reveals container IDs, names, statuses, image repositories, tags, and sizes, which can expose misconfigurations, outdated images, or running services for lateral movement. This is particularly effective in cloud or containerized environments where Docker is common, mapping to discovery tactics by uncovering infrastructure details without direct access.

## Requirements

1. A vulnerable web application endpoint that accepts and processes user-controlled URLs (e.g., image fetchers, webhooks, or import functions).
2. The target server must have the Docker daemon running and accessible internally (TCP on 127.0.0.1:2375 or Unix socket).
3. Network access to send HTTP requests to the vulnerable endpoint (e.g., via browser, curl, or Burp Suite).
4. Basic knowledge of the application's request format (e.g., POST with URL parameter).

## Defense

- Implement strict URL validation and whitelisting to block internal IP addresses (127.0.0.0/8, 169.254.0.0/16) and localhost references.
- Use a Web Application Firewall (WAF) to detect and block SSRF patterns, such as requests to non-public endpoints.
- Restrict Docker API access: Bind to specific interfaces, use TLS (port 2376), or limit to Unix sockets with file permissions; avoid exposing on TCP without authentication.
- Enable Docker API logging and monitor for unauthorized queries; use tools like Falco for container runtime security.

## Objectives

1. Trick the server into requesting Docker API endpoints to enumerate all containers (running and stopped).
2. Retrieve details on Docker images, including repositories and tags, to identify potential vulnerabilities.
3. Gather reconnaissance data for targeting specific containers or escalating access in a containerized environment.

## Instructions

### Step 1: Test Direct Docker API Access (Optional Verification)

**Context**: Before exploiting SSRF, verify the Docker API is accessible locally on the target by mounting the socket in a test container. This simulates internal access and confirms the endpoints work.

**Command** ([[commands/docker-run-bash-with-docker-socket-mount]]):
```bash
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock bash
```

> This command launches a temporary Bash container with the Docker socket mounted, allowing internal API queries. If successful, you'll drop into a Bash shell inside the container.

### Step 2: Enumerate Containers via Unix Socket

**Context**: From within the mounted container (or directly if you have shell access), use curl to query the Docker API via Unix socket. In an SSRF scenario, replace this with a payload URL like gopher://unix:/var/run/docker.sock:/v1.24/containers/json or http://localhost/v1.24/containers/json in the vulnerable endpoint's input field.

**Command** ([[commands/curl-list-docker-containers-via-unix-socket]]):
```bash
curl --unix-socket /var/run/docker.sock http://foo/containers/json
```

> This lists all containers in JSON format. For SSRF, submit this URL to the vulnerable app (e.g., via POST /import?url=http://127.0.0.1:2375/v1.24/containers/json). If the app echoes or processes the response, you'll see container details.

### Step 3: Enumerate Containers via TCP Socket

**Context**: If the Docker daemon uses TCP (port 2375), craft an SSRF payload targeting localhost:2375. This step confirms enumeration if Unix socket access is blocked but TCP is open internally.

**Command** ([[commands/curl-list-docker-containers-via-tcp-socket]]):
```bash
curl http://127.0.0.1:2375/v1.24/containers/json
```

> Executes a GET to the containers endpoint. Success returns a JSON array with container objects including ID, Image, Names, State, and Status. In SSRF, the server's response to your malicious request will contain this data.

### Step 4: Enumerate Images via Unix Socket

**Context**: Similar to container enumeration, query the images endpoint to list available Docker images. Use this in SSRF payloads to discover image vulnerabilities or custom builds.

**Command** ([[commands/curl-list-docker-images-via-unix-socket]]):
```bash
curl --unix-socket /var/run/docker.sock http://foo/images/json
```

> Returns JSON with image details like Id, RepoTags, and Size. For SSRF exploitation, input the equivalent URL into the vulnerable parameter and capture the echoed response.
