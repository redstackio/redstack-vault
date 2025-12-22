---
tags:
  - oauth
  - hardcoded-credentials
  - mobile-reverse-engineering
  - api-abuse
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/Jadx]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - iOS
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Decompile-Mobile-App-to-Extract-Hardcoded-OAuth-Keys]]'
  - '[[procedures/Authenticate-to-Instacart-API-Using-Extracted-OAuth-Key]]'
step_count: 2
techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.254Z'
description: >-
  Attack chain exploiting hardcoded OAuth keys in Instacart's Android and iOS
  apps via reverse engineering to gain unrestricted access to private API
  endpoints.
skill_level: intermediate
impact_level: high
id: d8d947b5-599e-4e87-acf2-bc2d50a06b7b
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
---
# OAuth Private Key Extraction from Instacart Mobile App Binaries Leading to Unauthorized API Access

Multi-stage attack chain demonstrating the extraction of hardcoded OAuth keys from Instacart's mobile apps and their use to access private API endpoints without authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Decompile App Binary] --> B[Extract OAuth Keys]
    B --> C[Authenticate to API]
    C --> D[Access Private Endpoints]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Jadx]] (for Android decompilation)
- Basic reverse engineering tools for iOS (e.g., Hopper or class-dump)

### Target Environment

- Instacart Android APK or iOS IPA file
- Access to the app binary (downloaded from app stores)
- Network access to Instacart API endpoints

### Initial Access Requirements

- No prior credentials needed
- Ability to download and decompile mobile app binaries
- Basic knowledge of OAuth and API interactions

## Detailed Attack Procedures

### Step 1: Decompile Mobile App Binary
procedure: [[procedures/Decompile-Mobile-App-to-Extract-Hardcoded-OAuth-Keys]]

**Objective**: Reverse engineer the Instacart mobile app to locate and extract embedded hardcoded OAuth keys, including the private key.

**Instructions**: Obtain the Instacart APK (Android) or IPA (iOS) file. For Android, use [[commands/jadx-decompile-apk]] to decompile the binary and search for OAuth-related strings in the output.

```bash
jadx -d instacart_output app.apk
```

For iOS, use similar tools like class-dump to dump headers and grep for keys. Search decompiled code for terms like "oauth", "private_key", or base64-encoded strings.

**Expected Output**: Decompiled source code directories containing hardcoded keys in configuration files or constants.

**Success Indicators**:
- Hardcoded OAuth public/private keys identified in decompiled code
- Keys validated as functional (e.g., not obfuscated or encrypted)

### Step 2: Authenticate and Access API
procedure: [[procedures/Authenticate-to-Instacart-API-Using-Extracted-OAuth-Key]]

**Objective**: Use the extracted private key to generate valid OAuth tokens and gain unrestricted access to Instacart's private API endpoints for data access or manipulation.

**Instructions**: With the extracted private key, construct an OAuth authentication request to the Instacart API. Use [[commands/curl-oauth-auth]] to test authentication and access a private endpoint, such as user data retrieval.

```bash
curl -X POST https://api.instacart.com/oauth/token \
  -H "Authorization: Bearer EXTRACTED_PRIVATE_KEY" \
  -d "grant_type=client_credentials"
```

Follow up by querying private endpoints, e.g., to fetch unauthorized user orders.

**Expected Output**: Successful authentication response with access token, followed by API responses containing private data.

**Success Indicators**:
- Valid OAuth token received without additional authentication
- Access to restricted API endpoints confirmed (e.g., 200 OK on private queries)

## Attack Chain Summary

### Key Achievements

1. Successful extraction of sensitive OAuth private key from mobile app binary without authentication.
2. Demonstration of unrestricted API access, enabling potential data exfiltration or manipulation.
3. Highlighting the risks of hardcoded credentials in client-side applications.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]] Credentials in Files
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
