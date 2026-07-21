from lesson_09.SubjectTable import SubjectTable


db = SubjectTable("postgresql://postgres:harry8@localhost:5432/postgres")


def test_1_create_chinese():
    name = "Chinese"

    new_id = db.create(name)

    created_subject_list = db.get_subject_by_id(new_id)

    db.delete(new_id)

    assert len(created_subject_list) == 1

    created_subject = created_subject_list[0]
    assert created_subject["subject_title"] == name


def test_2_change_to_japanese():
    start_name = "Chinese"
    subject_id = db.create(start_name)

    updated_name = "Japanese"
    db.update_name(subject_id, updated_name)

    updated_subject_list = db.get_subject_by_id(subject_id)

    db.delete(subject_id)

    assert len(updated_subject_list) == 1

    updated_subject = updated_subject_list[0]
    assert updated_subject["subject_title"] == updated_name


def test_3_delete_subject():
    name = "Chinese"
    subject_id = db.create(name)

    db.delete(subject_id)

    rows = db.get_subject_by_id(subject_id)

    assert len(rows) == 0
