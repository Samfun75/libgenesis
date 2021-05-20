from libgenesis import Libgen
from pathlib import Path
import pytest


class Testclass:
    """Testing of Libgen object, searching, result types, and download of the books."""
    @staticmethod
    def test_Libgen():
        # creat a Libgen object with return result limit set to 50
        lg = Libgen(sort="title", sort_mode="ASC", result_limit=50)
        assert isinstance(lg, Libgen)

    @staticmethod
    @pytest.mark.asyncio
    async def test_search():
        lg = Libgen()
        # search Libgen
        result = await lg.search('japan history')
        assert isinstance(result, dict)

    @staticmethod
    @pytest.mark.asyncio
    async def test_result():
        lg = Libgen()
        result = await lg.search('japan history')
        # check first result
        ids = [*result]
        assert isinstance(result[ids[0]], dict)

    @staticmethod
    @pytest.mark.asyncio
    async def test_download():
        lg = Libgen()
        result = await lg.search('japan history')
        ids = [*result]
        # download the first result and print the path
        file = await lg.download(result[ids[0]]['mirrors']['main'], dest_folder=Path("download_test"))
        assert Path.is_file(file)
