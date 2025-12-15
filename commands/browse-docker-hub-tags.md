---
data: >-
  echo "Visit https://hub.docker.com/r/taskcluster/taskcluster/tags" && curl -s
  https://hub.docker.com/v2/repositories/taskcluster/taskcluster/tags/?page_size=100
  | jq '.results[].name'
tags:
  - recon
  - docker
type: command
executor: bash
platforms:
  - Linux
  - Cloud
id: 95fea214-fa70-425f-a216-9718bad4361b
created_at: '2025-12-14T17:31:42.940Z'
updated_at: '2025-12-14T17:31:42.940Z'
verified: false
validated: true
submitted: true
---
# browse-docker-hub-tags

## Command

```bash
echo "Visit https://hub.docker.com/r/taskcluster/taskcluster/tags" && curl -s https://hub.docker.com/v2/repositories/taskcluster/taskcluster/tags/?page_size=100 | jq '.results[].name'
```

## Description

This command queries the Docker Hub API to list tags for the taskcluster/taskcluster repository, aiding in reconnaissance of available images.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `curl -s` | Silent curl to fetch API data | Yes |
| `jq '.results[].name'` | Parse JSON to extract tag names | Yes |
| `page_size=100` | Limit results to 100 tags | No |

## Examples

### Basic Usage

```bash
echo "Visit https://hub.docker.com/r/taskcluster/taskcluster/tags" && curl -s https://hub.docker.com/v2/repositories/taskcluster/taskcluster/tags/?page_size=100 | jq '.results[].name'
```

### Advanced Usage

```bash
curl -s https://hub.docker.com/v2/repositories/taskcluster/taskcluster/tags/?page=1&page_size=50 | jq '.results[] | select(.name | contains("v15")) | .name'
```

## Expected Output

A list of tag names, e.g., ["v15.0.0-20-g0eca18b7c", "c061025dc", ...]

## Related

- [[commands/docker-pull-taskcluster]]
