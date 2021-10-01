from datetime import datetime
from datetime import date
from datetime import timedelta
import os

from calandarUpdater.initialize import InitializeCalendar

class CalendarActions:

    def __init__(self):
        self.service = InitializeCalendar().start()

    def fetch_all_events_at_time(self, startTime, endTime):
        day = self.get_day_to_use()
        startTime = day.isoformat() + "T" + startTime + ":00Z"
        endTime = day.isoformat() + "T" + endTime + ":00Z"
        return self.service.events().list(
            timeMin=startTime,
            timeMax=endTime,
            calendarId=os.environ.get("CALENDAR_ID")
        ).execute().get('items', [])

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


    def get_day_to_use(self):
        now = datetime.now()
        if now.hour > 16:
            return date.today() + timedelta(days=1)
        else:
            return date.today()