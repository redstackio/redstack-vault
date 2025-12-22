---
tags:
  - django
  - setup
  - cache
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.678Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 990d020b-ee56-4090-944d-dfe0db6a91a2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Setup-Django-Project-with-DatabaseCache

## Summary

This procedure sets up a basic Django project configured with DatabaseCache backend using SQLite, enabling caching middleware to create exploitable pickled cache entries for deserialization attacks.

## Description

In a Django application, the DatabaseCache backend stores cache data in a database table using Python's pickle for serialization. By configuring middleware and creating a cache entry, an attacker can prepare the environment for payload injection. This targets django.core.cache.backends.db.DatabaseCache and requires access to the project's database file. Expected outcome is a populated cache table ready for manipulation, leading to RCE upon deserialization.

## Requirements

1. Python and Django installed (e.g., pip install django)
2. Local development environment for Django
3. Access to run Django management commands and start the server

## Defense

Defensive measures and detection strategies:

- Avoid using pickle-based backends in production; prefer JSON or signed serialization
- Restrict database access to prevent unauthorized modifications
- Monitor cache table for anomalous updates via database auditing

## Objectives

1. Establish a vulnerable caching setup in Django
2. Generate initial cache data for targeting
3. Prepare for payload injection without raising alerts

## Instructions

### Step 1: Create Django Project and App

**Context**: Initialize a new Django project and basic app to host a simple view.

Use Django's standard creation process:

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp myapp
```

> This creates the project structure and app. Add a simple view in myapp/views.py, e.g., def home(request): return HttpResponse('Hello').

### Step 2: Configure Caching in settings.py

**Context**: Enable DatabaseCache and middleware to handle caching.

Edit mysite/settings.py:

```python
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_KEY_PREFIX = ''
```

> Add the middleware for cache updates and fetches. Define the cache backend pointing to a table named 'my_cache_table'.

### Step 3: Create Cache Table and Run Server

**Context**: Migrate to create the cache table and populate it by accessing a page.

Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

Then visit http://127.0.0.1:8000/ in a browser to trigger caching.

> Migrations create the 'my_cache_table' with columns cache_key and value. Accessing the page stores pickled response data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- django
- cache-setup
