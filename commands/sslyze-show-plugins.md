---
id: new-uuid-for-show-plugins
name: sslyze-show-plugins
type: command
executor: bash
data: sslyze --help
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ssl
  - tls
  - reconnaissance
verified: true
validated: true
---

# sslyze-show-plugins

## Command

```bash
sslyze --help
```

## Description

This command displays the help output for SSLyze, including a list of available plugins and usage options. Use it to verify installation and understand scan capabilities before running assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--help` or `-h` | Show detailed help message and plugin list | No |

## Examples

### Basic Usage

```bash
sslyze --help
```

### Advanced Usage

Not applicable; this is a help invocation.

## Expected Output

A terminal output listing available plugins such as:
- PluginHeartbleed
- PluginCompression
- PluginOpenSSLCipherSuites
- PluginCertInfo
- And others, along with command-line options.

## Related

- [[procedures/Perform-SSL-TLS-Scan-with-SSLyze]]
- [[commands/sslyze-regular-scan]]
