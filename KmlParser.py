import xml.sax
import openpyxl

class KmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.content = ""
        self.site_name = ""
        self.site_coordinate = ""
        self.site_list = []
        self.in_placemark = 0

    def write_to_excel(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.cell("A1").value = "Site Name"
        ws.cell("B1").value = "Longtitude"
        ws.cell("C1").value = "Latitude"
        for site in self.site_list:
            ws.append(site)
        wb.save("test.xlsx")

    def startElement(self, tag, attributes):
        self.content = tag
        # print("Start tag:" + tag)
        if tag == "Placemark":
            self.in_placemark = 1

    def endElement(self, tag):
        # print("End tag:" + tag)
        if tag == "Placemark":
            co_list = self.site_coordinate.split(",")
            self.site_list.append([self.site_name, co_list[0], co_list[1]])
            self.site_name = ""
            self.site_coordinate = ""
            self.in_placemark = 0
        elif tag == "kml":
            self.write_to_excel()
            return

    def characters(self, content):
        if self.in_placemark == 0 or content.strip() == "":
            return
        elif self.content == "name":
            self.site_name = content
        elif self.content == "coordinates":
            self.site_coordinate = content
        else:
            return


if __name__ == "__main__":
    parser = xml.sax.make_parser()

    Handler = KmlHandler()
    parser.setContentHandler(Handler)

    parser.parse("test/test.xml")
