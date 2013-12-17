'''
test_buffer_overflow.py

Copyright 2012 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

from nose.plugins.attrib import attr
from w3af.plugins.tests.helper import PluginTest, PluginConfig


class TestBufferOverflow(PluginTest):

    target = 'http://moth/w3af/audit/buffer_overflow/index.php'

    _run_config = {
        'target': target + '?buf=',
        'plugins': {
            'audit': (PluginConfig('buffer_overflow',),),
        }
    }

    @attr('ci_fails')
    def test_found_bo(self):
        self._scan(self._run_config['target'], self._run_config['plugins'])

        vulns = self.kb.get('buffer_overflow', 'buffer_overflow')
        self.assertEquals(1, len(vulns))

        # Now some tests around specific details of the found vuln
        vuln = vulns[0]
        self.assertEquals('Buffer overflow vulnerability', vuln.get_name())
        self.assertEquals("buf", vuln.get_var())
        self.assertEquals(self.target, str(vuln.get_url()))