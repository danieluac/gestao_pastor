from odoo import models, fields, api

class EscalasModel(models.Model):
    _name = 'escala'
    _description = 'tabela onde serão cadastradas as informações de escala'

    name = fields.Char(string="Número")
    data_agendada = fields.Date( string="Data Agendada", required=True)
    foi_realizado = fields.Boolean( string="Foi realizada?", required=True, default=False)
    pastor_escalado_id = fields.Many2one("pastor", string='Pastor')
    paroquia_id = fields.Many2one("paroquia", string='Paroquia')

    @api.model
    def create(self, params):
        params['name'] = self.env['ir.sequence'].next_by_code(
                'escala.sequence') or _('New')
        return super(EscalasModel, self).create(params)