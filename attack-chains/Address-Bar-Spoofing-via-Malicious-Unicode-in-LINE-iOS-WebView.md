---
tags:
  - address-bar-spoofing
  - unicode-phishing
  - webview
  - ios
  - phishing
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - iOS
  - Mobile App
  - WebView
complexity: medium
procedures:
  - '[[procedures/Craft-Malicious-Unicode-URL-for-Spoofing]]'
  - '[[procedures/Trigger-Address-Bar-Update-in-WebView]]'
  - '[[procedures/Deceive-User-with-Phishing-Content]]'
step_count: 3
techniques:
  - '[[Phishing]]'
description: >-
  A phishing attack exploiting improper URL normalization in the LINE iOS app's
  internal browser to spoof the address bar with legitimate-looking domains
  while loading malicious content.
skill_level: intermediate
impact_level: low
id: 01a0f55b-7bba-401a-a67a-a513f6a73584
created_at: '2025-12-14T17:24:44.883Z'
updated_at: '2025-12-14T17:24:44.883Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Address Bar Spoofing via Malicious Unicode in LINE iOS WebView

## Overview

This attack chain demonstrates a vulnerability in the LINE iOS client's internal browser (WebView) where improper URL normalization allows attackers to insert malicious Unicode characters into domain names. During HTTP redirect processing or navigation to invalid hostnames, the address bar updates with a deceptive, normalized domain that appears legitimate, while the actual content loaded is from a phishing site. Discovered by researcher reinforchu and reported on January 21, 2021, via HackerOne (Report #1082991), this enables phishing attacks by deceiving users into interacting with malicious pages, though it was rated low severity and fixed without a bounty.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious URL] --> B[Trigger WebView Navigation]
    B --> C[Exploit Address Bar Timing]
    C --> D[Load Phishing Content]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on URL crafting and app interaction)

### Target Environment

- LINE iOS app (version vulnerable as of report, pre-2021 fix)
- iOS device with internal browser/WebView access
- No specific ports or services; occurs within the app's navigation

### Initial Access Requirements

- User must open a malicious link within the LINE app (e.g., via chat or direct navigation)
- No prior credentials needed; exploits client-side rendering
- Attacker crafts and distributes the URL via social engineering

## Detailed Attack Procedures

### Step 1: Craft Malicious Unicode URL
procedure: [[procedures/Craft-Malicious-Unicode-URL-for-Spoofing]]

**Objective**: Create a URL with Unicode characters that bypass URL normalization to display a fake legitimate domain.

**Instructions**: Design a URL incorporating Unicode characters (e.g., homoglyphs or invalid sequences) in the domain part to trigger improper normalization during processing. For example, use characters like U+1FDC0 or similar to mimic a trusted domain like "line.me" while pointing to an attacker-controlled server.

**Expected Output**: A crafted URL that, when navigated to in the LINE WebView, initiates a redirect or invalid hostname handling.

**Success Indicators**:
- URL parses without immediate rejection
- WebView begins navigation process

### Step 2: Trigger Address Bar Update
procedure: [[procedures/Trigger-Address-Bar-Update-in-WebView]]

**Objective**: Navigate to the URL in the LINE app's internal browser, exploiting timing mismatches to update the address bar deceptively.

**Instructions**: Within the LINE iOS app, open the crafted URL via the internal browser. The app's WebView processes the HTTP redirect or invalid hostname, canceling navigation but updating the address bar with a normalized version of the deceptive domain due to asynchronous timing issues.

**Expected Output**: Address bar shows a legitimate-looking domain (e.g., "secure-line.com"), but actual load is canceled or redirected subtly.

**Success Indicators**:
- Address bar displays spoofed domain
- No error prompts to user

### Step 3: Load and Deceive with Phishing Content
procedure: [[procedures/Deceive-User-with-Phishing-Content]]

**Objective**: Load malicious phishing content while the spoofed address bar convinces the user of legitimacy.

**Instructions**: As the WebView loads the actual malicious content from the attacker's server (bypassing the cancellation via redirect chaining), the user sees the spoofed domain and interacts with phishing elements like fake login forms.

**Expected Output**: User presented with phishing page mimicking a trusted site, leading to credential theft or further compromise.

**Success Indicators**:
- User enters data on phishing page
- No visual indicators of mismatch

## Attack Chain Summary

### Key Achievements

1. Successful spoofing of address bar to mimic legitimate domains
2. Loading of phishing content without user suspicion
3. Enabling low-severity phishing attacks via Unicode manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
