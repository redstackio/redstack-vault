---
id: tool-chrome-ios-13-1
url: 'https://www.google.com/chrome/'
tags:
  - browser
  - web-testing
type: tool
verified: false
platforms:
  - iOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.880Z'
validated: true
submitted: true
---
# Chrome-iOS-13-1

**Status**: Unverified

## Overview

Google Chrome browser version for iOS 13.1, used as a mobile client to access and test web vulnerabilities like XSS on sites such as pixiv.net.

## Description

Chrome on iOS 13.1 emulates a mobile user agent, which is critical for reproducing platform-specific issues in web applications. It supports JavaScript execution and is commonly used in pentesting for drive-by exploits and payload delivery via URLs.

## Features

- Feature 1: Full JavaScript engine (V8) for payload testing.
- Feature 2: Mobile user agent string for site-specific rendering.
- Feature 3: Developer tools for inspecting network and console output.

## Installation

### Requirements

- iOS 13.1 device or simulator.
- App Store access.

### Install Commands

No command-line install; download from App Store.

## Basic Usage

Open Chrome and navigate to target URLs.

### Common Options

| Option | Description |
|--------|-------------|
| Developer Menu | Enable via chrome://flags for advanced debugging |
| User Agent | Defaults to mobile iOS |

## Examples

### Example 1: Basic Usage

Navigate to https://www.pixiv.net/en/ in Chrome iOS 13.1.

### Example 2: Advanced Usage

Inject payload: https://www.pixiv.net/en/['-alert(document.cookie)-'] to test XSS.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User agent strings containing 'Chrome/78.0' (iOS 13.1 era) and mobile indicators.
- Console logs showing JavaScript errors from payloads.

## Related Procedures


## Related Tools

- [[Firefox-iOS]]
- [[Safari-iOS]]

## References

- Official documentation: https://support.google.com/chrome
- iOS specifics: Apple Developer docs
