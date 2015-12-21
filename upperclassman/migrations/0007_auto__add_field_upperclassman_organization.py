# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Upperclassman.organization'
        db.add_column(u'upperclassman_upperclassman', 'organization',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Upperclassman.organization'
        db.delete_column(u'upperclassman_upperclassman', 'organization')


    models = {
        u'upperclassman.upperclassman': {
            'Meta': {'object_name': 'Upperclassman'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'organization': ('django.db.models.fields.TextField', [], {}),
            'survey': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['upperclassman']