"""
Screenshots cleaner v2 with pathlib

Daniel Hjerppe - daniel.hjerppe@gmail.com

WORK IN PROGRESS 2023-09-12

Goes through your screenshots folder and organizes them based on name/year

"""

from pathlib import Path

BASE_PATH = Path.home()
DESKTOP_PATH = BASE_PATH.joinpath("Desktop")
SCRNSHT_PATH = DESKTOP_PATH.joinpath("Screenshots")

print(f"""
Looking for screenshots in: {DESKTOP_PATH}
Moving found screenshots to: {SCRNSHT_PATH}/*year*/
""")


SCRNSHT_LIST = DESKTOP_PATH.iterdir()
listOfDicts = []
listOfYears = []

for file in SCRNSHT_LIST:  # Go through files in list
    filename = file.name
    filetype = file.suffix
    if file.is_file() and filetype == ".png":  # Check that it's a png file
        screenshot = filename.split(" ")  # Split the name from whitespaces
        if screenshot[0] == "Screenshot":  # Check if the name begins with "Screenshot"
            year = screenshot[1].split("-")  # Split the name from "-"
            year = year[0]
            if len(year) == 4 and year.isnumeric():
                filedict = {
                    "filename": filename,
                    "year": year
                }
                listOfDicts.append(filedict)

                if year not in listOfYears:
                    listOfYears.append(year)
            else:
                print("- - - Error in year data! - - - ")
        else:
            print(f"{file} is not a valid screenshot.")

try:
    sanakirja = (listOfDicts[1])
    print(f"""Make these folders from Yearlist: {listOfYears}
    {SCRNSHT_PATH} / {sanakirja["year"]}
    """)

    for year in listOfYears:
        folderToCreate = Path(SCRNSHT_PATH / year)
        if not folderToCreate.is_dir():
            print(f"Doesn't exist, creating folder for year {year}")
            Path.mkdir(SCRNSHT_PATH / year)
        else:
            print(f"Folder {folderToCreate} exists already.")
        print()

    for filedict in listOfDicts:
        filetomove = filedict["filename"]
        fileyear = filedict["year"]
        print(f"Move file {filetomove} to {SCRNSHT_PATH / fileyear}")
        Path(DESKTOP_PATH / filetomove).rename(SCRNSHT_PATH / fileyear / filetomove)
except IndexError or NameError:
    print(f"No screenshots found in {DESKTOP_PATH}, stopping the program.")
