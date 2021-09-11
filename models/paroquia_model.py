
from odoo import models, fields, api

class ParoquiaModel(models.Model):
    _name = 'paroquia'
    _description = 'tabela onde serão cadastradas as informações de paroquias'

    name = fields.Char(required=True, string="Nome")
    location = fields.Text( string="Localização")
    pastor_id = fields.One2many("pastor", "paroquia_id", string='Pastores')

