# -*- coding: utf-8 -*-
#License: Copyright Rolan Benavent Talens. All rights reserved.

from odoo import api, fields, models

class Expedient(models.Model):  # Asegúrate de usar mayúscula
    _inherit = ['az_expedients.expedient']

    reclaims_ids = fields.One2many('az_reclaims.reclaim', 'expedient_id', string='Reclamaciones')
