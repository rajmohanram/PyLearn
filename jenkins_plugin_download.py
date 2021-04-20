#!/usr/bin/python
import sys
import zipfile
import urllib
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_plugin(name,version):
    pluginUrl = "http://updates.jenkins-ci.org/download/plugins/%s/%s/%s.hpi" % (name,version,name)
    print(f"downloading: {pluginUrl}")
    file = "%s.hpi" % name
    # request.urlretrieve(pluginUrl, file)
    download_dependencies(file)

def download_dependencies(file):
    z = zipfile.ZipFile(file, "r")
    manifestPath = "META-INF/MANIFEST.MF"
    bytes = z.read(manifestPath)
    dependencies = [x for x in bytes.decode("utf-8").split("\n") if "Dependencies" in x]
    for dep in dependencies:
        _dep = dep.strip()
        _deps = _dep.split(":")
        print(_deps)
        name = _deps[1].strip()
        version = _deps[2].strip()
        # download_plugin(name,version)
        print(name,version)


# download_plugin("junit","1.19")
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage sample: python download_jenkins_plugins.py junit 1.19")
        sys.exit(1)
    name = sys.argv[1]
    version = sys.argv[2]
    print(f"download {name},{version}")
    download_plugin(name,version)