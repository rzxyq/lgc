# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'NewStudent.extra_sa'
        db.alter_column(u'newstudent_newstudent', 'extra_sa', self.gf('django.db.models.fields.TextField')(max_length=250, null=True))

        # Changing field 'NewStudent.career_sa'
        db.alter_column(u'newstudent_newstudent', 'career_sa', self.gf('django.db.models.fields.TextField')(max_length=250, null=True))

        # Changing field 'NewStudent.sa3'
        db.alter_column(u'newstudent_newstudent', 'sa3', self.gf('django.db.models.fields.TextField')(max_length=250, null=True))

        # Changing field 'NewStudent.sa2'
        db.alter_column(u'newstudent_newstudent', 'sa2', self.gf('django.db.models.fields.TextField')(max_length=250, null=True))

        # Changing field 'NewStudent.sa1'
        db.alter_column(u'newstudent_newstudent', 'sa1', self.gf('django.db.models.fields.TextField')(max_length=250, null=True))

    def backwards(self, orm):

        # Changing field 'NewStudent.extra_sa'
        db.alter_column(u'newstudent_newstudent', 'extra_sa', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'NewStudent.career_sa'
        db.alter_column(u'newstudent_newstudent', 'career_sa', self.gf('django.db.models.fields.TextField')(default=1))

        # Changing field 'NewStudent.sa3'
        db.alter_column(u'newstudent_newstudent', 'sa3', self.gf('django.db.models.fields.TextField')(default=2))

        # Changing field 'NewStudent.sa2'
        db.alter_column(u'newstudent_newstudent', 'sa2', self.gf('django.db.models.fields.TextField')(default=2))

        # Changing field 'NewStudent.sa1'
        db.alter_column(u'newstudent_newstudent', 'sa1', self.gf('django.db.models.fields.TextField')(default=2))

    models = {
        u'newstudent.newstudent': {
            'Meta': {'object_name': 'NewStudent'},
            'career': ('django.db.models.fields.TextField', [], {}),
            'career_sa': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'extra_sa': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'extracurricular': ('django.db.models.fields.TextField', [], {}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'minor': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sa1': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'sa2': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'sa3': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'upperclassman': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['upperclassman.Upperclassman']", 'null': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'upperclassman.upperclassman': {
            'Meta': {'object_name': 'Upperclassman'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['newstudent']