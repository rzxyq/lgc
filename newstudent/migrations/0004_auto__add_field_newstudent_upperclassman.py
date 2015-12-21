# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewStudent.upperclassman'
        db.add_column(u'newstudent_newstudent', 'upperclassman',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['newstudent.NewStudent'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewStudent.upperclassman'
        db.delete_column(u'newstudent_newstudent', 'upperclassman_id')


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
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'upperclassman': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newstudent.NewStudent']", 'null': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['newstudent']