import pytest

from persistent_scheduler import PersistentScheduler


@pytest.fixture
def scheduler(celery_app):
    celery_app.conf['persistent_scheduler_redis_url'] = (
        'redis://localhost:6379/'
    )
    return PersistentScheduler(app=celery_app)


def test_setup_schedule_when_persistence_already_setup(scheduler):
    scheduler.persistence = {
        'entries': {}, '__version__': '4.1.0', 'tz': 'UTC', 'utc_enabled': True
    }

    scheduler.setup_schedule()

    expected_data = {
        'entries': {}, '__version__': '4.1.0', 'tz': 'UTC', 'utc_enabled': True
    }
    assert scheduler.persistence == expected_data


def test_setup_schedule_when_persistence_missing_utc_enabled(scheduler):
    scheduler.persistence = {
        'entries': {}, '__version__': '4.1.0', 'tz': 'UTC',
    }

    scheduler.setup_schedule()

    expected_data = {
        'entries': {}, '__version__': '4.1.0', 'tz': 'UTC', 'utc_enabled': True
    }
    assert scheduler.persistence == expected_data


def test_setup_schedule_when_persistence_missing_tz(scheduler):
    scheduler.persistence = {
        'entries': {}, '__version__': '4.1.0', 'utc_enabled': True
    }

    scheduler.setup_schedule()

    expected_data = {
        'entries': {}, '__version__': '4.1.0', 'tz': 'UTC', 'utc_enabled': True
    }
    assert scheduler.persistence == expected_data


def test_setup_schedule_when_persistence_missing_version(scheduler):
    scheduler.persistence = {
        'entries': {}, 'tz': 'UTC', 'utc_enabled': True
    }

    scheduler.setup_schedule()

    expected_data = {
        'entries': {}, '__version__': '4.1.0', 'tz': 'UTC', 'utc_enabled': True
    }
    assert scheduler.persistence == expected_data


def test_setup_schedule_when_persistence_is_empty(scheduler):
    scheduler.persistence.clear()

    scheduler.setup_schedule()

    expected_data = {
        'entries': {}, '__version__': '4.1.0', 'tz': 'UTC', 'utc_enabled': True
    }
    assert scheduler.persistence == expected_data


def test_set_and_get_schedule(scheduler):
    assert scheduler.get_schedule() == {}

    entries = {'foo': 'barr'}

    scheduler.set_schedule(schedule=entries)
    assert scheduler.get_schedule() == entries

    scheduler.schedule = entries
    assert scheduler.get_schedule() == entries


def test_info(scheduler):
    assert scheduler.info == ''
