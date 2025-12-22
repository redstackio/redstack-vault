---
id: 8b8fe352-e877-4e9c-bc8a-3a6bd0886d5d
name: ligolo-setup-script
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:22.791994+00:00'
updated_at: '2023-04-10T20:25:12.829563+00:00'
platforms:
  - Linux
tags:
  - setup
  - script
  - automation
validated: true
---

# Ligolo Setup Script

## Code

```bash
# Get Ligolo and dependencies
cd `go env GOPATH`/src
git clone https://github.com/sysdream/ligolo
cd ligolo
make dep

# Generate self-signed TLS certificates (will be placed in the certs folder)
make certs TLS_HOST=example.com

make build-all
```

## Description

This bash script automates the full setup of Ligolo by cloning the repository, installing dependencies, generating TLS certificates, and building all binaries. It serves as a quick way to prepare the tool for reverse tunneling operations without manual step-by-step execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| TLS_HOST | Hostname for TLS certificate generation | attacker.example.com |

## Usage

Save this as 'setup-ligolo.sh', make executable with `chmod +x setup-ligolo.sh`, and run `./setup-ligolo.sh`. Update TLS_HOST before execution. Use in red team setups to rapidly provision Ligolo on a new attacker VM. After running, deploy the agent binary to targets via existing access vectors like phishing or initial footholds.

## Detection

- Monitor for Git clones from github.com/sysdream/ligolo or Make invocations with 'dep', 'certs', or 'build-all' in process logs.
- EDR alerts on Go module downloads or binary compilations in temporary directories.
- Network logs showing connections to GitHub during setup phase.

## Related

- [[procedures/setup-ligolo-for-reverse-tunneling]]
- [[tools/ligolo]]
