import re
import codecs
import json
import goslate

class Utils(object) :

    @staticmethod
    def hasChinese(str):
        reChinese = re.compile(ur'[\u4e00-\u9fa5]+', re.UNICODE)
        return reChinese.search(str)

    @staticmethod
    def gSlate(str, lang = 'zh-CN'):
        gs = goslate.Goslate()
        return gs.translate(str, lang, source_language = 'de')