---
id: 395a5875-8ba6-4012-b030-8be483e95584
name: azure-device-management-and-token-generation-with-sharpaztoken
type: procedure
verified: true
submitted: true
created_at: '2023-05-24T07:30:25.190680+00:00'
updated_at: '2023-05-24T07:42:32.942941+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Pass The PRT]]'
  - '[[tags/Primary Refresh Token]]'
  - '[[tags/Refresh Tokens]]'
commands:
  - '[[commands/sharpaztoken-join-mdm-device]]'
  - '[[commands/sharpaztoken-generate-device-keys]]'
tools:
  - '[[tools/sharpaztoken]]'
validated: true
---

# Azure Device Management and Token Generation with SharpAzToken

## Summary

This procedure uses the SharpAzToken tool to manage Azure device enrollment in Mobile Device Management (MDM) and generate Primary Refresh Tokens (PRTs) and session keys from device certificates. It enables attackers with initial access tokens to join devices to MDM servers and extract persistent credentials for further Azure resource access, commonly used in cloud persistence and credential access scenarios.

## Description

SharpAzToken is a .NET-based tool for manipulating Azure authentication tokens and device management. In offensive security operations, this procedure allows an attacker to simulate or hijack device enrollment processes to obtain PRTs, which can be used for seamless authentication across Azure services without repeated credential prompts. The process targets Azure Active Directory (AAD) environments where MDM enrollment is enabled, requiring an initial access token (e.g., from a compromised user session). Step 1 handles device joining to generate a device certificate (PFX file), while Step 2 uses that certificate to derive a PRT and session key. This technique is particularly effective in hybrid environments with Intune or similar MDM solutions, enabling lateral movement or persistence in cloud infrastructures.

## Requirements

1. SharpAzToken tool installed and executable (see [[tools/sharpaztoken]] for installation).
2. Valid Azure access token obtained from a compromised session or application.
3. Device eligibility for MDM enrollment (e.g., compliant Windows device in the target AAD tenant).
4. Permissions for Azure device registration and token manipulation (e.g., User.ReadWrite.All scope).
5. For PRT generation: Access to a device certificate PFX file and either a PRT cookie (via tools like Mimikatz) or valid username/password credentials.

## Defense

Defensive measures and detection strategies:

- Restrict SharpAzToken and similar tools to authorized environments through application whitelisting and endpoint detection rules.
- Monitor Azure AD sign-in logs for anomalous device registrations and token requests from unfamiliar devices.
- Implement conditional access policies to require MFA for device enrollment and limit PRT issuance to trusted networks.
- Enable Azure AD Identity Protection to alert on risky token extractions or unusual authentication patterns.
- Regularly rotate access tokens and audit MDM enrollment events in Microsoft Endpoint Manager.

## Objectives

1. Join a device to an Azure MDM server to obtain a device certificate for persistent access.
2. Generate a Primary Refresh Token (PRT) and session key to enable long-term Azure authentication.
3. Establish credential access for further lateral movement in the Azure environment.

## Instructions

### Step 1: Join Device to MDM Server

**Context**: This step uses an access token to enroll a device in Azure MDM, generating a PFX certificate file that represents the device's identity. This simulates legitimate enrollment but allows extraction of credentials for malicious use. Ensure the access token has the necessary scopes for device management.

**Command** ([[commands/sharpaztoken-join-mdm-device]]):
```bash
SharpAzToken.exe mdm --joindevice --accesstoken $_ACCESS_TOKEN --devicename $_DEVICE_NAME --outpfxfile $_PFX_PATH
```

> This command initiates the MDM join process. Replace $_ACCESS_TOKEN with the base64-encoded or raw access token string. $_DEVICE_NAME should be a unique identifier (e.g., 'CompromisedDevice01'). $_PFX_PATH is the output file path (e.g., '/path/to/device.pfx'). Expected output includes success confirmation and the generated PFX file containing the device certificate and private key. Verify by checking the file existence and attempting to import it into a certificate store.

### Step 2: Generate PRT and Session Key from Device Certificate

**Context**: Using the PFX file from Step 1, this step extracts a PRT and session key, which can be used for token refresh and persistent access to Azure resources. Choose the refresh token method based on available artifacts: PRT cookie for on-device extraction or username/password for remote simulation.

**Command** ([[commands/sharpaztoken-generate-device-keys]]):
```bash
SharpAzToken.exe devicekeys --pfxpath $_PFX_PATH --refreshtoken (--prtcookie $_PRT_COOKIE or --username $_USERNAME --password $_PASSWORD)
```

> Specify $_PFX_PATH as the path to the PFX file from Step 1. For --prtcookie, provide the extracted PRT cookie (e.g., via Mimikatz on a Windows host). Alternatively, use --username and --password for credential-based refresh. Expected output is the PRT string and session key, which can be base64-encoded for storage or use in subsequent API calls. Success is indicated by valid token output verifiable against Azure token validation endpoints.
