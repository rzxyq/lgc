# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Upperclassman'
        db.create_table(u'upperclassman_upperclassman', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('netid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('college', self.gf('django.db.models.fields.IntegerField')()),
            ('major1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('major2', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'upperclassman', ['Upperclassman'])


    def backwards(self, orm):
        # Deleting model 'Upperclassman'
        db.delete_table(u'upperclassman_upperclassman')


    models = {
        u'upperclassman.upperclassman': {
            'Meta': {'object_name': 'Upperclassman'},
            'college': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['upperclassman']