---
id: uuid-enable-flag
tags:
  - feature-flag
  - rails-console
  - configuration
type: procedure
tools:
  - '[[tools/Docker]]'
  - '[[tools/GitLab-Rails-Console]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/docker-exec-bash-gitlab]]'
  - '[[commands/gitlab-rails-console]]'
  - '[[commands/feature-enable-vue-issuables-list]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-13T23:52:24.529Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Enable-Vue-Issuables-List-Feature-Flag

## Summary

This procedure accesses the GitLab Rails console via Docker to enable the vue_issuables_list feature flag, activating the Vue.js-based issue list rendering that exposes the stored XSS vulnerability.

## Description

GitLab uses feature flags to toggle experimental features. The vue_issuables_list flag switches the group issue list to a Vue component that unsafely renders user full names, allowing HTML attribute injection. This step requires container access and Ruby/Rails knowledge. Prerequisites include a running GitLab container. Outcomes: Flag enabled, verifiable in console, preparing the instance for payload testing.

## Requirements

1. Running GitLab Docker container
2. Root or sudo access to host for Docker exec
3. Basic Ruby/Rails familiarity

## Defense

Defensive measures and detection strategies:

- Disable or monitor feature flags in production via audit logs
- Restrict Rails console access with RBAC
- Alert on unauthorized flag changes in GitLab logs

## Objectives

1. Activate the vulnerable rendering path
2. Verify flag status without disrupting services
3. Enable subsequent XSS injection steps

## Instructions

### Step 1: Access Container Shell

**Context**: Enter the interactive bash shell of the GitLab container to run administrative commands.

**Command** ([[commands/docker-exec-bash-gitlab]]):
```bash
docker exec -it gitlab /bin/bash
```

> Starts an interactive TTY session inside the container. Expected output: Bash prompt (root@gitlab:/#). If failed, check container status with `docker ps`.

### Step 2: Launch Rails Console

**Context**: Start the interactive Ruby console for GitLab to execute feature management commands.

**Command** ([[commands/gitlab-rails-console]]):
```bash
gitlab-rails console
```

> Initializes the Rails IRB session. Expected output: irb(main):001:0> prompt. Use `exit` to quit.

### Step 3: Enable Feature Flag

**Context**: Toggle the specific flag to enable Vue-based issue list.

**Command** ([[commands/feature-enable-vue-issuables-list]]):
```ruby
Feature.enable(:vue_issuables_list)
```

> Enables the flag globally. Expected output: true or success message. Verify with `Feature.enabled?(:vue_issuables_list)` returning true.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/docker-exec-bash-gitlab]]
- [[commands/gitlab-rails-console]]
- [[commands/feature-enable-vue-issuables-list]]

## Tools Used

- [[tools/Docker]]
- [[tools/GitLab-Rails-Console]]

## Tags

- feature-flag
- rails-console
- configuration
