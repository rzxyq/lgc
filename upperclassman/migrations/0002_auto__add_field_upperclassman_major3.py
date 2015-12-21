# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Upperclassman.major3'
        db.add_column(u'upperclassman_upperclassman', 'major3',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Upperclassman.major3'
        db.delete_column(u'upperclassman_upperclassman', 'major3')


    models = {
        u'upperclassman.upperclassman': {
            'Meta': {'object_name': 'Upperclassman'},
            'college': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['upperclassman']