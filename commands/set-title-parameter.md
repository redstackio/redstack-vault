---
id: cmd-set-title-001
data: 'parameters.put("title","title");'
tags:
  - metadata
type: command
output: Parameter added to map
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.675Z'
verified: false
validated: true
submitted: true
---
# set-title-parameter

## Command

```java
parameters.put("title","title");
```

## Description

Adds the 'title' key to the parameters map with a basic string value for the infographic name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| parameters | HashMap | Yes |
| title | String title (e.g., 'title') | Yes |

## Examples

### Basic Usage

```java
parameters.put("title","title");
```

### Advanced Usage

```java
parameters.put("title", "Malicious Infographic");
```

## Expected Output

No output; 'title' key set.

## Related

- [[commands/set-publish-parameter]]
- [[procedures/Prepare-Malicious-XSS-Payload-for-Infographic-Content]]
