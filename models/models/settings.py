# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ReclaimsConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    reclaim_subtype_id = fields.Many2one('az_expedients.etype', string='Subtipo de expediente para reclamaciones')

    def set_values(self):
        super(ReclaimsConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('az_reclaims.reclaim_subtype_id', self.reclaim_subtype_id.id)

    @api.model
    def get_values(self):
        res = super(ReclaimsConfigSettings, self).get_values()
        reclaim_subtype_id = self.env['ir.config_parameter'].sudo().get_param('az_reclaims.reclaim_subtype_id', default=False)
        if reclaim_subtype_id:
            res.update(reclaim_subtype_id=int(reclaim_subtype_id))
        return res
