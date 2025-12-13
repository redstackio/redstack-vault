---
data: 'java -cp .:pippo-jaxb.jar ClientProgram malicious.xml Person.class'
tags:
  - java
  - execution
type: command
executor: bash
platforms:
  - Java
id: 0930ad24-6ba8-4168-9949-dfc315e1036d
created_at: '2025-12-13T09:00:27.229Z'
updated_at: '2025-12-13T09:00:27.229Z'
verified: false
validated: true
submitted: true
---
# Run Java Client

## Command

```bash
java -cp .:pippo-jaxb.jar ClientProgram malicious.xml Person.class
```

## Description

This command runs a Java client program that parses the provided XML file using the Pippo JAXB engine, suitable for demonstrating vulnerabilities like XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-cp` | Classpath including JAXB jar | Yes |
| `ClientProgram` | Main class name | Yes |
| `malicious.xml` | XML payload file | Yes |
| `Person.class` | Target class for unmarshalling | Yes |

## Examples

### Basic Usage

```bash
java -cp .:pippo-jaxb.jar ClientProgram malicious.xml Person.class
```

### Advanced Usage

```bash
java -Xmx512m -cp .:pippo-jaxb.jar ClientProgram malicious.xml Person.class
```

## Expected Output

Initiates XML parsing; may result in OutOfMemoryError if vulnerable.

## Related

- [[procedures/Execute-Java-Client-to-Parse-XML]]
- [[tools/Java-JDK]]
