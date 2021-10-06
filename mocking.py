# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:55:18 2021

@author: nicholas mirarchi
"""
import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
from gitRequest import repository_info
import json

Github = 'nmirarchi12'
RESP = 'True'
class TestHw4(unittest.TestCase):
    @patch('gitRequest.repository_info')
    def test_repository_info(self, mock_repository_info):

        mock_repository_info.return_value = Mock(ok=True)
        #mock_repository_info.json.return_value=myJson
        response = repository_info()
        #assert_list_equal(response.json(),myJson)
        assert_is_not_none(response)
"""
        repo_list = gitRequest.repository_info(Github)
        print(repo_list)
        self.assertIsInstance(repo_list, list)
        for i in repo_list:
            self.assertIsInstance(i, str)
"""