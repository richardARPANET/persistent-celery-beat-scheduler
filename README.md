# persistent-celery-beat-scheduler

[![PyPI](https://img.shields.io/pypi/v/persistent-celery-beat-scheduler.svg)](https://pypi.python.org/pypi/persistent-celery-beat-scheduler)
[![Python Versions](https://img.shields.io/pypi/pyversions/persistent-celery-beat-scheduler.svg)](https://pypi.python.org/pypi/persistent-celery-beat-scheduler)
[![Build Status](https://travis-ci.org/richardasaurus/persistent-celery-beat-scheduler.png?branch=master)](https://travis-ci.org/richardasaurus/persistent-celery-beat-scheduler)

![Logo](https://i.imgur.com/ychEU7k.png)

Celery Beat Scheduler that stores the scheduled tasks and runtime data in Redis.

## Installation


```bash
pip install persistent-celery-beat-scheduler
```

## Configuration

In your celery configuration file you need to set the following.

```python
persistent_scheduler_redis_url = 'redis://localhost:6379/'

# Optional: specify name for HSET key in Redis where scheduler data will be stored.
# Defaults to `celery-beat-scheduler` if not specified.
persistent_scheduler_key = 'myapp-celery-beat-scheduler'
```

## Usage

```bash
celery -A my_project.app.celery beat -S persistent_scheduler.PersistentScheduler
```
