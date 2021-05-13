# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from flectra import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def can_edit_vat(self):
        ''' `vat` is a commercial field, synced between the parent (commercial
        entity) and the children. Only the commercial entity should be able to
        edit it (as in backend). '''
        return not self.parent_id
