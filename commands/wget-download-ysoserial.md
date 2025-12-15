---
id: cmd-uuid-001
data: >-
  wget
  https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
tags:
  - download
  - tool-acquisition
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.127Z'
verified: false
validated: true
submitted: true
---
# wget-download-ysoserial

## Command

```bash
wget https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

## Description

This command uses wget to download the ysoserial JAR file from a GitHub repository, which is used for generating Java deserialization payloads in exploits like CVE-2021-35464.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Direct link to the JAR file on GitHub | Yes |

## Examples

### Basic Usage

```bash
wget https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

### Advanced Usage

```bash
wget -O ysoserial.jar https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

## Expected Output

Download progress shown, followed by 'saved [size] bytes' message. The file ysoserial-0.0.6-SNAPSHOT-all.jar is saved in the current directory.

## Related

- [[Related Procedure|procedures/Download-Ysoserial-Tool-for-Deserialization-Payloads]]
