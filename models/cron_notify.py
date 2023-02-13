# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from datetime import datetime

class CronNotify(models.Model):
    _name = 'cron.notify'
    _description = 'cron_notify'

    name = fields.Char(string="Aviso", required=True)
    email_template = fields.Many2one('mail.template', string="Plantilla de Correo", required=True)
    model_name = fields.Many2one('ir.model', string="Modelo", required=True, ondelete='cascade', related="email_template.model_id")
    start_date = fields.Datetime(string="Fecha de Inicio",default=datetime.today(), required=True)
    interval_number = fields.Integer(string="Ejecutar cada:", requiered=True)
    interval_type = fields.Selection([('minutes','Minutos'),('hours','Horas'),('days','Dias'),('weeks','Semanas'),('months','Meses')], default="days",string="")
    cron_id = fields.Many2one('ir.cron', string="Cron", readonly=True)
    users = fields.Many2many('res.partner', string="Usuarios a Notificar")

    

