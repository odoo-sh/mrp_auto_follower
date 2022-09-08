# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = "mrp.production"
    
    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:
            self.message_subscribe(self.user_id.partner_id.ids)
