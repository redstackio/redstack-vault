---
type: code
language: cs
verified: true
tags:
  - .net
  - pop-gadget
  - serialization
platforms:
  - Windows
  - .NET
validated: true
---

# Create-ExpandedWrapper-Instance

## Code

```cs
ExpandedWrapper<Process, ObjectDataProvider> myExpWrap = new ExpandedWrapper<Process, ObjectDataProvider>();
```

## Description

This C# code snippet instantiates an ExpandedWrapper class, a key component in .NET POP gadget chains for deserialization exploits. It wraps Process and ObjectDataProvider types to facilitate property chaining that leads to arbitrary code execution during deserialization.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Process | Target type for execution context (e.g., spawning processes) | N/A |
| ObjectDataProvider | Type for dynamic object invocation and property setting | N/A |

## Usage

Embed this instantiation within a larger serialized object graph, often generated with tools like ysoserial.net. Deliver via vulnerable endpoints (e.g., web forms accepting serialized data). Used in red team exercises to simulate RCE via deserialization in .NET applications.

## Detection

- Monitor .NET deserialization logs for instantiation of suspicious types like ExpandedWrapper.
- Enable ETW tracing for .NET runtime to capture gadget chain formations.
- Signature-based detection on serialized payloads containing these class names.

## Related

- [[procedures/Exploit-DotNET-Serialization-with-POP-Gadgets]]
