# -*- coding: utf-8 -*-
from odoo import models, fields

class License(models.Model):
    _name = 'az_reclaims.license'
    _description = 'License'

    name = fields.Char('Matrícula', required=True)