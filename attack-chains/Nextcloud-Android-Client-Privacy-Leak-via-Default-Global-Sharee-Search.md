---
tags:
  - privacy-leak
  - information-disclosure
  - nextcloud
  - android
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Exfiltration]]'
verified: false
platforms:
  - Web
  - Android
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Nextcloud-Instance-with-Default-Settings]]'
  - '[[procedures/Perform-Sharee-Search-Using-Android-App]]'
  - '[[procedures/Observe-and-Confirm-Data-Leak-to-External-Server]]'
step_count: 3
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
updated_at: '2025-12-14T17:24:45.125Z'
description: >-
  Demonstrates a privacy vulnerability in Nextcloud where the Android client
  leaks user search queries and server IP to an external lookup server due to
  missing 'lookup' parameter in API requests.
skill_level: intermediate
impact_level: medium
id: 8c04fcbb-9454-405b-9048-244b43bf38ca
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
---
# Nextcloud Android Client Privacy Leak via Default Global Sharee Search

Multi-stage attack chain demonstrating a privacy leak in Nextcloud's sharing functionality, where the Android client inadvertently sends user search queries and the server's IP to an external lookup server without consent.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Nextcloud Instance] --> B[Search Sharee in Android App]
    B --> C[Observe External Leak]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Nextcloud server installation
- Nextcloud Android app
- Network monitoring tools (e.g., Wireshark for observation)

### Target Environment

- Nextcloud server (PHP-based)
- Android device with Nextcloud app
- Access to external Nextcloud lookup server logs or network traffic

### Initial Access Requirements

- Administrative access to set up Nextcloud instance
- Installed Nextcloud Android client
- No special credentials needed beyond default setup

## Detailed Attack Procedures

### Step 1: Setup Nextcloud Instance
procedure: [[procedures/Set-Up-Nextcloud-Instance-with-Default-Settings]]

**Objective**: Establish a default Nextcloud environment where the global address book search is enabled by default, mimicking a standard deployment.

**Instructions**: Install and configure a fresh Nextcloud instance ensuring the 'Search global and public address book for users' option is active in the settings. This setting is enabled by default in most installations.

**Expected Output**: A running Nextcloud server ready for client connections, with global lookup functionality active.

**Success Indicators**:
- Nextcloud dashboard accessible via web
- Sharing features available without custom configuration changes

### Step 2: Perform Sharee Search Using Android App
procedure: [[procedures/Perform-Sharee-Search-Using-Android-App]]

**Objective**: Trigger a sharee search from the Android client to initiate an API request that omits the critical 'lookup' parameter.

**Instructions**: Open the Nextcloud Android app, navigate to a file or folder, select the share option, and enter a search term in the sharee lookup field. The app will send an API request to the server without specifying the 'lookup' parameter.

**Expected Output**: The app displays search results, but the underlying request defaults to global lookup on the server side.

**Success Indicators**:
- Search interface responds in the app
- No explicit global search toggle is required or visible to the user

### Step 3: Observe and Confirm Data Leak
procedure: [[procedures/Observe-and-Confirm-Data-Leak-to-External-Server]]

**Objective**: Verify that the search query and originating server IP are transmitted to the external Nextcloud lookup server.

**Instructions**: Monitor server logs or network traffic on the Nextcloud instance. The server will process the request at ShareesAPIController.php (line 144), defaulting 'lookup' to true and querying the external server with the search term and IP.

**Expected Output**: Logs or traffic showing outbound request to the external lookup server containing the search query and source IP.

**Success Indicators**:
- External server receives unintended data
- Confirmation of leak without user consent, unlike web/desktop clients

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable Nextcloud environment
2. Triggered leak via Android app search without parameter inclusion
3. Confirmed privacy violation through external data transmission

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exfiltration Over Unencrypted Non-C2 Protocol]] Exfiltration Over Unencrypted Non-C2 Protocol

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Exfiltration]] Exfiltration

---
*Last updated: 2023-10-01T00:00:00Z*
