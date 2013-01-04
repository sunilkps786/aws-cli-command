#!/usr/bin/env python
# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import unittest
import awscli.clidriver


class TestCreateQueue(unittest.TestCase):

    def setUp(self):
        self.driver = awscli.clidriver.CLIDriver()
        self.prefix = 'aws sqs create-queue'
        self.queue_name = 'foobar'

    def test_simple(self):
        cmdline = self.prefix
        cmdline += ' --queue-name %s' % self.queue_name
        result = {'QueueName': self.queue_name}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)


if __name__ == "__main__":
    unittest.main()
