from xml.dom.minidom import Document

# Content of a typical kml file
'''
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.1">
<Documents>
    <Placemark>
        <name>Simple placemark</name>
        <description>Description of the place</description>
        <Point>
            <coordinates>-122.0822035425683,37.42228990140251,0</coordinates>
        </Point>
    </Placemark>
</Documents>
</kml>
'''


class Site:
    def __init__(self):
        self.name = ''
        self.longtitude = ''
        self.latitude = ''


def generate_xml(data):
    dom = Document()

    kml = dom.createElement("kml")
    kml.setAttribute("xmlns", "http://earth.google.com/kml/2.1")
    dom.appendChild(kml)

    doc = dom.createElement("Document")
    kml.appendChild(doc)

    for site in data:
        placemark = dom.createElement("Placemark")
        doc.appendChild(placemark)

        name = dom.createElement("name")
        placemark.appendChild(name)
        site_name = dom.createTextNode(site[0])
        name.appendChild(site_name)

        point = dom.createElement("Point")
        placemark.appendChild(point)

        coordinates = dom.createElement("coordinates")
        point.appendChild(coordinates)
        delimiter = ','
        # combine longtitue, latitude and altitude
        coordinates_txt = dom.createTextNode(
            delimiter.join([site[1], site[2], "0"]))
        coordinates.appendChild(coordinates_txt)

    f = open('test_gen.xml', 'a')
    dom.writexml(f, addindent='    ', newl='')
    f.close()


def main():
    data = [["test1", "1.11", "2.22"],
            ["test2", "3.33", "4.44"]]
    generate_xml(data)

if __name__ == "__main__":
    main()