---
data: toxiproxy-cli inspect csrf
tags:
  - inspection
  - cli
type: command
executor: bash
platforms:
  - macOS
id: fe04bf50-787f-43e5-8f35-e2c40e8285ec
created_at: '2025-12-14T17:27:29.699Z'
updated_at: '2025-12-14T17:27:29.699Z'
verified: false
validated: true
submitted: true
---
# toxiproxy-cli-inspect-csrf

## Command

```bash
toxiproxy-cli inspect csrf
```

## Description

Inspects the configuration of a specific Toxiproxy named 'csrf', retrieving details like listen address, upstream, and enabled status via the CLI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| inspect | Subcommand for viewing details | Yes |
| csrf | Proxy name to inspect | Yes |

## Examples

### Basic Usage

```bash
toxiproxy-cli inspect csrf
```

### Advanced Usage

```bash
toxiproxy-cli list | grep csrf
```

## Expected Output

JSON output: {"Name":"csrf","Listen":"0.0.0.0:2773","Upstream":{"Url":"attacker:9999"},"Enabled":true}.

## Related

- [[procedures/Verify-Proxy-Creation-with-Toxiproxy-CLI]]
- [[tools/toxiproxy-cli]]
