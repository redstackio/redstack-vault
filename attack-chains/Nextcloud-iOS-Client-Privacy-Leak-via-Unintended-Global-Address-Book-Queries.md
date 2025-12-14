---
id: ac-nextcloud-ios-leak-001
tags:
  - privacy-leak
  - nextcloud
  - ios
  - data-leak
  - improper-access-control
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
verified: false
platforms:
  - iOS
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Configure-Default-Nextcloud-Server-for-Global-Address-Book]]'
  - '[[procedures/Perform-Sharee-Search-in-Nextcloud-iOS-Client]]'
  - '[[procedures/Analyze-Data-Leakage-to-Nextcloud-Lookup-Server]]'
step_count: 3
techniques:
  - '[[Automated Collection]]'
  - '[[Remote System Discovery]]'
updated_at: '2025-12-14T17:24:39.982Z'
description: >-
  Demonstrates how default Nextcloud server configuration combined with iOS
  client behavior leads to unintended leakage of search terms and server IP to
  the external Nextcloud lookup server.
skill_level: low
impact_level: medium
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Automated Collection]]'
  - '[[Remote System Discovery]]'
---
# Nextcloud iOS Client Privacy Leak via Unintended Global Address Book Queries

Multi-stage attack chain demonstrating a complete privacy leak workflow in Nextcloud due to default configurations and client-side omissions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Default Server] --> B[Trigger iOS Search]
    B --> C[Observe External Leak]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Nextcloud server instance (self-hosted or VM)
- Nextcloud iOS app installed on an iOS device
- Network access to monitor traffic (e.g., proxy or server logs)

### Target Environment

- Nextcloud server running default PHP-based configuration
- iOS platform with Nextcloud client
- Services: Nextcloud server, Nextcloud lookup server
- Ports: Standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Administrative access to set up Nextcloud server
- User account on Nextcloud for sharing files
- No prior network position needed beyond standard internet access

## Detailed Attack Procedures

### Step 1: Server Setup
procedure: [[procedures/Configure-Default-Nextcloud-Server-for-Global-Address-Book]]

**Objective**: Establish a Nextcloud server with default settings that enable global address book searches, setting the stage for unintended queries.

**Instructions**: Install and configure a fresh Nextcloud instance, ensuring the 'Search global and public address book for users' option is enabled by default in the sharing settings. This is the standard out-of-the-box behavior without explicit disabling.

**Expected Output**: Nextcloud server running with global lookup active, confirmed via admin settings panel.

**Success Indicators**:
- Global address book search option is toggled on in server config
- Server logs show no custom overrides for lookup parameters

### Step 2: Trigger Search in iOS Client
procedure: [[procedures/Perform-Sharee-Search-in-Nextcloud-iOS-Client]]

**Objective**: Use the iOS Nextcloud app to initiate a sharee search, which omits the critical 'lookup' parameter, forcing the server to default to global querying.

**Instructions**: Log into the Nextcloud iOS app, navigate to a file, select share, and enter a search term for potential sharees. The app sends a request to the server's ShareesAPIController endpoint without specifying 'lookup=false', causing default activation.

**Expected Output**: Search interface in iOS app processes the query, but underlying network request lacks the parameter.

**Success Indicators**:
- Search term entered and processed in app
- No explicit global search consent prompted (unlike web/desktop clients)

### Step 3: Observe Leakage
procedure: [[procedures/Analyze-Data-Leakage-to-Nextcloud-Lookup-Server]]

**Objective**: Monitor and verify the unintended transmission of search terms and server IP to the external Nextcloud lookup server.

**Instructions**: Inspect server-side logs or use a network proxy to capture traffic from the Nextcloud server to the lookup server (e.g., lookup.nextcloud.com). Confirm that the missing 'lookup' parameter at line 144 in ShareesAPIController.php defaults to true, triggering the external query.

**Expected Output**: Captured requests showing search terms (e.g., username) and originating server IP sent externally without user consent.

**Success Indicators**:
- External query observed in logs/traffic
- Privacy violation confirmed: data leaked to Nextcloud's central lookup service

## Attack Chain Summary

### Key Achievements

1. Exposed default configuration flaw enabling global searches
2. Demonstrated iOS client omission leading to unintended requests
3. Verified privacy impact through external data transmission

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Automated Collection]] Automated Collection
- [[Remote System Discovery]] Remote System Discovery

### MITRE ATT&CK Tactics

- [[Collection]] Collection
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
