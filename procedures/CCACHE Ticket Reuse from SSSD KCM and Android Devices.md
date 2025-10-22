---
id: c056dba0-d44c-4d8c-99fc-1e3865ac9fb6
name: CCACHE Ticket Reuse from SSSD KCM and Android Devices
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.612728+00:00'
updated_at: '2023-04-10T20:26:03.218449+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[CCACHE ticket reuse from SSSD KCM]]'
commands:
- '[[Clone SSSDKCMExtractor repository]]'
- '[[Extract secrets using SSSDKCMExtractor]]'
- '[[Retrieve secret key]]'
---

# CCACHE Ticket Reuse from SSSD KCM and Android Devices

## Summary

CCACHE ticket reuse from SSSD KCM and Android Devices is a technique used to steal credentials from Active Directory (AD) environments. This technique involves stealing CCACHE tickets, which are used to authenticate users in AD environments. CCACHE tickets can be stolen from Linux systems that use 

## Description

# Description

CCACHE ticket reuse from SSSD KCM and Android Devices is a technique used to steal credentials from Active Directory (AD) environments. This technique involves stealing CCACHE tickets, which are used to authenticate users in AD environments. CCACHE tickets can be stolen from Linux systems that use the System Security Services Daemon (SSSD) Kerberos Credential Manager (KCM) to cache tickets. Additionally, CCACHE tickets can also be extracted from Samsung Android devices that store them in plain text. Attackers can use these stolen tickets to access AD resources without being detected.

To execute this technique, attackers must first gain access to a Linux system that uses SSSD KCM to cache CCACHE tickets. Once access is gained, attackers can use the SSSD Secrets Database Path and SSS Secrets Key Path commands to extract the CCACHE tickets from the system. Attackers can also extract CCACHE tickets from Samsung Android devices using the SSD KCM Extractor and Extract Secrets from Samsung Android Devices commands.

The business value of this technique is that it allows attackers to gain access to sensitive AD resources, such as confidential data, intellectual property, and financial information.

## Requirements

1. Access to a Linux system that uses SSSD KCM to cache CCACHE tickets

1. Access to Samsung Android devices that store CCACHE tickets in plain text

## Defense

1. Use strong passwords and multi-factor authentication to prevent unauthorized access to Linux systems and Samsung Android devices

1. Monitor for unusual activity, such as suspicious logins and abnormal network traffic

1. Encrypt CCACHE tickets to make them more difficult to steal

## Objectives

1. Steal CCACHE tickets from Linux systems that use SSSD KCM to cache tickets

1. Steal CCACHE tickets from Samsung Android devices that store them in plain text

1. Access AD resources without being detected

# Instructions

1. To access or modify the SSSD secrets database, use the appropriate SSSD command-line tool or API.

**Code**: [[/var/lib/sss/secrets/secrets.ldb]]

> The SSSD secrets database contains sensitive information such as passwords and keys used by various services. It is important to ensure that this database is properly secured and only accessible by authorized users or processes. The SSSD provides various commands and APIs to manage this database, including sssctl, sssd-secrets, and sss_cache. These tools can be used to view, add, modify, or remove secrets from the database, as well as to clear the cache or reload the SSSD configuration.

2. To access the secrets key, use the following path:

**Code**: [[/var/lib/sss/secrets/.secrets.mkey]]

> This command provides the path to the secrets key used by the SSS (System Security Services Daemon) to securely store and retrieve sensitive information such as passwords and keys. The key is stored as a hidden file at the specified path, and can be accessed by authorized users or processes to access the secrets stored within.

**Command** ([[Retrieve secret key]]):

```bash
/var/lib/sss/secrets/.secrets.mkey
```

3. To extract the KCM file from SSD, use the following command:

**Code**: [[SSSDKCMExtractor]]

> Arguments:
- input_file: The path to the SSD file
- output_file: The path to the output KCM file

Example:
SSDKCMExtractor input_file.ssd output_file.kcm

4. To extract secrets from Samsung Android devices, follow these steps:
1. Clone the SSSDKCMExtractor repository using the command 'git clone https://github.com/fireeye/SSSDKCMExtractor'
2. Navigate to the cloned directory.
3. Run the command 'python3 SSSDKCMExtractor.py --database secrets.ldb --key secrets.mkey' to extract the secrets from the device.

**Code**: [[git clone https://github.com/fireeye/SSSDKCMExtrac]]

> This command clones the SSSDKCMExtractor repository and runs a python script to extract secrets from Samsung Android devices. The '--database' option specifies the name of the database file to be created and the '--key' option specifies the name of the key file to be used for decryption. The extracted secrets can be used for further analysis and investigation.

**Command** ([[Clone SSSDKCMExtractor repository]]):

```bash
git clone https://github.com/fireeye/SSSDKCMExtractor
```

**Command** ([[Extract secrets using SSSDKCMExtractor]]):

```bash
python3 SSSDKCMExtractor.py --database secrets.ldb --key secrets.mkey
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Clone SSSDKCMExtractor repository]]
- [[Extract secrets using SSSDKCMExtractor]]
- [[Retrieve secret key]]

## Tags

- [[Active Directory Attacks]]
- [[CCACHE ticket reuse from SSSD KCM]]
