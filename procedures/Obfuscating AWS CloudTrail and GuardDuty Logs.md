---
id: aead8875-3fa1-435b-9562-a762a0e85012
name: Obfuscating AWS CloudTrail and GuardDuty Logs
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.790674+00:00'
updated_at: '2023-04-10T20:19:56.104956+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Disabling Security Tools|T1089 - Disabling Security Tools]]'
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques:
- '[[File Deletion|T1070.004 - File Deletion]]'
tags:
- '[[Cloud - AWS]]'
- '[[Cover tracks by obfuscating Cloudtrail logs and Guard Duty]]'
commands:
- '[[Modify User Agent for Kali/Parrot/Pentoo Linux]]'
---

# Obfuscating AWS CloudTrail and GuardDuty Logs

## Summary

Obfuscating AWS CloudTrail and GuardDuty logs is a technique used by attackers to hide their tracks and avoid detection. By modifying the user-agent string in the AWSCLI, the attacker can make it appear that the requests are coming from a legitimate source. This can help them avoid detection by Clo

## Description

# Description

Obfuscating AWS CloudTrail and GuardDuty logs is a technique used by attackers to hide their tracks and avoid detection. By modifying the user-agent string in the AWSCLI, the attacker can make it appear that the requests are coming from a legitimate source. This can help them avoid detection by CloudTrail and GuardDuty, which are AWS services that monitor and log activity within an AWS environment. By obfuscating the logs, the attacker can make it more difficult for security teams to identify and respond to the attack.

From a technical perspective, this technique involves modifying the user-agent string in the AWSCLI. The user-agent string is a piece of information that is sent with every HTTP request and identifies the client making the request. By modifying this string, the attacker can make it appear that the requests are coming from a legitimate source, such as a web browser or mobile app.

The business value of this technique is that it can help attackers avoid detection and maintain access to an AWS environment. By obfuscating their activity, attackers can continue to exfiltrate data, move laterally within the environment, and achieve their objectives without being detected.

## Requirements

1. Access to an AWS environment

1. AWSCLI installed on the attacker's machine

1. Authentication credentials for the AWS environment

## Defense

1. Monitor CloudTrail and GuardDuty logs for suspicious activity

1. Implement network segmentation to limit lateral movement within the environment

1. Use multi-factor authentication to protect authentication credentials

## Objectives

1. Obfuscate AWS CloudTrail and GuardDuty logs to avoid detection

1. Maintain access to an AWS environment and achieve attacker objectives

# Instructions

1. To avoid generating a log when using the AWS CLI on Kali Linux, Pentoo, or Parrot Linux, modify the user agent to hide that information from GuardDuty.

**Code**: [[boto3_session = boto3.session.Session()
ua = boto3]]

> This code modifies the user agent used by the AWS CLI to avoid generating a log when running on Kali Linux, Pentoo, or Parrot Linux. GuardDuty triggers a finding around API calls made from Kali Linux, so modifying the user agent can help you avoid generating unnecessary logs. The `boto3.session.Session()` method is used to create a new session object, and the `ua` variable is set to the current user agent. The `if` statement checks if the user agent contains the name of any of the three Linux distributions mentioned above. If it does, the user agent is modified to hide that information from GuardDuty, and a message is printed to inform the user that the modification has been made.

**Command** ([[Modify User Agent for Kali/Parrot/Pentoo Linux]]):

```bash
boto3_session = boto3.session.Session()
ua = boto3_session._session.user_agent()
if 'kali' in ua.lower() or 'parrot' in ua.lower() or 'pentoo' in ua.lower():  # If the local OS is Kali/Parrot/Pentoo Linux
    # GuardDuty triggers a finding around API calls made from Kali Linux, so let's avoid that...
    self.print('Detected environment as one of Kali/Parrot/Pentoo Linux. Modifying user agent to hide that from GuardDuty...')
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Disabling Security Tools|T1089 - Disabling Security Tools]]
- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

### Sub-Techniques

- [[File Deletion|T1070.004 - File Deletion]]

## Commands Used

- [[Modify User Agent for Kali/Parrot/Pentoo Linux]]

## Tags

- [[Cloud - AWS]]
- [[Cover tracks by obfuscating Cloudtrail logs and Guard Duty]]
