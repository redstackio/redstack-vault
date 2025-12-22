---
id: cmd-uuid-1
data: 'www.███/News/Speeches?Search={{7*7}}'
name: test-template-injection-math
tags:
  - csti-test
type: command
output: Page renders 49 from the evaluation
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.258Z'
verified: false
validated: true
submitted: true
---
# test-template-injection-math

## Command

```bash
# Browser URL: www.███/News/Speeches?Search={{7*7}}
```

## Description

This command tests for Client Side Template Injection by supplying a mathematical expression in the Search parameter, which the template engine evaluates if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Search | Template expression like {{7*7}} | Yes |

## Examples

### Basic Usage

```bash
www.███/News/Speeches?Search={{7*7}}
```

### Advanced Usage

Test other expressions like {{1+1}} for confirmation.

```bash
www.███/News/Speeches?Search={{1+1}}
```

## Expected Output

The page content includes the evaluated result "49", embedded in search results or UI elements.

## Related

- [[Related Procedure: Test-for-Template-Injection-with-Math]]
