import pytest

from hacker_news_subs import SubmissionDownloader


@pytest.fixture
def sub_downloader():
    return SubmissionDownloader(3)


def test_sub_downloader(sub_downloader):
    subs = sub_downloader.fetch()
    assert len(subs) == sub_downloader.max_num_subs
    for sub in subs:
        assert 'title' in sub and 'num_comments' in sub and 'url' in sub
