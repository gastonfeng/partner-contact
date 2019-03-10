# Copyright 2016 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from psycopg2 import IntegrityError

from odoo.tests import TransactionCase
from odoo.tools.misc import mute_logger


@mute_logger('odoo.sql_db')
class CompanyTypeTest(TransactionCase):

    def setUp(self):
        super(CompanyTypeTest, self).setUp()

        vals = {'name': 'Limited Corporation',
                'shortcut': 'Ltd.'}

        c_type_obj = self.env['res.partner.company.type']

        self.type_ltd = c_type_obj.create(vals)

    def test_00_duplicate(self):
        # Test Duplicate type
        vals = {'name': 'Limited Corporation',
                'shortcut': 'Ltd.'}

        c_type_obj = self.env['res.partner.company.type']

        with self.assertRaises(IntegrityError):
            c_type_obj.create(vals)
