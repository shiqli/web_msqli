# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Formula'
        db.create_table(u'mathlatex_formula', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('formula', self.gf('django.db.models.fields.TextField')()),
            ('formula_hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'mathlatex', ['Formula'])


    def backwards(self, orm):
        # Deleting model 'Formula'
        db.delete_table(u'mathlatex_formula')


    models = {
        u'mathlatex.formula': {
            'Meta': {'object_name': 'Formula'},
            'formula': ('django.db.models.fields.TextField', [], {}),
            'formula_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mathlatex']