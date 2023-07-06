# -*- coding: utf-8 -*-
# create-weblinks-itexi.py
#
# This file is part of LilyPond, the GNU music typesetter.
#
# Copyright (C) 2009--2022  Graham Percival <graham@percival-music.ca>
#
# LilyPond is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LilyPond is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LilyPond.  If not, see <http://www.gnu.org/licenses/>.


import codecs
import glob
import os
import sys

import langdefs
from version_data import version_data

# Force encoding for stdout, Python up to version 3.7 falls back to
# ASCII with LANG=C (which the build system exports).
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# translation data -- shouldn't be here; see issue
# https://sourceforge.net/p/testlilyissues/issues/1050/

langs = [i.code if i.code != 'en' else '' for i in langdefs.WEB_LANGUAGES]


# these links are relative from /website/ on lilypond.org
depth = "../"

# Get/update node translations
# TODO: this should likely be autogenerated or maintained via PO files.
'''
for i in ca cs de es fr hu it ja nl pt zh; do
    echo "'"$i"': {"
    (echo '--' ; grep -nH -B1 translationof Documentation/$i/web/* ) \
        | python3 -c 'import re, sys; print(re.sub(sys.argv[1], sys.argv[2], sys.stdin.read()))' \
            '(?m)^--\n.*@(?:unnum|sub)[^ ]* (.*)\n.*@translationof (.*)\n' "'\2': '\1',\n" \
        | grep -E 'Source|Learning|Glossary|Essay|Notation|Usage|Snippets|Web|Changes|Extending|Internals|Contributor'
    echo "},"
done
'''

