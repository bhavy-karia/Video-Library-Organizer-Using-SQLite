import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    print("\n")
    print("*" * 50)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("*" * 50)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))

def main():
    while True:
        print("\nYoutube Manager with Database")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        choice = input("Enter Your Choice ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("\nEnter The Name Of The Video ")
            time = input("Enter The Time Of The Video ")
            add_videos(name, time)
        elif choice == "3":
            video_id = input("\nEnter The Video ID To Update ")
            name = input("Enter The Name Of The Video ")
            time = input("Enter The Time Of The Video ")
            update_videos(video_id, name, time)
        elif choice == "4":
            video_id = input("\nEnter The Video ID That You Want To Delete ")
            delete_videos(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice")
    con.close()

if __name__ == "__main__":
    main()