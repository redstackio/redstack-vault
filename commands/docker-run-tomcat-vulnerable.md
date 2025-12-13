---
data: 'docker run -d --name hrs_tomcat_11 -p 43022:8080 tomcat:10.1.13'
tags:
  - docker
  - setup
type: command
executor: bash
platforms:
  - Linux
id: 468b50c0-16b6-40bf-bf0a-de30279172a2
created_at: '2025-12-13T09:01:22.412Z'
updated_at: '2025-12-13T09:01:22.412Z'
verified: false
validated: true
submitted: true
---
# docker-run-tomcat-vulnerable

## Command

```bash
docker run -d --name hrs_tomcat_11 -p 43022:8080 tomcat:10.1.13
```

## Description

Runs a Docker container with Apache Tomcat version 10.1.13 in detached mode, naming it hrs_tomcat_11 and mapping host port 43022 to container port 8080, used to set up a vulnerable instance for reproducing the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Run in detached mode | Yes |
| `--name` | Assign name to container | Yes |
| `-p` | Publish container port to host | Yes |
| `tomcat:10.1.13` | Docker image to use | Yes |

## Examples

### Basic Usage

```bash
docker run -d --name hrs_tomcat_11 -p 43022:8080 tomcat:10.1.13
```

## Expected Output

Container ID or startup confirmation.

## Related

- [[procedures/Set-Up-Vulnerable-Tomcat-Instance-with-Docker]]
- [[tools/Docker]]
