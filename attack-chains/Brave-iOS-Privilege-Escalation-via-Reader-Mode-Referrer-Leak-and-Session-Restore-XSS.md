---
id: ac-brave-ios-referrer-xss-escalation
tags:
  - xss
  - referrer-leak
  - privilege-escalation
  - brave-ios
  - ios
  - mobile-browser
type: attack_chain
tools:
  - '[[tools/reader_uuid_leakage-php]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - iOS
  - Mobile
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Leak-UUID-Key-via-Brave-Reader-Mode-Referrer]]'
  - '[[procedures/Execute-XSS-via-Brave-Session-Restore]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T03:16:14.699Z'
description: >-
  Multi-stage attack exploiting referrer policy misconfiguration in Brave iOS
  ReaderViewLoading.html and XSS in SessionRestoreHandler.swift to leak a
  sensitive UUID key and execute arbitrary JavaScript on the privileged
  internal://local origin.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Brave iOS Privilege Escalation via Reader Mode Referrer Leak and Session Restore XSS

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in Brave iOS to achieve privilege escalation on the internal://local origin.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Visit Malicious Page] --> B[Activate Reader Mode]
    B --> C[Long Press Link in New Private Tab]
    C --> D[Load Original Page to Leak UUID]
    D --> E[Capture Leaked UUID on Server]
    E --> F[Click Exploit URL for XSS Execution]
    F --> G[Arbitrary JS on Internal Origin]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/reader_uuid_leakage-php]]

### Target Environment

- Target OS/Platform: iOS 14.x and below
- Required services/ports: None (client-side browser exploit)
- Network access requirements: Victim must visit attacker-controlled HTTPS page

### Initial Access Requirements

- Credential requirements: None
- Network position: Victim browsing web
- Prior access needed: None, social engineering to lure victim to malicious page

## Detailed Attack Procedures

### Step 1: Visit the Malicious Page
procedure: [[procedures/Leak-UUID-Key-via-Brave-Reader-Mode-Referrer]]

**Objective**: Load the attacker's malicious page to set up the environment for reader mode interaction.

**Instructions**: Direct the victim to load the malicious page at `https://csrf.jp/brave/reader_uuid_leakage.php`, which contains hyperlinks and exploit URLs designed to interact with Brave's reader mode. This page serves as the entry point for the attack.

**Expected Output**: Page loads in Brave iOS browser, displaying hyperlinks.

**Success Indicators**:
- Page successfully loaded without errors
- Hyperlinks visible for interaction

### Step 2: Open the Page in Reader Mode
procedure: [[procedures/Leak-UUID-Key-via-Brave-Reader-Mode-Referrer]]

**Objective**: Activate reader mode to generate the internal reader mode URL containing the sensitive uuidKey.

**Instructions**: In Brave iOS, activate reader mode on the loaded page. This uses Reader.html and potentially ReaderViewLoading.html templates, which expose the reader mode URL with the uuidKey.

**Expected Output**: Page switches to reader mode view, generating an internal URL like `internal://reader?url=...&uuidKey=...`.

**Success Indicators**:
- Reader mode activated successfully
- Clean, distilled article view displayed

### Step 3: Long Tap a Hyperlink and Open in New Private Tab
procedure: [[procedures/Leak-UUID-Key-via-Brave-Reader-Mode-Referrer]]

**Objective**: Trigger navigation that loads ReaderViewLoading.html without referrer protection to prepare for leakage.

**Instructions**: Select a hyperlink on the page in reader mode, long-press it, and choose to open in a new private tab. This navigation uses ReaderViewLoading.html, which lacks proper referrer policy.

**Expected Output**: New private tab opens, loading the linked content via ReaderViewLoading.html.

**Success Indicators**:
- New private tab created
- Navigation completes without blocking

### Step 4: Wait and Tap 'Load Original Page'
procedure: [[procedures/Leak-UUID-Key-via-Brave-Reader-Mode-Referrer]]

**Objective**: Restore the session to send the REFERER header containing the uuidKey to the attacker's server.

**Instructions**: Wait several seconds for the page to load, then tap 'Load original page' to restore the session. During this, the REFERER header leaks the uuidKey due to the missing meta referrer policy in ReaderViewLoading.html.

**Expected Output**: Original page loads, and REFERER header is sent to attacker's server.

**Success Indicators**:
- 'Load original page' option appears and is tappable
- Page restores to full view

### Step 5: UUID Key is Stolen Through REFERER Header
procedure: [[procedures/Leak-UUID-Key-via-Brave-Reader-Mode-Referrer]]

**Objective**: Capture the leaked uuidKey on the attacker's server for use in further exploitation.

**Instructions**: The server-side script at `https://csrf.jp/brave/reader_uuid_leakage.php` automatically captures the leaked uuidKey from the REFERER header sent during the navigation.

**Expected Output**: Attacker's server logs receive the uuidKey value.

**Success Indicators**:
- Server logs show REFERER header with uuidKey
- Key extracted for next stage

### Step 6: Click the Exploit URL to Trigger XSS
procedure: [[procedures/Execute-XSS-via-Brave-Session-Restore]]

**Objective**: Deliver and execute arbitrary JavaScript on the privileged internal://local origin via unvalidated URL restoration.

**Instructions**: On the malicious page, click a specially crafted exploit URL that provides a `javascript:` URL to SessionRestoreHandler. This handler restores it without validation, executing JavaScript on `internal://local`.

**Expected Output**: JavaScript executes in high-privilege context, allowing access to internal app features.

**Success Indicators**:
- Arbitrary JS runs (e.g., alert or console log in internal context)
- Privilege escalation confirmed via internal API access

## Attack Chain Summary

### Key Achievements

1. Successful leakage of sensitive uuidKey from Brave's reader mode internal URL via referrer header.
2. Chained exploitation of XSS in session restoration to execute JavaScript on privileged internal origin.
3. Achieved privilege escalation in Brave iOS 1.32.3 and higher on iOS 14.x and below, potentially exposing internal browser features.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Privilege Escalation]]

---

*Last updated: 2023-10-01T00:00:00Z*
