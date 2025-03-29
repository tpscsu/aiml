course_details = {
    "CSC101": {
        "room_number": "3004",
        "instructor": "Haynes",
        "meeting_time": "8:00 a.m."
    },
    "CSC102": {
        "room_number": "4501",
        "instructor": "Alvarado",
        "meeting_time": "9:00 a.m."
    },
    "CSC103": {
        "room_number": "6755",
        "instructor": "Rich",
        "meeting_time": "10:00 a.m."
    },
    "NET110": {
        "room_number": "1244",
        "instructor": "Burke",
        "meeting_time": "11:00 a.m."
    },
    "COM241": {
        "room_number": "1411",
        "instructor": "Lee",
        "meeting_time": "1:00 p.m."
    }
}


def get_course_details(course_number):
    details = course_details.get(course_number)

    if details:
        return (f"Course Number: {course_number}\n"
                f"Room Number: {details['room_number']}\n"
                f"Instructor: {details['instructor']}\n"
                f"Meeting Time: {details['meeting_time']}")
    else:
        return "Course number not found."


def main():
    course_number = input("Enter a course number (e.g., CSC101): ").strip()

    details = get_course_details(course_number)
    print(details)


if __name__ == "__main__":
    main()
