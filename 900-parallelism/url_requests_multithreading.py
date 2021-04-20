import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_req(url):
    try:
        begin_time = datetime.now()
        response = requests.get(url, verify=False, timeout=(2, 3))
        status_code = str(response.status_code)
        response_time = datetime.now() - begin_time
        if re.search(r"^2[0-9][0-9]$", status_code):
            state = 'up'
            status = 'success'

        if re.search(r"^4[0-9][0-9]$", status_code):
            state = 'down'
            status = 'Client error'

        if re.search(r"^5[0-9][0-9]$", status_code):
            state = 'down'
            status = 'Server error'


    except requests.ConnectionError as e:
        state = 'down'
        status = "Connection error"
        status_code = None
        response_time = timedelta(seconds=0)

    return [state, status, status_code, int(response_time.total_seconds()*1000)]



def runner():
    url_list = ['https://getbootstrap.com/',
                'https://data-flair.training/',
                'https://pypi.org/',
                'https://www.google.com/',
                'https://www.looklinux.com/',
                'https://www.kernel.org/',
                'https://www.ietf.org/',
                'https://www.icann.org/',
                'https://www.iana.org/',
                'https://www.isc.org/',
                'http://172.16.127.130/',
                'http://172.16.127.131/'
                ]
    threads = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for url in url_list:
            threads.append(executor.submit(get_req, url))

        for task in as_completed(threads):
            print(task.result())


if __name__ == "__main__":
    runner()