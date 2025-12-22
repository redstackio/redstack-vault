---
type: command
executor: bash
data: >-
  docker run --rm -it -v $_LOCAL_DIR:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl
  -v -u $_REPO_URL
tags:
  - docker
  - exfiltration
  - mercurial
platforms:
  - Linux
verified: true
validated: true
---

# Run DVCS Ripper Docker Container

## Command

```bash
docker run --rm -it -v $_LOCAL_DIR:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl -v -u $_REPO_URL
```

## Description

This command launches a Docker container using the k0st/alpine-dvcs-ripper image to execute rip-hg.pl, which clones a Mercurial repository to the mounted volume. It facilitates isolated exfiltration of source code without installing dependencies on the host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LOCAL_DIR | Path to local directory on host to mount as /work in container | Yes |
| --rm | Automatically remove container after exit | Built-in |
| -it | Run in interactive mode with pseudo-TTY | Built-in |
| -v $_LOCAL_DIR:/work:rw | Mount host directory read-write | Yes |
| k0st/alpine-dvcs-ripper | Docker image name | Yes |
| rip-hg.pl | Script to execute inside container | Built-in |
| -v | Verbose output | Optional |
| -u | Update existing repository | Optional |
| $_REPO_URL | URL of the target Mercurial repository | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -it -v /tmp/repo:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl https://hg.example.com/my-repo
```

### Advanced Usage

```bash
docker run --rm -it -v /home/user/extract:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl -v -u --user username --pass password https://hg.example.com/protected-repo
```

## Expected Output

The command outputs verbose cloning progress, such as:

cloning https://hg.example.com/my-repo
requesting all changes
adding changesets
adding manifests
adding file changes
added 1234 changesets with 5678 changes to 123 files
updating to branch default
456 files updated, 0 files merged, 0 remove, 0 unresolved
Extraction complete to /work.

## Related

- [[procedures/mercurial-source-code-extraction-with-rip-hg-pl]]
- [[commands/download-rip-hg-pl-script]]
