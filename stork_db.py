import psycopg2
import uuid


def main():
    conn = psycopg2.connect(
        database="jcb", host="localhost", user="jcb", password="", port="5432"
    )
    cursor = conn.cursor()

    print("Please enter your username.")
    username = input()

    cursor.execute("SELECT user_id FROM users WHERE username = %s;", (username,))
    user_id = cursor.fetchone()

    if user_id:
        print("Username found!")
        return user_id

    else:
        print("Adding username to database...")
        user_id = insert_user(username)
        print("Username added!")
        return user_id

    cursor.close()
    conn.close()


def insert_user(username):
    conn = psycopg2.connect(
        database="jcb", host="localhost", user="jcb", password="", port="5432"
    )
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())

    cursor.execute(
        """
    INSERT INTO users (user_id, username)
    VALUES (%s, %s);
    """,
        (user_id, username),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return user_id


def insert_story(user_id, story_text):
    conn = psycopg2.connect(
        database="jcb", host="localhost", user="jcb", password="", port="5432"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO stories (user_id, story_text)
        VALUES (%s, %s);
    """,
        (user_id, story_text),
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_stories_by_username(username):
    conn = psycopg2.connect(
        database="jcb", host="localhost", user="jcb", password="", port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(
        """
    SELECT 
        u.username,
        s.story_text
    FROM 
        users u
    JOIN 
        stories s ON u.user_id = s.user_id
    WHERE 
        u.username = %s;
    """,
        (username,),
    )

    # Fetch all the stories for the given username
    stories = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    for story in stories:
        print(f"Username: {story[0]}, Story: {story[1]}")

    return stories
