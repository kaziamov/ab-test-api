from ab_test_api.database import get_connection


def make_migration(file='database.sql') -> None:
    with open(file, 'r') as f, get_connection() as conn:
        command = f.read()
        with conn.cursor() as cur:
            cur.execute(command)


if __name__ == "__main__":
    make_migration()