translations = {
    'ca': {
        'Source': 'Font',
        'Learning': 'Aprenentatge',
        'Music glossary': 'Glossari musical',
        'Essay': 'Monografia',
        'Notation': 'Notació',
        'Usage': 'Ús',
        'Snippets': 'Fragments',
        'Web': 'Web',
        'Changes': 'Canvis',

        'Extending': 'Extensions',
        'Internals': 'Funcionament intern',
        'Contributor': 'Guia del col·laborador',

        ' (split HTML)': ' (HTML seccionat)',
        ' (big HTML)': ' (HTML monolític)',

        'Regression tests for ': 'Proves de regressió per a ',
        'PDF of regtests for ': 'Proves de regressió en PDF per a ',
        'abc2ly Regression tests for ': 'Proves de regressió d\'abc2ly per a ',
        'PDF of abc2ly regtests for ': 'Proves de regressió d\'abc2ly en PDF per a ',
        'MusicXML Regression tests for ': 'Proves de regressió de MusicXML per a ',
        'PDF of MusicXML regtests for ': 'Proves de regressió de MusicXML en PDF per a ',

        'Doc tarball for ': 'Tarball de la documentació per a ',
    },
    'cs': {
        'Source': 'Source',
        'Learning': 'Učení',
        'Music glossary': 'Slovníček',
        'Essay': 'Článek',
        'Notation': 'Notový zápis',
        'Usage': 'Používání',
        'Snippets': 'Úryvky',
        'Web': 'Web',
        'Changes': 'Změny',

        'Extending': 'Rozšíření',
        'Internals': 'Vnitřnosti',
        'Contributor': 'Vývojářské',

        ' (split HTML)': ' (rozdělené HTML)',
        ' (big HTML)': ' (velké HTML)',

        'Regression tests for ': 'Zkoušky regresí ',
        'PDF of regtests for ': 'PDF zkoušky regresí ',
        'abc2ly Regression tests for ': 'abc2ly zkoušky regresí ',
        'PDF of abc2ly regtests for ': 'PDF abc2ly zkoušky regresí ',
        'MusicXML Regression tests for ': 'MusicXML zkoušky regresí ',
        'PDF of MusicXML regtests for ': 'PDF MusicXML zkoušky regresí ',

        'Doc tarball for ': 'Doc tarball for ',
    },
    'de': {
        'Source': 'Quellen',
        'Learning': 'Einführung',
        'Music glossary': 'Glossar',
        'Essay': 'Aufsatz',
        'Notation': 'Notation',
        'Usage': 'Benutzung',
        'Snippets': 'Schnipsel',
        'Web': 'Web',
        'Changes': 'Änderungen',

        'Extending': 'Erweitern',
        'Internals': 'Interna',
        'Contributor': 'Beitragen',

        ' (split HTML)': ' (geteiltes HTML)',
        ' (big HTML)': ' (großes HTML)',

        'Regression tests for ': 'Regressionstests für ',
        'PDF of regtests for ': 'PDF der Regressionstests für ',
        'abc2ly Regression tests for ': 'abc2ly Regressionstests für ',
        'PDF of abc2ly regtests for ': 'PDF der abc2ly Regressionstests für ',
        'MusicXML Regression tests for ': 'MusicXML Regressionstests für ',
        'PDF of MusicXML regtests for ': 'PDF der MusicXML Regressionstests für ',

        'Doc tarball for ': 'Dokumentation tar-gepackt für ',
    },
    'es': {
        'Source': 'Código fuente',

        'Learning': 'Aprendizaje',
        'Music glossary': 'Glosario',
        'Essay': 'Ensayo',
        'Notation': 'Notación',
        'Usage': 'Utilización',
        'Snippets': 'Fragmentos',
        'Web': 'Web',
        'Changes': 'Cambios',
        'Extending': 'Extensión',
        'Internals': 'Funcionamiento interno',
        'Contributor': 'Guía del colaborador',

        # keep the spaces!
        ' (split HTML)': ' (HTML seccionado)',
        ' (big HTML)': ' (HTML monolítico)',

        'Regression tests for ': 'Pruebas de regresión para ',
        'PDF of regtests for ': 'Pruebas en PDF para ',
        'abc2ly Regression tests for ': 'Pruebas de regresión de abc2ly para ',
        'PDF of abc2ly regtests for ': 'Pruebas de abc2ly en PDF para ',
        'MusicXML Regression tests for ': 'Pruebas de regresión de MusicXML para ',
        'PDF of MusicXML regtests for ': 'Pruebas de MusicXML en PDF para ',

        'Doc tarball for ': 'Tarball de la documentación para ',
    },
    'fr': {
        'Source': 'Sources',

        'Learning': 'Initiation',
        'Music glossary': 'Glossaire',
        'Essay': 'Essai',
        'Notation': 'Notation',
        'Usage': 'Utilisation',
        'Snippets': 'Morceaux choisis',
        'Web': 'Web',
        'Changes': 'Nouveautés',
        'Extending': 'Extension',
        'Internals': 'Propriétés internes',
        'Contributor': 'Guide du contributeur',

        # keep the spaces!
        ' (split HTML)': ' (HTML multipages)',
        ' (big HTML)': ' (HTML en page unique)',

        'Regression tests for ': 'Tests de régression pour ',
        'PDF of regtests for ': 'PDF des tests de régression pour ',
        'abc2ly Regression tests for ': 'Tests de régression de abc2ly pour ',
        'PDF of abc2ly regtests for ': 'PDF des tests de régression de abc2ly pour ',
        'MusicXML Regression tests for ': 'Tests de régression de MusicXML pour ',
        'PDF of MusicXML regtests for ': 'PDF des tests de régression de MusicXML pour ',

        'Doc tarball for ': 'Archive de la documentation pour ',
    },
    'hu': {
        'Source': 'Forrás',
        'Learning': 'Tankönyv',
        'Music glossary': 'Fogalomtár',
        'Essay': 'Esszé',
        'Notation': 'Kottaírás',
        'Usage': 'Használat',
        'Snippets': 'Kódrészletek',
        'Web': 'Web',
        'Changes': 'Változások',
        'Extending': 'Bővítés',
        'Internals': 'Belső működés',
        'Contributor': 'Közreműködés',

        ' (split HTML)': ' (HTML oldalak)',
        ' (big HTML)': ' (egy nagy HTML oldal)',

        'Regression tests for ': 'Regressziós tesztek - verzió: ',
        'PDF of regtests for ': 'PDF formátumban - verzió: ',
        'abc2ly Regression tests for ': 'abc2ly regressziós tesztek - verzió: ',
        'PDF of abc2ly regtests for ': 'PDF formátumban - verzió: ',
        'MusicXML Regression tests for ': 'MusicXML regressziós tesztek - verzió: ',
        'PDF of MusicXML regtests for ': 'PDF formátumban - verzió: ',

        'Doc tarball for ': 'Tömörített csomag - verzió: ',
    },
    'it': {
        'Source': 'Sorgenti',
        'Learning': 'Apprendimento',
        'Music glossary': 'Glossario',
        'Essay': 'Saggio',
        'Notation': 'Notazione',
        'Usage': 'Uso',
        'Snippets': 'Frammenti',
        'Web': 'Web',
        'Changes': 'Cambiamenti',
        'Extending': 'Estendere',
        'Internals': 'Funzionamento interno',
        'Contributor': 'Guida del collaboratore',

        # keep the spaces!
        ' (split HTML)': ' (HTML multipagina)',
        ' (big HTML)': ' (HTML pagina unica)',

        'Regression tests for ': 'Test di collaudo per ',
        'PDF of regtests for ': 'PDF dei test di collaudo per ',
        'abc2ly Regression tests for ': 'Test di collaudo di abc2ly per ',
        'PDF of abc2ly regtests for ': 'PDF dei test di collaudo di abc2ly per ',
        'MusicXML Regression tests for ': 'Test di collaudo di MusicXML per ',
        'PDF of MusicXML regtests for ': 'PDF dei test di collaudo di MusicXML per ',

        'Doc tarball for ': 'Archivio della documentazione per ',
    },
    'ja': {
        'Source': 'ソース',
        'Learning': '学習',
        'Music glossary': '用語集',
        'Essay': 'エッセー',
        'Notation': '記譜法',
        'Usage': '使用方法',
        'Snippets': 'コード断片集',
        'Web': 'Web',
        'Changes': '変更点',

        # TODO
        'Extending': '拡張',
        'Internals': '内部リファレンス',
        'Contributor': '貢献者向けガイド',

        # keep the spaces!
        ' (split HTML)': ' (ページ毎に分割された HTML)',
        ' (big HTML)': ' (1 つの大きな HTML)',

        'Regression tests for ': '回帰テスト バージョン ',
        'PDF of regtests for ': '回帰テスト (PDF 版) バージョン ',
        'abc2ly Regression tests for ': 'abc2ly 回帰テスト バージョン ',
        'PDF of abc2ly regtests for ': 'abc2ly 回帰テスト (PDF 版) バージョン ',
        'MusicXML Regression tests for ': 'MusicXML 回帰テスト バージョン ',
        'PDF of MusicXML regtests for ': 'MusicXML 回帰テスト (PDF 版) バージョン ',

        'Doc tarball for ': 'ドキュメント アーカイブ バージョン ',

    },
    'nl': {
        'Source': 'Broncode',

        'Learning': 'Beginnen',
        'Music glossary': 'Terminologie',
        'Essay': 'Essay',
        'Notation': 'Notatie',
        'Usage': 'Gebruik',
        'Snippets': 'Snippers',
        'Web': 'Web',
        'Changes': 'Veranderingen',
        'Extending': 'Uitbreidingen',
        'Internals': 'Internals',
        'Contributor': 'Contributor',

        # keep the spaces!
        ' (split HTML)': ' (opgesplitste HTML)',
        ' (big HTML)': ' (grote pagina HTML)',

        'Regression tests for ': 'Regressietesten voor ',
        'PDF of regtests for ': 'PDF van regressietesten voor ',
        'abc2ly Regression tests for ': 'abc2ly regressietesten voor ',
        'PDF of abc2ly regtests for ': 'abc2ly regressietesten voor ',
        'MusicXML Regression tests for ': 'MusicXML regressietesten voor ',
        'PDF of MusicXML regtests for ': 'MusicXML regressietesten voor ',

        'Doc tarball for ': 'Tarball met documentation voor ',
    },
    'pt': {
        'Source': 'Código-fonte',

        'Learning': 'Aprendizagem',
        'Music glossary': 'Glossário',
        'Essay': 'Ensaio',
        'Notation': 'Notação',
        'Usage': 'Uso',
        'Snippets': 'Trechos',
        'Web': 'Web',
        'Changes': 'Mudanças',
        'Extending': 'Extensão',
        'Internals': 'Procedimentos internos',
        'Contributor': 'Guia do contribuidor',

        # keep the spaces!
        ' (split HTML)': ' (HTML dividido)',
        ' (big HTML)': ' (HTML único)',

        'Regression tests for ': 'Testes de regressão de ',
        'PDF of regtests for ': 'PDF dos testes de regressão de ',
        'abc2ly Regression tests for ': 'Testes de regressão de abc2ly de ',
        'PDF of abc2ly regtests for ': 'PDF dos testos de regressão de abc2ly de ',
        'MusicXML Regression tests for ': 'Testes de regressão de MusicXML de ',
        'PDF of MusicXML regtests for ': 'PDF des testos de regressão de MusicXML de ',

        'Doc tarball for ': 'Arquivo da documentação de ',
    },
    'zh': {
        'Source': '源码',
        'Learning': '学习',
        'Music glossary': '音乐术语表',
        'Essay': '文章',
        'Notation': '记谱法',
        'Usage': '使用',
        'Snippets': '片断',
        'Web': 'Web',
        'Changes': '变化',

        'Extending': '扩展',
        'Internals': '内部机制',
        'Contributor': '贡献者',

        # keep the spaces!
        ' (split HTML)': ' (分开的 HTML)',
        ' (big HTML)': ' (大的 HTML)',

        'Regression tests for ': '回归测试 ',
        'PDF of regtests for ': '回归测试的 PDF ',
        'abc2ly Regression tests for ': 'abc2ly 回归测试 ',
        'PDF of abc2ly regtests for ': 'abc2ly 的 PDF 回归测试 ',
        'MusicXML Regression tests for ': 'MusicXML 回归测试 ',
        'PDF of MusicXML regtests for ': 'MusicXML 的 PDF 回归测试 ',

        'Doc tarball for ': '为文档压缩包',
    },
}


