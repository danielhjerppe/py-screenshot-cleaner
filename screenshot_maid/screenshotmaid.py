import os
import collections
from pprint import pprint

"""
Screenshots cleaner

Daniel Hjerppe - daniel.hjerppe@gmail.com

WORK IN PROGRESS 2021-10-20

Goes through your screenshots folder and organizes them based on name/year



"""


BASE_PATH = os.path.expanduser("~")
DESKTOP_PATH = os.path.join(BASE_PATH, "Desktop",)
SCRNSHT_PATH = os.path.join(DESKTOP_PATH, "Screenshots")

DEST_DIRS = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]


def basic_debug():
    print(BASE_PATH)
    print(DESKTOP_PATH)
    print(SCRNSHT_PATH)
    pprint(DEST_DIRS)

# Make folders for screenshots


def screenshot_folders():
    for d in DEST_DIRS:
        dir_path = os.path.join(SCRNSHT_PATH, d)
        if not os.path.isdir(dir_path):
            print("%s not found in this %s folder" % (d, SCRNSHT_PATH))
            print("Creating folder %s in %s" % (d, SCRNSHT_PATH))
            os.mkdir(dir_path)
        else:
            print("Folder %s in %s was found" % (d, SCRNSHT_PATH))
            pass



# List screenshots by date
screenshots_mapping = collections.defaultdict(list)


def screenshots_list():
    global screenshots_mapping
    print(screenshots_mapping)
    screenshots_list = os.listdir(SCRNSHT_PATH)
    # print(screenshots_list)

    for ss in screenshots_list:
        if ss[0] != ".":
            print(ss)
            ss_name = ss.split("-")
            ss_name = ss_name[0]
            ss_name = ss_name.split(" ")
            # print(ss_name)

            for year in ss_name:
                isnumber = str.isnumeric(year)
                if isnumber and os.path.isfile(os.path.join(SCRNSHT_PATH, ss)):
                    print("Year:", year)
                    screenshots_mapping[year].append(ss)
            pprint(screenshots_mapping)


        elif ss[0] == ".":
            pass
            # print("OMG! %s" % ss)


def screenshots_move():
    # Move screenshots to correct folders
    print(screenshots_mapping)
    for year, ss in screenshots_mapping.items():
        if year == "2016":
            for i in ss:
                os.rename(os.path.join(SCRNSHT_PATH, i), os.path.join(SCRNSHT_PATH, "2016", i))
                print("Year %s found" % year)
        elif year == "2017":
            for i in ss:
                os.rename(os.path.join(SCRNSHT_PATH, i), os.path.join(SCRNSHT_PATH, "2017", i))
                print("Year %s found" % year)
        elif year == "2018":
            for i in ss:
                os.rename(os.path.join(SCRNSHT_PATH, i), os.path.join(SCRNSHT_PATH, "2018", i))
                print("Year %s found" % year)
        elif year == "2019":
            for i in ss:
                os.rename(os.path.join(SCRNSHT_PATH, i), os.path.join(SCRNSHT_PATH, "2019", i))
                print("Year %s found" % year)
        elif year == "2020":
            for i in ss:
                os.rename(os.path.join(SCRNSHT_PATH, i), os.path.join(SCRNSHT_PATH, "2020", i))
                print("Year %s found" % year)
        elif year == "2021":
            for i in ss:
                os.rename(os.path.join(SCRNSHT_PATH, i), os.path.join(SCRNSHT_PATH, "2021", i))
                print("Year %s found" % year)
        else:
            print("WHAAT?!?!")


def main():
    basic_debug()
    screenshot_folders()
    screenshots_list()
    screenshots_move()
    print("Done!")

if __name__ == "__main__":
    main()