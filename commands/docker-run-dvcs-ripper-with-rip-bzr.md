---
id: 05c6095d-b80b-410a-967b-c4f127e6088f
name: docker-run-dvcs-ripper-with-rip-bzr
type: command
executor: bash
data: >-
  docker run --rm -it -v $_HOST_WORK_DIR:/work:rw k0st/alpine-dvcs-ripper
  rip-bzr.pl -v -u $_REPO_URL
output: null
created_at: '2023-04-06T03:56:00.324877+00:00'
updated_at: '2023-04-10T20:33:54.895926+00:00'
platforms:
  - Linux
tags:
  - docker
  - extraction
  - vcs-rip
verified: true
validated: true
---

# docker-run-dvcs-ripper-with-rip-bzr

## Command

```bash
docker run --rm -it -v $_HOST_WORK_DIR:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl -v -u $_REPO_URL
```

## Description

This command launches a Docker container from the k0st/alpine-dvcs-ripper image, mounting a host directory for output, and runs rip-bzr.pl to extract a Bazaar repository. The -u flag enables unauthenticated access, and -v provides verbose output. Use this to rip exposed bzr repos without installing dependencies locally.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HOST_WORK_DIR | Path to local directory for extracted files (e.g., /tmp/bzr-out) | Yes |
| $_REPO_URL | Full URL of the Bazaar repository (e.g., http://example.com/bzr/repo) | Yes |
| --rm | Remove container after run | Built-in |
| -it | Interactive terminal mode | Built-in |
| -v | Mount volume read-write | Built-in |
| -v (rip-bzr) | Verbose mode for logging | Built-in |
| -u (rip-bzr) | Unauthenticated access | Built-in |

## Examples

### Basic Usage

```bash
docker run --rm -it -v /tmp/extract:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl -v -u http://target.com/bzr/repo
```

### With Custom Image Pull

First pull the image if needed:
```bash
docker pull k0st/alpine-dvcs-ripper
```
Then run as above.

## Expected Output

The command starts the container and runs rip-bzr.pl, producing verbose logs like:

Starting rip-bzr on http://target.com/bzr/repo
Fetching branch list...
Downloading file: /trunk/main.py (100%)
Cloning revision 1...
Extraction complete. Files saved to /work.

If successful, the host directory ($_HOST_WORK_DIR) will contain the repo structure (e.g., trunk/, branches/). Errors include 'Repository not found' or Docker permission issues.

## Related

- [[procedures/Extract-Source-Code-from-Bazaar-Repository-using-rip-bzr]]
- [[tools/dvcs-ripper]]
