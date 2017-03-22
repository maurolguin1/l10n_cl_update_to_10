# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import xmlrpclib
import re

class Update10(models.TransientModel):
    _name = 'update10'
    _inherit = 'res.config.settings'

    server_old = fields.Char('Server Old', help="Server Old", default='190.114.253.252')
    port_old = fields.Char('Port Old', help="Port Old" ,default='8071')
    db_old = fields.Char('Data Base Old', help="Data Base Old" ,default='db')
    user_old = fields.Char('User Old')
    pass_old = fields.Char('Password Old')

    server_new = fields.Char('This Server', help="Server Old", default='190.114.253.252')
    port_new = fields.Char('Port New', help="Port New" ,default='8069')
    db_new = fields.Char('Data Base New', help="Data Base New" ,default='db')
    user_new = fields.Char('User New')
    pass_new = fields.Char('Password New')

    val_materials  = fields.Boolean('Import materials', help='Import materials', default=True)

    @api.one
    def update_server(self):

        # Insertamos el hash
        if not self.server_old:
            raise ValidationError(_('Error 0001! You need a Old server!'))
        if not self.server_new:
            raise ValidationError(_('Error 0001! You need a New server!'))

        HOST='190.114.253.252'
        PORT=8069
        DB='libredte'
        USER='admin'
        PASS='1234567890'
        url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

        common_proxy = xmlrpclib.ServerProxy(url+'common')
        object_proxy = xmlrpclib.ServerProxy(url+'object')
        uid = common_proxy.login(DB,USER,PASS)

        product = object_proxy.execute(DB,uid,PASS,'product.template','search',[('active','=',True)])
        for id in product:
            raise ValidationError(_(product.name))


