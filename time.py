
from boyfriend import send_message
from apscheduler.schedulers.blocking import BlockingScheduler



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_message, 'interval', seconds = 2)

sched.start()