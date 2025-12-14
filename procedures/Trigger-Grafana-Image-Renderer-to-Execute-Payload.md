---
id: proc-uuid-004
tags:
  - rce
  - image-renderer
  - trigger
  - grafana
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:54.870Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Trigger-Grafana-Image-Renderer-to-Execute-Payload

## Summary

This procedure triggers the Grafana image rendering endpoint, causing the server to process the injected configuration and execute the bash reverse shell command, connecting back to the attacker's listener.

## Description

Accessing the /render endpoint in Grafana invokes the grafana-image-renderer plugin, which uses the modified rendering_args to prefix the renderer command with bash -c, executing the reverse shell. This achieves RCE without further authentication, as the configuration is already applied via the API.

## Requirements

1. Injected configuration from prior step
2. Access to Grafana instance URL (https://INSTANCE_SUBDOMAIN.aivencloud.com)
3. Active netcat listener on port 4444

## Defense

Defensive measures and detection strategies:

- Disable or sandbox image rendering plugins
- Monitor renderer logs for anomalous command prefixes
- Restrict endpoint access and validate renderer arguments

## Objectives

1. Invoke the vulnerable rendering process
2. Execute the injected bash command
3. Establish reverse shell session

## Instructions

### Step 1: Access Render Endpoint

**Context**: Use a browser or HTTP client to hit the trigger URL.

Open https://INSTANCE_SUBDOMAIN.aivencloud.com/render/x in a web browser, replacing INSTANCE_SUBDOMAIN with your Grafana service details.

**Expected Output**: Page load attempt; renderer invoked in background.

### Step 2: Verify Shell Connection

**Context**: Check the netcat listener for incoming connection.

Observe the listener output for the reverse shell connection.

**Expected Output**: Connection from Grafana IP, followed by bash prompt (e.g., "whoami" returns grafana user).

### Step 3: Interact with Shell

**Context**: Use the shell for post-exploitation.

Once connected, run commands like `id` or `ls` to confirm access.

**Expected Output**: Target system responses indicating RCE success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- image-renderer
- trigger
- grafana
