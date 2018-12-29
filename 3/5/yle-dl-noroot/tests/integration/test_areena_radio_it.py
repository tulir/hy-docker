# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, unicode_literals
from utils import fetch_title, fetch_stream_url, fetch_metadata
from yledl import StreamFilters


def test_radio_title():
    title = fetch_title('https://areena.yle.fi/1-3361013')

    assert len(title) == 1
    assert title[0].startswith(
        'Tiedeykkönen: '
        'Suorat aurinkobiopolttoaineet mullistavat energiantuotannon')


def test_radio_title_hls():
    title = fetch_title('https://areena.yle.fi/1-4551633')

    assert len(title) == 1
    assert title[0].startswith(
        'Ilmastonmuutos: Ihminen elää ilman vettä vain muutaman päivän')


def test_radio_stream_url_rtmp():
    url = fetch_stream_url('https://areena.yle.fi/1-3361013')

    assert len(url) == 1
    assert 'rtmp' in url[0]


def test_radio_stream_url_hls():
    url = fetch_stream_url('https://areena.yle.fi/1-4551633')

    assert len(url) == 1
    assert 'a.mp3' in url[0]


def test_radio_stream_url_media_url():
    # The default stream is RTMP. This test is about the secondary
    # "media_url" stream. Therefore the rtmpdump backend is disabled.
    filters = StreamFilters(enabled_backends=['wget', 'ffmpeg'])
    url = fetch_stream_url('https://areena.yle.fi/1-4561516', filters)

    assert len(url) == 1
    assert '.mp3?primaryToken=' in url[0]


def test_radio_metadata_rtmp():
    metadata = fetch_metadata('https://areena.yle.fi/1-3361013')

    assert len(metadata) == 1
    assert len(metadata[0]['flavors']) == 2
    assert all(f.get('media_type') == 'audio' for f in metadata[0]['flavors'])
    assert metadata[0]['duration_seconds'] == 2884


def test_radio_metadata_hls():
    metadata = fetch_metadata('https://areena.yle.fi/1-4551633')

    assert len(metadata) == 1
    assert len(metadata[0]['flavors']) == 1
    assert metadata[0]['flavors'][0]['media_type'] == 'audio'
    assert metadata[0]['duration_seconds'] == 2954


def test_radio_live_url():
    url = fetch_stream_url('https://areena.yle.fi/radio/ohjelmat/yle-puhe')

    assert len(url) == 1
    assert '.m3u8' in url[0]


def test_radio_live_url2():
    url = fetch_stream_url('https://areena.yle.fi/radio/ohjelmat/'
                           'yle-radio-suomi?_c=yle-radio-suomi-oulu')

    assert len(url) == 1
    assert '.m3u8' in url[0]

def test_radio_live_metadata():
    metadata = fetch_metadata('https://areena.yle.fi/radio/ohjelmat/yle-puhe')

    assert len(metadata) == 1
    assert len(metadata[0]['flavors']) >= 1
    assert all(f.get('media_type') == 'audio' for f in metadata[0]['flavors'])
    assert metadata[0]['title'].startswith('Yle Puhe')
