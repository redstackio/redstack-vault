---
type: command
executor: bash
data: >-
  git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8 &&
  make install
platforms:
  - Linux
tags:
  - installation
  - build
  - git
verified: true
validated: true
---

# git-clone-and-build-hashcat

## Command

```bash
git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8 && make install
```

## Description

This command clones the Hashcat source code from GitHub, compiles it with parallel jobs, and installs the binary to the system path. It is the final step in setting up Hashcat for use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-j 8` | Number of parallel compilation jobs (adjust to CPU cores) | Yes |
| `https://github.com/hashcat/hashcat.git` | Repository URL | Built-in |
| `make install` | Installs compiled binaries to /usr/local | Built-in |

## Examples

### Basic Usage

```bash
git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8 && make install
```

### Advanced Usage

For a specific branch: `git clone -b master https://github.com/hashcat/hashcat.git ...`

## Expected Output

Cloning into 'hashcat'...
remote: Enumerating objects: 10000, done.
remote: Total 10000 (delta 0), reused 0 (delta 0), pack-reused 10000
Receiving objects: 100% (10000/10000), 5.00 MiB | 1.00 MiB/s, done.
cd hashcat
make -j 8
CC src/hashcat.c
... (compilation output)
make install
install -m 755 hashcat /usr/local/bin
```

## Related

- [[procedures/Install-Hashcat-from-Source]]
- [[tools/Hashcat]]
