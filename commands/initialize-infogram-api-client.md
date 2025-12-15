---
id: cmd-infogram-init-001
data: 'InfogramAPI infogram = new InfogramAPI([API-Key], [API-Secret]);'
tags:
  - api-auth
type: command
output: Authenticated API instance
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.695Z'
verified: false
validated: true
submitted: true
---
# initialize-infogram-api-client

## Command

```java
InfogramAPI infogram = new InfogramAPI([API-Key], [API-Secret]);
```

## Description

Initializes the Infogram API client with provided key and secret for authenticated requests. Use this at the start of any API interaction script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [API-Key] | Alphanumeric API key from Infogram settings | Yes |
| [API-Secret] | Alphanumeric API secret from settings | Yes |

## Examples

### Basic Usage

```java
InfogramAPI infogram = new InfogramAPI("your-api-key", "your-api-secret");
```

### Advanced Usage

In a main method with error handling:

```java
try {
  InfogramAPI infogram = new InfogramAPI("key", "secret");
  // Proceed with requests
} catch (Exception e) {
  System.err.println("Auth failed: " + e.getMessage());
}
```

## Expected Output

A usable InfogramAPI object instance ready for sendRequest calls. No output printed; errors if credentials invalid.

## Related

- [[commands/send-post-request-to-infographics]]
- [[procedures/Create-Infographic-via-API-to-Inject-Stored-XSS]]
