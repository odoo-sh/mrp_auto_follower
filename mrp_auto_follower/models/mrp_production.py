# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = "mrp.production"
    
    user_id = fields.Many2one(tracking=1)
