# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReclaimE(models.Model):

    _name = 'az_reclaims.reclaim'
    _description = 'Campos específicos de las Reclamaciones Patrimoniales'

    expedient_id = fields.Many2one('az_expedients.expedient', string='Expediente', required=True)
    damage_type = fields.Selection([
        ('personas', 'Personas'),
        ('vehiculo', 'Vehículo'),
        ('bien_consecionado', 'Bien consecionado'),
        ('edificio', 'Edificio'),
        ('agricola', 'Agrícola'),
        ('otro', 'Otro'),
    ], string='Tipo de daño', help='Seleccione el tipo de daño reclamado')
    other_damage = fields.Text(string='Otro tipo de daño')
    reference = fields.Char(string='Referencia')
    description = fields.Text(string='Descripción')