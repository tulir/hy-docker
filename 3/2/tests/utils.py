from __future__ import print_function, absolute_import, unicode_literals
import sys
import json
from io import BytesIO
from yledl import download, StreamFilters, IOContext, \
    DownloadLimits, StreamAction, RD_SUCCESS
from yledl.http import HttpClient


# Context manager for capturing stdout output. See
# https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._bytesio = BytesIO()
        return self

    def __exit__(self, *args):
        self.extend(self._bytesio.getvalue().decode('UTF-8').splitlines())
        del self._bytesio    # free up some memory
        sys.stdout = self._stdout


def fetch_title(url, filters=StreamFilters()):
    return fetch(url, StreamAction.PRINT_STREAM_TITLE, filters)


def fetch_stream_url(url, filters=StreamFilters()):
    return fetch(url, StreamAction.PRINT_STREAM_URL, filters)


def fetch_episode_pages(url, filters=StreamFilters()):
    return fetch(url, StreamAction.PRINT_EPISODE_PAGES, filters)


def fetch_metadata(url, filters=StreamFilters()):
    return json.loads('\n'.join(
        fetch(url, StreamAction.PRINT_METADATA, filters)))


def fetch(url, action, filters):
    # Initialize rtmpdump_binary to avoid a file system lookup in tests
    io = IOContext(destdir='/tmp/', rtmpdump_binary='rtmpdump')
    httpclient = HttpClient()

    with Capturing() as output:
        res = download(url,
                       action,
                       io,
                       httpclient,
                       stream_filters = filters,
                       postprocess_command = None)
        assert res == RD_SUCCESS

    return output
