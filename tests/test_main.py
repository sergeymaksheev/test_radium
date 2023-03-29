"""Tests_for_main_module"""
from unittest import mock
import pytest
from pytest_mock import MockerFixture
from unittest.mock import MagicMock, AsyncMock
from main import get_clone, get_hash


@pytest.fixture(name="isfile_mock")
def isfile_fixture(mocker: MockerFixture) -> MagicMock:
    """Isfile fixture"""
    isfile_mock = MagicMock(return_value=False)
    mocker.patch('main.isfile', isfile_mock)
    return isfile_mock


@pytest.mark.asyncio
async def test_get_clone_success(mocker: MockerFixture):
    """Success."""
    repo_clone_from_mock = MagicMock()
    mocker.patch('main.Repo.clone_from', repo_clone_from_mock)
    get_hash_mock = MagicMock()
    mocker.patch('main.get_hash', get_hash_mock)
    
    await get_clone()
    
    repo_clone_from_mock.assert_called_once()
    get_hash_mock.assert_called_once()


def test_get_hash_success_recursion(mocker: MockerFixture,
                                    isfile_mock: MagicMock):
    """Success recursion"""
    name = 'test_dir'
    listdir_mock = MagicMock(return_value=[name])
    mocker.patch('main.listdir', listdir_mock)

    with mock.patch('main.get_hash') as mock_get_hash:
        test_path = 'test_dir_name'
        get_hash(test_path)
        isfile_mock.assert_called_once()
        listdir_mock.assert_called_once_with('test_dir_name')
        assert mock_get_hash.called
        assert mock_get_hash.call_count == 1
        mock_get_hash.assert_called_once_with(dir_temp=f"{test_path}/{name}")


def test_get_hash_success_print_hash(mocker: MockerFixture,
                                     isfile_mock: MagicMock):
    """Success print hash"""
    open_mock = MagicMock()
    open_mock.__enter__ = MagicMock(return_value='test')
    
    mocker.patch('main.open', open_mock)
    isfile_mock.return_value = True
    print_mock = MagicMock()
    mocker.patch('main.print', print_mock)

    hashlib_mock = MagicMock()
    mocker.patch('main.hashlib', hashlib_mock)

    test_file = 'test_file'
    get_hash(test_file)
    isfile_mock.assert_called_once()
    open_mock.assert_called_once()
    print_mock.assert_called_once()

