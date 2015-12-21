# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewStudent'
        db.create_table(u'newstudent_newstudent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('netid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hometown', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('college', self.gf('django.db.models.fields.IntegerField')()),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('minor', self.gf('django.db.models.fields.TextField')()),
            ('extracurricular', self.gf('django.db.models.fields.TextField')()),
            ('extra_sa', self.gf('django.db.models.fields.TextField')(null=True)),
            ('career', self.gf('django.db.models.fields.TextField')()),
            ('career_sa', self.gf('django.db.models.fields.TextField')()),
            ('sa1', self.gf('django.db.models.fields.TextField')()),
            ('sa2', self.gf('django.db.models.fields.TextField')()),
            ('sa3', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'newstudent', ['NewStudent'])


    def backwards(self, orm):
        # Deleting model 'NewStudent'
        db.delete_table(u'newstudent_newstudent')


    models = {
        u'newstudent.newstudent': {
            'Meta': {'object_name': 'NewStudent'},
            'career': ('django.db.models.fields.TextField', [], {}),
            'career_sa': ('django.db.models.fields.TextField', [], {}),
            'college': ('django.db.models.fields.IntegerField', [], {}),
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
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['newstudent']