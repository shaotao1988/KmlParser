import xml.sax

class KmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.content = ""
        self.site_name = ""
        self.coordinate = ""
        self.longtitude = ""
        self.altitude = ""
        self.flag = 0
        print("####")

    def startElement(self, tag, attributes):
        self.content = tag
        print("Start tag:" + tag)
        if tag == "Placemark":
            self.flag = 1

    def endElement(self, tag):
        print("End tag:" + tag)
        if tag == "Placemark":
            #print(self.site_name)
            #print(self.coordiante)
            self.site_name = ""
            self.site_coordinate = ""
            self.flag = ""
            return

    def characters(self, content):
        if self.flag == 0 or content.strip() == "":
            return
        elif self.content == "name":
            self.site_name += content
            print("name:" + self.site_name)
        elif self.content == "coordinates":
            self.coordinate += content
            print("coordinates:" + self.coordinate)
        else:
            return

if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    #parser.setFeature(xml.sax.handler.feature_namespace, 0)

    Handler = KmlHandler()
    parser.setContentHandler(Handler)

    parser.parse("test.xml")
