---
type: command
executor: bash
data: |
  eyewitness --web --single https://$_TARGET_URL
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - web
created_at: '2020-07-24T17:11:37.846370+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
verified: true
validated: true
---

# eyewitness-screenshot-single-url

## Command

```bash
eyewitness --web --single https://$_TARGET_URL
```

## Description

This command uses Eyewitness to capture a screenshot of a single website URL using a headless Selenium browser. It is useful for quick visual reconnaissance of a specific web target during penetration testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --web | Run in headless web mode using Selenium/Chrome | Yes |
| --single | Specify a single URL to screenshot | Yes |
| $_TARGET_URL | The full URL of the target website (e.g., https://example.com) | Yes |

## Examples

### Basic Usage

```bash
eyewitness --web --single https://redstack.io
```

### Advanced Usage

```bash
eyewitness --web --single https://redstack.io --timeout 30 --resolution 1920,1080
```

## Expected Output

The command creates a screenshots/ directory with a subfolder for the hostname (e.g., redstack.io), containing a PNG screenshot and a JSON file with metadata like page title, status code, and load time. Console output shows progress: "Starting Eyewitness..." followed by "Screenshot saved" or errors like connection timeouts.

## Related

- [[procedures/Capture-Website-Screenshots-with-Eyewitness]]
- [[tools/eyewitness]]