# actual program

manuals = sys.argv[1:] # get manual names from the command line

def getTrans(text, lang):
    if not lang:
        return text
    trans = translations.get(lang.split('_')[0], {}).get(text, None)
    if not trans:
        trans = text
        sys.stderr.write(
            'create-weblinks-itexi: warning: [%(lang)s]: translation missing for: %(text)s\n' % locals())
    return trans


def macroLang(name, lang):
    if lang:
        return name + '-' + lang
    return name


def make_macro(name, string):
    print("@macro", name)
    print(string)
    print("@end macro")
    print("")

def make_download(name, version, download, text):
    string = f"""\
@uref{{https://gitlab.com/lilypond/lilypond/-/releases/\
v{version}/downloads/lilypond-{version}-{download},
{text}: LilyPond {version}}}"""
    make_macro(name, string)

def make_download_source(name, version, lang):
    assert "." in version
    vstring = "v%s.%s" % tuple(version.split(".", 2)[0:2])
    string = f"""\
@uref{{https://lilypond.org/download/sources/{vstring}/lilypond-{version}.tar.gz, \
{getTrans("Source", lang)}: lilypond-{version}.tar.gz}}"""
    make_macro(macroLang(name, lang), string)

def make_all_downloads(macroName, version):
    make_download("download"+macroName+"Linux", version,
                  "linux-x86_64.tar.gz", "GNU/Linux x86_64")
    make_download("download"+macroName+"Darwin", version,
                  "darwin-x86_64.tar.gz", "macOS x86_64")
    make_download("download"+macroName+"Mingw", version,
                  "mingw-x86_64.zip", "Windows x86_64")


