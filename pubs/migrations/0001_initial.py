# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table(u'pubs_publisher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'pubs', ['Publisher'])

        # Adding model 'Author'
        db.create_table(u'pubs_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal(u'pubs', ['Author'])

        # Adding model 'Book'
        db.create_table(u'pubs_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pubs.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'pubs', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'pubs_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'pubs.book'], null=False)),
            ('author', models.ForeignKey(orm[u'pubs.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding model 'Keyword'
        db.create_table(u'pubs_keyword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword_text', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'pubs', ['Keyword'])

        # Adding model 'Journal'
        db.create_table(u'pubs_journal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abreviation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pubs.Publisher'])),
        ))
        db.send_create_signal(u'pubs', ['Journal'])

        # Adding model 'Publication'
        db.create_table(u'pubs_publication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pubs.Journal'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2008)),
            ('volume', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('issue', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('doi', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_page', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.URLField')(default='http://www.acs.org', max_length=200)),
        ))
        db.send_create_signal(u'pubs', ['Publication'])

        # Adding M2M table for field keywords on 'Publication'
        m2m_table_name = db.shorten_name(u'pubs_publication_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publication', models.ForeignKey(orm[u'pubs.publication'], null=False)),
            ('keyword', models.ForeignKey(orm[u'pubs.keyword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['publication_id', 'keyword_id'])

        # Adding M2M table for field authors on 'Publication'
        m2m_table_name = db.shorten_name(u'pubs_publication_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publication', models.ForeignKey(orm[u'pubs.publication'], null=False)),
            ('author', models.ForeignKey(orm[u'pubs.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['publication_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table(u'pubs_publisher')

        # Deleting model 'Author'
        db.delete_table(u'pubs_author')

        # Deleting model 'Book'
        db.delete_table(u'pubs_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'pubs_book_authors'))

        # Deleting model 'Keyword'
        db.delete_table(u'pubs_keyword')

        # Deleting model 'Journal'
        db.delete_table(u'pubs_journal')

        # Deleting model 'Publication'
        db.delete_table(u'pubs_publication')

        # Removing M2M table for field keywords on 'Publication'
        db.delete_table(db.shorten_name(u'pubs_publication_keywords'))

        # Removing M2M table for field authors on 'Publication'
        db.delete_table(db.shorten_name(u'pubs_publication_authors'))


    models = {
        u'pubs.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'pubs.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pubs.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubs.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pubs.journal': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Journal'},
            'abreviation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubs.Publisher']"})
        },
        u'pubs.keyword': {
            'Meta': {'ordering': "('keyword_text',)", 'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword_text': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'pubs.publication': {
            'Meta': {'ordering': "('headline',)", 'object_name': 'Publication'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pubs.Author']", 'symmetrical': 'False'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "'http://www.acs.org'", 'max_length': '200'}),
            'issue': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubs.Journal']"}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pubs.Keyword']", 'symmetrical': 'False'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'start_page': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2008'})
        },
        u'pubs.publisher': {
            'Meta': {'ordering': "['name']", 'object_name': 'Publisher'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['pubs']