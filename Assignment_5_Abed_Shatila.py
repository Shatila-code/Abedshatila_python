courseCatalog = {}
listStudent = {}

class Course:
    def __init__(self, courseCode, courseName, credits, courseType):
        self.courseCode = courseCode
        self.courseName = courseName
        self.credits = credits
        self.courseType = courseType
 

    @staticmethod
    def addCourse(course):
        courseCatalog[course.courseCode] = course



class Student:
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName
        self.enrolledCourses = {}


    def addStudentCourse(self, courseCode):
        if courseCode in courseCatalog:
            self.enrolledCourses[courseCode] = courseCatalog[courseCode]
        else:
            print("Course not found.")


    def dropCourse(self, courseCode):
        if courseCode in self.enrolledCourses:
            del self.enrolledCourses[courseCode]
        else:
            print("Course not found.")



def studentSystem():
    while True:
        option = int(input("1. Add course \n"
                           "2. Enroll student in course \n"
                           "3. Drop course for student \n"
                           "4. List student courses \n"
                           "5. Save course catalog \n"
                           "6. Load course catalog \n"
                           "7. Exit "))


        if option == 1:
            courseCode = input("Enter course code: ")
            if courseCode in courseCatalog:
                print("Course already exists.")
            else:
                courseName = input("Enter course name: ")
                credits = float(input("Enter number of credits: "))
                courseType = input("Enter course type: ")
                c1 = Course(courseCode, courseName, credits, courseType)
                Course.addCourse(c1)


        elif option == 2:
            studentId = input("Enter student ID: ")
            if studentId not in listStudent:
                studentName = input("Enter student name: ")
                listStudent[studentId] = Student(studentId, studentName)
            courseCode = input("Enter course code: ")
            listStudent[studentId].addStudentCourse(courseCode)


        elif option == 3:
            studentId = input("Enter student ID: ")
            if studentId in listStudent:
                courseCode = input("Enter course code: ")
                listStudent[studentId].dropCourse(courseCode)
            else:
                print("Student not found.")


        elif option == 4:
            studentId = input("Enter student ID: ")
            if studentId in listStudent:
                print("Enrolled courses:")
                for courseCode, course in listStudent[studentId].enrolledCourses.items():
                    print(f"{courseCode}: {course.courseName}")
            else:
                print("Student not found.")


        elif option == 5:
            with open("course_catalog.txt", "w") as f:
                for courseCode, course in courseCatalog.items():
                    f.write(f"{courseCode},{course.courseName},{course.credits},{course.courseType}\n")
            print("Course catalog saved.")


        elif option == 6:
            with open("course_catalog.txt", "r") as f:
                for line in f.readlines():
                    courseCode, courseName, credits, courseType = line.strip().split(",")
                    c1 = Course(courseCode, courseName, float(credits), courseType)
                    Course.addCourse(c1)
            print("Course catalog loaded.")


        elif option == 7:
            break


studentSystem()