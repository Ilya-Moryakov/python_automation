from sqlalchemy import create_engine, text


class SubjectTable:
    __scripts = {
        "select": text("SELECT * FROM subject"),
        "delete_by_id": text("DELETE FROM subject"
                             " WHERE subject_id = :id_to_delete"),
        "insert_new": text("INSERT INTO subject (subject_title) "
                           "VALUES (:new_name) RETURNING subject_id"),
        "select_by_id": text("SELECT * FROM subject "
                             "WHERE subject_id = :select_id"),
        "update_name": text("UPDATE subject SET subject_title = :new_name"
                            " WHERE subject_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, subject_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_id"],
                     {"id_to_delete": subject_id})
        conn.commit()
        conn.close()

    def create(self, name):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["insert_new"], {"new_name": name})
        new_id = result.scalar()  # Забираем точный сгенерированный ID
        conn.commit()
        conn.close()
        return new_id

    def get_subject_by_id(self, subject_id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select_by_id"],
            {"select_id": subject_id}
        )
        subject = result.mappings().all()
        conn.close()
        return subject

    def update_name(self, subject_id, new_name):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update_name"],
                     {"new_name": new_name, "id": subject_id})
        conn.commit()
        conn.close()