def make_ver_link(macroname, url, linktext):
    make_macro(macroname, f"@uref{{{url},{linktext}}}")

# TODO: this kind of thing should really be in a central place for
# lilypond python build scripts


def translateNameToUrl(manual, version):
    ver_split = version.split('.')
    ver_minor = ver_split[0] + '.' + ver_split[1]
    url = depth + "doc/v" + ver_minor + "/Documentation/"

    return url+manual


def addLang(url, lang):
    if lang:
        base, ext = os.path.splitext(url)
        return base + '.' + lang + ext
    else:
        return url


def make_manual_links(name, version, lang):
    """Here is where all the macros manualStableLearningSplit,
    manualStableLearningBig, manualStableLearningSplitNoName, etc. are
    created on the fly.  Hopefully this documentation string will help
    others a bit while grepping for those.
    """
    for m in manuals:
        manual = m
        # TODO: this is a stupid way of doing it
        if m == 'music-glossary':
            mshort = 'Glossary'
        else:
            mshort = m.capitalize()
        if manual == 'music-glossary':
            manual = 'Music glossary'
        url = translateNameToUrl(m, version)

        if url.endswith('.html'):
            make_ver_link(macroLang("manual"+name+mshort+'Pdf', lang),
                          addLang(url, lang),
                          getTrans(manual.capitalize(), lang) + '.pdf')
            make_ver_link(macroLang("manual"+name+mshort+'Split', lang),
                          addLang(url, lang),
                          getTrans(manual.capitalize(), lang) +
                          getTrans(' (split HTML)', lang))
            make_ver_link(macroLang("manual"+name+mshort+'Big', lang),
                          addLang(url, lang),
                          getTrans(manual.capitalize(), lang) +
                          getTrans(' (big HTML)', lang))
            newurl = url
        else:
            make_ver_link(macroLang("manual"+name+mshort+'Pdf', lang),
                          # TODO: this is an even stupider way of doing it
                          addLang(url+'.pdf', lang),
                          getTrans(manual.capitalize(), lang) + '.pdf')
            make_ver_link(macroLang("manual"+name+mshort+'Split', lang),
                          addLang(url + '/index.html', lang),
                          getTrans(manual.capitalize(), lang) +
                          getTrans(' (split HTML)', lang))
            make_ver_link(macroLang("manual"+name+mshort+'Big', lang),
                          addLang(url + '-big-page.html', lang),
                          getTrans(manual.capitalize(), lang) +
                          getTrans(' (big HTML)', lang))
            newurl = url + '/index.html'
        make_ver_link(macroLang("manual"+name+mshort+'SplitNoName', lang),
                      addLang(newurl, lang),
                      getTrans(manual.capitalize(), lang))


