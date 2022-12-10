from Utilities.ReadFromXml import readFromXml

if __name__ == "__main__":
    data = readFromXml()
    for i in data:
        i.get_info()
        print()

