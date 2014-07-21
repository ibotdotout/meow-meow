#!/usr/bin/env python
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def when_file_changed(filename):
    def top_package():
        return os.path.abspath(".").rsplit("/", 1)[1].replace("-", "_")

    def package(filename):
        basename = os.path.basename(filename)
        if not basename.startswith("test_"):
            package = filename.replace("./", "").replace(".py", "")
        else:
            package = filename.replace("./tests/unit", "").replace(".py", "")
            package = top_package() + package.replace("/test_", "/")
        package = package.replace("/", ".")
        return package

    def test_file(filename):
        basename = os.path.basename(filename)
        if not basename.startswith("test_"):
            filename = filename.replace(top_package(), "tests/unit")
            filename = filename.replace(basename, "test_" + basename)
        return filename

    cls()
    print(os.path.abspath(filename))
    args = {"package": package(filename), "testfile": test_file(filename)}
    cmd = "nosetests --with-coverage --cover-erase --cover-package={package}" \
          " -v {testfile}".format(**args)
    os.system(cmd)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class ModifiedHandler(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def on_created(self, event):
        when_file_changed(event.src_path)

    def on_any_event(self, event):
        pass

    def on_modified(self, event):
        pass

if __name__ == '__main__':
    args = sys.argv[1:]
    event_handler = ModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler,
                      path=args[1] if args else '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
