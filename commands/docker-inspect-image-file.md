---
data: >-
  docker run --rm -it taskcluster/taskcluster:v15.0.0-20-g0eca18b7c cat
  /app/node_modules/sentry-api/test.js | grep -i token
tags:
  - docker
  - inspect
type: command
executor: bash
platforms:
  - Linux
  - Docker
id: ae024f68-a7d6-42ea-a77e-89dc82d33d86
created_at: '2025-12-14T17:31:42.936Z'
updated_at: '2025-12-14T17:31:42.936Z'
verified: false
validated: true
submitted: true
---
# docker-inspect-image-file

## Command

```bash
docker run --rm -it taskcluster/taskcluster:v15.0.0-20-g0eca18b7c cat /app/node_modules/sentry-api/test.js | grep -i token
```

## Description

Runs a temporary container to extract and search for tokens in a specific file within the image.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--rm` | Remove container after run | Yes |
| `-it` | Interactive mode | Yes |
| `cat /app/node_modules/sentry-api/test.js` | Display file contents | Yes |
| `grep -i token` | Case-insensitive search for 'token' | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -it taskcluster/taskcluster:v15.0.0-20-g0eca18b7c cat /app/node_modules/sentry-api/test.js | grep -i token
```

### Advanced Usage

```bash
docker run --rm taskcluster/taskcluster:v15.0.0-20-g0eca18b7c find /app -name "*.js" -exec grep -l "token" {} \;
```

## Expected Output

Line containing the token: e.g., "Bearer 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9"

## Related

- [[commands/curl-sentry-api-test]]
