---
data: npx typeorm init --name Test --database mysql
tags:
  - setup
  - typeorm
type: command
output: 'Generates project files including ormconfig.json, entity folder, and index.ts'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.120Z'
id: da3824be-f025-47d3-b38b-64be7e412b45
verified: false
validated: true
submitted: true
---
# npx-typeorm-init

## Command

```bash
npx typeorm init --name Test --database mysql
```

## Description

Initializes a new TypeORM project with the specified name and database type, used to set up a local test environment for vulnerability reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--name` | Project name (e.g., 'Test') | Yes |
| `--database` | Database type (e.g., 'mysql') | Yes |

## Examples

### Basic Usage

```bash
npx typeorm init --name Test --database mysql
```

### Advanced Usage

```bash
npx typeorm init --name MyProject --database mysql --dataSource src/data-source.ts
```

## Expected Output

Console messages indicating file generation, e.g., "TypeORM project has been created successfully." Project directory created with config and sample files.

## Related

- [[Related Procedure: Initialize-TypeORM-Project]]
