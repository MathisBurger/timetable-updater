from dataFetcher.dataFetcher import DataFetcher
from dotenv import load_dotenv
from calandarUpdater import actions
from lesson_translator import get_time_by_lesson
from lesson_ignore import check_is_ignored
from name_translator import translate_name

load_dotenv()

fetcher = DataFetcher()
subs = fetcher.get_substitutions()
actions = actions.CalendarActions()
for sub in subs:
    time = get_time_by_lesson(sub[1])
    if not check_is_ignored(sub[2]):
        lesson = actions.fetch_all_events_at_time(startTime=time[0], endTime=time[1])[0]
        actions.update_lesson(
            summary=translate_name(str(sub[2]).replace(' ', '')),
            room=str(sub[4]).replace(' ', ''),
            eventId=lesson['id']
        )
        print(f"Updated event with id {lesson['id']}")
