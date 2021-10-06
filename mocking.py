# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:55:18 2021

@author: nicholas mirarchi
"""
import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
import gitRequest
import json

Github = 'nmirarchi12'
RESP = 'True'
class TestHw4(unittest.TestCase):
    @patch('gitRequest.repository_info')
    def test_repository_info(self, mock_repository_info):
        mock_repository_info.return_value = Mock(ok=True)
        response = gitRequest.repository_info(Github)
        assert_is_not_none(response)
        
    @patch('gitRequest.repository_info')
    def test_repositorys(self, mock_repository_info):
        mock_repository_info.return_value = [200, {"User": "nmirarchi12",
                                     "Repo: DO180 Number of commits": "1",
                                     "Repo: DO180-apps Number of commits": "2",
                                     "Repo: HW-04a Number of commits": "10",
                                     "Repo: php-app Number of commits": "11",
                                     "Repo: SSW-567 Number of commits": "7",
                                     "Repo: Triangle567 Number of commits": "8"}]
        self.assertTrue(gitRequest.repository_info("nmirarchi12"))
        
    @patch('gitRequest.repository_info')
    def test_repositorys2(self, mock_repository_info):
        mock_repository_info.return_value = [200, {"User": "nmirarchi12",
                                     "Repo: DO180 Number of commits": "1",
                                     "Repo: DO180-apps Number of commits": "2",
                                     "Repo: HW-04a Number of commits": "10",
                                     "Repo: php-app Number of commits": "11",
                                     "Repo: SSW-567 Number of commits": "7",
                                     "Repo: Triangle567 Number of commits": "8"}]
        self.assertIs(mock_repository_info(), gitRequest.repository_info("nmirarchi12"))
"""
        repo_list = gitRequest.repository_info(Github)
        self.assertIsInstance(repo_list, list)
        for i in repo_list:
            self.assertIsInstance(i, str)
"""

if __name__ == '__main__':
    print('Running unit tests')
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestHw4)
    unittest.TextTestRunner(verbosity = 2).run(test_suite)