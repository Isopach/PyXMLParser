# coding: UTF-8

import xml.sax
import wiser

class WikipediaHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentTag = ""
        self.title = ""
        self.text = ""
        self.category =""

    # pageタグ開始なら.titleと.textをリセット
    def startElement(self, name, attrs):
        self.currentTag = name
        if name == "page":
            self.title = ""
            self.text = ""
            self.category = ""

    # pageタグ終了ならDBへ登録
    def endElement(self, name):
        if name == "page":
            wiser.add_document(self.title.strip(), self.text.strip(), self.category.strip())

    # titleとtextタグの中身は対応する変数へ
    def characters(self, content):
        if self.currentTag == "title":
            self.title += content
        elif self.currentTag == "text":
            self.text += content
        elif self.currentTag == "category":
            self.category += content

def load_wikipedia_dump(path):
    parser = xml.sax.make_parser()
    parser.setContentHandler(WikipediaHandler())
    parser.parse(path)

#if __name__ == "__main__":
    # load_wikipedia_dump("wiki1m.xml")
