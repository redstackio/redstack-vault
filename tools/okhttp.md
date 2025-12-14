---
url: 'https://square.github.io/okhttp/'
tags:
  - http-client
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.051Z'
id: 20c604eb-81f0-4477-8a40-1410646392d2
validated: true
submitted: true
---
# okhttp

**Status**: Unverified

## Overview

OkHttp is an HTTP client library for Java and Android, used by the Shopify Ping app for making API requests including OAuth flows and logout attempts.

## Description

OkHttp handles HTTP/1.1 and HTTP/2, supports connection pooling, and is configured in version 3.12.12 for the app's requests. In security testing, it's relevant for understanding app traffic and potential interception points.

## Features

- Feature 1: Efficient HTTP client with gzip support
- Feature 2: Automatic token handling in headers
- Feature 3: Integration with Android networking

## Installation

### Requirements

- Java 8+ or Android SDK

### Install Commands

```bash
# Via Gradle in Android project
dependencies {
    implementation 'com.squareup.okhttp3:okhttp:3.12.12'
}
```

## Basic Usage

```bash
# Example in Java
OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder().url("https://example.com").build();
Response response = client.newCall(request).execute();
```

### Common Options

| Option | Description |
|--------|-------------|
| `--version` | Check version |
| N/A | Library, not CLI |

## Examples

### Example 1: Basic Usage

As above for GET request.

### Example 2: Advanced Usage

Add headers for auth:

```java
Request request = new Request.Builder()
    .url("https://accounts.shopify.com/oauth/userinfo")
    .addHeader("Authorization", "Bearer " + token)
    .build();
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traces showing okhttp User-Agent
- App disassembly revealing okhttp dependencies

## Related Procedures

- [[procedures/Perform-OAuth-Login-in-Shopify-Ping-App]]

## Related Tools

- [[Apache HttpClient]]

## References

- Official documentation: https://square.github.io/okhttp/
