from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.check_ins import CheckIns
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError

class AttendeesRepository:
    def insert_attendee(self, attendde_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                attendee = (
                    Attendees(
                        id=attendde_info.get("uuid"),
                        name=attendde_info.get("name"),
                        email=attendde_info.get("email"),
                        event_id=attendde_info.get("event_id")
                    )
                )
                database.session.add(attendee)
                database.session.commit()

                return attendde_info
            except IntegrityError:
                raise HttpConflictError('Participante ja cadastrado!')
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_attendee_badge_by_id(self, attendee_id: str):
        with db_connection_handler as database:
            try:
                attendee = (
                    database.session
                        .query(Attendees)
                        .join(Events, Events.id == Attendees.event_id)
                        .filter(Attendees.id==attendee_id)
                        .with_entities(
                            Attendees.name,
                            Attendees.email,
                            Events.title
                        )
                        .one()
                )
                return attendee
            except NoResultFound:
                return None

    def get_attendees_by_event_id(self, event_id: str) -> List[Attendees]:
        with db_connection_handler as database:
            attendees = (
                database.session
                    .query(Attendees)
                    .outerjoin(CheckIns, CheckIns.attendeeId==Attendees.id)
                    .filter(Attendees.event_id==event_id)
                    .with_entities(
                        Attendees.id,
                        Attendees.name,
                        Attendees.email,
                        CheckIns.created_at.label('checkedInAt'),
                        Attendees.created_at.label('createdAt')
                    )
                    .all()
            )
            return attendees