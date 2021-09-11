
from odoo import models, fields, api


class PastorModel(models.Model):
    _name = 'pastor'
    _description = 'tabela onde serão cadastradas as informações de pastores da igreja'

    name = fields.Char(required=True, string="Nome")
    email = fields.Char( string="Email")
    photo = fields.Binary( string="Foto")
    date_born = fields.Date(required=True, string="Data de nascimento")
    consecration_date = fields.Date( string="Data da consagração", required=True)
    gender = fields.Selection([('M', "Masculino"), ('F', 'Femenino')], string="Genero", required=True)
    contact = fields.Char(required=True, string="Telefone:")
    marital_status = fields.Selection([('casado', "Casado"), ('solteiro', 'Solteiro'), ('viuvo', 'Viuvo')], string="Estado Civil", required=True)
    paroquia_id = fields.Many2one('paroquia', required=True)
    culto_id = fields.One2many("culto", "pastor_dirigente_id", string="Cultos Dirigidos")
    escala_id = fields.One2many("escala", "pastor_escalado_id", string="Escalas")


