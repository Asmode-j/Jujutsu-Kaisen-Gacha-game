import sqlite3


class Artifacts:
    def __init__(self,id_artifact, name_artifact, text_artifact):
        self.id_art = id_artifact
        self.name_art = name_artifact
        self.text_art = text_artifact


list_obj_all_artifacts = []

dict_all_artifacts = {}


def create_class_arts():
    base = sqlite3.connect("JJK_Data.db")
    sql = base.cursor()

    all_artifacts = sql.execute("SELECT * FROM Artifacts").fetchall()
    base.commit()

    ALL_Artifacts = [i for i in all_artifacts]


    def create_all_arts():
        for art in ALL_Artifacts:
            list_obj_all_artifacts.append(Artifacts(art[0],art[1],art[2]))

        for obj in list_obj_all_artifacts:
            dict_all_artifacts[obj.id_art] = obj

    create_all_arts()

create_class_arts()

# print(list_obj_all_artifacts)
# print(dict_all_artifacts)

# print(dict_all_artifacts.get(f"pa_01_1").name_art)
# print(dict_all_artifacts.get(f"a_1").name_art)
