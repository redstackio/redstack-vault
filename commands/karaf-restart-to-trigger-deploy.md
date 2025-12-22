---
id: efb215f0-b2bf-42d2-9104-e7bc2cd4c0c3
name: karaf-restart-to-trigger-deploy
type: command
executor: bash
data: cd /opt/apache-karaf/bin && ./stop && nohup ./start &
output: null
created_at: '2023-04-06T03:56:44.442744+00:00'
updated_at: '2023-04-10T20:24:44.655630+00:00'
platforms:
  - Linux
tags:
  - restart
  - deployment-trigger
verified: true
validated: true
---

# karaf-restart-to-trigger-deploy

## Command

```bash
cd /opt/apache-karaf/bin && ./stop && nohup ./start &
```

## Description

This command stops and restarts the Apache Karaf service to force re-scanning of the deploy directory, triggering processing of the uploaded XXE payload. Run this on the target server after uploading the XML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/opt/apache-karaf/bin` | Path to Karaf bin directory | Yes |
| `./stop` | Stops the running Karaf instance | Built-in |
| `nohup ./start &` | Starts Karaf in background, detached | Built-in |

## Examples

### Basic Usage

```bash
cd /opt/apache-karaf/bin && ./stop && nohup ./start &
[1] 12345
Stopping Apache Karaf ...
Apache Karaf ... (\^Z)\(Ctrl+C\): 

Starting Apache Karaf ...
```

### Advanced Usage (With Logging)

```bash
cd /opt/apache-karaf/bin && ./stop && nohup ./start > /tmp/karaf-start.log 2>&1 &
```

## Expected Output

Process termination and startup messages:

```
Stopping Apache Karaf
Apache Karaf stopped
Starting Apache Karaf
Apache Karaf started in Xs
```

Success: Karaf restarts without errors; check logs (tail -f ../data/log/karaf.log) for 'Features XML parsed' or DTD fetch attempts. Failure: Bind errors if port 8181 in use; kill processes manually.

## Related

- [[procedures/Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration]]
- [[commands/scp-deploy-xml-to-karaf]]
