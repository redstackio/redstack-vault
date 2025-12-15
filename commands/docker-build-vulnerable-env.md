---
data: >-
  git clone https://github.com/neex/phuip-fpizdam.git && cd phuip-fpizdam &&
  docker build -t vulnerable-php-fpm . && docker run -d -p 80:80 --name vuln-php
  vulnerable-php-fpm
tags:
  - setup
  - docker
type: command
executor: bash
platforms:
  - Linux
id: 15376ebc-6527-4d97-abf8-867b1f89b54f
created_at: '2025-12-14T17:23:49.465Z'
updated_at: '2025-12-14T17:23:49.465Z'
verified: false
validated: true
submitted: true
---
# docker-build-vulnerable-env

## Command

```bash
git clone https://github.com/neex/phuip-fpizdam.git && cd phuip-fpizdam && docker build -t vulnerable-php-fpm . && docker run -d -p 80:80 --name vuln-php vulnerable-php-fpm
```

## Description

This command clones the phuip-fpizdam repository, builds a Docker image with vulnerable PHP and Nginx, and runs the container exposing port 80 for testing the CVE-2019-11043 exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git clone` | Clones the repo | Yes |
| `docker build` | Builds image from Dockerfile | Yes |
| `docker run` | Starts container | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/neex/phuip-fpizdam.git && cd phuip-fpizdam && docker build -t vulnerable-php-fpm .
```

### Advanced Usage

```bash
docker run -d -p 80:80 --name vuln-php -v /path/to/logs:/var/log/nginx vulnerable-php-fpm
```

## Expected Output

Repository cloned successfully.
Successfully built <image_id>
<container_id>

## Related

- [[Related Procedure]]
