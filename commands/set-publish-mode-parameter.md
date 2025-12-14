---
id: cmd-set-publish-mode-001
data: 'parameters.put("publish_mode", "public");'
tags:
  - visibility
type: command
output: Parameter added to map
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.646Z'
verified: false
validated: true
submitted: true
---
# set-publish-mode-parameter

## Command

```java
parameters.put("publish_mode", "public");
```

## Description

Sets the publish mode to public, allowing broader access to the infographic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| parameters | HashMap | Yes |
| publish_mode | 'public' or other mode | Yes |

## Examples

### Basic Usage

```java
parameters.put("publish_mode", "public");
```

### Advanced Usage

For private: ```java
parameters.put("publish_mode", "private");
```

## Expected Output

No output; mode set.

## Related

- [[commands/send-post-request-to-infographics]]
- [[procedures/Prepare-Malicious-XSS-Payload-for-Infographic-Content]]
