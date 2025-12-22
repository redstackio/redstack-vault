---
id: be5f5bcf-467e-4eda-bea9-3598df80952d
type: command
executor: cmd
data: net start webclient
output: null
created_at: '2023-04-06T03:56:02.931434+00:00'
updated_at: '2023-04-10T20:25:52.370784+00:00'
platforms:
  - Windows
tags:
  - service
  - webdav
  - printnightmare
verified: true
validated: true
---

# net-start-webclient

## Command

```cmd
net start webclient
```

## Description

Starts the WebClient service on Windows, enabling WebDAV and HTTP UNC path access required for loading remote files in exploits like PrintNightmare.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; starts the service | N/A |

## Examples

### Basic Usage

```cmd
net start webclient
```

### Check Status

```cmd
sc query webclient
```

## Expected Output

The WebClient service is starting.
The WebClient service was started successfully.

## Related

- [[procedures/PrintNightmare-WebDAV-Attack]]
- [[techniques/Web Service|T1102 - Web Service]]
