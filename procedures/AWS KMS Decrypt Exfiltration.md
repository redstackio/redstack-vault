---
id: b4c10c19-3046-4a3f-ba9a-4072ed6f3f12
name: AWS KMS Decrypt Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.458451+00:00'
updated_at: '2023-04-10T20:20:34.522772+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
sub_techniques:
- '[[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol|T1048.002 - Exfiltration
  Over Asymmetric Encrypted Non-C2 Protocol]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[Decrypt the secret using the key]]'
- '[[KMS]]'
commands:
- '[[Decrypt EncryptedFile using AWS KMS]]'
---

# AWS KMS Decrypt Exfiltration

## Summary

AWS KMS Decrypt Exfiltration is a technique used by attackers to exfiltrate sensitive information from an AWS environment. This technique involves obtaining access to the AWS Key Management Service (KMS) and using it to decrypt encrypted secrets. Once the secrets are decrypted, they can be exfiltra

## Description

# Description

AWS KMS Decrypt Exfiltration is a technique used by attackers to exfiltrate sensitive information from an AWS environment. This technique involves obtaining access to the AWS Key Management Service (KMS) and using it to decrypt encrypted secrets. Once the secrets are decrypted, they can be exfiltrated using various methods such as exfiltration over an alternative protocol or command and control channel.

From a technical standpoint, this technique requires the attacker to have access to the AWS KMS and the encrypted secrets. The attacker can then use the AWS KMS Decrypt command to decrypt the secrets. The decrypted secrets can be exfiltrated using various methods. This technique can be used to obtain sensitive data such as credentials, access keys, and other secrets.

The business value of this technique is that it allows attackers to obtain sensitive information that can be used to further their attack or gain access to other systems. It is important for organizations to have proper access controls in place to prevent unauthorized access to the AWS KMS and encrypted secrets.

## Requirements

1. Access to the AWS KMS and encrypted secrets

## Defense

1. Ensure proper access controls are in place to prevent unauthorized access to the AWS KMS and encrypted secrets.

1. Monitor for unusual activity such as excessive use of the AWS KMS Decrypt command.

1. Implement network segmentation to limit access to sensitive systems and data.

## Objectives

1. Obtain sensitive information such as credentials and access keys

# Instructions

1. To decrypt a file using AWS KMS, run the following command:

**Code**: [[aws kms decrypt --ciphertext-blob fileb://Encrypte]]

> This command decrypts a file using the AWS Key Management Service (KMS). The --ciphertext-blob parameter specifies the encrypted file, which should be in binary format. The --output parameter specifies the format of the output, which is set to text in this case. The --query parameter specifies that we want to retrieve the plaintext value from the output.

**Command** ([[Decrypt EncryptedFile using AWS KMS]]):

```bash
aws kms decrypt --ciphertext-blob fileb://EncryptedFile --output text --query plaintext
```

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

### Sub-Techniques

- [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol|T1048.002 - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]

## Commands Used

- [[Decrypt EncryptedFile using AWS KMS]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[Decrypt the secret using the key]]
- [[KMS]]
