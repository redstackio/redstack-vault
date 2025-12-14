---
id: cmd-set-publish-001
data: 'parameters.put("publish", "true");'
tags:
  - publish
type: command
output: Parameter added to map
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.670Z'
verified: false
validated: true
submitted: true
---
# set-publish-parameter

## Command

```java
parameters.put("publish", "true");
```

## Description

Enables publishing of the infographic by setting the 'publish' flag to true in parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| parameters | HashMap | Yes |
| publish | Boolean as string 'true' | Yes |

## Examples

### Basic Usage

```java
parameters.put("publish", "true");
```

### Advanced Usage

For private: ```java
parameters.put("publish", "false");
```

## Expected Output

No output; flag set.

## Related

- [[commands/set-publish-mode-parameter]]
- [[procedures/Prepare-Malicious-XSS-Payload-for-Infographic-Content]]
