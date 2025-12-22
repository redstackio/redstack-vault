---
id: 1a9e0a85-c765-44e5-a2d2-e9242c2d3ad3
name: deepce-enumerate-docker
type: command
executor: bash
data: ./deepce.sh
output: null
created_at: '2023-04-06T03:56:16.860323+00:00'
updated_at: '2023-04-10T20:33:48.514623+00:00'
platforms:
  - Linux
tags:
  - docker
  - enumeration
verified: true
validated: true
---

# deepce-enumerate-docker

## Command

```bash
./deepce.sh
```

## Description

This command runs the deepce script in enumeration mode to discover Docker containers, mounts, and potential exploitation vectors without performing exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Default enumeration mode | N/A |

## Examples

### Basic Usage

```bash
./deepce.sh
```

### Advanced Usage

Run from within a container or host with Docker access.

## Expected Output

Detailed console output including:
- List of running containers and their PIDs
- Mounted volumes and host paths
- Privileged containers and capabilities
- Potential escape paths

## Related

- [[procedures/Docker-Security-Assessment]]
- [[commands/deepce-exploit-privileged-container]]
