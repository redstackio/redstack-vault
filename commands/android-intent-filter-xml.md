---
id: cmd-uuid-3
data: |-
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="https" />
    <data android:host="qvay.app.link" />
  </intent-filter>
tags:
  - android
  - manifest
type: command
output: null
executor: xml
platforms:
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.303Z'
verified: false
validated: true
submitted: true
---
# android-intent-filter-xml

## Command

```xml
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="https" />
  <data android:host="qvay.app.link" />
</intent-filter>
```

## Description

XML snippet for AndroidManifest.xml to register an intent-filter intercepting HTTPS deeplinks to qvay.app.link, enabling hijacking of Branch.io magic links.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| action.VIEW | Intent action for URI viewing | Yes |
| category.DEFAULT | For implicit intents | Yes |
| category.BROWSABLE | For browser-like handling | Yes |
| scheme.https | Matches HTTPS | Yes |
| host.qvay.app.link | Specific Branch.io domain | Yes |

## Examples

### Basic Usage

Insert into <activity> tag in AndroidManifest.xml.

### Advanced Usage

Add path or query matching for finer control.

## Expected Output

App receives Intent with matching data when deeplink opened.

## Related

- [[procedures/Configure-Malicious-App-for-Deeplink-Interception]]
