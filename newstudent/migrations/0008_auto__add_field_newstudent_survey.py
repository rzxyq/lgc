# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewStudent.survey'
        db.add_column(u'newstudent_newstudent', 'survey',
                      self.gf('django.db.models.fields.TextField')(default='HI'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewStudent.survey'
        db.delete_column(u'newstudent_newstudent', 'survey')


    models = {
        u'newstudent.newstudent': {
            'Meta': {'object_name': 'NewStudent'},
            'career': ('django.db.models.fields.TextField', [], {}),
            'career_sa': ('django.db.models.fields.TextField', [], {'max_length': '75', 'null': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'extra_sa': ('django.db.models.fields.TextField', [], {'max_length': '75', 'null': 'True'}),
            'extracurricular': ('django.db.models.fields.TextField', [], {}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'minor': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sa1': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'sa2': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'sa3': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True'}),
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'survey': ('django.db.models.fields.TextField', [], {}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['newstudent']