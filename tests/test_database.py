from sqlalchemy import select
import pytest



@pytest.mark.usefixtures("filled_db")
def test_filled_db(db_session):
    from docker_test.schema import Dog

    statement = select(Dog).order_by(Dog.age)

    with db_session() as session:
        dogs = session.scalars(statement).all()

    assert len(dogs) == 1
    fido = dogs[0]
    assert fido.name == "Fido"

@pytest.mark.usefixtures("filled_db")
def test_filled_db_two(db_session):
    from docker_test.schema import Dog

    statement = select(Dog).order_by(Dog.age)

    with db_session() as session:
        dogs = session.scalars(statement).all()

    assert len(dogs) == 1
    fido = dogs[0]
    assert fido.age == 3
