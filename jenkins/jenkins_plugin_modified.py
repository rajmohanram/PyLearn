#!/usr/bin/python
import sys
import zipfile
import urllib
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_plugin(name,version):
    pluginUrl = f"https://updates.jenkins-ci.org/download/plugins/{name}/{version}/{name}.hpi"
    print(f"downloading from {pluginUrl}")
    file = f"plugins/{name}.hpi"
    request.urlretrieve(pluginUrl, file)
    download_dependencies(file)


def download_dependencies(file):
    z = zipfile.ZipFile(file, "r")
    manifestPath = "META-INF/MANIFEST.MF"
    bytes = z.read(manifestPath)
    manifest_content = bytes.decode("utf-8")
    content_list = manifest_content.split()
    try:
        start = content_list.index('Plugin-Dependencies:') + 1
        end = content_list.index('Plugin-Developers:')
        dep_string = "".join(content_list[start:end])
        dependencies = dep_string.split(',')
        for dep in dependencies:
            print(dep)
            _dep = dep.rstrip(';resolution:=optional')
            _deps = _dep.split(":")
            print(_deps)
            name = _deps[0].strip()
            version = _deps[1].strip()
            download_plugin(name, version)
    except:
        pass



# download_plugin("junit","1.19")
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage sample: python download_jenkins_plugins.py junit 2.0.4")
        sys.exit(1)
    name = sys.argv[1]
    version = sys.argv[2]
    print(f"downloading plugin {name}")
    download_plugin(name, version)