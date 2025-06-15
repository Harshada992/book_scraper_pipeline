from apscheduler.schedulers.blocking import BlockingScheduler
from crew_runner import books, transform_and_save

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', hour=9, minute=0)
def scheduled_job():
    print("Running scheduled job...")
    transform_and_save(books)

scheduler.start()
