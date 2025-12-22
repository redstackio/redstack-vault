---
type: command
executor: bash
data: chromium-browser --no-sandbox --user-data-dir /tmp/
platforms:
  - Linux
tags:
  - browser
  - testing
verified: true
validated: true
---

# chromium-run-as-root

## Command

```bash
chromium-browser --no-sandbox --user-data-dir /tmp/ $_URL
```

## Description

This command launches the Chromium browser as root, disabling the security sandbox to allow execution in restricted or containerized environments. It is useful in penetration testing or debugging scenarios where sandbox restrictions interfere with tool integration or custom configurations. Note: Running without sandbox poses security risks and should only be done in isolated testing setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--no-sandbox` | Disables Chromium's security sandbox for unrestricted operation | Yes |
| `--user-data-dir /tmp/` | Sets the user data directory to /tmp/ to avoid permission issues when running as root | Yes |
| `$_URL` | The target URL to open (e.g., http://example.com); optional if launching without a specific site | No |

## Examples

### Basic Usage

```bash
chromium-browser --no-sandbox --user-data-dir /tmp/
```

### Advanced Usage (with URL)

```bash
chromium-browser --no-sandbox --user-data-dir /tmp/ http://target-site.com
```

## Expected Output

The browser window opens without sandbox restrictions, allowing full access to system resources. Console output may include warnings about sandbox disablement:

```
[1234:5678:010101:WARNING:process_singleton_posix.cc(300)] Could not lock /tmp/SingletonCookie
[1234:5678:010101:ERROR:sandbox_linux.cc(1234)] Running without sandbox
DevTools listening on ws://127.0.0.1:12345/devtools/browser/...
```

Successful launch shows the Chromium interface ready for use, with no sandbox-related errors blocking functionality.

## Related

- [[Related Procedure: Browser-Based Web Testing]]
- [[tools/Chromium]]
