"""Tests_for_app_module."""

from unittest import mock

import pytest
from pytest_mock import MockerFixture

from src.app import generate_hash, run_clone, start


@pytest.fixture(name="open_mock")
def open_fixture(mocker: MockerFixture) -> mock.MagicMock:
    """Open fixture.

    Args:
        mocker: open_mocker

    # noqa: DAR201

    """
    open_mock = mock.MagicMock()
    mocker.patch("src.app.open", open_mock)
    return open_mock


@pytest.fixture(name="isfile_mock")
def isfile_fixture(mocker: MockerFixture) -> mock.MagicMock:
    """Isfile fixture.

    Args:
        mocker: isfile_mocker

    # noqa: DAR201

    """
    isfile_mock = mock.MagicMock(return_value=False)
    mocker.patch("src.app.isfile", isfile_mock)
    return isfile_mock


@pytest.mark.asyncio
async def test_run_clone_success(mocker: MockerFixture):
    """Test run clone success.

    Args:
        mocker: MockerFixture

    """
    repo_clone_from_mock = mock.MagicMock()
    mocker.patch("src.app.Repo.clone_from", repo_clone_from_mock)
    test_path_to_repo = "test_path_to_repo"
    test_dir_temp = "test_dir_temp"
    await run_clone(test_path_to_repo, test_dir_temp)

    repo_clone_from_mock.assert_called_once_with(
        test_path_to_repo,
        test_dir_temp,
    )


def test_generate_hash_success_recursion(
    mocker: MockerFixture,
    isfile_mock: mock.MagicMock,
):
    """Test generate hash success recursion.

    Args:
        mocker: MockerFixture,
        isfile_mock: MagicMock

    """
    name = "test_dir"
    listdir_mock = mock.MagicMock(return_value=[name])
    mocker.patch("src.app.listdir", listdir_mock)

    with mock.patch("src.app.generate_hash") as mock_generate_hash:
        test_path = "test_dir_name"
        generate_hash(test_path)
        isfile_mock.assert_called_once()
        listdir_mock.assert_called_once_with("test_dir_name")
        mock_generate_hash.assert_called_once_with(
            dir_temp=f"{test_path}/{name}",)


def test_get_hash_success_generate_hash(
    mocker: MockerFixture,
    isfile_mock: mock.MagicMock,
    open_mock: mock.MagicMock,
):
    """Test get hash success generate hash.

    Args:
        mocker: MockerFixture,
        isfile_mock: MagicMock,
        open_mock: mock.MagicMock,

    """
    isfile_mock.return_value = True
    print_mock = mock.MagicMock()
    mocker.patch("src.app.print", print_mock)

    hashlib_mock = mock.MagicMock()
    mocker.patch("src.app.hashlib", hashlib_mock)

    test_file = "test_file"
    generate_hash(test_file)
    isfile_mock.assert_called_once()
    open_mock.assert_called_once()


@pytest.mark.asyncio
async def test_start_success(
    mocker: MockerFixture,
    open_mock: mock.MagicMock,
):
    """Test start success.

    Args:
        mocker: MockerFixture,
        open_mock: mock.MagicMock,

    """
    generate_hash_mock = mock.MagicMock()
    mocker.patch("src.app.generate_hash", generate_hash_mock)
    temporary_directory_mock = mock.MagicMock()
    mocker.patch("src.app.tempfile.TemporaryDirectory", temporary_directory_mock)
    asyncio_gather_mock = mock.AsyncMock()
    mocker.patch("src.app.asyncio.gather", asyncio_gather_mock)
    json_mock = mock.MagicMock()
    mocker.patch("src.app.json", json_mock)

    await start()
    temporary_directory_mock.assert_called_once()
    asyncio_gather_mock.assert_awaited_once()
    generate_hash_mock.assert_called_once()
    open_mock.assert_called_once()


if __name__ == '__main__':
    pytest.main()
