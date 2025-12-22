---
tags:
  - setup
  - proxy
  - haproxy
type: procedure
tools:
  - '[[tools/HAProxy]]'
  - '[[tools/wget]]'
  - '[[tools/tar]]'
  - '[[tools/make]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/wget-download-haproxy]]'
  - '[[commands/tar-extract-haproxy]]'
  - '[[commands/cd-change-to-haproxy-dir]]'
  - '[[commands/make-compile-haproxy]]'
  - '[[commands/haproxy-run-with-config]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 15fd05f5-623c-4db2-9d02-7ab3e00dde89
created_at: '2025-12-13T09:01:22.135Z'
updated_at: '2025-12-13T09:01:22.135Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Compile and Setup HAProxy Frontend Proxy

## Summary

This procedure compiles and configures HAProxy version 1.5.3 as a frontend proxy that restricts access to specific URIs, setting up the environment for demonstrating HTTP request smuggling vulnerabilities when paired with a Node.js backend.

## Description

The procedure involves downloading, extracting, compiling, and running HAProxy with a configuration that binds to port 80, denies access to /flag paths via ACL, and proxies requests to a backend server on 127.0.0.1:8080. This setup creates a desynchronization point for smuggling attacks due to differences in header parsing between HAProxy and Node.js.

## Requirements

1. Linux environment with build tools installed
2. Internet access for downloading source code
3. Configuration file (haproxy.cfg) prepared with appropriate ACLs and backend proxy settings

## Defense

Defensive measures and detection strategies:

- Use updated versions of HAProxy and Node.js that mitigate smuggling vulnerabilities
- Monitor proxy logs for anomalous header usage or desynchronized requests

## Objectives

1. Establish a vulnerable proxy setup
2. Prepare for smuggling exploitation
3. Verify proxy restrictions are in place

## Instructions

### Step 1: Download HAProxy Source

**Context**: Obtain the source code for HAProxy 1.5.3 to compile a vulnerable version.

**Command** ([[commands/wget-download-haproxy]]):
```bash
wget https://www.haproxy.org/download/1.5/src/haproxy-1.5.3.tar.gz
```

> Downloads the tarball from the official site; expect the file to be saved locally.

### Step 2: Extract Tarball

**Context**: Extract the downloaded archive to access the source files.

**Command** ([[commands/tar-extract-haproxy]]):
```bash
tar zxvf haproxy-1.5.3.tar.gz
```

> Extracts the contents into a directory named haproxy-1.5.3.

### Step 3: Change Directory

**Context**: Navigate into the extracted directory for compilation.

**Command** ([[commands/cd-change-to-haproxy-dir]]):
```bash
cd haproxy-1.5.3
```

> Changes the working directory to haproxy-1.5.3.

### Step 4: Compile HAProxy

**Context**: Build the HAProxy binary targeting Linux kernel 2.6.28+.

**Command** ([[commands/make-compile-haproxy]]):
```bash
make TARGET=linux2628
```

> Compiles the source code into an executable binary.

### Step 5: Run HAProxy

**Context**: Start HAProxy with the custom configuration in debug mode.

**Command** ([[commands/haproxy-run-with-config]]):
```bash
./haproxy -f haproxy.cfg -d
```

> Launches HAProxy, binding to port 80 and enabling debug output.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/wget-download-haproxy]]
- [[commands/tar-extract-haproxy]]
- [[commands/cd-change-to-haproxy-dir]]
- [[commands/make-compile-haproxy]]
- [[commands/haproxy-run-with-config]]

## Tools Used

- [[tools/HAProxy]]
- [[tools/wget]]
- [[tools/tar]]
- [[tools/make]]

## Tags

- [[setup]]
- [[proxy]]
- [[tools/HAProxy]]
