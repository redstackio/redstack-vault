---
data: 'sudo docker run -p 80:5488 -v /jsreport-home:/jsreport jsreport/jsreport:2.5.0'
tags:
  - setup
  - docker
type: command
executor: bash
platforms:
  - Linux
id: 93312308-6cd9-4a9f-8663-2f17ffeeb2b2
created_at: '2025-12-14T17:23:24.950Z'
updated_at: '2025-12-14T17:23:24.950Z'
verified: false
validated: true
submitted: true
---
# docker-run-jsreport-vulnerable

## Command

```bash
sudo docker run -p 80:5488 -v /jsreport-home:/jsreport jsreport/jsreport:2.5.0
```

## Description

Starts a Docker container for the vulnerable jsreport 2.5.0 image, mapping ports and mounting a volume for persistence. Used to deploy the target environment for RCE exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p 80:5488` | Maps host port 80 to container 5488 for web access | Yes |
| `-v /jsreport-home:/jsreport` | Mounts host directory for data storage | Yes |

## Examples

### Basic Usage

```bash
sudo docker run -p 80:5488 -v /jsreport-home:/jsreport jsreport/jsreport:2.5.0
```

### Advanced Usage

Add `--rm` for auto-cleanup:

```bash
sudo docker run --rm -p 80:5488 -v /jsreport-home:/jsreport jsreport/jsreport:2.5.0
```

## Expected Output

Docker logs showing "info: jsreport server successfully started on port 5488" and container ID.

## Related

- [[procedures/setup-jsreport-server-with-docker]]
