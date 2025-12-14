---
id: proc-access-docker-containers
tags:
  - discovery
  - docker
  - containers
type: procedure
tools:
  - '[[tools/Portainer]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.002]]'
updated_at: '2025-12-14T17:23:28.048Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.002]]'
---
# Access Docker Containers via Portainer

## Summary

This procedure uses the Portainer dashboard to enumerate and inspect Docker containers, revealing internal infrastructure details in environments like Nextcloud.

## Description

After login, the dashboard displays running containers, allowing viewing of 17 instances including Postgres and production ones. This step involves navigating the UI to gather metadata like IPs, volumes, and stacks, aiding in target selection for exploitation. Prerequisites: authenticated Portainer session. Outcomes: full visibility into the Docker backend.

## Requirements

1. Administrative access to Portainer
2. Web browser for UI interaction
3. Basic understanding of Docker concepts

## Defense

Defensive measures and detection strategies:

- Limit Portainer visibility to essential containers only
- Implement role-based access control (RBAC) in Portainer
- Monitor API calls for container enumeration

## Objectives

1. List all running containers
2. Extract internal details
3. Identify high-value targets like production services

## Instructions

### Step 1: Navigate to Containers Section

**Context**: Access the main dashboard area for Docker management.

From the sidebar, select 'Containers'.

> The list populates with active containers, showing names, statuses, and resources.

### Step 2: Inspect Container Details

**Context**: Click on individual containers to view metadata.

Select a container (e.g., Postgres) and review tabs for IP, volumes, images.

> Details expose internal network and storage, confirming access depth.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Portainer]]

## Tags

- [[Discovery]]
- [[docker]]
