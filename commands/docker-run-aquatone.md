---
id: 309664c5-55d7-4625-9764-d1f6469b6ab5
name: docker-run-aquatone
type: command
executor: bash
data: docker run -it txt3rob/aquatone-docker aq $_DOMAIN
output: null
created_at: '2023-04-06T03:56:25.578426+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - scanning
verified: true
validated: true
---

# docker-run-aquatone

## Command

```bash
docker run -it txt3rob/aquatone-docker aq $_DOMAIN
```

## Description

Runs the full Aquatone workflow (discover, scan, gather) inside the Docker container for the target domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain (e.g., example.com) | Yes |
| -it | Interactive terminal mode | No |
| -v | Optional volume mount for output (e.g., -v /host/path:/root/.aquatone) | No |

## Examples

### Basic Usage

```bash
docker run -it txt3rob/aquatone-docker aq example.com
```

### With Volume Mount

```bash
docker run -it -v ~/.aquatone:/root/.aquatone txt3rob/aquatone-docker aq example.com
```

## Expected Output

Container logs showing discovery, scanning, and gathering progress, with results in /root/.aquatone/$_DOMAIN/ (or mounted host path).

## Related

- [[procedures/Subdomain-Enumeration-with-Aquatone]]
- [[tools/Aquatone]]
