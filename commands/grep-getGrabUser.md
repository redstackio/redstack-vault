---
id: cmd-grep-getGrabUser
data: grep getGrabUser
tags:
  - search
  - js-analysis
type: command
output: >-
  Found JavaScript code snippet showing iOS implementation: public static
  initGrabUser() { if(Utils.Condition.isIOSApp()){
  Stores.GrabUser.setGrabUser(window.grabUser); }
  if(Utils.Condition.isAndroidApp()){
  Stores.GrabUser.setGrabUser(JSON.parse(Android.getGrabUser())); } }
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:22.854Z'
verified: false
validated: true
submitted: true
---
# grep-getGrabUser

## Command

```bash
grep getGrabUser
```

## Description

This command searches for references to the 'getGrabUser' function in webpage source code, typically used to analyze JavaScript for mobile app exposures like in Grab's help pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| getGrabUser | String pattern to match function references | Yes |

## Examples

### Basic Usage

```bash
grep getGrabUser help_page_source.html
```

### Advanced Usage

```bash
grep -n -i "getGrabUser" *.js
```

## Expected Output

Lines containing 'getGrabUser', such as JS code revealing platform-specific implementations for Android and iOS user data handling.

## Related

- [[Related Procedure]] Analyze-iOS-WebView-Implementation
