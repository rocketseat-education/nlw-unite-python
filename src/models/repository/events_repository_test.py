import pytest

from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Novo Registro no banco de dados")
def test_insert_event():
    event = {
        "uuid": "meu-uuid-e-nois2",
        "title": "meu title",
        "slug": "meu-slug-aqui!2",
        "maximum_attendees": 20,
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)


@pytest.mark.skip(reason="Não precisa")
def test_get_event_by_id():
    event_id = "meu-uuid-e-nois2"
    events_repository = EventsRepository()
    response = events_repository.get_eventy_by_id(event_id)
    print(response)
    print(response.title)
