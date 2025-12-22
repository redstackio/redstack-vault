---
type: code
language: xml
verified: true
created_at: '2023-04-06T03:55:51.712383+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - iis
  - machine-key
  - leak
validated: true
---

# sample-iis-machine-key-configuration

## Code

```xml
<machineKey validationKey="87AC8F432C8DB844A4EFD024301AC1AB5808BEE9D1870689B63794D33EE3B55CDB315BB480721A107187561F388C6BEF5B623BF31E2E725FC3F3F71A32BA5DFC" decryptionKey="E001A307CCC8B1ADEA2C55B1246CDCFE8579576997FF92E7" validation="SHA1" />
```

## Description

This XML snippet represents a sample IIS machineKey configuration element, commonly found in web.config or machine.config files. It defines the keys for validating (integrity) and decrypting (confidentiality) ASP.NET data like ViewState, session state, and authentication tickets. Leaks of this configuration enable attackers to decrypt protected application data offline.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| validationKey | Hex string for HMAC validation (SHA1 in this case; 128+ chars for security) | 87AC8F432C8DB844A4EFD024301AC1AB5808BEE9D1870689B63794D33EE3B55CDB315BB480721A107187561F388C6BEF5B623BF31E2E725FC3F3F71A32BA5DFC |
| decryptionKey | Hex string for symmetric decryption (24 bytes here indicates TripleDES) | E001A307CCC8B1ADEA2C55B1246CDCFE8579576997FF92E7 |
| validation | Algorithm for integrity checks (SHA1, MD5, etc.; SHA1 is legacy/insecure) | SHA1 |

## Usage

In an attack, search for this in leaked files. Extract decryptionKey and use with decryption tools to process captured blobs (e.g., base64-decode .ASPXAUTH cookie, then decrypt). Integrate into procedures like session hijacking after initial access via phishing or RCE. For config files, temporarily set this key if needed, but primarily for runtime data.

## Detection

- Secret scanning alerts for 'machineKey' in code repos.
- Anomalous network traffic with encrypted ASP.NET payloads to unknown decryptors.
- File integrity monitoring on config files showing unauthorized edits.
- SIEM rules for DPAPI usage spikes or aspnet_regiis executions.

## Related

- [[procedures/IIS-Machine-Key-Exploitation]]
- [[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]
