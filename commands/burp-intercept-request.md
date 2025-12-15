---
id: 123e4567-e89b-12d3-a456-426614174004
name: burp-intercept-request
type: command
executor: bash
data: |-
  # Burp Suite is GUI-based; start listener via command line if automated
  java -jar burpsuite_pro.jar --listen 8080
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.406Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - proxy
  - intercept
verified: false
validated: true
submitted: true
---

# burp-intercept-request

## Command

```bash
# Burp Suite is GUI-based; start listener via command line if automated
java -jar burpsuite_pro.jar --listen 8080
```

## Description

Starts Burp Suite in listener mode to intercept HTTP/HTTPS traffic from the TikTok app, allowing capture of API requests for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--listen` | Port to listen on (default 8080) | No |
| `burpsuite_pro.jar` | Path to Burp JAR file | Yes |

## Examples

### Basic Usage

```bash
java -jar burpsuite_pro.jar
```

### Advanced Usage

```bash
java -jar /path/to/burpsuite_pro.jar --listen 8080
```

## Expected Output

Burp Suite launches with proxy listener active; traffic appears in Proxy > Intercept tab upon configuration.

## Related

- [[Related Procedure]]
