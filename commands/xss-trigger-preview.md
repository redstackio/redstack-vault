---
data: '// Triggered by payload on preview: alert(1) or custom JS'
tags:
  - xss
type: command
output: JS execution
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.129Z'
id: 02282df4-d65f-4967-96ea-4645efdcc3f3
verified: false
validated: true
submitted: true
---
# xss-trigger-preview

## Command

```javascript
// Triggered by payload on preview: alert(1) or custom JS
```

## Description

JavaScript executed when victim previews the malicious template, firing from the onload attribute after parsing.

## Parameters

None.

## Examples

### Basic Usage

```javascript
alert(1); // Proof of execution
```

### Advanced Usage

Load scripts or exfil data.

## Expected Output

Arbitrary JS runs in domain context.

## Related

- [[commands/xss-payload-injection]]
