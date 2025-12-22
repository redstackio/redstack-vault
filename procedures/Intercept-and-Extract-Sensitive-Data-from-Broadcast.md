---
id: proc-shopify-intercept-data-001
tags:
  - android
  - data-extraction
  - broadcast-intercept
type: procedure
tools:
  - '[[tools/Custom-POC-APK-shopifyhack]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:32:10.993Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Intercept-and-Extract-Sensitive-Data-from-Broadcast

## Summary

This procedure uses the POC app's receiver to capture and process the Shopify broadcast, extracting sensitive extras like access tokens from the body and admin cookies from headers for potential exfiltration or use in account takeover.

## Description

The HackBroadcastReceiver in the POC APK listens for the implicit broadcast, parses Intent extras (e.g., 'response_headers', 'response_body'), and logs or stores data such as tokens and cookies, exploiting the lack of signature permissions.

## Requirements

1. POC APK installed and receiver registered
2. Shopify login performed to trigger broadcast
3. No additional tools needed; handled by POC

## Defense

Defensive measures and detection strategies:

- Protect broadcasts with custom permissions or use explicit Intents
- Scan for apps registering receivers for sensitive actions
- Use runtime app analysis to detect data leakage

## Objectives

1. Capture full API response data
2. Extract credentials silently
3. Enable further exploitation like remote sending of data

## Instructions

### Step 1: Activate Receiver

**Context**: Ensure the POC is running to receive broadcasts.

Launch the POC app briefly or rely on background registration.

> Receiver activates on install; no manual start needed post-trigger.

### Step 2: Process Broadcast

**Context**: Automatically intercept when Shopify sends the Intent.

The receiver code (in POC) handles onReceive:

```java
// Pseudo-code from POC
public void onReceive(Context context, Intent intent) {
    String headers = intent.getStringExtra("response_headers");
    String body = intent.getStringExtra("response_body");
    Log.v("SHOPIFYHACK", "Cookie: " + extractCookie(headers));
    Log.v("SHOPIFYHACK", "Token: " + extractToken(body));
}
```

> Data is logged with 'SHOPIFYHACK' tag for later retrieval.

### Step 3: Verify Extraction

**Context**: Confirm data capture before viewing logs.

No output visible; prepare for log inspection in next step.

> Success if logs (next procedure) show extracted items.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-POC-APK-shopifyhack]]

## Tags

- android
- data-extraction
- broadcast-intercept
