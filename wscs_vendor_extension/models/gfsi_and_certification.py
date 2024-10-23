# -*- coding: utf-8 -*-
from odoo import fields, models


class GfsiScheme(models.Model):
    _name = 'gfsi.scheme'
    _description = 'GFSI Scheme'

    name = fields.Char(string='Scheme Name', required=True)


class GfsiGradeZip(models.Model):
    _name = 'gfsi.gradezip'
    _description = 'GFSI Grade Zip'

    name = fields.Char(string='Grade Zip', required=True)


class GfsiCertification(models.Model):
    _name = 'gfsi.certification'
    _description = 'GFSI Certification'

    name = fields.Char(string='Certification', required=True)
