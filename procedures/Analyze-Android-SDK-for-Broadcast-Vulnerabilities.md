---
tags:
  - android
  - static-analysis
  - broadcast-receiver
  - code-review
type: procedure
tools:
  - '[[tools/JADX]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Android
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0858c7e5-b774-4a55-ae4d-2d18899c47ea
created_at: '2025-12-14T17:24:42.119Z'
updated_at: '2025-12-14T17:24:42.119Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze Android SDK for Broadcast Vulnerabilities

## Summary

This procedure involves static code analysis of Android SDKs, such as Mapbox, to detect the use of global Broadcast Receivers that expose sensitive data like location information to interception by other apps on the device. It highlights the absence of process isolation via LocalBroadcastManager, enabling identification of information disclosure risks.

## Description

In the Mapbox Android SDK (versions prior to 4.2.1), location services requests are handled using standard Broadcast Receivers, which send intents globally across the device. This allows any app with a matching intent filter to receive the broadcasts, potentially disclosing user location data. The procedure uses decompilation to review the SDK's location module, confirming the root cause: reliance on `sendBroadcast()` instead of local broadcasts. Prerequisites include access to the SDK source or binaries; outcomes include pinpointing vulnerable intent actions and filters for exploitation planning.

## Requirements

1. Mapbox Android SDK binary (JAR/APK) or source code access
2. Decompilation tool like [[tools/JADX]]
3. Basic knowledge of Android app architecture and intents

## Defense

Defensive measures and detection strategies:

- Migrate to LocalBroadcastManager for intra-app communications to restrict broadcasts to the app's process
- Use explicit intents with package targeting to prevent implicit reception
- Static analysis tools in CI/CD pipelines to flag global broadcasts of sensitive data
- Runtime monitoring for unexpected broadcast receptions via app logs or security frameworks like Android's SafetyNet

## Objectives

1. Identify BroadcastReceiver implementations in the SDK's location services
2. Confirm lack of isolation mechanisms leading to cross-app data exposure
3. Document vulnerable intent actions for potential exploitation

## Instructions

### Step 1: Obtain and Decompile SDK

**Context**: Acquire the target SDK and decompile it to access readable Java code for analysis.

Use [[tools/JADX]] to decompile the Mapbox SDK APK or JAR. Launch the GUI version and open the file, or use CLI for batch processing.

> In JADX GUI, navigate to the location services package (e.g., com.mapbox.services.location) and search for classes extending BroadcastReceiver.

### Step 2: Review Broadcast Implementation

**Context**: Examine the code for insecure broadcast patterns to validate the vulnerability.

Search for methods calling `context.sendBroadcast(intent)` without `LocalBroadcastManager`. Note intent actions (e.g., custom actions for location updates) and any extras containing sensitive data like GPS coordinates.

> Look for absence of import `androidx.localbroadcastmanager.content.LocalBroadcastManager`; presence of global sends indicates exposure. Cross-reference with documentation to confirm location data handling.

### Step 3: Validate Impact

**Context**: Assess the scope of data exposure and potential receivers.

Review intent filters in the receiver; if implicit (action-only), any app can register. Test in an emulator by simulating broadcasts if source is available.

> Expected: Confirmation of low-severity info disclosure, as other apps can register dynamically or statically to intercept.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/JADX]]

## Tags

- [[android]]
- [[static-analysis]]
- [[broadcast-receiver]]
