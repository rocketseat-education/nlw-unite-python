from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events


class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            event = Events(
                id=eventsInfo.get("uuid"),
                title=eventsInfo.get("title"),
                details=eventsInfo.get("details"),
                slug=eventsInfo.get("slug"),
                maximum_attendees=eventsInfo.get("maximum_attendees"),
            )
            database.session.add(event)
            database.session.commit()

            return eventsInfo

    def get_eventy_by_id(self, event_id: str) -> Events:
        with db_connection_handler as database:
            event = (
                database.session
                .query(Events)
                .filter(Events.id == event_id)
                .one()
            )
            return event
