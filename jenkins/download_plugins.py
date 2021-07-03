import requests
from multiprocessing import Pool


def download_plugin(plugin):
    download_url = "http://updates.jenkins-ci.org/latest/%s.hpi" % (plugin)
    r = requests.get(download_url, stream = True)
    with open(plugin +".hpi","wb") as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)


if __name__ == '__main__':
    plugins = ["token-micro"]
    # 4 Threads in parallel
    pool = Pool(processes=4)
    pool.map(download_plugin, plugins)
