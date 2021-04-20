# http://jsonplaceholder.typicode.com/todos/1
import requests
from datetime import datetime





def get_todos(todo_id):
    url = f"http://jsonplaceholder.typicode.com/todos/{todo_id}"
    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json()
        print(data['id'], data['title'])


if __name__ == '__main__':
    start_time = datetime.now()

    for i in range(1,201):
        get_todos(i)

    end_time = datetime.now()
    diff_time = end_time - start_time
    diff_time_in_minutes = divmod(diff_time.total_seconds(), 60)
    print(f'\n{diff_time_in_minutes}')


# It took 42 seconds to complete without multiprocessing