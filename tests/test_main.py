"""Tests_for_main_module"""
import responses
import pytest
from datetime import datetime


# @responses.activate
# def test_start():
#     valid_json_answer = {
#         "lastActionTime": 1626615588,
#         "timeDiff": 16984
#     }
#     responses.add(responses.GET, "https://www.avito.ru/web/user/get-status/177868588",
#                   json=valid_json_answer, status=200)
#     some_resource_client = SomeResourceClient("https://www.avito.ru")
#     res = some_resource_client.get_user_last_action_time(177868588)
#     assert res == datetime.fromtimestamp(valid_json_answer.get("lastActionTime") - valid_json_answer.get("timeDiff"))

# def test_get_clone():
#     valid_answer = {}
#     responses.add(responses. , "https://gitea.radium.group/radium/project-configuration.git")
