---
id: cmd-hashmap-create-001
data: 'Map<String, String> parameters = new HashMap<String, String>();'
tags:
  - parameters
type: command
output: Empty parameter map
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.690Z'
verified: false
validated: true
submitted: true
---
# create-parameters-hashmap

## Command

```java
Map<String, String> parameters = new HashMap<String, String>();
```

## Description

Creates a new HashMap to store string key-value pairs for API request parameters, such as content and title for infographic creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard Java import required: import java.util.HashMap; import java.util.Map; | No |

## Examples

### Basic Usage

```java
Map<String, String> parameters = new HashMap<String, String>FILL IN LATER();
```

### Advanced Usage

With imports:

```java
import java.util.HashMap;
import java.util.Map;

public class Main {
  public static void main(String[] args) {
    Map<String, String> parameters = new HashMap<String, String>();
  }
}
```

## Expected Output

An empty HashMap instance; no console output.

## Related

- [[commands/set-content-xss-payload]]
- [[procedures/Prepare-Malicious-XSS-Payload-for-Infographic-Content]]
