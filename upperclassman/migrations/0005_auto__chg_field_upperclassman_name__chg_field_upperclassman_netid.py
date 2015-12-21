# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Upperclassman.name'
        db.alter_column(u'upperclassman_upperclassman', 'name', self.gf('django.db.models.fields.CharField')(max_length=35))

        # Changing field 'Upperclassman.netid'
        db.alter_column(u'upperclassman_upperclassman', 'netid', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Upperclassman.name'
        db.alter_column(u'upperclassman_upperclassman', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Upperclassman.netid'
        db.alter_column(u'upperclassman_upperclassman', 'netid', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'year': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['upperclassman']