---
id: ae5b405c-7eca-4f3b-bcbf-c7161dbe199e
name: docker-pull-aquatone-image
type: command
executor: bash
data: docker pull txt3rob/aquatone-docker
output: null
created_at: '2023-04-06T03:56:25.578356+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - installation
verified: true
validated: true
---

# docker-pull-aquatone-image

## Command

```bash
docker pull txt3rob/aquatone-docker
```

## Description

Downloads the Aquatone Docker image from Docker Hub for containerized execution without local Ruby setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Pulls latest image | No |

## Examples

### Basic Usage

```bash
docker pull txt3rob/aquatone-docker
```

## Expected Output

latest: Pulling from txt3rob/aquatone-docker
Digest: sha256:...
Status: Downloaded newer image for txt3rob/aquatone-docker:latest

## Related

- [[procedures/Subdomain-Enumeration-with-Aquatone]]
- [[tools/Aquatone]]
