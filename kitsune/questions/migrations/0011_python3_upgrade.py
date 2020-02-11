# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-05 08:38
from __future__ import unicode_literals

from django.db import migrations
import kitsune.sumo.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20190816_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='locale',
            field=kitsune.sumo.models.LocaleField(choices=[('af', 'Afrikaans'), ('ar', 'عربي'), ('az', 'Azərbaycanca'), ('bg', 'Български'), ('bm', 'Bamanankan'), ('bn', 'বাংলা'), ('bs', 'Bosanski'), ('ca', 'català'), ('cs', 'Čeština'), ('da', 'Dansk'), ('de', 'Deutsch'), ('ee', 'Èʋegbe'), ('el', 'Ελληνικά'), ('en-US', 'English'), ('es', 'Español'), ('et', 'eesti keel'), ('eu', 'Euskara'), ('fa', 'فارسی'), ('fi', 'suomi'), ('fr', 'Français'), ('fy-NL', 'Frysk'), ('ga-IE', 'Gaeilge (Éire)'), ('gl', 'Galego'), ('gn', "Avañe'ẽ"), ('gu-IN', 'ગુજરાતી'), ('ha', 'هَرْشَن هَوْسَ'), ('he', 'עברית'), ('hi-IN', 'हिन्दी (भारत)'), ('hr', 'Hrvatski'), ('hu', 'Magyar'), ('dsb', 'Dolnoserbšćina'), ('hsb', 'Hornjoserbsce'), ('id', 'Bahasa Indonesia'), ('ig', 'Asụsụ Igbo'), ('it', 'Italiano'), ('ja', '日本語'), ('ka', 'ქართული'), ('km', 'ខ្មែរ'), ('kn', 'ಕನ್ನಡ'), ('ko', '한국어'), ('ln', 'Lingála'), ('lt', 'lietuvių kalba'), ('mg', 'Malagasy'), ('mk', 'Македонски'), ('ml', 'മലയാളം'), ('ms', 'Bahasa Melayu'), ('ne-NP', 'नेपाली'), ('nl', 'Nederlands'), ('no', 'Norsk'), ('pl', 'Polski'), ('pt-BR', 'Português (do Brasil)'), ('pt-PT', 'Português (Europeu)'), ('ro', 'română'), ('ru', 'Русский'), ('si', 'සිංහල'), ('sk', 'slovenčina'), ('sl', 'slovenščina'), ('sq', 'Shqip'), ('sr', 'Српски'), ('sw', 'Kiswahili'), ('sv', 'Svenska'), ('ta', 'தமிழ்'), ('ta-LK', 'தமிழ் (இலங்கை)'), ('te', 'తెలుగు'), ('th', 'ไทย'), ('tn', 'Setswana'), ('tr', 'Türkçe'), ('uk', 'Українська'), ('ur', 'اُردو'), ('vi', 'Tiếng Việt'), ('wo', 'Wolof'), ('xh', 'isiXhosa'), ('yo', 'èdè Yorùbá'), ('zh-CN', '中文 (简体)'), ('zh-TW', '正體中文 (繁體)'), ('zu', 'isiZulu')], default='en-US', max_length=7),
        ),
        migrations.AlterField(
            model_name='questionlocale',
            name='locale',
            field=kitsune.sumo.models.LocaleField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('bm', 'Bambara'), ('bn', 'Bengali'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('da', 'Danish'), ('de', 'German'), ('ee', 'Ewe'), ('el', 'Greek'), ('en-US', 'English'), ('es', 'Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy-NL', 'Frisian'), ('ga-IE', 'Irish (Ireland)'), ('gl', 'Galician'), ('gn', 'Guarani'), ('gu-IN', 'Gujarati'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi-IN', 'Hindi (India)'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('dsb', 'Lower Sorbian'), ('hsb', 'Upper Sorbian'), ('id', 'Indonesian'), ('ig', 'Igbo'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('mg', 'Malagasy'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('ms', 'Malay'), ('ne-NP', 'Nepali'), ('nl', 'Dutch'), ('no', 'Norwegian'), ('pl', 'Polish'), ('pt-BR', 'Portuguese (Brazilian)'), ('pt-PT', 'Portuguese (Portugal)'), ('ro', 'Romanian'), ('ru', 'Russian'), ('si', 'Sinhala'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sw', 'Swahili'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('ta-LK', 'Tamil (Sri Lanka)'), ('te', 'Telugu'), ('th', 'Thai'), ('tn', 'Tswana'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yo', 'Yoruba'), ('zh-CN', 'Chinese (Simplified)'), ('zh-TW', 'Chinese (Traditional)'), ('zu', 'Zulu')], default='en-US', max_length=7, unique=True),
        ),
    ]