def make_regtest_links(name, version, lang):
    ver_split = version.split('.')
    ver_minor = ver_split[0] + '.' + ver_split[1]
    url = depth + "doc/v" + ver_minor + "/input/regression/"

    make_ver_link(macroLang("regtest"+name, lang),
                  url+"collated-files.html",
                  getTrans("Regression tests for ", lang)+version)
    make_ver_link(macroLang("regtest"+name+"Pdf", lang),
                  url+"collated-files.pdf",
                  getTrans("PDF of regtests for ", lang)+version)
    make_ver_link(macroLang("regtest"+name+"Xml", lang),
                  url+"musicxml/collated-files.html",
                  getTrans("MusicXML Regression tests for ", lang)+version)
    make_ver_link(macroLang("regtest"+name+"Abc", lang),
                  url+"abc2ly/collated-files.html",
                  getTrans("abc2ly Regression tests for ", lang)+version)
    make_ver_link(macroLang("regtest"+name+"XmlPdf", lang),
                  url+"musicxml/collated-files.pdf",
                  getTrans("PDF of MusicXML regtests for ", lang)+version)
    make_ver_link(macroLang("regtest"+name+"AbcPdf", lang),
                  url+"abc2ly/collated-files.pdf",
                  getTrans("PDF of abc2ly regtests for ", lang)+version)

def make_doctarball_links(name, version, lang):
    make_download(macroLang("doctarball"+name, lang), version,
                  "documentation.tar.xz",
                  getTrans("Doc tarball for ", lang)+version)


print("@c This file was autogenerated")
print("@c     from: %s" % version_data["TOPLEVEL_VERSION"])
print("@c     by:   %s" % sys.argv[0])
print("")
print("@c ************************ Download binaries ************")
print("")

make_all_downloads("Stable", version_data["VERSION_STABLE"])
make_all_downloads("Devel", version_data["VERSION_DEVEL"])

print("@c ************************ Download source ************")
print("")

for lang in langs:
    print("@c *********", lang or "en", "***")
    make_download_source("downloadStableSource", version_data["VERSION_STABLE"], lang)
    make_download_source("downloadDevelSource", version_data["VERSION_DEVEL"], lang)

print("@c ************************ Manual links ************")
print("")

for lang in langs:
    print("@c *********", lang or "en", "***")
    make_manual_links("Stable", version_data["VERSION_STABLE"], lang)
    make_manual_links("Devel", version_data["VERSION_DEVEL"], lang)

    make_doctarball_links("Stable", version_data["VERSION_STABLE"], lang)
    make_doctarball_links("Devel", version_data["VERSION_DEVEL"], lang)

print("@c ************************ Regtest links ************")
print("")

for lang in langs:
    print("@c *********", lang or "en", "***")
    make_regtest_links("Stable", version_data["VERSION_STABLE"], lang)
    make_regtest_links("Devel", version_data["VERSION_DEVEL"], lang)
print("@c ***************************************************")

# Inside the web docs, rweb{} can be an ordinary internal reference.
print(r"""
@unmacro rweb

@macro rweb{TEXT}
@vindex \TEXT\
@ref{\TEXT\}
@end macro

@unmacro rwebnamed

@macro rwebnamed{TEXT,DISPLAY}
@vindex \TEXT\
@ref{\TEXT\,,\DISPLAY\}
@end macro
""")
