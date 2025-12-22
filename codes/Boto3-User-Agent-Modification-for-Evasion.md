---
id: 11a8e754-ca35-4fcd-8979-5fd1d8cf6a98
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:09.785882+00:00'
updated_at: '2023-04-10T20:19:56.119287+00:00'
tags:
  - Defense-Evasion
  - AWS
  - GuardDuty
platforms:
  - AWS
  - Cloud
  - Linux
validated: true
---

# Boto3-User-Agent-Modification-for-Evasion

## Code

```python
boto3_session = boto3.session.Session()
ua = boto3_session._session.user_agent()
if 'kali' in ua.lower() or 'parrot' in ua.lower() or 'pentoo' in ua.lower():  # If the local OS is Kali/Parrot/Pentoo Linux
    # GuardDuty triggers a finding around API calls made from Kali Linux, so let's avoid that...
    self.print('Detected environment as one of Kali/Parrot/Pentoo Linux. Modifying user agent to hide that from GuardDuty...')
```

## Description

This Python code snippet uses the Boto3 library to create an AWS session, inspect the current user-agent string, and modify it if it contains indicators of security-focused Linux distributions (Kali, Parrot, or Pentoo). The modification prevents AWS GuardDuty from detecting and alerting on API calls originating from these environments, thereby obfuscating attacker activity in CloudTrail logs. It is intended for integration into larger Python scripts that interact with AWS services.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ua | The user-agent string from the Boto3 session | 'Boto3/1.26.0 Python/3.9.2 Linux/5.4.0-kali5-amd64 Botocore/1.29.0' |
| self | Reference to the class instance for printing output (assumes this is used within a class method) | N/A |

## Usage

Integrate this snippet at the start of any Python script using Boto3 for AWS API calls, particularly in red team operations targeting AWS environments. For example, embed it in a custom AWS client class before initializing clients like S3 or EC2. Execute the script with `python3 your_script.py`. This is useful during initial access or persistence phases to avoid log-based detection.

## Detection

- Monitor Python scripts or processes invoking Boto3 for modifications to session.user_agent().
- AWS GuardDuty custom rules can detect API calls with inconsistent or suspicious user-agents (e.g., generic strings from known evasion patterns).
- CloudTrail logs showing API activity without OS indicators but from IP ranges associated with security tools.
- Process monitoring for Python executions with boto3 imports on endpoints with AWS credentials.

## Related

- [[procedures/Obfuscate-AWS-CloudTrail-and-GuardDuty-Logs]]
- [[tools/Boto3]]
