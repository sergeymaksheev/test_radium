"""Tests_for_app_module."""

from unittest import mock

import pytest
from pytest_mock import MockerFixture

from app import generate_hash, run_clone


@pytest.fixture(name="isfile_mock")
def isfile_fixture(mocker: MockerFixture) -> mock.MagicMock:
    """Isfile fixture.

    Args:
        mocker: isfile_mocker

    # noqa: DAR201

    """
    isfile_mock = mock.MagicMock(return_value=False)
    mocker.patch("app.isfile", isfile_mock)
    return isfile_mock


@pytest.mark.asyncio
async def test_run_clone_success(mocker: MockerFixture):
    """Test run clone success.

    Args:
        mocker: MockerFixture

    """
    repo_clone_from_mock = mock.MagicMock()
    mocker.patch("app.Repo.clone_from", repo_clone_from_mock)
    generate_hash_mock = mock.MagicMock()
    mocker.patch("app.generate_hash", generate_hash_mock)
    test_path_to_repo = "test"
    await run_clone(test_path_to_repo)

    repo_clone_from_mock.assert_called_once()
    generate_hash_mock.assert_called_once()


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
    mocker.patch("app.listdir", listdir_mock)

    with mock.patch("app.generate_hash") as mock_generate_hash:
        test_path = "test_dir_name"
        generate_hash(test_path)
        isfile_mock.assert_called_once()
        listdir_mock.assert_called_once_with("test_dir_name")
        mock_generate_hash.assert_called_once_with(
            dir_temp="{test_path}/{name}".format(
                test_path=test_path,
                name=name,
            ),
        )


def test_get_hash_success_generate_hash(
    mocker: MockerFixture,
    isfile_mock: mock.MagicMock,
):
    """Test get hash success generate hash.

    Args:
        mocker: MockerFixture,
        isfile_mock: MagicMock

    """
    open_mock = mock.MagicMock()
    mocker.patch("app.open", open_mock)
    isfile_mock.return_value = True
    print_mock = mock.MagicMock()
    mocker.patch("app.print", print_mock)

    hashlib_mock = mock.MagicMock()
    mocker.patch("app.hashlib", hashlib_mock)

    test_file = "test_file"
    generate_hash(test_file)
    isfile_mock.assert_called_once()
    open_mock.assert_called_once()
