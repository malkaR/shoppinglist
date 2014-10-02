# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ListItem'
        db.create_table(u'list_listitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('store', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'list', ['ListItem'])


    def backwards(self, orm):
        # Deleting model 'ListItem'
        db.delete_table(u'list_listitem')


    models = {
        u'list.listitem': {
            'Meta': {'object_name': 'ListItem'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'store': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['list']