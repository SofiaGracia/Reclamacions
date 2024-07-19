# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ReclaimC(models.Model):
    _inherit = ['az_expedients.expedient']
    _description = 'Campos comunes de las Reclamaciones Patrimoniales'

    document_editor = fields.Selection([
        ('particular', 'Particular'),
        ('inspector', 'Inspector'),
        ('brigada', 'Brigada'),
        ('policia', 'Policía'),
        ('empresa concesionaria', 'Empresa concesionaria'),
        ('tecnico ayuntamiento', 'Técnico ayuntamiento'),
        ('tecnico externo', 'Técnico externo'),
        ('otro', 'Otro'),
    ], string='Redactor del documento', help='Seleccione el redactor del documento')
    other_editor = fields.Text(string='Otro redactor del documento', help='Introduzca el redactor del documento')
    amount = fields.Monetary(string='Importe', help='Introduzca el importe')
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)
    damage_state = fields.Selection([
        ('expediente_paralizado', 'Expediente paralizado'),
        ('reparacion_por_parte_de_la_brigada','Reparación por parte de la Brigada'),
        ('indemnizacion','Indemnización'),
        ('no_procede','No procede'),
        ('otro', 'Otro'),
    ], string='Estado de reparación del daño', default='expediente_paralizado', help='Seleccione el estado de la reclamación')
    other_state = fields.Text(string='Otro estado', help='Introduzca otro estado')
    reclaims_ids = fields.One2many('az_reclaims.reclaim', 'expedient_id', string='Reclamaciones')