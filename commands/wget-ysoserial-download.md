---
data: >-
  wget
  https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
tags:
  - download
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:18.964Z'
id: e7287024-2544-4ecc-a24b-9de3d6d5b8c7
verified: false
validated: true
submitted: true
---
# wget-ysoserial-download

## Command

```bash
wget https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

## Description

Downloads the ysoserial JAR file from a GitHub repository, used for generating Java deserialization exploits.

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

The file ysoserial-0.0.6-SNAPSHOT-all.jar is saved to the current directory, with progress shown during download.

## Related

- [[Related Procedure]]
