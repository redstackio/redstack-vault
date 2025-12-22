---
id: fdc59323-7c9e-4382-b741-1daee7de8068
name: jinja2-join-filter
type: command
executor: jinja2
data: '|join'
output: null
created_at: '2023-04-06T03:56:39.901743+00:00'
updated_at: '2023-04-10T20:23:43.898958+00:00'
platforms:
  - Web
tags:
  - jinja2
  - ssti
verified: true
validated: true
---

# jinja2-join-filter

## Command

```jinja2
|join
```

## Description

The join filter in Jinja2 concatenates elements of a list or tuple into a single string, using an optional delimiter (default empty). In SSTI exploits, it's used to build forbidden attribute names like '__class__' from parts to bypass filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| list/tuple | Iterable of strings to join (e.g., ["__", "class", "__"]) | Yes |
| delimiter | Optional separator (e.g., ',') | No |

## Examples

### Basic Usage

```jinja2
["a", "b"]|join  # Outputs: "ab"
```

### Advanced Usage

```jinja2
["__", "class", "__"]|join  # Outputs: "__class__"
["_"*2, "class", "_"*2]|join  # Dynamic build
```

## Expected Output

A single concatenated string from the input iterable. In SSTI: Successful construction of attribute names without filter triggers.

## Related

- [[procedures/Bypass-Jinja2-Filters-for-SSTI-Code-Execution]]
