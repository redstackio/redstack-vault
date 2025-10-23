---
id: 8b7a1a73-544f-472b-8fdf-9971ca598611
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:31.880390+00:00'
updated_at: '2023-04-06T03:56:31.891227+00:00'
---

# Code Snippet 8b7a1a73

**Language**: Python

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                        concurrentConnections=30,
                        requestsPerConnection=30,
                        pipeline=False
                        )

    # Queue multiple requests with different parameters
    for i in range(30):
        engine.queue(target.req, i)
        engine.queue(target.req, target.baseInput, gate='race1')

    # Start the engine and open gate for race condition
    engine.start(timeout=5)
    engine.openGate('race1')
    engine.complete(timeout=60)


def handleResponse(req, interesting):
    # Add request to table
    table.add(req)
```


