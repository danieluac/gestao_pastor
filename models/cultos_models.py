from odoo import models, fields, api, _

class CultoModel(models.Model):
    _name = 'culto'
    _description = 'tabela onde serão cadastradas as informações de cultos'

    name = fields.Char( string="Número")
    tema = fields.Char( string="Tema do culto", required=True)
    data = fields.Date( string="Data realizado", required=True)
    membros_admitidos = fields.Integer( string="Membros admitidos", required=True)
    pastor_dirigente_id = fields.Many2one("pastor", string='Pastor')
    paroquia_id = fields.Many2one("paroquia", string='Paroquia')

    @api.model
    def create(self, params):
        params['name'] = self.env['ir.sequence'].next_by_code(
                'culto.sequence') or _('New')
        return super(CultoModel, self).create(params)