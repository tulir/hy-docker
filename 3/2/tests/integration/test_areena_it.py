# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, unicode_literals
import os
import pytest
from utils import fetch_title, fetch_stream_url, fetch_episode_pages, \
    fetch_metadata


def test_areena_akamai_hds_title():
    title = fetch_title('https://areena.yle.fi/1-1418526')

    assert len(title) == 1
    assert 'The Deputy Mayor' in title[0]


def test_areena_akamai_hds_stream_url():
    streamurl = fetch_stream_url('https://areena.yle.fi/1-1418526')

    assert len(streamurl) == 1
    assert 'manifest.f4m' in streamurl[0]


def test_areena_akamai_hds_metadata():
    metadata = fetch_metadata('https://areena.yle.fi/1-1418526')

    assert len(metadata) == 1
    flavors = metadata[0]['flavors']
    assert len(flavors) == 1
    assert all(f.get('media_type') == 'video' for f in flavors)
    assert all('bitrate' in f and
               'height' in f and
               'width' in f
               for f in flavors)
    assert metadata[0]['duration_seconds'] == 1601
    assert metadata[0]['region'] == 'World'
    assert metadata[0]['publish_timestamp'] == '2012-01-19T12:00:00+02:00'
    assert 'expired_timestamp' not in metadata[0]
    assert len(metadata[0]['subtitles']) == 0


def test_areena_html5_stream_url():
    streamurl = fetch_stream_url('https://areena.yle.fi/1-403848')

    assert len(streamurl) == 1
    assert '/a.mp4?' in streamurl[0]


def test_areena_html5_metadata():
    metadata = fetch_metadata('https://areena.yle.fi/1-403848')

    assert len(metadata) == 1
    flavors = metadata[0]['flavors']
    assert len(flavors) == 2
    assert all(f.get('media_type') == 'video' for f in flavors)
    assert all('bitrate' in f and
               'height' in f and
               'width' in f
               for f in flavors)
    assert metadata[0]['duration_seconds'] == 3196
    assert metadata[0]['region'] == 'World'
    assert metadata[0]['publish_timestamp'] == '2017-07-16T14:00:00+03:00'
    assert 'expired_timestamp' not in metadata[0]
    assert len(metadata[0]['subtitles']) == 1


@pytest.mark.skipif(os.getenv('ENABLE_FINLAND_TESTS') != '1',
                    reason="Test works only in Finland")
def test_areena_iphone_stream_url():
    streamurl = fetch_stream_url('https://areena.yle.fi/1-4247408')

    assert len(streamurl) == 1
    assert '/a.m3u8?' in streamurl[0]


@pytest.mark.skipif(os.getenv('ENABLE_FINLAND_TESTS') != '1',
                    reason="Test works only in Finland")
def test_areena_iphone_metadata():
    metadata = fetch_metadata('https://areena.yle.fi/1-4247408')

    assert len(metadata) == 1
    flavors = metadata[0]['flavors']
    assert len(flavors) == 1
    assert all(f.get('media_type') == 'video' for f in flavors)
    assert all('bitrate' in f and
               'height' in f and
               'width' in f
               for f in flavors)
    assert metadata[0]['duration_seconds'] == 234
    assert metadata[0]['region'] == 'Finland'
    assert metadata[0]['publish_timestamp'] == '2017-11-08T01:15:00+02:00'


def test_areena_series_titles():
    titles = fetch_title('https://areena.yle.fi/1-3826480')

    assert len(titles) == 10
    assert all(['Suomi on ruotsalainen' in t for t in titles])


def test_areena_series_urls():
    urls = fetch_stream_url('https://areena.yle.fi/1-3826480')

    assert len(urls) == 10
    assert all(['a.mp4' in url for url in urls])


@pytest.mark.skipif(os.getenv('ENABLE_FINLAND_TESTS') != '1',
                    reason="Test works only in Finland")
def test_areena_live_url():
    streamurl = fetch_stream_url('https://areena.yle.fi/tv/suorat/yle-tv1')

    assert len(streamurl) == 1
    assert '.f4m' in streamurl[0]


@pytest.mark.skipif(os.getenv('ENABLE_FINLAND_TESTS') != '1',
                    reason="Test works only in Finland")
def test_areena_live_metadata():
    metadata = fetch_metadata('https://areena.yle.fi/tv/suorat/yle-tv1')

    assert len(metadata) == 1
    assert len(metadata[0]['flavors']) >= 1
    assert all(f.get('media_type') == 'video' for f in metadata[0]['flavors'])
    assert metadata[0]['region'] == 'Finland'


@pytest.mark.skipif(os.getenv('ENABLE_FINLAND_TESTS') != '1',
                    reason="Test works only in Finland")
def test_areena_ohjelmat_embedded_live_url():
    streamurl = fetch_stream_url('https://areena.yle.fi/tv/ohjelmat/30-595?play=yle-tv2')

    assert len(streamurl) == 1
    assert 'master.m3u8' in streamurl[0]


@pytest.mark.skipif(os.getenv('ENABLE_FINLAND_TESTS') != '1',
                    reason="Test works only in Finland")
def test_areena_ohjelmat_embedded_live_metadata():
    metadata = fetch_metadata('https://areena.yle.fi/tv/ohjelmat/30-595?play=yle-tv2')

    assert len(metadata) == 1
    assert len(metadata[0]['flavors']) >= 1
    assert all(f.get('media_type') == 'video' for f in metadata[0]['flavors'])
    assert metadata[0]['region'] == 'Finland'


def test_areena_html5_clip_title():
    title = fetch_title('https://areena.yle.fi/1-3523087')

    assert len(title) == 1
    assert 'Metsien kätkemä' in title[0]


def test_areena_html5_clip_stream_url():
    streamurl = fetch_stream_url('https://areena.yle.fi/1-3523087')

    assert len(streamurl) == 1
    assert '/a.mp4?' in streamurl[0]


def test_areena_episode_pages():
    episodes = fetch_episode_pages('https://areena.yle.fi/1-3148871')

    # The first page contains 12 episodes, make sure we get several pages
    assert len(episodes) > 20
