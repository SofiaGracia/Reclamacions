# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Reclaim(models.Model):

    _name = 'az_reclaims.reclaim'
    _description = 'Reclamació Patrimonial'

    name = fields.Char(string='Identificador', required=True, copy=False, readonly=True, default='Nova Reclamació')
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
    add_licences = fields.Boolean(string='Añadir matrículas', help='Marque esta casilla si desea añadir matrículas afectadas')
    licenses = fields.Many2many('az_reclaims.license', string='Matrículas afectadas')
    address_type = fields.Selection([
        ('estructurado','Estructurado'),
        ('no_estructurado','No estructurado'),
    ], string='Formato de dirección', default='estructurado', help='Seleccione el formato de dirección')
    un_address = fields.Text(string='Dirección', help='Introduzca la dirección del daño')
    road_type = fields.Selection([
        ('avenida', 'Avenida'),
        ('calle', 'Calle'),
        ('camino', 'Camino'),
        ('carretera', 'Carretera'),
        ('paseo', 'Paseo'),
        ('plaza', 'Plaza'),
        ('travesia', 'Travesía'),
    ], string='Tipo de vía', help='Seleccione el tipo de vía')
    road_name = fields.Text(string='Nombre de la vía')
    road_number = fields.Char(string='Número')
    floor = fields.Char(string='Piso')
    staircase = fields.Char(string='Escalera')
    level = fields.Char(string='Planta')
    door = fields.Char(string='Puerta')
    cad_ref = fields.Text(string='Referencia Catastral')
    polygon_parcel = fields.Char(string='Poligon/parcela')#Preguntar
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

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('az_reclaims.reclaim') or 'New'
        return super(Reclaim, self).create(vals)
    

