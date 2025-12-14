---
id: cmd-789652-check-reflection
data: 'curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=1" -s | grep -i pt'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.881Z'
verified: false
validated: true
submitted: true
---
# curl-check-reflection

## Command

```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=1" -s | grep -i pt
```

## Description

This command uses curl to fetch the Topcoder ReviewBoard page with a benign 'pt' value and greps for reflections, helping identify if the parameter is unsanitized in the HTML response. Use it during initial vulnerability reconnaissance for XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target endpoint with pt parameter | Yes |
| -s | Silent mode to suppress progress meter | No |
| grep -i pt | Case-insensitive search for 'pt' reflections | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=1" -s | grep -i pt
```

### Advanced Usage

```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=1" -s -H "User-Agent: Mozilla/5.0" | grep -i pt=1
```

## Expected Output

Lines from HTML showing reflected 'pt=1', e.g., '<param name="pt" value="1">' or similar unescaped text, indicating potential XSS.

## Related

- [[Related Procedure: Observe-pt-Parameter-Reflection]]
