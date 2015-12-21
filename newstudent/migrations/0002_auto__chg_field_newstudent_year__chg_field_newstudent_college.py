# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'NewStudent.year'
        db.alter_column(u'newstudent_newstudent', 'year', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'NewStudent.college'
        db.alter_column(u'newstudent_newstudent', 'college', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'NewStudent.year'
        db.alter_column(u'newstudent_newstudent', 'year', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'NewStudent.college'
        db.alter_column(u'newstudent_newstudent', 'college', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'newstudent.newstudent': {
            'Meta': {'object_name': 'NewStudent'},
            'career': ('django.db.models.fields.TextField', [], {}),
            'career_sa': ('django.db.models.fields.TextField', [], {}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'extra_sa': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'extracurricular': ('django.db.models.fields.TextField', [], {}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'minor': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sa1': ('django.db.models.fields.TextField', [], {}),
            'sa2': ('django.db.models.fields.TextField', [], {}),
            'sa3': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['newstudent']