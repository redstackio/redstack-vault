---
id: cmd-gitlab-ctl-restart
data: gitlab-ctl restart unicorn
tags:
  - persistence
  - service
type: command
output: 'ok: run: unicorn: (pid 46755) 1s'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.754Z'
verified: false
validated: true
submitted: true
---
# gitlab-ctl-restart-unicorn

## Command

```bash
gitlab-ctl restart unicorn
```

## Description

Restarts the Unicorn web server in GitLab to persist file overwrites in race condition scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| restart | Action to perform | Yes |
| unicorn | Target service | Yes |

## Examples

### Basic Usage

```bash
gitlab-ctl restart unicorn
```

## Expected Output

ok: run: unicorn: (pid XXX) Xs, indicating successful restart.

## Related

- [[procedures/Restart-Unicorn-to-Persist-Overwrites]]
