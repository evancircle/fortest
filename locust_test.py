from locust import HttpLocust,TaskSet,task
import json

def postdata(self):
    self.client.post("/dlo/report_data",{"no":"BLtotest","type":"getuuid"})


class UserBehavior(TaskSet):
    tasks = {postdata:1}

    def on_start(self):
        postdata(self)

class WebUserLocust(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000

#if __name__ == '__main__':
#    subprocess.Popen('locust -f .\locust_test.py --host=http://api.epoque.cn', shell=True)
