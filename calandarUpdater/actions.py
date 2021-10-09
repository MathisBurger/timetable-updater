from datetime import datetime
from datetime import date
from datetime import timedelta
from datetime import time
import os
from calandarUpdater.initialize import InitializeCalendar


class CalendarActions:

    def __init__(self):
        self.service = InitializeCalendar().start()

    # This method fetches all events that happen at the
    # given time on the calculated day
    def fetch_all_events_at_time(self, start, end):
        day = self.get_day_to_use()
        startTime = (datetime.combine(day, time(hour=int(start[0]), minute=int(start[1])))).isoformat() + 'Z'
        endTime = (datetime.combine(day, time(hour=int(end[0]), minute=int(end[1])))).isoformat() + 'Z'
        return self.service.events().list(
            maxResults=10,
            timeMin=startTime,
            timeMax=endTime,
            calendarId=os.environ.get("CALENDAR_ID")
        ).execute().get('items', [])

    # This method updates a lesson with the given id
    def update_lesson(self, summary, room, eventId):
        self.service.events().patch(
            calendarId=os.environ.get("CALENDAR_ID"),
            body={
                "summary": summary,
                "location": room,
                "id": eventId
            },
            sendUpdates="all"
        ).execute()

    # This method checks what day is
    # the relevant day in the substitution plan
    def get_day_to_use(self):
        now = datetime.utcnow()
        if now.hour > 16:
            return date.today() + timedelta(days=1)
        else:
            return date.today()
