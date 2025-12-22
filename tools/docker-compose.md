---
url: 'https://docs.docker.com/compose'
tags:
  - container-orchestration
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.375Z'
id: 8826dec9-1af4-4651-803b-a8c4295be821
validated: true
submitted: true
---
# docker-compose

**Status**: Unverified

## Overview

Tool for defining and running multi-container Docker applications, used to spin up Rocket.Chat with MongoDB.

## Description

Orchestrates the vulnerable stack from the repo's docker-compose.yml, starting services in background.

## Features

- Feature 1: YAML config for services
- Feature 2: Detached mode
- Feature 3: Dependency management

## Installation

### Requirements

- Docker

### Install Commands

```bash
sudo apt install docker-compose
```

## Basic Usage

```bash
docker-compose --help
```

### Common Options

| Option | Description |
|--------|-------------|
| up -d | Start in detached |

## Examples

### Example 1: Basic Usage

```bash
docker-compose up -d
```

### Example 2: Advanced Usage

```bash
docker-compose up -d --build
```

## MITRE ATT&CK Mapping

### Techniques

- [[Deploy Container]] Deploy Container

### Tactics

- [[Persistence]]

## Detection

- Docker container startups

## Related Procedures


## Related Tools

- [[tools/git]]

## References

- Docker Compose docs
