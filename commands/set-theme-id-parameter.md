---
id: cmd-set-theme-001
data: 'parameters.put("theme_id", "7291");'
tags:
  - configuration
type: command
output: Parameter added to map
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.680Z'
verified: false
validated: true
submitted: true
---
# set-theme-id-parameter

## Command

```java
parameters.put("theme_id", "7291");
```

## Description

Sets the theme ID for the infographic to a specific value (7291) in the parameters map, configuring appearance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| parameters | HashMap<String, String> | Yes |
| theme_id | String ID of theme (e.g., '7291') | Yes |

## Examples

### Basic Usage

```java
parameters.put("theme_id", "7291");
```

### Advanced Usage

```java
parameters.put("theme_id", "7291");
// Use different ID if needed
parameters.put("theme_id", "other-id");
```

## Expected Output

No output; key 'theme_id' added with value '7291'.

## Related

- [[commands/set-title-parameter]]
- [[procedures/Prepare-Malicious-XSS-Payload-for-Infographic-Content]]
