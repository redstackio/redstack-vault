---
id: f109bc51-828b-42d1-9193-3e8d1f15bf54
name: Golden-SAML-Attack-Using-Shimit
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.729566+00:00'
updated_at: '2023-04-10T20:20:18.041590+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/AWS - Golden SAML Attack]]'
  - '[[tags/Cloud - AWS]]'
commands:
  - '[[commands/pip-install-shimit-dependencies]]'
  - '[[commands/run-shimit-for-golden-saml-forgery]]'
platforms:
  - AWS
tools: []
validated: true
---

# Golden-SAML-Attack-Using-Shimit

## Summary

This procedure automates the creation of a forged SAML assertion (Golden SAML) using the Shimit tool to impersonate a legitimate user and gain unauthorized access to AWS resources. It requires prior compromise of an Active Directory Federation Services (ADFS) server to extract private keys and certificates, enabling the attacker to sign malicious SAML tokens that can be redeemed via AWS STS for administrative sessions.

## Description

The Golden SAML attack exploits federated identity trust between ADFS and AWS by forging SAML assertions with an attacker-controlled private key matching a trusted certificate. Shimit simplifies this by handling token generation, including embedding arbitrary AWS role ARNs for privilege escalation. This technique is effective in hybrid environments where ADFS federates with AWS IAM roles, allowing persistence or lateral movement without native AWS credentials. The process assumes the attacker has domain admin access to enumerate and extract ADFS metadata, then uses Shimit to craft tokens redeemable at sts.amazonaws.com. Detection is challenging as the traffic mimics legitimate federation flows.

## Requirements

1. Compromised access to an ADFS server in the target domain (e.g., domain admin credentials).
2. Extracted private key (.pem) and certificate (.crt) files from the ADFS token-signing store.
3. Target AWS account ID and desired role ARNs (e.g., admin roles federated via SAML).
4. Python 3 environment on the attacker's machine with pip access.
5. Network access to the ADFS IdP endpoint and AWS STS.

## Defense

- Enable MFA for ADFS and AWS console access to prevent initial compromise.
- Monitor AWS CloudTrail for unusual STS AssumeRoleWithSAML calls, especially with unexpected role ARNs or IP sources.
- Regularly rotate ADFS token-signing certificates and restrict key export via HSM or policy.
- Implement SAML signature validation and anomaly detection in federation logs (e.g., via SIEM rules for mismatched certs).
- Use AWS IAM policies to limit federated role assumptions and audit SAML providers.

## Objectives

1. Forge a valid SAML assertion signed with a trusted ADFS certificate to impersonate a domain user.
2. Redeem the forged token via AWS STS to obtain temporary admin credentials.
3. Achieve persistent access to AWS resources without alerting credential rotation.

## Instructions

### Step 1: Install Shimit Dependencies

**Context**: Before running Shimit, install the required Python libraries for SAML parsing, signing, and AWS interaction. This ensures the tool can process XML, handle cryptography, and interface with boto3 for token validation.

**Command** ([[commands/pip-install-shimit-dependencies]]):
```bash
python -m pip install boto3 botocore defusedxml enum python_dateutil lxml signxml
```

> This command fetches and installs the packages from PyPI. Verify installation by checking `pip list` for the new entries. If behind a proxy, add `--proxy` flag.

### Step 2: Run Shimit to Forge SAML Token

**Context**: With dependencies installed, execute Shimit using extracted ADFS details to generate a Golden SAML assertion. Specify the IdP endpoint, key/cert files, user details, and target AWS roles to embed in the token. The output is a SAML XML file usable with AWS STS.

**Command** ([[commands/run-shimit-for-golden-saml-forgery]]):
```bash
python shimit.py -idp $_IDP_ENDPOINT -pk $_PRIVATE_KEY_FILE -c $_CERT_FILE -u $_USERNAME -n $_NAME_ID -r $_ROLE_ARN1 -r $_ROLE_ARN2 -id $_AWS_ACCOUNT_ID
```

> Replace placeholders with actual values (e.g., -idp https://adfs.example.com/adfs/ls/, -pk token_signing_key.pem). The command generates a signed SAML assertion in the current directory (e.g., golden_saml.xml). Validate by curling it to AWS STS: `curl -d @golden_saml.xml https://sts.amazonaws.com` to confirm session tokens are issued.
